#!/usr/bin/env python3
"""
Regenerates everything derived from data/terms.json:
  1. The static term-card markup inside index.html (crawlable, no-JS-safe).
  2. One standalone static page per term under words/<slug>.html, each
     targeting that word's own long-tail search ("what does X mean toronto
     slang") with a longer write-up, real internal links, and a sources
     section — not just a copy of the dictionary card.
  3. sitemap.xml, so every generated page is actually indexable.

Run this after editing data/terms.json:
    python3 scripts/build.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_PATH = ROOT / "data" / "terms.json"
INDEX_PATH = ROOT / "index.html"
WORDS_DIR = ROOT / "words"
SITEMAP_PATH = ROOT / "sitemap.xml"

SITE_URL = "https://lukasjt.github.io/TorontoMansDictionary"

BEGIN_MARK = "<!-- BEGIN GENERATED TERM CARDS (run scripts/build.py after editing data/terms.json) -->"
END_MARK = "<!-- END GENERATED TERM CARDS -->"

CATEGORY_BLURB = {
    "Geography & Identity": "Words like this are about place — the specific streets, boundaries and nicknames that tell you exactly which part of the GTA someone means.",
    "Getting Around": "This is TTC and highway culture — the nicknames locals actually use instead of the official names.",
    "People & Respect": "This is relationship vocabulary — how people in the GTA refer to friends, crews, and showing respect.",
    "Talk & Fillers": "This is conversational glue — words and tags that hold a sentence together in everyday GTA speech.",
    "Hype & Approval": "This is hype vocabulary — words used to big something up, whether it's an outfit, a song, or a moment.",
    "Beef & Bad Vibes": "This is the vocabulary for when something, or someone, isn't hitting right.",
    "Money": "Money slang travels fast through hip-hop and drill culture, and the GTA scene has its own well-worn set of terms for it.",
    "Culture & Sports": "This one's tied to Toronto's culture at large — sports, food or music that's become part of the city's identity.",
}

ORIGIN_MATCHERS = [
    (r"patois|jamaican", "It's one of many Toronto terms that trace back to Jamaican Patois, brought into the city through Toronto's Caribbean communities. Read the fuller story in our <a href=\"../history.html#how\">history of Toronto slang</a>."),
    (r"somali|arabic", "It's part of the Somali- and Arabic-rooted vocabulary that entered Toronto slang through the city's East African and Middle Eastern communities. Read more in our <a href=\"../history.html#how\">history of Toronto slang</a>."),
    (r"mte|multiethnolect|denis|linguist", "It's part of what linguists formally call Multicultural Toronto English (MTE) — see our <a href=\"../history.html#mte\">MTE research section</a> for the academic side of this."),
    (r"uk|london|mle", "It overlaps with UK street slang — multiethnolects like Toronto's Multicultural Toronto English and London's Multicultural London English share real linguistic DNA. More in our <a href=\"../history.html#mte\">history page</a>."),
    (r"drake|raptors|ovo|drill|hip-hop|rap", "It's tied to Toronto's music and sports culture more than to a specific immigrant-language root — see our <a href=\"../history.html#global\">\"from the block to global\"</a> section for how that side of Toronto slang spread."),
    (r"highway|expressway|avenue|area code|municipalit|neighbourhood|amalgamation", "It's geography slang — shorthand locals use instead of the official name. More GTA geography terms are in the dictionary's <a href=\"../index.html?cat=Geography+%26+Identity\">Geography &amp; Identity</a> category."),
    (r"hockey", "It comes out of Canadian hockey culture rather than the city's immigrant-language history."),
]

DEFAULT_ORIGIN_NOTE = "Like a lot of GTA slang, its exact origin is debated even among people who use it every day — see our <a href=\"../history.html\">full history of Toronto slang</a> for the bigger picture on how this vocabulary formed."


def strip_quotes(s):
    return re.sub(r'^["“]+|["”]+$', "", s.strip())


def esc(s):
    return html.escape(s, quote=True)


def origin_note(origin):
    low = origin.lower()
    for pattern, note in ORIGIN_MATCHERS:
        if re.search(pattern, low):
            return note
    return DEFAULT_ORIGIN_NOTE


def wordle_puzzle_word(term):
    word = term.get("puzzleWord")
    if not word and re.fullmatch(r"[A-Za-z]+", term["term"]) and 4 <= len(term["term"]) <= 8:
        word = term["term"].upper()
    return word.upper() if word else None


def build_card(term):
    slug = term["slug"]
    categories = term.get("categories", [])
    cat_attr = esc("|".join(categories))
    first_cat = esc(categories[0]) if categories else ""
    example = esc(strip_quotes(term["example"]))
    card_id = "term-" + slug
    body_id = card_id + "-body"

    return f'''      <article class="term-card" itemprop="hasDefinedTerm" itemscope itemtype="https://schema.org/DefinedTerm" data-slug="{esc(slug)}" data-categories="{cat_attr}" id="{card_id}">
        <button class="term-card-header" type="button" aria-expanded="false" aria-controls="{body_id}">
          <h3 class="term-name" itemprop="name">{esc(term["term"])}</h3>
          <span class="term-cats">{first_cat}</span>
          <span class="chevron" aria-hidden="true">›</span>
        </button>
        <div class="term-body" id="{body_id}" hidden itemprop="description">
          <p class="term-definition">{esc(term["definition"])}</p>
          <p class="term-example">“{example}”</p>
          <p class="term-origin">{esc(term["origin"])}</p>
          <div class="term-votes">
            <button type="button" class="vote-btn vote-up" data-dir="1" aria-label="Upvote this word">▲ <span class="vote-up-count">0</span></button>
            <button type="button" class="vote-btn vote-down" data-dir="-1" aria-label="Downvote this word">▼ <span class="vote-down-count">0</span></button>
            <span class="vote-note">votes stay in your browser only</span>
          </div>
          <a class="word-page-link" href="words/{esc(slug)}.html">Full write-up on "{esc(term["term"])}" →</a>
        </div>
      </article>'''


def related_terms(term, all_terms, n=4):
    cats = set(term.get("categories", []))
    others = [t for t in all_terms if t["slug"] != term["slug"] and cats & set(t.get("categories", []))]
    return others[:n]


def build_word_page(term, all_terms):
    slug = term["slug"]
    name = term["term"]
    definition = term["definition"]
    example = strip_quotes(term["example"])
    origin = term["origin"]
    categories = term.get("categories", [])
    primary_cat = categories[0] if categories else "Toronto Slang"
    blurb = CATEGORY_BLURB.get(primary_cat, "This word is part of the everyday vocabulary documented in the Toronto Mans Dictionary.")
    onote = origin_note(origin)
    puzzle_word = wordle_puzzle_word(term)
    related = related_terms(term, all_terms)
    source_url = term.get("sourceUrl")
    source_label = term.get("sourceLabel")

    cat_links = " ".join(
        f'<a class="chip-static" href="../index.html?cat={html.escape(c, quote=True).replace(" ", "+")}">{esc(c)}</a>'
        for c in categories
    )

    related_html = ""
    if related:
        items = "\n".join(
            f'          <li><a href="{esc(r["slug"])}.html">{esc(r["term"])}</a> — {esc(r["definition"][:90].rsplit(" ", 1)[0])}…</li>'
            for r in related
        )
        related_html = f'''
      <h2>Related words</h2>
      <ul class="related-list">
{items}
      </ul>'''

    torontle_html = ""
    if puzzle_word:
        torontle_html = f'''
      <div class="torontle-cta">
        <p>This word is a possible <strong>Torontle</strong> answer — the Wordle-style game built from this dictionary.</p>
        <a class="btn-ghost" href="../wordle.html">Play Torontle →</a>
      </div>'''

    if source_url:
        sources_html = f'<p>Specific source for this entry: <a href="{esc(source_url)}" target="_blank" rel="noopener">{esc(source_label or source_url)}</a>. General research sources for the whole dictionary are listed in <a href="../SOURCES.md" target="_blank" rel="noopener">SOURCES.md</a>.</p>'
    else:
        sources_html = '<p>This entry was compiled through general research into Toronto/GTA slang rather than one single citable source — see the full bibliography in <a href="../SOURCES.md" target="_blank" rel="noopener">SOURCES.md</a> and the wider context in our <a href="../history.html">history of Toronto slang</a>.</p>'

    title = f'What Does "{name}" Mean? Toronto Slang Definition | Toronto Mans Dictionary'
    meta_desc = f'{definition} Full definition, example, and origin of "{name}" in Toronto/GTA slang.'
    meta_desc = meta_desc if len(meta_desc) <= 300 else meta_desc[:297] + "..."

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<meta name="keywords" content="what does {esc(name.lower())} mean, {esc(name.lower())} toronto slang, {esc(name.lower())} meaning, toronto slang dictionary">
<link rel="canonical" href="{SITE_URL}/words/{esc(slug)}.html">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#101114">

<meta property="og:type" content="article">
<meta property="og:site_name" content="Toronto Mans Dictionary">
<meta property="og:title" content="What Does &quot;{esc(name)}&quot; Mean? | Toronto Mans Dictionary">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:url" content="{SITE_URL}/words/{esc(slug)}.html">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="What Does &quot;{esc(name)}&quot; Mean In Toronto Slang?">
<meta name="twitter:description" content="{esc(meta_desc)}">

<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍁</text></svg>">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/article.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": {json.dumps(name)},
  "description": {json.dumps(definition)},
  "inDefinedTermSet": "{SITE_URL}/index.html",
  "url": "{SITE_URL}/words/{esc(slug)}.html"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": {json.dumps(f'What does "{name}" mean in Toronto slang?')},
      "acceptedAnswer": {{ "@type": "Answer", "text": {json.dumps(definition)} }}
    }}
  ]
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="../index.html">
      <span class="logo-mark">TO</span>
      <span class="logo-text">Toronto Mans Dictionary</span>
    </a>
    <nav class="header-nav">
      <a href="../index.html#browse">Browse</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../history.html">History</a>
      <a href="../faq.html">FAQ</a>
      <button type="button" class="btn-ghost" data-open-submit-modal>Submit a term</button>
    </nav>
  </div>
</header>

<main class="article-page">
  <div class="wrap article-wrap">

    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Dictionary</a> <span aria-hidden="true">/</span> <span>{esc(name)}</span>
    </nav>

    <article>
      <header class="article-header word-page-header">
        <div class="chip-row">{cat_links}</div>
        <h1>{esc(name)}</h1>
        <p class="article-dek">{esc(definition)}</p>
      </header>

      <h2>How it's used</h2>
      <p>{blurb}</p>
      <p class="term-example word-page-example">“{esc(example)}”</p>

      <h2>Where it comes from</h2>
      <p><strong>Origin:</strong> {esc(origin)}. {onote}</p>

      <h2>Sources</h2>
      {sources_html}
      {torontle_html}
      {related_html}

      <div class="article-cta">
        <a class="btn-ghost" href="../index.html#{esc(slug)}">See it in the full dictionary →</a>
        <a class="btn-ghost" href="../history.html">Read the history of Toronto slang →</a>
      </div>
    </article>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="ad-slot ad-slot-rectangle" id="ad-slot-word-page" aria-hidden="true">
      <span class="ad-slot-label">Advertisement</span>
    </div>
    <nav class="footer-nav" aria-label="Footer">
      <a href="../index.html">Dictionary</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../history.html">History</a>
      <a href="../faq.html">FAQ</a>
    </nav>
    <div class="footer-inner">
      <p>Toronto Mans Dictionary — an independent, fan-made reference. Not affiliated with Urban Dictionary, the City of Toronto, or the TTC.</p>
      <p><a href="../SOURCES.md" target="_blank" rel="noopener">Sources &amp; photo credits</a></p>
    </div>
  </div>
</footer>

<script src="../js/submit-modal.js"></script>
</body>
</html>
'''
    return page


def build_sitemap(terms):
    urls = [
        (f"{SITE_URL}/index.html", "weekly", "1.0"),
        (f"{SITE_URL}/wordle.html", "daily", "0.8"),
        (f"{SITE_URL}/history.html", "monthly", "0.7"),
        (f"{SITE_URL}/faq.html", "monthly", "0.7"),
    ]
    for t in terms:
        urls.append((f"{SITE_URL}/words/{t['slug']}.html", "monthly", "0.6"))

    entries = "\n".join(
        f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for loc, freq, prio in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'


def main():
    terms = json.loads(TERMS_PATH.read_text(encoding="utf-8"))
    terms = sorted(terms, key=lambda t: t["term"].lower())

    # 1. index.html term cards
    cards_html = "\n".join(build_card(t) for t in terms)
    block = BEGIN_MARK + "\n" + cards_html + "\n      " + END_MARK
    index_html = INDEX_PATH.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL)
    if not pattern.search(index_html):
        raise SystemExit(
            "Could not find BEGIN/END GENERATED TERM CARDS markers in index.html. "
            "Add them around the #term-grid contents first."
        )
    INDEX_PATH.write_text(pattern.sub(block, index_html), encoding="utf-8")
    print(f"Wrote {len(terms)} term cards into {INDEX_PATH.relative_to(ROOT)}")

    # 2. words/<slug>.html
    WORDS_DIR.mkdir(exist_ok=True)
    existing_slugs = {p.stem for p in WORDS_DIR.glob("*.html")}
    current_slugs = {t["slug"] for t in terms}
    for t in terms:
        page = build_word_page(t, terms)
        (WORDS_DIR / f"{t['slug']}.html").write_text(page, encoding="utf-8")
    stale = existing_slugs - current_slugs
    for slug in stale:
        (WORDS_DIR / f"{slug}.html").unlink()
    if stale:
        print(f"Removed {len(stale)} stale word page(s): {', '.join(sorted(stale))}")
    print(f"Wrote {len(terms)} word pages into {WORDS_DIR.relative_to(ROOT)}/")

    # 3. sitemap.xml
    SITEMAP_PATH.write_text(build_sitemap(terms), encoding="utf-8")
    print(f"Wrote sitemap.xml with {4 + len(terms)} URLs")


if __name__ == "__main__":
    main()
