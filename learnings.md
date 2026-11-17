# Learnings log

Append a dated entry after every run in which the user gave feedback, corrected something, approved a variant or
stated a new rule. Format: **date · topic**, then what the user said, the rule it implies, and an example. When a
rule is general, also fold it into `style-guide.md`.

---

**2026-09-30 · Setup (Caniato IT, Nimerenco RO)**

1. **Facts must be verified in several reliable sources.** User: "изключително важно да използваш само вярна и проверена
   информация сравнена в поне от няколко достоверни източника… ако за нещо не си сигурен… не го казвай като
   твърдение". Rule: ≥2 independent sources for a statement, hedge or omit the rest, and search beyond the given link.
   Example: the given OA Sport article said "Davis Cup 2024, Malaga", but four other outlets said Bologna, Nov 2025.
   Another: the 707 points and "Best of Nation" appeared only in actualdecluj.ro, so they were left out.
2. **Profile angle.** User asked to add "Кой е Карло Алберто Каниато" to the hook/caption. Rule: for posts about a
   person the public doesn't know yet, the "Кой е X – …?" hook plus an opening "Кой е X?" paragraph works well.
3. **Translation quality.** User: translate "като native speaker, но без slang… нормален натурален език", because
   the posts are for educational platforms. Rule: native-level, polished, standard register, with a self-review pass.
   Example fixes: IT "speranza" → "promessa"; RO "categorie" → "probă"; RO "abilități" → "competențe".
4. **Literal accuracy of wording.** Self-caught errors:
   - "първото място на подиума" for a bronze sounds like 1st place;
   - "без гарантирано място" contradicts what a wild card is;
   - "до върха още от първия път" and "цяла седмица състезания" were not supported by the sources.
   Rule: re-read every sentence and check that it is literally true.
5. **Length limit.** User: "текста в описанието трябва да е максимум 2,200 characters". Rule: ≤2,200 UTF-16 chars per
   caption, translation included. The IT Caniato caption was 2371, trimmed to 2137.
6. **The sheet file.** User asked not to be told to close the xlsx: "затвори файла сам, добави текста и отвори файла
   отново". `rtm_sheet.py` handles this. The user doesn't need to press Save after our edits.

7. **Scope answers (user, 2026-09-30).** No hashtags. The identical caption goes to FB and IG. BG posts follow the same
   formula as IT/RO. No image suggestions for now. The user supplies the link/topic. Avoid politics, big tragedies and
   yellow news. Memorial posts for famous people do happen: who they were, their achievements, their life. A memorial
   format was drafted in `style-guide.md` as a proposed default, to be confirmed on the first real memorial.


**2026-10-07 · Aris Dejeu (RO, NATO blackout competition)**

1. **BG draft approved without changes** ("супер е текста"). The structure (pride opener → facts → scale → pivot → 👉 list of what makes it impressive → plain-language sentence → own words → quote → forward teaser → values → CTA) works for a student-award story too.
2. **Single-source sensational details stay out.** Playtech alone claimed a 3-day isolation "without internet/phone" (and its wording was contradictory); left out. Rule: when one outlet adds a dramatic angle the others don't mention, omit it.
3. **Word the status literally.** Self-caught: "младия румънски журналист" → he is a journalism *student*; "където учи по Еразъм" → sources speak in past tense ("се е намирал"), so "където е бил". Rule: don't upgrade a student to a professional title, and keep tense true to the sources.
4. **The given link can mislabel institutions.** primanews.ro said "Facultatea de Științele Comunicării"; the university/other outlets say the Department of Political Science and Communication Sciences, Journalism programme.

**2026-10-07 · Нина Дамянова (BG memorial)**

1. **Memorial hook must not mention the death.** User: "хуука не искам да е 'почина актрисата...' а нещо като тя направи еди какво си за българското кино". Rule: hook = what the person did / is remembered for; the death goes in the first caption line. Example: "Българската актриса, която отдаде близо 30 години на сцената на Театър „Българска армия“". Folded into style-guide.md.
2. **User's reference memorial** (Сърчаджиев, hook "Българинът, зад най-запомнящия се образ във Време разделно") is the format to follow: biography and life path in the caption, ends with "Поклон пред светлата му памет. 🕯️", no share CTA.
3. **Thin public biography → say so, don't pad.** All outlets copied one theatre statement; no birthplace, education, awards or film roles. The user suggested a cinema angle, but no film work was confirmed, so the hook stayed on theatre and the gap was explained. Age omitted (only birth year known).
4. **Sheet locked by Excel in a modal state** (RPC_E_CALL_REJECTED): don't kill Excel; tell the user to press Esc / close it, then retry.
5. **Memorial hooks: short and punchy.** User rejected "Българската актриса, която отдаде близо 30 години на сцената на Театър „Българска армия“" ("дълъг е и не много грабващ") and "Българската актриса, която беше Ния от „Железният светилник“". Chose from a list in chat: "От Талев до Шекспир: 30 години на една сцена". Rule: memorial hook ≤ 8 words; contrast "От X до Y" with names everyone knows from school works well; when a hook is rejected, offer 8–10 options in chat grouped by angle instead of picking one.

**2026-10-12 · Twisted Jiu Jitsu, 8 медала в Лисабон (BG)**

1. **Club press release as the only primary source.** The BNT article just republished the club's PDF, and IBJJF results for the Lisbon Open weren't online yet. Medal details were used (the club is the official source for its own athletes), but the gap was flagged to the user. The club's self-claim "най-голямата академия" was hedged as "се определя като".

**2026-10-12 · Wilma De Angelis (IT memorial)**

1. **BG draft approved** without text changes ("ок, преведи").
2. **User asked whether the nephew's quote is real.** Rule: for every quote, record in the sources *where it was originally published* (e.g. a Facebook post) and which outlets quote it **verbatim**. Say plainly if the original post itself wasn't seen. Example: "Le tue canzoni…" appears verbatim in ANSA + Il Fatto Quotidiano, from Fabio De Angelis' Facebook post.
3. **Hook sub-line.** User: add "прочети историята на Уилма Де Анджелис в описанието" to the hook and translate it. Rule: for memorial posts, give a second line on the image, "Прочети историята на [Име] в описанието" / IT "Leggi la storia di [Nome] nella descrizione" / RO "Citește povestea lui/ei [Nume] în descriere". Folded into style-guide.md.
4. **IT memorial closing: "Ciao, Wilma. Che la terra ti sia lieve." REJECTED** by the user ("това нещо не ми харесва"). Don't use it. Offered 6 alternatives in chat; the user chose **"Onore alla sua memoria. 🕯️"**, which is now the IT memorial closing line.
5. **Sheet scrolling.** User: couldn't scroll slowly or see two posts at once, because auto-fit rows were taller than the screen and Excel scrolls one row at a time. Fix: `rtm_sheet.py` now sets a fixed data-row height (ROW_HEIGHT = 150 pt) on every write, plus a `format` command for existing rows. To read a full text, click the cell and expand the formula bar.

**2026-10-13 · Девора Аврамова, 20 км в Париж (BG)**

1. **BG draft approved without changes and published the same day.** The achievement formula worked for an individual sports record.
2. **"Best ever" claims from a federation need a check against record lists.** BG media called it the best Bulgarian result at 20 km, but Wikipedia lists Mircheva's 1:07:38 as a 20 km split inside a half marathon (Valencia 2019). Rule: when an "all-time best" may conflict with en-route splits or other lists, attribute it ("според БФЛА") instead of stating it as our own fact, and avoid the word "рекорд" if no source uses it. Also, split times are not records: write "най-силните в историята" with attribution, not "подобри рекорда".

**2026-11-02 · Никола Цолов, дебют във Формула 1 (BG)**

1. **BG draft approved without changes** ("одобрявам този пост"). A motorsport story with no medal still works on the achievement formula: the "first ever" milestone carries the post, and the ranking (12th) becomes impressive through context (gap to the team's regular driver, only his second time in the car, hardest circuit).
2. **Some news sites block WebFetch** (nova.bg, rainews.it return "unable to fetch"). Rule: when the user's own link can't be fetched, rebuild the story from the full-results pages and the national agency (BTA/ANSA) instead of guessing, and say nothing that those sources don't carry.
3. **Classification tables disagree on mid-field positions after penalties.** PlanetF1, Motorsport Week and The Race differed from P7 down in Mexico. Rule: use only the positions that every table agrees on (the top of the order and the driver we write about).
4. **Dramatic session details stay out when single-sourced.** Brake overheating with the radio line "something is smoking" (F1Oversteer only) and a pit stop for a numb right leg (BTA only) were both omitted.

**2026-11-02 · Кими Антонели, световен шампион (IT draft)**

1. **Career totals vs season totals.** Wikipedia's driver infobox gives career figures (9 wins, 19 podiums, 530 pts); the Formula1.com driver profile splits the season out (2026: 9 wins, 16 podiums, 7 poles, 380 pts). Rule: for "this season" claims use the official F1 profile's season block, not the Wikipedia infobox.
2. **Record claims need the previous holder's exact figure.** "Youngest champion" was published with 20 years 68 days vs Vettel's 23 years 134 days (2010) in ESPN, Gulf News and RaceFans — all three used, so the comparison is stated, not hedged.
3. **Explain the mechanism when a result looks contradictory.** User: "в текста пише че е шампион Кими, а после пише Той финишира трети, не разбирам това". Rule: when a headline fact and the race result seem to clash (champion but 3rd; medal but not 1st), add one plain sentence saying how it works — "Шампионът не се решава в едно състезание, а по точките за целия сезон" — before stating the result. Don't assume the reader follows the sport.

**2026-11-02 · Sheet scrolling, second report**

1. **The cause was the freeze panes, not the row height.** User: "last time i asked you that i would like to scroll freely through it". The tabs had drifted to freeze `E3` (IT), `G2` (RO) and `E4` (BG), which pins one or two whole 150 pt posts plus columns A–D, leaving almost nothing scrollable. Rule: check `ws.freeze_panes` first when scrolling is reported as broken, not just the row heights.
2. **Fix in `rtm_sheet.py`, step 1 (not enough):** `ROW_HEIGHT` 150 → 80 pt, `FREEZE = "B2"` re-applied on every write, sheet view reset to `topLeftCell = "A1"`. `fix_row_heights` became `fix_view`.
3. **Single-line rows were tried and rejected.** After the 80 pt fix the user said "no it's still not like a normal excell. i want to scroll to whatever row i want, seeing the other rows at the same time", so rows went to one line, `wrap_text=False`. The user then said: "не не, нека редовете са по-големи, даже може да са толкова големи колкото е дълъг текста". Rule: **the whole post must be visible in the cell.** Don't propose compact rows again.
4. **Full auto-fit was tried and rejected too.** `EntireRow.AutoFit` over Excel COM, with description columns at width 120/font 9 and sources at width 70/font 8, put every row at 276–409 pt with nothing clipped. The user: "сега текста в таблицата е някак по-малък от преди… като тръгна да скролвам ми скролва твърде много надолу или нагоре. искам свободен скрол аз да си избера кой пост да си гледам". Two lessons: never shrink the font to win space, and tall rows break scrolling.
5. **The settled layout: fixed 120 pt rows, default font 11, `wrap_text=True`, widths back to 70 (descriptions) and 40 (sources), freeze `B2`.** Excel scrolls whole rows and the wheel moves three per notch, so the row height *is* the scroll step: 120 pt ≈ 8 lines per post, several posts on screen, a notch moves about a third of a screen. The full text is read in the formula bar or with `rtm_sheet.py show <tab> <n>`. The `autofit_in_excel()` helper was removed.
6. **This setting was argued over four times (150 → 80 → 15 → auto-fit → 120).** Don't change the row height, the font size or the column widths again without being asked; when something looks wrong in the sheet, check `freeze_panes` and the stored heights first.
3. **Repeated PermissionError on save.** The script's `close_in_excel` matches on `$wb.FullName`, which can miss; closing the workbook over COM by name (`$wb.Name -like "real-time-posts*"`, `Close($true)`) worked. Don't ask the user to close it.

**2026-11-04 · Двойно злато за Румъния, Европейско по джудо U23 (RO)**

1. **The given link's headline was misleading, and the federation's own wording resolved it.** Mediafax: "două medalii de aur … după 13 ani de așteptare", which reads as "first gold in 13 years". False: Ioan Dzițac won the U23 European title at 73 kg in Chișinău in 2025 (Wikipedia 2025 edition, newsweek.ro, stiripesurse.ro). FRJudo's exact wording is "pentru prima dată după 13 ani când țara noastră reușește să cucerească două titluri la aceeași ediție" — two titles at one edition. Rule: when a "after X years" claim appears, work out *what exactly* the streak counts and check the intervening editions; the national federation's own phrasing beats the news headline.
2. **Hook must name the medals.** User rejected "Две европейски титли за Румъния на едно първенство – след 13 години чакане": "искам в хуука да пише нещо свързано със златни медали". Offered 7 options grouped by angle; the user chose **"Два златни медала за Румъния на Европейското по джудо U23"** — plain, with the medal and the event, no "after 13 years" angle. Rule: prefer "златни медали" over "титли" in achievement hooks, and keep the hook self-explanatory without the backstory.
3. **Sources disagreeing on a number → a formulation true for both.** Bogdan's final: 27 seconds (alba24, citing the EJU) vs 29 seconds (proalba, ziarulunirea) → "за по-малко от 30 секунди" / "în mai puțin de 30 de secunde".
4. **Ages omitted.** Vișa's date of birth (2 Apr 2006) only in judoinsite; Bogdan's age (20) only in alba24 — one source each, so neither was used.
5. **Excel modal state again (RPC_E_CALL_REJECTED).** `GetActiveObject("Excel.Application")` reported `Workbooks.Count = 0` although the process held the file, and `BindToMoniker` on the full path failed three times with "Call was rejected by callee". Rule: `Workbooks.Count = 0` with the window title showing the file is the same modal symptom; retry a few times, don't kill Excel, deliver the text in chat and save the row once the user clears the dialog.

**2026-11-04 · Карлос Насар, световно в Нинбо (BG) – пренаписване след края на състезанието**

1. **Don't publish a post written mid-competition; rewrite it when the event ends.** The first version was written while the clean and jerk was still running, so it could only claim the snatch world record. The user came back: "мисля, че състезанието е приключило и освен рекорд карлос взе и титлата". Rule: when a post is drafted during a live event, write the gap into the notes column (it was) **and** re-check the result before publishing; the headline fact usually upgrades (record → title).
2. **Headline numbers that look wrong are often intermediate totals.** epicenter.bg gave "403 кг световен рекорд" alongside 415 kg; BTA explains it: 403 was the total record after his 218/220 kg second attempt, before the 230 kg third. Rule: a smaller total in the same report is a provisional record during the competition, not a contradiction — check the attempt order before calling it an error.
3. **bnrnews.bg contradicted itself** (Alipour's snatch 191 kg in the lead, 181 kg further down). Only the figures confirmed by BTA and the Wikipedia protocol were used.
4. **"Четвърта титла в четвърта различна категория" is worth the fact-check** — 81 kg Tashkent 2021, 89 kg Manama 2024, 94 kg Førde 2025, 95 kg Ningbo 2026. It carries the "И най-интересното?" pivot better than repeating the records.
5. **Quote left out:** "Аз съм върховният хищник" appears only in headlines (epicenter.bg, forbesbulgaria.com citing gong.bg) and was said **before** the trip to China, not after the title. No primary source for the full wording → omitted.
6. **Explain the sport's mechanics in one plain paragraph.** As with the Antonelli "champion but 3rd" case, the reader doesn't know that снатч/клийн-енд-джърк are two movements with three attempts each and that the champion is decided on the sum — one short paragraph makes all three records make sense.
