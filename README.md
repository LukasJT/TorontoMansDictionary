# Toronto Mans Dictionary

An Urban Dictionary-style reference for real Toronto and GTA slang — searchable,
filterable, with real photography of the city and sourced (not invented)
definitions. Plus Torontle, a Wordle clone built from the same dictionary, a
researched history article, and an FAQ page.

No build step to run the site. No framework. Plain HTML/CSS/JS. There is a
small Python script that regenerates static HTML from the data — see below.

## Running it locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

or

```bash
npx serve .
```

`wordle.html` fetches `data/terms.json` at runtime, which browsers block over
`file://` — serve the folder rather than double-clicking the files.
`index.html` doesn't have that problem: its dictionary content is static HTML
(see below), so it even works opened directly from disk.

## Project structure

```
index.html            Dictionary page — term cards are pre-rendered static HTML
wordle.html            Torontle, the Wordle clone
quiz.html               Toronto Slang Quiz (multiple choice, built from terms.json)
history.html             The History of Toronto Slang (long-form article)
faq.html                  Toronto Slang FAQ (FAQPage structured data)
neighbourhoods.html        Toronto Slang By Neighbourhood (long-form article)
all-words.html              Flat A-Z link list of every word page
words/<slug>.html            One standalone static page per term (own title/meta/
                              JSON-LD, expanded write-up, sources, related words)
categories/<cat>.html         One hub page per slang category
guide/*.html                   General Toronto content, not slang-specific: history,
                                Indigenous history, neighbourhoods, landmarks, food,
                                sports, festivals, multiculturalism, transit, parks,
                                media, economy, education, nicknames, weather,
                                architecture, art, waterfront, LGBTQ+ history,
                                medical history, tech scene, the public library,
                                housing costs, the CNE, famous Torontonians,
                                airports, city government, the comedy scene, the
                                zoo/science centre, craft beer, safety/crime stats,
                                ethnic enclaves, the ravine system, newspapers,
                                cycling, religious diversity, coffee culture,
                                Union Station, GO Transit, Ontario Place, historic
                                extreme weather, the cocktail/distillery scene,
                                broadcasting history, and dedicated pages for
                                Scarborough, Etobicoke, North York, Mississauga,
                                Brampton and Vaughan, plus a guide/index.html hub
404.html                     Custom not-found page
css/style.css               Shared design tokens, header/footer, dictionary, ad blocks
css/wordle.css               Torontle-specific styles
css/quiz.css                  Quiz-specific styles
css/article.css                Shared styles for history/faq/neighbourhoods/words/categories
css/guide.css                   Toronto Guide-specific styles
js/app.js                    Dictionary search/filter/sort/vote — enhances static HTML, no fetch
js/wordle.js                  Torontle game logic
js/quiz.js                     Quiz logic
js/ads.js                       House-ad rotation + unfilled-ad-slot fallback
js/submit-modal.js               "Submit a term" modal (mailto, no backend)
data/terms.json                  The dictionary itself — one JSON object per term
scripts/build.py                  Regenerates index.html's cards, words/*.html,
                                   categories/*.html, all-words.html and sitemap.xml
                                   from terms.json
scripts/build_guide.py             Regenerates guide/*.html from hand-authored prose
                                    (not derived from terms.json — real, separate
                                    content about the city itself)
robots.txt / sitemap.xml      Basic technical SEO
SOURCES.md                    Research sources + photo credits + how to extend
```

## Adding a term

1. Add an object to `data/terms.json`:

    ```json
    {
      "term": "Example Word",
      "slug": "example-word",
      "categories": ["Talk & Fillers"],
      "origin": "Where it likely comes from",
      "definition": "What it means.",
      "example": "A sentence using it naturally."
    }
    ```

2. Regenerate the static dictionary page:

    ```bash
    python3 scripts/build.py
    ```

That's it — `index.html`'s term cards, every `words/<slug>.html` page, and
`sitemap.xml` are all real static HTML/XML generated from `data/terms.json`,
not built by JavaScript at runtime — so the dictionary is fully readable by
search engines and by browsers with JavaScript disabled. `js/app.js` only
handles search, filtering, sorting and voting on top of that existing markup.
`scripts/build.py` is what keeps all of it in sync with `data/terms.json` —
re-run it any time the data changes; it also deletes any `words/*.html` page
whose term was removed.

If the term is a single clean word (or you add a `puzzleWord` override, see
existing entries like `"Brodie / Crodie"`), it's automatically eligible to
show up as a Torontle answer too — no extra step needed there.

Two more optional fields per term: `sourceUrl` + `sourceLabel` link a term's
`words/<slug>.html` page straight to a specific citation (used for a handful
of terms with a real, direct single source, e.g. `"mans"` → Derek Denis's
paper). Leave them off and the page falls back to a generic link to
`SOURCES.md` and `history.html` — don't invent a citation that isn't real.

## Notes

- Vote counts on each card are seeded deterministically per term (so they
  look like a real, lived-in dictionary instead of starting at zero) plus
  whatever you personally click, stored in `localStorage`. There's no
  backend, so votes aren't shared between visitors — the UI says so.
- "Submit a term" opens an in-page form and hands off a pre-filled `mailto:`
  link to the site owner — there's no backend to send mail automatically, so
  it relies on the visitor's own email client (with a copy-paste fallback if
  none is configured).
- Background photography is loaded live from Wikimedia Commons under
  Creative Commons licenses. See `SOURCES.md` for exact credits and the full
  research source list behind every definition.
- `#ad-slot-*` elements across the pages are empty, clearly labelled
  placeholders reserved for a future ad network — nothing is wired up yet.
