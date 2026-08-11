#!/usr/bin/env python3
"""
Generates the Toronto Guide section (guide/*.html) — general city content
(history, neighbourhoods, landmarks, food, sports, festivals,
multiculturalism) distinct from the slang dictionary. Each page's prose is
authored below as data, not derived from data/terms.json, because this is
genuinely different content, not a reformatting of the dictionary.

Run after editing PAGES below:
    python3 scripts/build_guide.py

Does NOT touch data/terms.json, index.html, words/, categories/, or
sitemap.xml — run scripts/build.py separately for that (it also folds
guide/*.html into the sitemap if this has been run at least once).
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE_DIR = ROOT / "guide"
SITE_URL = "https://torontomansdictionary.com"

AD_LEADERBOARD_KEY = "b0d876a5bc546839f85bdbd7b4e4425c"
AD_RECTANGLE_KEY = "6479608cfcb307756d4ff6a52291ac76"


def esc(s):
    return html.escape(s, quote=True)


def commons(filename):
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{filename}"


def ad_leaderboard():
    return f'''<div class="ad-block">
      <p class="ad-caption">Advertisement</p>
      <div class="ad-row">
        <div class="house-ad-slot"></div>
        <div class="ad-unit" data-ad="leaderboard" style="width:728px;height:90px">
          <script>
            atOptions = {{
              'key' : '{AD_LEADERBOARD_KEY}',
              'format' : 'iframe',
              'height' : 90,
              'width' : 728,
              'params' : {{}}
            }};
          </script>
          <script src="https://www.highperformanceformat.com/{AD_LEADERBOARD_KEY}/invoke.js"></script>
        </div>
        <div class="house-ad-slot"></div>
      </div>
    </div>'''


def ad_rectangle():
    return f'''<div class="ad-block">
      <p class="ad-caption">Advertisement</p>
      <div class="ad-row">
        <div class="house-ad-slot"></div>
        <div class="ad-unit" data-ad="rectangle" style="width:300px;height:250px">
          <script>
            atOptions = {{
              'key' : '{AD_RECTANGLE_KEY}',
              'format' : 'iframe',
              'height' : 250,
              'width' : 300,
              'params' : {{}}
            }};
          </script>
          <script src="https://www.highperformanceformat.com/{AD_RECTANGLE_KEY}/invoke.js"></script>
        </div>
        <div class="house-ad-slot"></div>
      </div>
    </div>'''


def figure(filename, alt, credit):
    return f'''<figure class="guide-photo">
        <img src="{commons(filename)}" alt="{esc(alt)}" loading="lazy">
        <figcaption>{credit}</figcaption>
      </figure>'''


# ---------------------------------------------------------------------------
# Page data. `sections` is a list of (heading_or_None, html_body) tuples;
# body strings are already-safe HTML (hand-written, not user input).
# ---------------------------------------------------------------------------

PAGES = [
    {
        "slug": "history",
        "title": "The History of Toronto: From York to the 6ix",
        "kicker": "1793 to now",
        "h1": "The History of Toronto",
        "dek": "How a fort on Lake Ontario became Canada's largest city — founding, war, railways, amalgamation, and the immigration waves that reshaped it.",
        "meta_desc": "The real history of Toronto: its 1793 founding as York, the War of 1812, 19th-century railway boom, the 1998 amalgamation of six municipalities, and how immigration built the modern city.",
        "keywords": "history of Toronto, Toronto founded York 1793, Toronto amalgamation 1998, Toronto history timeline",
        "hero_img": "Toronto_skyline_(2012).jpg",
        "hero_alt": "The Toronto skyline seen across the water",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto is old enough to have burned down once and been renamed twice, and young enough that its current shape — one city, not six — dates to 1998, well within living memory. Here\'s the actual timeline, not the postcard version.</p>'),
            ("From York to Toronto (1793–1834)", '<p>Toronto started as <strong>York</strong>, a garrison town founded in 1793 by John Graves Simcoe, Lieutenant Governor of Upper Canada, who made it the colonial capital. It was named for Prince Frederick, Duke of York and Albany. During the War of 1812, American forces captured and burned York in April 1813 — part of why, when the British later burned Washington, D.C., it was framed as retaliation. York was incorporated as the City of Toronto on March 6, 1834, with a population of roughly 9,000, taking a version of its Indigenous Mohawk/Wyandot-derived name back.</p>'),
            ("Rail, industry, and rapid growth (1850s–1900s)", '<p>Railways — the Grand Trunk and others — turned Toronto into central Canada\'s transport and financial hub through the second half of the 19th century, pulling in immigrants and industry fast enough that the city earned the nickname <a href="../words/hogtown.html">Hogtown</a>, partly for its dominant meatpacking industry and partly as a political jab from smaller Ontario towns annoyed at Toronto\'s outsized influence in the provincial legislature.</p>'),
            ("Amalgamation: six cities become one (1998)", '<p>For most of the 20th century, "Toronto" was actually a cluster of separate municipalities — old Toronto, <strong>North York</strong>, <strong>Etobicoke</strong>, <strong>Scarborough</strong>, <strong>York</strong>, and <strong>East York</strong> — governed together loosely as Metropolitan Toronto starting in 1953. On January 1, 1998, the Ontario provincial government forced a full merger, creating the single "megacity" that exists today. It\'s the reason locals still identify strongly with their old municipality (ask anyone from Scarborough), and it\'s the direct origin of Toronto\'s most famous modern nickname — see <a href="../words/the-six.html">The Six / The 6ix</a>, which refers to exactly these six former cities.</p>'),
            ("The immigration waves that built modern Toronto", '<p>The amalgamation is the political story; the more consequential one is demographic. Waves of immigration — Caribbean and especially Jamaican through the 1960s–80s, Somali following the 1991 civil war, and continuous South Asian, East Asian, Filipino, Latin American and Eastern European immigration since — transformed Toronto\'s inner suburbs into some of the most ethnically dense neighbourhoods anywhere. That density is the direct cause of the vocabulary this whole site documents; read the <a href="../history.html">full history of Toronto slang</a> for that side of the story specifically, or <a href="multiculturalism.html">how multicultural Toronto actually is</a> for the numbers.</p>'),
        ],
        "sources": [
            ("Wikipedia — History of Toronto", "https://en.wikipedia.org/wiki/History_of_Toronto"),
            ("Wikipedia — Amalgamation of Toronto", "https://en.wikipedia.org/wiki/Amalgamation_of_Toronto"),
            ("Wikipedia — York, Upper Canada", "https://en.wikipedia.org/wiki/York,_Upper_Canada"),
            ("historyoftoronto.ca — Understanding when Toronto amalgamated and its impact", "https://historyoftoronto.ca/blog/understanding-when-toronto-amalgamated-and-its-impact-on-the-city"),
        ],
        "related_words": ["hogtown", "the-six", "t-dot"],
    },
    {
        "slug": "neighbourhoods",
        "title": "Toronto Neighbourhoods Guide: Downtown, Kensington & Beyond",
        "kicker": "The city, area by area",
        "h1": "Toronto Neighbourhoods Guide",
        "dek": "A general guide to Toronto's neighbourhoods — where downtown actually is, what Kensington Market and the Distillery District are like, and how the inner suburbs fit together. (For the slang side of specific neighbourhoods, see our dedicated page on that.)",
        "meta_desc": "A guide to Toronto's neighbourhoods: downtown core, Kensington Market, the Distillery District, Yorkville, The Beaches, Liberty Village, and the inner suburbs — what each one actually is.",
        "keywords": "Toronto neighbourhoods, Kensington Market, Distillery District, downtown Toronto, Toronto areas guide",
        "hero_img": "Kensington_Market_Toronto_August_2017_03.jpg",
        "hero_alt": "A colourful street in Kensington Market, Toronto",
        "hero_credit": "Kensington Market — Arild Vågen, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto is a city of neighbourhoods more than a single downtown core — a legacy of the 1998 amalgamation of six formerly separate municipalities (see the <a href="history.html">full history</a>). Here\'s a general-purpose map in words.</p>'),
            ("Downtown core", '<p>The financial and entertainment district around Bay Street, Yonge-Dundas Square, and the CN Tower — Toronto\'s skyline, and the part most visitors see first. Nathan Phillips Square and Old/New City Hall anchor its civic centre.</p>'),
            ("Kensington Market", '<p>A dense, low-rise, intensely multicultural market neighbourhood just west of downtown — Portuguese bakeries, Caribbean grocers, vintage shops and vegan cafés on the same block. One of the most walkable, distinct neighbourhoods in the city and a genuine reflection of Toronto\'s diversity rather than a curated tourist version of it.</p>'),
            ("The Distillery District", '<p>A pedestrian-only historic district of restored Victorian-era industrial buildings — formerly the Gooderham and Worts distillery, once the largest in the British Empire — now full of galleries, restaurants and shops. Cobblestone streets, no cars, and a well-known holiday market in December.</p>'),
            ("Yorkville, The Beaches, Liberty Village", '<p>Three very different slices of the city: <strong>Yorkville</strong> is upscale shopping and old Victorian rowhouses turned boutiques; <strong>The Beaches</strong> is a laid-back lakeside neighbourhood with a literal boardwalk; <strong>Liberty Village</strong> is a converted industrial area now full of condos, startups and gyms.</p>'),
            ("The inner suburbs: Scarborough, Etobicoke, North York, York, East York", '<p>The five other former municipalities that merged into Toronto in 1998. Together they hold most of the city\'s population and, not incidentally, most of the immigration-driven cultural and linguistic history documented on this site — see our dedicated piece on <a href="../neighbourhoods.html">Toronto slang by neighbourhood</a> for how Jane and Finch, Rexdale, Scarborough and Malvern specifically shaped the vocabulary in this dictionary.</p>'),
        ],
        "sources": [
            ("Wikipedia — Neighbourhoods of Toronto", "https://en.wikipedia.org/wiki/List_of_Toronto_neighbourhoods"),
            ("Wikipedia — Distillery District", "https://en.wikipedia.org/wiki/Distillery_District"),
            ("Wikipedia — Kensington Market", "https://en.wikipedia.org/wiki/Kensington_Market"),
        ],
        "related_words": ["scarbs", "jane-and-finch", "rexdale", "malvern"],
    },
    {
        "slug": "landmarks",
        "title": "Toronto Landmarks: CN Tower, Casa Loma, ROM & More",
        "kicker": "What to actually look at",
        "h1": "Toronto Landmarks",
        "dek": "The buildings and sites that define Toronto's skyline and street level — from the CN Tower down to a 19th-century castle in midtown.",
        "meta_desc": "A guide to Toronto's landmarks: the CN Tower, Casa Loma, the Royal Ontario Museum, St. Lawrence Market, Nathan Phillips Square and the Distillery District — history and context for each.",
        "keywords": "Toronto landmarks, CN Tower, Casa Loma, Royal Ontario Museum, St Lawrence Market, Toronto attractions",
        "hero_img": "Toronto-CN-tower-and-Canadian-flag-skyline.jpg",
        "hero_alt": "The CN Tower rising above the Toronto skyline",
        "hero_credit": "CN Tower and Toronto skyline — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto\'s skyline is recognizable mostly because of one building, but the city\'s actual landmarks — the ones locals reference constantly — go well beyond it.</p>'),
            ("The CN Tower", '<p>Completed in 1975, the CN Tower stands 553.3 metres tall and was the tallest free-standing structure on Earth for 34 years, until 2007. It was built by Canadian National Railway partly as a broadcast antenna and partly as a statement about what Canadian engineering could do. It remains the single most recognizable symbol of the city, visible from most of the GTA.</p>' + figure("Toronto-CN-tower-and-Canadian-flag-skyline.jpg", "The CN Tower against the Toronto skyline", "CN Tower — Wikimedia Commons, CC BY-SA 4.0")),
            ("Casa Loma", '<p>A genuine Gothic Revival castle in midtown Toronto, built from 1911 to 1914 for financier Sir Henry Pellatt. It\'s now a historic house museum with gardens, secret passages, and a conservatory — one of the few places in North America where "there\'s a castle" is a true, unqualified statement about a major city.</p>' + figure("Casa_Loma,_Toronto,_Ontario_(29709454210).jpg", "Casa Loma, a Gothic Revival castle in midtown Toronto", "Casa Loma — Wikimedia Commons, Creative Commons licensed")),
            ("Royal Ontario Museum (ROM)", '<p>Canada\'s largest museum, opened in 1914, holding over 18 million items across art, world culture and natural history. Its most talked-about feature isn\'t inside the collection — it\'s the building itself: the <strong>Michael Lee-Chin Crystal</strong>, a jagged aluminum-and-glass extension designed by Daniel Libeskind and opened in 2007, which still divides opinion on Toronto architecture message boards.</p>' + figure("Michael_Lee-Chin_Crystal,_Daniel_Libeskind,_2007_-_Royal_Ontario_Museum,_Toronto_(1277497687).jpg", "The Michael Lee-Chin Crystal addition to the Royal Ontario Museum", "ROM / Michael Lee-Chin Crystal — Wikimedia Commons, CC BY-SA 2.0")),
            ("St. Lawrence Market", '<p>A working public market on Front Street dating back to the early 19th century, repeatedly ranked among the best food markets in the world. Its signature order is the peameal bacon sandwich — officially declared Toronto\'s signature dish in 2016, and a direct callback to the meatpacking industry that gave the city its <a href="../words/hogtown.html">Hogtown</a> nickname in the first place.</p>' + figure("St_Lawrence_Market,_Toronto,_West_partial_view_20170417_1.jpg", "St. Lawrence Market in Toronto", "St. Lawrence Market — Wikimedia Commons, Creative Commons licensed")),
            ("Nathan Phillips Square & City Hall", '<p>Toronto\'s civic square, home to the distinctive curved twin towers of the current City Hall (opened 1965) and the giant illuminated TORONTO sign that shows up in basically every tourist photo of the city. It\'s also where most large public gatherings, rallies and the Raptors\' 2019 championship celebration happened.</p>' + figure("Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg", "Nathan Phillips Square and Toronto City Hall", "Nathan Phillips Square — City of Toronto via Wikimedia Commons, CC BY 2.0")),
            ("The Distillery District", '<p>See our <a href="neighbourhoods.html">neighbourhoods guide</a> for the full picture — but it\'s worth listing as a landmark in its own right: a completely car-free historic district of restored Victorian industrial buildings, once the largest distillery in the British Empire.</p>'),
        ],
        "sources": [
            ("Wikipedia — CN Tower", "https://en.wikipedia.org/wiki/CN_Tower"),
            ("Wikipedia — Casa Loma", "https://en.wikipedia.org/wiki/Casa_Loma"),
            ("Wikipedia — Royal Ontario Museum", "https://en.wikipedia.org/wiki/Royal_Ontario_Museum"),
            ("Wikipedia — St. Lawrence Market", "https://en.wikipedia.org/wiki/St._Lawrence_Market"),
            ("Wikipedia — Nathan Phillips Square", "https://en.wikipedia.org/wiki/Nathan_Phillips_Square"),
        ],
        "related_words": ["hogtown", "the-six"],
    },
    {
        "slug": "food",
        "title": "Toronto Food Culture: What the City Actually Eats",
        "kicker": "200+ cuisines, one city",
        "h1": "Toronto Food Culture",
        "dek": "Toronto's food scene isn't one cuisine with some diversity mixed in — it's genuinely built from over 200 cuisines. Here's what that actually looks like on the ground.",
        "meta_desc": "A guide to Toronto's food culture: the peameal bacon sandwich, Jamaican patties, St. Lawrence and Kensington markets, and how 200+ cuisines built the city's actual food identity.",
        "keywords": "Toronto food, Toronto food culture, peameal bacon sandwich, Toronto multicultural food, St Lawrence Market food",
        "hero_img": "St_Lawrence_Market,_Toronto,_West_partial_view_20170417_1.jpg",
        "hero_alt": "St. Lawrence Market, Toronto's historic food market",
        "hero_credit": "St. Lawrence Market — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto restaurants represent more than 200 cuisines from communities spanning some 140 ethnic backgrounds — not a marketing line, just what the city\'s food map actually looks like once you leave any single neighbourhood.</p>'),
            ("The peameal bacon sandwich", '<p>Toronto\'s official signature dish (declared in 2016): thick-cut, cornmeal-crusted back bacon on a soft bun, sold at <a href="landmarks.html">St. Lawrence Market</a> since the 19th century. It\'s a direct product of the same meatpacking boom that got the city nicknamed <a href="../words/hogtown.html">Hogtown</a> — the dish and the nickname share an origin story.</p>'),
            ("The Jamaican patty", '<p>A flaky, curry-coloured pastry filled with spiced beef, chicken or vegetables, sold at corner stores across the city — as ordinary a Toronto lunch as a hot dog is in New York. It arrived with Caribbean immigration through the 1960s–80s, the same wave that shaped much of the <a href="../history.html">slang documented on this site</a>. Full dictionary entry: <a href="../words/patty.html">Patty</a>.</p>'),
            ("Kensington Market and St. Lawrence Market", '<p>Toronto\'s two defining food markets, and near-opposites in character. <strong>St. Lawrence Market</strong> is a formal, historic public market — vendors, stalls, fixed hours. <strong>Kensington Market</strong> is looser and more street-level: Portuguese bakeries, Caribbean grocers, Asian noodle shops and vegan cafés on the same block, reflecting the neighbourhood\'s layered immigration history directly.</p>' + figure("Kensington_Market_Toronto_August_2017_03.jpg", "A street in Kensington Market, Toronto", "Kensington Market — Arild Vågen, CC BY-SA 4.0")),
            ("Roti, and the wider Caribbean and South Asian food scene", '<p>A Caribbean flatbread wrapped around curried meat, chickpeas or vegetables, especially common in Scarborough — full entry: <a href="../words/roti.html">Roti</a>. It sits alongside a much larger South Asian and Caribbean food scene across Scarborough and the inner suburbs that rarely makes "best of Toronto" lists aimed at tourists, despite being some of the most consistently excellent food in the city.</p>'),
        ],
        "sources": [
            ("Michelin Guide — 6 Iconic Toronto Foods You Need to Try", "https://guide.michelin.com/us/en/article/dining-out/6-iconic-toronto-foods-you-need-to-try"),
            ("Wikipedia — Cuisine of Toronto (via Toronto article)", "https://en.wikipedia.org/wiki/Toronto"),
        ],
        "related_words": ["patty", "roti", "hogtown"],
    },
    {
        "slug": "sports",
        "title": "Toronto Sports Culture: Raptors, Leafs, Jays & More",
        "kicker": "We The North, and everyone else",
        "h1": "Toronto Sports Culture",
        "dek": "Toronto is one of a handful of cities with a major team in every big North American league — hockey, basketball, baseball, football, and soccer, all headquartered a few kilometres apart downtown.",
        "meta_desc": "A guide to Toronto's sports teams and culture: the Maple Leafs, Raptors, Blue Jays, Argonauts and Toronto FC — history, championships, and why We The North became a citywide identity.",
        "keywords": "Toronto sports, Toronto Raptors, Toronto Maple Leafs, Toronto Blue Jays, We The North, Toronto sports teams",
        "hero_img": "Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg",
        "hero_alt": "Rogers Centre, home of the Toronto Blue Jays",
        "hero_credit": "Rogers Centre — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto fields a team in every major North American professional league, almost all of it owned by the same company (MLSE) and clustered within walking distance of each other downtown.</p>'),
            ("Toronto Maple Leafs (NHL)", '<p>Founded in 1917, one of the NHL\'s "Original Six" franchises, with 13 Stanley Cups — though none since 1967, a drought long enough to be its own running joke across Canada. They play at Scotiabank Arena, seating roughly 19,800.</p>'),
            ("Toronto Raptors (NBA)", '<p>Founded in 1995 as the NBA\'s attempt to bring basketball back to Canada. Their 2019 championship run produced the slogan that became a citywide identity well beyond basketball fans — full entry: <a href="../words/we-the-north.html">We The North</a>, unveiled in April 2014 as marketing and adopted almost immediately as something closer to civic pride.</p>'),
            ("Toronto Blue Jays (MLB)", '<p>Founded in 1976, Canada\'s only MLB team, playing at Rogers Centre (formerly SkyDome) — the first stadium in the world with a fully retractable roof when it opened in 1989. Their back-to-back 1992 and 1993 World Series wins remain the only World Series titles ever won by a non-U.S. team.</p>' + figure("Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg", "Rogers Centre, home of the Toronto Blue Jays", "Rogers Centre — Wikimedia Commons, Creative Commons licensed")),
            ("Toronto Argonauts (CFL)", '<p>Founded in 1873 — one of the oldest sports franchises in North America, professional or otherwise — and the most decorated team in Canadian Football League history, with a record number of Grey Cup championships.</p>'),
            ("Toronto FC (MLS)", '<p>Plays at BMO Field, Canada\'s first soccer-specific stadium, at Exhibition Place near the lakeshore.</p>'),
        ],
        "sources": [
            ("Wikipedia — Toronto Maple Leafs", "https://en.wikipedia.org/wiki/Toronto_Maple_Leafs"),
            ("Wikipedia — Toronto Argonauts", "https://en.wikipedia.org/wiki/Toronto_Argonauts"),
            ("Wikipedia — History of the Toronto Blue Jays", "https://en.wikipedia.org/wiki/History_of_the_Toronto_Blue_Jays"),
            ("Wikipedia — Toronto FC", "https://en.wikipedia.org/wiki/Toronto_FC"),
        ],
        "related_words": ["we-the-north"],
    },
    {
        "slug": "festivals",
        "title": "Toronto Festivals: Caribana, TIFF, Pride & Nuit Blanche",
        "kicker": "The calendar runs all year",
        "h1": "Toronto Festivals & Events",
        "dek": "From the largest Caribbean carnival in North America to one of the world's biggest film festivals, Toronto's event calendar is packed almost year-round.",
        "meta_desc": "A guide to Toronto's major festivals: Caribana / Toronto Caribbean Carnival, TIFF, Pride Toronto, and Nuit Blanche — history, scale, and what each actually is.",
        "keywords": "Toronto festivals, Caribana, Toronto Caribbean Carnival, TIFF Toronto International Film Festival, Pride Toronto, Nuit Blanche",
        "hero_img": "Caribana_Toronto_2011_(2).jpg",
        "hero_alt": "Costumed performers at the Toronto Caribbean Carnival (Caribana)",
        "hero_credit": "Caribana Toronto — Ruth Choi, CC BY-SA 2.0",
        "sections": [
            (None, '<p>Toronto\'s festival calendar is dense enough that "quiet weekend downtown" is a fairly rare occurrence between June and September.</p>'),
            ("Caribana / Toronto Caribbean Carnival", '<p>Founded in 1967 by Toronto\'s Caribbean community as a gift to Canada\'s Centennial, held every August, and now the largest Caribbean festival in North America and one of the largest outdoor festivals on the continent, drawing well over a million visitors. It celebrates the 1838 emancipation of enslaved people across the British Caribbean, and its costumes, music and scale trace directly back to Trinidad Carnival traditions brought over by Caribbean immigrants — the same community whose Jamaican Patois shaped much of <a href="../history.html">Toronto slang</a>.</p>' + figure("Caribana_Toronto_2011_(2).jpg", "Costumed performers at Toronto's Caribana parade", "Caribana Toronto 2011 — Ruth Choi, CC BY-SA 2.0")),
            ("TIFF (Toronto International Film Festival)", '<p>Held annually in early September, TIFF is one of the largest publicly attended film festivals in the world and a major awards-season launchpad — films that premiere well at TIFF are reliably in the following year\'s Oscar conversation.</p>'),
            ("Pride Toronto", '<p>A month of programming through June, anchored by a parade down Yonge Street that draws over a million spectators, centred on the Church and Wellesley Village.</p>'),
            ("Nuit Blanche", '<p>An overnight, free-admission contemporary art event held once a year, turning stretches of the city into an all-night outdoor gallery.</p>'),
        ],
        "sources": [
            ("Wikipedia — History of Caribana", "https://en.wikipedia.org/wiki/History_of_Caribana"),
            ("Wikipedia — Caribana", "https://en.wikipedia.org/wiki/Caribana"),
            ("Destination Toronto — Toronto Caribbean Carnival", "https://www.destinationtoronto.com/events/annual-festivals-and-events/toronto-caribbean-carnival/"),
        ],
        "related_words": ["big-up", "one-love"],
    },
    {
        "slug": "multiculturalism",
        "title": "Toronto's Multiculturalism: The Numbers Behind the Reputation",
        "kicker": "Not just a slogan",
        "h1": "Toronto's Multiculturalism, By The Numbers",
        "dek": "Toronto's reputation as one of the most diverse cities on Earth isn't marketing copy — the actual demographic numbers back it up, and they're the direct reason this dictionary exists at all.",
        "meta_desc": "The real numbers behind Toronto's reputation as the world's most diverse city: immigrant population share, visible minority statistics, and how many languages are actually spoken.",
        "keywords": "Toronto multiculturalism, Toronto diversity statistics, most diverse city in the world, Toronto immigrant population",
        "hero_img": "Kensington_Market_Toronto_August_2017_03.jpg",
        "hero_alt": "Kensington Market, one of Toronto's most multicultural neighbourhoods",
        "hero_credit": "Kensington Market — Arild Vågen, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto has been named the most diverse city in the world by both the United Nations and the BBC. That\'s not a slogan — it\'s the direct precondition for everything else on this site.</p>'),
            ("The immigrant population", '<p>According to the 2016 census, <strong>49% of Toronto\'s population</strong> was born outside Canada — just under half the city, among the highest immigrant shares of any major city on Earth, trailing only Miami as an immigrant-gateway city. Toronto alone accounts for roughly <strong>36% of Canada\'s entire immigrant population</strong>.</p>'),
            ("Visible minority population and language diversity", '<p>By the 2021 census, Toronto\'s visible minority population was about <strong>1.54 million people — 55.7% of the city\'s total population</strong>. The Toronto region is home to people from an estimated <strong>250 countries</strong>, speaking somewhere between <strong>160 and 190 languages</strong>, with over 250 distinct ethnicities represented.</p>'),
            ("Why this is the whole premise of this site", '<p>Density this high, sustained across multiple immigration waves concentrated in specific inner-suburb neighbourhoods, is exactly the mechanism linguists point to for how <a href="../history.html#mte">Multicultural Toronto English</a> — what this whole dictionary documents — actually formed. The numbers on this page aren\'t background trivia; they\'re the direct cause of every entry in the <a href="../index.html#browse">dictionary</a> itself.</p>'),
        ],
        "sources": [
            ("Wikipedia — Demographics of Toronto", "https://en.wikipedia.org/wiki/Demographics_of_Toronto"),
            ("Statistics Canada — Ethnocultural diversity in Canadian cities", "https://www.statcan.gc.ca/o1/en/plus/7238-ethnocultural-diversity-canadian-cities"),
            ("Study Abroad Foundation — Why Toronto is the most multicultural city in the world", "https://www.studyabroadfoundation.org/blogs/why-toronto-most-multicultural-city-world"),
        ],
        "related_words": ["mans", "wagwan", "wallahi"],
    },
]


def build_page(page, all_pages):
    slug = page["slug"]
    body_html = "\n".join(
        (f'<h2>{esc(heading)}</h2>\n{body}' if heading else body)
        for heading, body in page["sections"]
    )
    sources_html = "\n".join(
        f'<li><a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a></li>'
        for label, url in page["sources"]
    )
    related_html = ""
    if page.get("related_words"):
        links = " ".join(
            f'<a class="chip-static" href="../words/{esc(w)}.html">{esc(w.replace("-", " ").title())}</a>'
            for w in page["related_words"]
        )
        related_html = f'''
      <h2>Related dictionary terms</h2>
      <div class="chip-row">{links}</div>'''

    other_pages = [p for p in all_pages if p["slug"] != slug]
    other_links = "\n".join(
        f'          <li><a href="{esc(p["slug"])}.html">{esc(p["h1"])}</a> — {esc(p["dek"][:80].rsplit(" ", 1)[0])}…</li>'
        for p in other_pages
    )

    title = f"{page['title']} | Toronto Mans Dictionary"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(page['meta_desc'])}">
<meta name="keywords" content="{esc(page['keywords'])}">
<link rel="canonical" href="{SITE_URL}/guide/{esc(slug)}.html">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#101114">
<link rel="preconnect" href="https://www.highperformanceformat.com">
<link rel="preconnect" href="https://commons.wikimedia.org">

<meta property="og:type" content="article">
<meta property="og:site_name" content="Toronto Mans Dictionary">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['meta_desc'])}">
<meta property="og:url" content="{SITE_URL}/guide/{esc(slug)}.html">
<meta property="og:image" content="{commons(page['hero_img'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(page['title'])}">
<meta name="twitter:description" content="{esc(page['meta_desc'])}">
<meta name="twitter:image" content="{commons(page['hero_img'])}">

<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍁</text></svg>">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/article.css">
<link rel="stylesheet" href="../css/guide.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(page['title'])},
  "description": {json.dumps(page['meta_desc'])},
  "author": {{ "@type": "Organization", "name": "Toronto Mans Dictionary" }},
  "publisher": {{ "@type": "Organization", "name": "Toronto Mans Dictionary" }},
  "mainEntityOfPage": "{SITE_URL}/guide/{esc(slug)}.html",
  "image": "{commons(page['hero_img'])}",
  "datePublished": "2026-08-11",
  "dateModified": "2026-08-11"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Dictionary", "item": "{SITE_URL}/index.html" }},
    {{ "@type": "ListItem", "position": 2, "name": "Toronto Guide", "item": "{SITE_URL}/guide/index.html" }},
    {{ "@type": "ListItem", "position": 3, "name": {json.dumps(page['h1'])}, "item": "{SITE_URL}/guide/{esc(slug)}.html" }}
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
      <a href="../quiz.html">Quiz</a>
      <a href="../history.html">Slang History</a>
      <a href="index.html" class="active">Guide</a>
      <button type="button" class="btn-ghost" data-open-submit-modal>Submit a term</button>
    </nav>
  </div>
</header>

<main class="article-page">
  <div class="wrap article-wrap">

    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Dictionary</a> <span aria-hidden="true">/</span> <a href="index.html">Guide</a> <span aria-hidden="true">/</span> <span>{esc(page['h1'])}</span>
    </nav>

    <article>
      <header class="article-header">
        <p class="hero-kicker">{esc(page['kicker'])}</p>
        <h1>{esc(page['h1'])}</h1>
        <p class="article-dek">{esc(page['dek'])}</p>
      </header>

      {figure(page['hero_img'], page['hero_alt'], page['hero_credit'])}

      {ad_leaderboard()}

      {body_html}

      {ad_rectangle()}

      <h2>Sources</h2>
      <ul class="source-list">
{sources_html}
      </ul>
      {related_html}

      <h2>More in the Toronto Guide</h2>
      <ul class="related-list">
{other_links}
      </ul>

      <div class="article-cta">
        <a class="btn-ghost" href="../index.html#browse">Browse the slang dictionary →</a>
        <a class="btn-ghost" href="../history.html">Read the history of Toronto slang →</a>
      </div>
    </article>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <nav class="footer-nav" aria-label="Footer">
      <a href="../index.html">Dictionary</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../quiz.html">Quiz</a>
      <a href="../history.html">Slang History</a>
      <a href="../faq.html">FAQ</a>
      <a href="../all-words.html">All Words</a>
      <a href="../neighbourhoods.html">Slang By Neighbourhood</a>
      <a href="index.html">Toronto Guide</a>
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


def build_hub(all_pages):
    cards = "\n".join(
        f'''      <a class="guide-card" href="{esc(p["slug"])}.html">
        <div class="guide-card-img" style="background-image:url('{commons(p["hero_img"])}')"></div>
        <div class="guide-card-body">
          <h2>{esc(p["h1"])}</h2>
          <p>{esc(p["dek"])}</p>
        </div>
      </a>'''
        for p in all_pages
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Toronto Guide: History, Culture, Food, Sports & Landmarks | Toronto Mans Dictionary</title>
<meta name="description" content="A guide to Toronto beyond the slang dictionary: the city's history, neighbourhoods, landmarks, food culture, sports teams, festivals, and multiculturalism, with real photos and sources.">
<meta name="keywords" content="Toronto guide, Toronto culture, Toronto history, Toronto landmarks, Toronto food, Toronto sports, Toronto festivals">
<link rel="canonical" href="{SITE_URL}/guide/index.html">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#101114">
<link rel="preconnect" href="https://www.highperformanceformat.com">
<link rel="preconnect" href="https://commons.wikimedia.org">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Toronto Mans Dictionary">
<meta property="og:title" content="Toronto Guide: History, Culture, Food, Sports &amp; Landmarks">
<meta property="og:description" content="A guide to Toronto beyond the slang dictionary — history, neighbourhoods, landmarks, food, sports, festivals and multiculturalism.">
<meta property="og:url" content="{SITE_URL}/guide/index.html">
<meta property="og:image" content="{commons('Toronto-CN-tower-and-Canadian-flag-skyline.jpg')}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Toronto Guide">
<meta name="twitter:description" content="History, culture, food, sports, festivals and landmarks — the city behind the slang.">
<meta name="twitter:image" content="{commons('Toronto-CN-tower-and-Canadian-flag-skyline.jpg')}">

<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍁</text></svg>">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/article.css">
<link rel="stylesheet" href="../css/guide.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Toronto Guide",
  "description": "A guide to Toronto's history, neighbourhoods, landmarks, food culture, sports and festivals.",
  "url": "{SITE_URL}/guide/index.html",
  "isPartOf": "{SITE_URL}/index.html"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Dictionary", "item": "{SITE_URL}/index.html" }},
    {{ "@type": "ListItem", "position": 2, "name": "Toronto Guide", "item": "{SITE_URL}/guide/index.html" }}
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
      <a href="../quiz.html">Quiz</a>
      <a href="../history.html">Slang History</a>
      <a href="index.html" class="active">Guide</a>
      <button type="button" class="btn-ghost" data-open-submit-modal>Submit a term</button>
    </nav>
  </div>
</header>

<main class="article-page">
  <div class="wrap article-wrap">

    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Dictionary</a> <span aria-hidden="true">/</span> <span>Guide</span>
    </nav>

    <header class="article-header">
      <p class="hero-kicker">Beyond the dictionary</p>
      <h1>The Toronto Guide</h1>
      <p class="article-dek">This site started as a slang dictionary, but the slang doesn't make sense without the city behind it. Seven pages on the actual Toronto — history, neighbourhoods, landmarks, food, sports, festivals, and the multiculturalism that built all of it.</p>
    </header>

    {ad_leaderboard()}

    <div class="guide-grid">
{cards}
    </div>

    <div class="article-cta">
      <a class="btn-ghost" href="../history.html">Read the history of Toronto slang →</a>
      <a class="btn-ghost" href="../index.html#browse">Browse the dictionary →</a>
    </div>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <nav class="footer-nav" aria-label="Footer">
      <a href="../index.html">Dictionary</a>
      <a href="../wordle.html">Torontle</a>
      <a href="../quiz.html">Quiz</a>
      <a href="../history.html">Slang History</a>
      <a href="../faq.html">FAQ</a>
      <a href="../all-words.html">All Words</a>
      <a href="../neighbourhoods.html">Slang By Neighbourhood</a>
      <a href="index.html">Toronto Guide</a>
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


def main():
    GUIDE_DIR.mkdir(exist_ok=True)
    for page in PAGES:
        out = build_page(page, PAGES)
        (GUIDE_DIR / f"{page['slug']}.html").write_text(out, encoding="utf-8")
        print(f"Wrote guide/{page['slug']}.html")
    (GUIDE_DIR / "index.html").write_text(build_hub(PAGES), encoding="utf-8")
    print("Wrote guide/index.html")


if __name__ == "__main__":
    main()
