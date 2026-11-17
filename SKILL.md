---
name: real-time-static-post
description: "Write real-time viral marketing posts for Уча.се (BG), eduboom.it (IT) and eduboom.ro (RO): a static image with a strong HOOK plus a long, engaging caption about a trending news story (sport, science, olympiads, young talents, national pride), or a memorial post on the death of a famous person. Every fact is cross-checked in several reliable sources. The draft is always written in Bulgarian first; after the user approves it, it is translated into native-level Italian or Romanian. Every post is logged in the tracking sheet content\\real-time-marketing\\real-time-posts.xlsx. Use when the user gives a news link and asks for a post / хуук / описание / real-time пост, says 'напиши пост за тази новина', 'real time post', 'преведи поста на италиански/румънски', or invokes /real-time-static-post. NOT for paid ad creatives (ad-from-concept, ad-recreate, ad-translate)."
metadata:
  version: 1.0.0
---

# Real-time static post (hook + caption)

The format is one static image with a short, strong **hook** printed on it, plus a long **caption** (the
"описание") that keeps the reader interested to the last line. Topics are real-time news that stir pride or curiosity:
young talents, olympiads, science awards, sporting records, national firsts. The second post type is **memorial
posts** on the death of a famous person: who they were, their achievements and their life (see `style-guide.md`).
The identical caption is posted to Facebook and Instagram. **No hashtags and no image suggestions.** Avoid politics,
big tragedies and tabloid news.

Brands and markets:

| Market | Brand | Tab in the sheet | Caption language |
|---|---|---|---|
| Bulgaria | Уча.се | България (BG) | Bulgarian only |
| Italy | eduboom.it | Италия (IT) | BG draft → Italian |
| Romania | eduboom.ro | Румъния (RO) | BG draft → Romanian |

## Files (read them every run)

- `style-guide.md`: **the formula.** Covers structure, hook patterns, tone, emoji use, CTA, the translation standard and glossaries.
- `examples.md`: the user's three original reference posts and every approved finished post. Match their voice.
- `learnings.md`: **a running log of user feedback.** Read it before writing. Append to it after every run (see step 9).
- `scripts/rtm_sheet.py`: sheet helper with the commands `add`, `update`, `show` and `check`. It closes the file in Excel if it is open, writes, and reopens it.

## Workflow

1. **Read the source.** WebFetch the user's link. Extract every fact: names, ages, schools, places, dates, scores,
   rankings, numbers and quotes.
2. **Fact-check. This is non-negotiable.** Search the web beyond the given link (WebSearch, 3–6 queries in the
   source's language and in English), and WebFetch at least 3–4 independent credible outlets. Official sources
   (the university, federation or organiser) have the most weight.
   - A fact goes in as a **statement** only if at least 2 independent reliable sources confirm it.
   - If it has one source, or it is plausible but unconfirmed, **hedge it** ("според медиите", "смята се",
     "описва се като", "по думите му") or **leave it out**.
   - If sources disagree (e.g. participant counts), use a formulation that is true for all of them ("близо", "около").
   - **The user's link can itself be wrong.** It happened: OA Sport said "Davis Cup 2024, Malaga" when it was
     Bologna, Nov 2025. Always cross-check the given article too.
   - Don't invent context, "first ever" claims, "first attempt" claims, ages, years of study or ranking jumps that no
     source states. Check that each sentence is literally true. Example: "първото място на подиума" reads as 1st place;
     for a bronze write "се качи на подиума".
   - Record the result for the `sources` column: fact → outlets, plus a line "НЕ Е ИЗПОЛЗВАНО (…)" listing the facts
     you left out and why.
3. **Write the Bulgarian draft** by following `style-guide.md`. Write it from the target market's point of view: an
   IT post celebrates Italy, an RO post celebrates Romania. Give 1 main hook and 2 alternative hooks. If the user asks
   for a "Кой е X" angle (profiles of a person), put it in the hook and open the caption with "Кой е X?".
4. **Check the length.** Each caption must be **≤ 2,200 characters**, counted in UTF-16 units (an emoji = 2). The
   translation is usually 10–15% longer than the Bulgarian, so keep the BG draft at ~1,900 or less when a translation
   will follow.
5. **Log it.** Write a JSON file in the scratchpad (keys: date, topic, link, sources, hook_bg, desc_bg, status,
   notes), then run:
   `python "%USERPROFILE%\.claude\skills\real-time-static-post\scripts\rtm_sheet.py" add <it|ro|bg> <row.json>`
   Status: `Чернова`. Notes: "Чака одобрение на BG текста преди превод на <IT/RO>."
6. **Show the user** the hook, the full caption, a short fact-check summary (what is confirmed, what is hedged, what
   was left out and why), the alternative hooks, and the sources as markdown links.
7. **After approval, translate** (IT/RO only). See `style-guide.md` → Translation. The translation must read as if
   a native writer had written it for an educational brand: natural and polished, no slang, no calques. Keep original-language
   quotes verbatim (take them from the source, don't back-translate). Do a native-speaker self-review pass
   sentence by sentence before saving. If you find an accuracy issue in the BG text while translating, fix both and
   tell the user. Save with `update <it|ro> <n>` (hook_tr, desc_tr, status `Преведен`, notes), then run `check`.
8. **If the user asks for changes**, apply them with `update`. Don't rebuild the workbook, because the user may have
   edited it. You never need to ask the user to close or save the file: the script saves, closes and reopens it.
9. **Learn.** Whenever the user gives feedback, corrects something, approves a variant or states a new rule, append a
   dated entry to `learnings.md`: what they said, the rule it implies, and a short example. If the rule is general,
   also fold it into `style-guide.md` so the guide stays the single source of truth. When a post is approved, add
   its final version to `examples.md`.

## Answering the user

Reply in the user's language (usually Bulgarian), in a strict professional manner. Keep chat short: post text, fact-check
notes and sources. The full source list lives in the sheet.
