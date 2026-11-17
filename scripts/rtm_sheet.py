"""Tracking sheet for real-time static posts (content\\real-time-marketing\\real-time-posts.xlsx).

Commands:
  python rtm_sheet.py add    <it|ro|bg> <row.json> [--no-open]      append a row (№ is assigned automatically)
  python rtm_sheet.py update <it|ro|bg> <n> <row.json> [--no-open]  overwrite only the fields present in the JSON
  python rtm_sheet.py show   <it|ro|bg> <n>                         print one row
  python rtm_sheet.py check                                         character count of every description
  python rtm_sheet.py format [--no-open]                            repair the view: fixed row height, freeze panes, scrolled to the top

row.json keys (all optional for update): date, topic, link, sources, hook_bg, desc_bg,
hook_tr, desc_tr (translation, IT/RO tabs only), status, published, notes.

Before writing, the script saves and closes the workbook if it is open in Excel (only that
workbook). It then edits the existing file in place, so the user's own edits are kept, and
reopens the file. Descriptions over 2,200 characters are refused. The count is in UTF-16
units, so an emoji counts as 2, the same way Instagram and Facebook count it.
"""
import json
import os
import subprocess
import sys

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

PATH = r"C:\Users\mariya.georgieva\Desktop\claude-code\content\real-time-marketing\real-time-posts.xlsx"
LIMIT = 2200
STATUSES = ["Чернова", "Одобрен (BG)", "Преведен", "Публикуван", "Отказан"]
TABS = {"it": ("Италия (IT)", "IT"), "ro": ("Румъния (RO)", "RO"), "bg": ("България (BG)", None)}


def headers(lang):
    h = ["№", "Дата на новината", "Тема / категория", "Линк към оригиналната новина",
         "Проверени източници", "Хуук (BG)", "Описание (BG)"]
    if lang:
        h += [f"Хуук ({lang})", f"Описание ({lang})"]
    return h + ["Статус", "Дата на публикуване", "Бележки"]


def key_map(lang):
    m = {"date": "Дата на новината", "topic": "Тема / категория", "link": "Линк към оригиналната новина",
         "sources": "Проверени източници", "hook_bg": "Хуук (BG)", "desc_bg": "Описание (BG)",
         "status": "Статус", "published": "Дата на публикуване", "notes": "Бележки"}
    if lang:
        m.update({"hook_tr": f"Хуук ({lang})", "desc_tr": f"Описание ({lang})"})
    return m


WIDTHS = {"№": 5, "Дата на новината": 13, "Тема / категория": 16, "Линк към оригиналната новина": 32,
          "Проверени източници": 40, "Статус": 15, "Дата на публикуване": 14, "Бележки": 30}
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
# The user wants the whole post visible in the cell, so data cells wrap and the rows are auto-fitted
# to the text (user, 2026-11-02: "нека редовете са по-големи, даже може да са толкова големи колкото
# е дълъг текста"). Excel caps a row at 409.5 pt, so a very long post is still clipped at that height.
WRAP = Alignment(wrap_text=True, vertical="top")
# Excel scrolls whole rows, so the row height IS the scroll step: the wheel moves three rows per
# notch. Auto-fitted rows (300-409 pt) jump more than a screen per notch and cannot be scrolled
# through, while one-line rows show nothing. 120 pt is the middle ground the user settled on: about
# eight lines of each post in the default font, several posts on screen, and a notch moves roughly a
# third of a screen. The full text is read by clicking the cell or with `rtm_sheet.py show`.
ROW_HEIGHT = 120
DESC_WIDTH = 70
# Freeze the header row and the № column only. Anything lower (E3, E4, G2 …) pins whole posts in
# place and leaves almost nothing scrollable, which is what broke scrolling before.
FREEZE = "B2"


def fix_view(ws):
    """Fixed row height, default font, wrapped cells, freeze panes B2, scrolled to the top."""
    for c in ws[1]:
        name = str(c.value)
        width = WIDTHS.get(name, DESC_WIDTH if name.startswith("Описание") else 30)
        ws.column_dimensions[c.column_letter].width = width
    for r in range(2, ws.max_row + 1):
        ws.row_dimensions[r].height = ROW_HEIGHT
        for c in ws[r]:
            c.alignment = WRAP
            if c.font.size and c.font.size != 11:
                c.font = Font(size=11, color=c.font.color, underline=c.font.underline)
    ws.freeze_panes = FREEZE
    for view in ws.views.sheetView:
        view.topLeftCell = "A1"
        view.selection = []


def build_tab(ws, lang):
    for i, name in enumerate(headers(lang), 1):
        c = ws.cell(row=1, column=i, value=name)
        c.font = Font(bold=True, color="FFFFFF", size=11)
        c.fill = PatternFill("solid", fgColor="2E75B6" if (lang and f"({lang})" in name) else "1F3864")
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        c.border = BORDER
        ws.column_dimensions[c.column_letter].width = WIDTHS.get(
            name, DESC_WIDTH if name.startswith("Описание") else 30)
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = FREEZE
    ws.auto_filter.ref = f"A1:{ws.cell(row=1, column=len(headers(lang))).column_letter}1"
    letter = ws.cell(row=1, column=headers(lang).index("Статус") + 1).column_letter
    dv = DataValidation(type="list", formula1='"' + ",".join(STATUSES) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"{letter}2:{letter}500")


def load():
    if not os.path.exists(PATH):
        os.makedirs(os.path.dirname(PATH), exist_ok=True)
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
        for tab, lang in TABS.values():
            build_tab(wb.create_sheet(tab), lang)
        return wb
    return openpyxl.load_workbook(PATH)


def ps(cmd):
    return subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True).stdout.strip()


def close_in_excel():
    return ps(
        "try { $xl=[Runtime.InteropServices.Marshal]::GetActiveObject('Excel.Application');"
        f" foreach($wb in @($xl.Workbooks)){{ if($wb.FullName -eq '{PATH}'){{ $wb.Save(); $wb.Close($false); 'closed' }} }} }} catch {{ }}"
    )


def reopen():
    os.startfile(PATH)


def ulen(s):
    return len((s or "").encode("utf-16-le")) // 2


def check_lengths(data):
    bad = [(k, ulen(data[k])) for k in ("desc_bg", "desc_tr") if data.get(k) and ulen(data[k]) > LIMIT]
    if bad:
        sys.exit("REFUSED: over %d characters: %s" % (LIMIT, ", ".join(f"{k}={n}" for k, n in bad)))


def write_row(ws, lang, r, data):
    col = {c.value: i + 1 for i, c in enumerate(ws[1])}
    for key, header in key_map(lang).items():
        if key in data:
            c = ws.cell(row=r, column=col[header], value=data[key])
            c.alignment = WRAP
            c.border = BORDER
            if key == "link" and data[key]:
                c.hyperlink = data[key]
                c.font = Font(color="0563C1", underline="single")
    for i in range(1, len(col) + 1):
        ws.cell(row=r, column=i).border = BORDER
        ws.cell(row=r, column=i).alignment = WRAP
    fix_view(ws)


def find_row(ws, n):
    for r in range(2, ws.max_row + 1):
        if ws.cell(row=r, column=1).value == n:
            return r
    sys.exit(f"row № {n} not found in {ws.title}")


def read_json(p):
    with open(p, encoding="utf-8-sig") as f:
        return json.load(f)


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    no_open = "--no-open" in sys.argv
    cmd = a[0] if a else ""
    if cmd == "check":
        wb = load()
        for ws in wb:
            for r in range(2, ws.max_row + 1):
                for c in ws[1]:
                    if str(c.value).startswith("Описание"):
                        n = ulen(ws.cell(row=r, column=c.column).value)
                        print(f"{ws.title} №{ws.cell(row=r, column=1).value} {c.value}: {n}{'  OVER LIMIT' if n > LIMIT else ''}")
        return
    if cmd == "format":
        close_in_excel()
        wb = load()
        for ws in wb:
            fix_view(ws)
        wb.save(PATH)
        print(f"format: rows {ROW_HEIGHT}pt, default font, freeze panes {FREEZE} on every tab")
        if not no_open:
            reopen()
        return
    tab, lang = TABS[a[1]]
    if cmd == "show":
        ws = load()[tab]
        r = find_row(ws, int(a[2]))
        for c in ws[1]:
            print(f"=== {c.value}\n{ws.cell(row=r, column=c.column).value}\n")
        return
    data = read_json(a[-1])
    check_lengths(data)
    close_in_excel()
    wb = load()
    ws = wb[tab]
    if cmd == "add":
        nums = [ws.cell(row=r, column=1).value for r in range(2, ws.max_row + 1)]
        n = max([x for x in nums if isinstance(x, int)], default=0) + 1
        r = ws.max_row + 1
        ws.cell(row=r, column=1, value=n)
        data.setdefault("status", "Чернова")
    elif cmd == "update":
        n = int(a[2])
        r = find_row(ws, n)
    else:
        sys.exit(__doc__)
    write_row(ws, lang, r, data)
    wb.save(PATH)
    print(f"{cmd}: {tab} №{n} saved")
    if not no_open:
        reopen()


if __name__ == "__main__":
    main()
