# Toronto Mans Dictionary

An Urban Dictionary-style reference for real Toronto and GTA slang — searchable,
filterable, with real photography of the city and sourced (not invented)
definitions.

No build step. No framework. Plain HTML/CSS/JS.

## Running it locally

Opening `index.html` directly won't work — the browser blocks `fetch()` on
`file://` URLs, so the dictionary data won't load. Serve the folder instead:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

or

```bash
npx serve .
```

## Project structure

```
index.html          Page markup
css/style.css        All styling (custom properties, no framework)
js/app.js            Search, filter, sort, word-of-the-day, vote UI
data/terms.json       The dictionary itself — one JSON object per term
SOURCES.md            Research sources + photo credits + how to extend
```

## Adding a term

Add an object to `data/terms.json`:

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

No code changes needed — the page reads the file at load time.

## Notes

- Vote counts on each card are seeded deterministically per term (so they
  look like a real, lived-in dictionary instead of starting at zero) plus
  whatever you personally click, stored in `localStorage`. There's no
  backend, so votes aren't shared between visitors — the UI says so.
- Background photography is loaded live from Wikimedia Commons under
  Creative Commons licenses. See `SOURCES.md` for exact credits and the full
  research source list behind every definition.
