#!/usr/bin/env python3
"""
Regenerates everything derived from data/terms.json:
  1. The static term-card markup inside index.html (crawlable, no-JS-safe).
  2. One standalone static page per term under words/<slug>.html, each
     targeting that word's own long-tail search ("what does X mean toronto
     slang") with a longer write-up, real internal links, and a sources
     section — not just a copy of the dictionary card.
  3. One hub page per category under categories/<cat-slug>.html ("Toronto
     Money Slang", etc.) — targets category-level searches, distinct content
     from the word pages (curated list + category-specific framing, not a
     copy of any single definition).
  4. all-words.html — a flat, crawl-friendly A-Z link list of every word page.
  5. sitemap.xml, so every generated page is actually indexable.

neighbourhoods.html is real editorial content and is hand-written, not
generated here — see that file directly to edit it.

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
CATEGORIES_DIR = ROOT / "categories"
ALL_WORDS_PATH = ROOT / "all-words.html"
SITEMAP_PATH = ROOT / "sitemap.xml"
NEIGHBOURHOODS_PATH = ROOT / "neighbourhoods.html"  # hand-written, only read for sitemap check

SITE_URL = "https://torontomansdictionary.com"

BEGIN_MARK = "<!-- BEGIN GENERATED TERM CARDS (run scripts/build.py after editing data/terms.json) -->"
END_MARK = "<!-- END GENERATED TERM CARDS -->"

CAT_LINKS_BEGIN = "<!-- BEGIN GENERATED CATEGORY LINKS (run scripts/build.py) -->"
CAT_LINKS_END = "<!-- END GENERATED CATEGORY LINKS -->"

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
    (r"highway|expressway|avenue|area code|municipalit|neighbourhood|amalgamation|scarborough|mississauga", "It's geography slang — shorthand locals use instead of the official name. More GTA geography terms are in the <a href=\"../categories/geography-identity.html\">Geography &amp; Identity category</a>, or see how it maps onto real places in <a href=\"../neighbourhoods.html\">Toronto Slang By Neighbourhood</a>."),
    (r"hockey", "It comes out of Canadian hockey culture rather than the city's immigrant-language history."),
]

DEFAULT_ORIGIN_NOTE = "Like a lot of GTA slang, its exact origin is debated even among people who use it every day — see our <a href=\"../history.html\">full history of Toronto slang</a> for the bigger picture on how this vocabulary formed."

CATEGORY_INTRO = {
    "Geography & Identity": "Toronto slang is obsessed with place — which highway, which area code, which side of Steeles you're on. This is the vocabulary locals use to say exactly where they mean without saying the official name, and it's often the first slang a newcomer to the GTA has to learn just to follow directions.",
    "Getting Around": "Nobody in Toronto calls the TTC or the highways by their full names. This is the shorthand — nicknames for transit and roads that are so normalized locally that the official names sound formal by comparison.",
    "People & Respect": "This category is about how people in the GTA talk about each other — friends, crews, strangers — and how they show (or withhold) respect. A lot of it, like \"mans\" and \"bredren,\" traces directly back to Jamaican Patois via Toronto's Caribbean communities.",
    "Talk & Fillers": "These are the connective words — the tags, interjections and filler phrases that don't carry much meaning on their own but instantly mark how someone from the GTA actually talks, as opposed to how a script might write it.",
    "Hype & Approval": "When something's genuinely good in Toronto slang, there's a whole vocabulary for saying so — from Patois-rooted words like \"peng\" and \"leng\" to general intensifiers like \"mad\" and \"bare.\"",
    "Beef & Bad Vibes": "The flip side of hype vocabulary: words for when something is bad, someone's annoying you, or there's tension. Tone does a lot of the work here — the same word said flat versus shouted can mean mild annoyance or real anger.",
    "Money": "Money slang moves fast through hip-hop and drill culture generally, and Toronto's rap scene has adopted (and sometimes localized) a well-worn set of terms for cash, in amounts small and large.",
    "Culture & Sports": "Words tied to Toronto's culture at large rather than to a specific immigrant-language root — sports (the Raptors' \"We The North\"), music (Drake's OVO), and food (patty, roti) that have become part of the city's shared identity.",
}


def slugify_category(cat):
    return re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")


# Real ad-network banner units (highperformanceformat.com / Adsterra-style
# "atOptions" banner format — static IAB sizes, no popups/redirects). Only
# the two sizes used repeatedly across the generated word/category pages
# live here; the other formats (skyscraper, mobile banner, native banner)
# are hand-placed once each in the non-generated pages.
AD_BANNERS = {
    "rectangle": {"key": "6479608cfcb307756d4ff6a52291ac76", "w": 300, "h": 250},
    "leaderboard": {"key": "b0d876a5bc546839f85bdbd7b4e4425c", "w": 728, "h": 90},
}


def ad_block(kind):
    """A labelled ad row: real banner unit in the middle, empty house-ad
    tiles on either side (filled by js/ads.js when there's room)."""
    ad = AD_BANNERS[kind]
    return f'''<div class="ad-block">
      <p class="ad-caption">Advertisement</p>
      <div class="ad-row">
        <div class="house-ad-slot"></div>
        <div class="ad-unit" data-ad="{kind}" style="width:{ad["w"]}px;height:{ad["h"]}px">
          <script>
            atOptions = {{
              'key' : '{ad["key"]}',
              'format' : 'iframe',
              'height' : {ad["h"]},
              'width' : {ad["w"]},
              'params' : {{}}
            }};
          </script>
          <script src="https://www.highperformanceformat.com/{ad["key"]}/invoke.js"></script>
        </div>
        <div class="house-ad-slot"></div>
      </div>
    </div>'''


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
    # A ring, not a fixed top-N: walk forward through this term's primary
    # category (alphabetical, wrapping around) so that repeatedly clicking
    # the first related word actually traverses every term in the category
    # instead of bouncing between the same handful every time.
    categories = term.get("categories", [])
    if not categories:
        return []
    primary_cat = categories[0]
    cat_list = [t for t in all_terms if primary_cat in t.get("categories", [])]
    if len(cat_list) <= 1:
        return []
    idx = next(i for i, t in enumerate(cat_list) if t["slug"] == term["slug"])
    count = min(n, len(cat_list) - 1)
    return [cat_list[(idx + 1 + i) % len(cat_list)] for i in range(count)]


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
        f'<a class="chip-static" href="../categories/{slugify_category(c)}.html">{esc(c)}</a>'
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

      {ad_block("rectangle")}

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
    {ad_block("leaderboard")}
    <nav class="footer-nav" aria-label="Footer">
      <a href="../index.html">Dictionary</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../history.html">History</a>
      <a href="../faq.html">FAQ</a>
      <a href="../all-words.html">All Words</a>
      <a href="../neighbourhoods.html">Neighbourhoods</a>
    </nav>
    <div class="footer-inner">
      <p>Toronto Mans Dictionary — an independent, fan-made reference. Not affiliated with Urban Dictionary, the City of Toronto, or the TTC.</p>
      <p><a href="../SOURCES.md" target="_blank" rel="noopener">Sources &amp; photo credits</a></p>
    </div>
  </div>
</footer>

<script src="../js/ads.js"></script>
<script src="../js/submit-modal.js"></script>
</body>
</html>
'''
    return page


def build_category_page(cat, cat_terms, all_categories):
    cat_slug = slugify_category(cat)
    intro = CATEGORY_INTRO.get(cat, "Part of the vocabulary documented in the Toronto Mans Dictionary.")
    blurb = CATEGORY_BLURB.get(cat, "")

    items = "\n".join(
        f'          <li><a href="../words/{esc(t["slug"])}.html"><strong>{esc(t["term"])}</strong></a> — {esc(t["definition"])}</li>'
        for t in cat_terms
    )

    other_cats = " ".join(
        f'<a class="chip-static" href="{slugify_category(c)}.html">{esc(c)}</a>'
        for c in all_categories if c != cat
    )

    title = f'Toronto {cat} Slang: {len(cat_terms)} Words, Defined | Toronto Mans Dictionary'
    meta_desc = f'{intro[:230]}'
    if len(meta_desc) > 250:
        meta_desc = meta_desc[:247] + "..."

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="{SITE_URL}/categories/{esc(cat_slug)}.html">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#101114">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Toronto Mans Dictionary">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:url" content="{SITE_URL}/categories/{esc(cat_slug)}.html">

<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍁</text></svg>">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/article.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": {json.dumps(f"Toronto {cat} Slang")},
  "description": {json.dumps(intro)},
  "url": "{SITE_URL}/categories/{esc(cat_slug)}.html",
  "isPartOf": "{SITE_URL}/index.html"
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
      <a href="../index.html">Dictionary</a> <span aria-hidden="true">/</span> <span>{esc(cat)}</span>
    </nav>

    <article>
      <header class="article-header">
        <p class="hero-kicker">Category</p>
        <h1>Toronto {esc(cat)} Slang</h1>
        <p class="article-dek">{esc(intro)}</p>
      </header>

      <p>{esc(blurb)}</p>

      {ad_block("rectangle")}

      <h2>{len(cat_terms)} words in this category</h2>
      <ul class="related-list">
{items}
      </ul>

      <h2>Other categories</h2>
      <div class="chip-row">{other_cats}</div>

      <div class="article-cta">
        <a class="btn-ghost" href="../all-words.html">See every word A-Z →</a>
        <a class="btn-ghost" href="../index.html#browse">Browse the full dictionary →</a>
      </div>
    </article>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <nav class="footer-nav" aria-label="Footer">
      <a href="../index.html">Dictionary</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../history.html">History</a>
      <a href="../faq.html">FAQ</a>
      <a href="../all-words.html">All Words</a>
      <a href="../neighbourhoods.html">Neighbourhoods</a>
    </nav>
    <div class="footer-inner">
      <p>Toronto Mans Dictionary — an independent, fan-made reference. Not affiliated with Urban Dictionary, the City of Toronto, or the TTC.</p>
      <p><a href="../SOURCES.md" target="_blank" rel="noopener">Sources &amp; photo credits</a></p>
    </div>
  </div>
</footer>

<script src="../js/ads.js"></script>
<script src="../js/submit-modal.js"></script>
</body>
</html>
'''
    return page


def build_all_words_page(terms):
    items = "\n".join(
        f'        <li><a href="words/{esc(t["slug"])}.html">{esc(t["term"])}</a></li>'
        for t in terms
    )
    title = f"All {len(terms)} Toronto Slang Words, A-Z | Toronto Mans Dictionary"
    meta_desc = f"Every Toronto and GTA slang word in this dictionary, listed A-Z with a direct link to each word's full definition page — {len(terms)} terms and counting."

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="{SITE_URL}/all-words.html">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#101114">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Toronto Mans Dictionary">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:url" content="{SITE_URL}/all-words.html">

<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍁</text></svg>">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/article.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "All Toronto Slang Words",
  "url": "{SITE_URL}/all-words.html",
  "numberOfItems": {len(terms)}
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html">
      <span class="logo-mark">TO</span>
      <span class="logo-text">Toronto Mans Dictionary</span>
    </a>
    <nav class="header-nav">
      <a href="index.html#browse">Browse</a>
      <a href="wordle.html">Torontle</a>
      <a href="history.html">History</a>
      <a href="faq.html">FAQ</a>
      <button type="button" class="btn-ghost" data-open-submit-modal>Submit a term</button>
    </nav>
  </div>
</header>

<main class="article-page">
  <div class="wrap article-wrap">

    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="index.html">Dictionary</a> <span aria-hidden="true">/</span> <span>All Words</span>
    </nav>

    <header class="article-header">
      <p class="hero-kicker">Every entry, one list</p>
      <h1>All {len(terms)} Words, A-Z</h1>
      <p class="article-dek">A flat, no-frills list of every word in the Toronto Mans Dictionary. Each one links straight to its own full write-up.</p>
    </header>

    {ad_block("leaderboard")}

    <ul class="all-words-list">
{items}
    </ul>

    <div class="article-cta">
      <a class="btn-ghost" href="index.html#browse">Browse with search &amp; filters →</a>
      <a class="btn-ghost" href="neighbourhoods.html">Slang by neighbourhood →</a>
    </div>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <nav class="footer-nav" aria-label="Footer">
      <a href="index.html">Dictionary</a>
      <a href="wordle.html">Torontle</a>
      <a href="history.html">History</a>
      <a href="faq.html">FAQ</a>
      <a href="all-words.html">All Words</a>
      <a href="neighbourhoods.html">Neighbourhoods</a>
    </nav>
    <div class="footer-inner">
      <p>Toronto Mans Dictionary — an independent, fan-made reference. Not affiliated with Urban Dictionary, the City of Toronto, or the TTC.</p>
      <p><a href="SOURCES.md" target="_blank" rel="noopener">Sources &amp; photo credits</a></p>
    </div>
  </div>
</footer>

<script src="js/ads.js"></script>
<script src="js/submit-modal.js"></script>
</body>
</html>
'''
    return page


def build_category_links_block(all_categories):
    links = "\n".join(
        f'          <a class="chip-static" href="categories/{slugify_category(c)}.html">{esc(c)}</a>'
        for c in all_categories
    )
    return f'''{CAT_LINKS_BEGIN}
        <p class="category-links-label">Or jump straight to a category:</p>
        <div class="chip-row">
{links}
        </div>
        {CAT_LINKS_END}'''


def build_sitemap(terms, categories):
    urls = [
        (f"{SITE_URL}/index.html", "weekly", "1.0"),
        (f"{SITE_URL}/wordle.html", "daily", "0.8"),
        (f"{SITE_URL}/history.html", "monthly", "0.7"),
        (f"{SITE_URL}/faq.html", "monthly", "0.7"),
        (f"{SITE_URL}/all-words.html", "weekly", "0.7"),
    ]
    if NEIGHBOURHOODS_PATH.exists():
        urls.append((f"{SITE_URL}/neighbourhoods.html", "monthly", "0.7"))
    for c in categories:
        urls.append((f"{SITE_URL}/categories/{slugify_category(c)}.html", "monthly", "0.65"))
    for t in terms:
        urls.append((f"{SITE_URL}/words/{t['slug']}.html", "monthly", "0.6"))

    entries = "\n".join(
        f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for loc, freq, prio in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n', len(urls)


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
    index_html = pattern.sub(block, index_html)
    print(f"Wrote {len(terms)} term cards into {INDEX_PATH.relative_to(ROOT)}")

    categories = sorted({c for t in terms for c in t.get("categories", [])})

    # 1b. static category-links row in index.html
    cat_block = build_category_links_block(categories)
    cat_pattern = re.compile(re.escape(CAT_LINKS_BEGIN) + r".*?" + re.escape(CAT_LINKS_END), re.DOTALL)
    if not cat_pattern.search(index_html):
        raise SystemExit(
            "Could not find BEGIN/END GENERATED CATEGORY LINKS markers in index.html."
        )
    index_html = cat_pattern.sub(cat_block, index_html)
    INDEX_PATH.write_text(index_html, encoding="utf-8")
    print(f"Wrote {len(categories)} category links into {INDEX_PATH.relative_to(ROOT)}")

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

    # 3. categories/<cat-slug>.html
    CATEGORIES_DIR.mkdir(exist_ok=True)
    existing_cat_slugs = {p.stem for p in CATEGORIES_DIR.glob("*.html")}
    current_cat_slugs = {slugify_category(c) for c in categories}
    for c in categories:
        cat_terms = [t for t in terms if c in t.get("categories", [])]
        page = build_category_page(c, cat_terms, categories)
        (CATEGORIES_DIR / f"{slugify_category(c)}.html").write_text(page, encoding="utf-8")
    stale_cats = existing_cat_slugs - current_cat_slugs
    for slug in stale_cats:
        (CATEGORIES_DIR / f"{slug}.html").unlink()
    print(f"Wrote {len(categories)} category pages into {CATEGORIES_DIR.relative_to(ROOT)}/")

    # 4. all-words.html
    ALL_WORDS_PATH.write_text(build_all_words_page(terms), encoding="utf-8")
    print(f"Wrote {ALL_WORDS_PATH.relative_to(ROOT)}")

    # 5. sitemap.xml
    sitemap_xml, url_count = build_sitemap(terms, categories)
    SITEMAP_PATH.write_text(sitemap_xml, encoding="utf-8")
    print(f"Wrote sitemap.xml with {url_count} URLs")
    if not NEIGHBOURHOODS_PATH.exists():
        print("Note: neighbourhoods.html doesn't exist yet — not included in sitemap.xml until it's created.")


if __name__ == "__main__":
    main()
