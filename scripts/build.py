#!/usr/bin/env python3
"""
Regenerates the static term-card markup inside index.html from data/terms.json.

Why this exists: the dictionary used to be built client-side (JS fetched
terms.json and rendered cards on load). That's invisible to search engines
that don't execute JS, and it's a slower first paint. Instead, the term cards
now live directly in index.html as real HTML (crawlable, no-JS-safe), and
js/app.js enhances that existing markup in place (search/filter/sort/vote)
rather than building it from scratch.

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

BEGIN_MARK = "<!-- BEGIN GENERATED TERM CARDS (run scripts/build.py after editing data/terms.json) -->"
END_MARK = "<!-- END GENERATED TERM CARDS -->"


def strip_quotes(s):
    return re.sub(r'^["“]+|["”]+$', "", s.strip())


def esc(s):
    return html.escape(s, quote=True)


def slugify_id(slug):
    return "term-" + slug


def build_card(term):
    slug = term["slug"]
    categories = term.get("categories", [])
    cat_attr = esc("|".join(categories))
    first_cat = esc(categories[0]) if categories else ""
    example = esc(strip_quotes(term["example"]))
    card_id = slugify_id(slug)
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
        </div>
      </article>'''


def main():
    terms = json.loads(TERMS_PATH.read_text(encoding="utf-8"))
    terms = sorted(terms, key=lambda t: t["term"].lower())
    cards_html = "\n".join(build_card(t) for t in terms)
    block = BEGIN_MARK + "\n" + cards_html + "\n      " + END_MARK

    index_html = INDEX_PATH.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL)
    if not pattern.search(index_html):
        raise SystemExit(
            "Could not find BEGIN/END GENERATED TERM CARDS markers in index.html. "
            "Add them around the #term-grid contents first."
        )
    new_index = pattern.sub(block, index_html)
    INDEX_PATH.write_text(new_index, encoding="utf-8")
    print(f"Wrote {len(terms)} term cards into {INDEX_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
