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
            (None, '<p>Toronto is old enough to have burned down once and been renamed twice, and young enough that its current shape — one city, not six — dates to 1998, well within living memory. Here\'s the actual timeline, not the postcard version — starting from the 1793 founding of York. For what came before that, including where the name "Toronto" actually comes from, see our separate page on <a href="indigenous-history.html">Toronto\'s Indigenous history</a>.</p>'),
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
    {
        "slug": "transit",
        "title": "Toronto Transit: The TTC, Subway, Streetcars & PATH",
        "kicker": "Getting around the 6ix",
        "h1": "Toronto Transit: The TTC",
        "dek": "Canada's first subway, a streetcar network locals fought to save, and North America's largest underground pedestrian city — how Toronto actually gets around.",
        "meta_desc": "A guide to Toronto's transit system: the TTC subway (Canada's first, opened 1954), the historic streetcar network, and the PATH underground pedestrian network.",
        "keywords": "TTC Toronto, Toronto subway history, Toronto streetcar, PATH Toronto underground, Toronto transit guide",
        "hero_img": "CLRV_TTC_Streetcar_No_4004_(8063115473).jpg",
        "hero_alt": "A CLRV streetcar operated by the Toronto Transit Commission",
        "hero_credit": "TTC streetcar — Peter Broster, CC BY 2.0",
        "sections": [
            (None, '<p>The TTC (Toronto Transit Commission) runs the subway, streetcars and buses that most Torontonians mean when they say <a href="../words/the-rocket.html">the Rocket</a> — and getting around downtown often means going underground in more ways than one.</p>'),
            ("The subway: Canada's first (1954)", '<p>Toronto\'s subway opened on March 30, 1954 — the first in Canada — running under Yonge Street with 12 stations across 7.4 km. It has since grown to three lines, 70 stations and 70.1 km of track. The nickname <a href="../words/the-rocket.html">the Rocket</a> dates to the red-painted original subway cars.</p>'),
            ("Streetcars older than the subway by nearly a century", '<p>Toronto\'s streetcar network is much older than its subway — the first line, along Yonge Street, opened in 1861, making it the first streetcar line in Canada. By 1972 the city had actually planned to phase streetcars out entirely in favour of buses, until a citizens\' campaign called "Streetcars for Toronto," led by urbanist Jane Jacobs and transit advocate Steve Munro, successfully pushed the city to keep them. Toronto now runs one of the only surviving major streetcar networks in North America.</p>'),
            ("The PATH: the world's largest underground shopping complex", '<p>Beneath the Financial District sits the <strong>PATH</strong>, a climate-controlled pedestrian network connecting dozens of office towers, hotels and shopping concourses — officially recognized by Guinness World Records as the largest underground shopping complex on Earth by total retail floor space. In a city with genuinely brutal winters, it lets a meaningful chunk of downtown commute and shop without ever stepping outside.</p>'),
            ("Late nights and the vomit comet", '<p>When the subway shuts down overnight, the TTC\'s Blue Night bus network takes over — see <a href="../words/vomit-comet.html">the Vomit Comet</a> for what locals actually call it, and why.</p>'),
        ],
        "sources": [
            ("The Canadian Encyclopedia — Toronto Subway", "https://www.thecanadianencyclopedia.ca/en/article/toronto-subway"),
            ("City of Toronto — Canada's First Subway", "https://www.toronto.ca/explore-enjoy/history-art-culture/online-exhibits/web-exhibits/web-exhibits-transportation/canadas-first-subway/canadas-first-subway-underground-downtown/"),
            ("Wikipedia — Yonge streetcar line", "https://en.wikipedia.org/wiki/Yonge_streetcar_line"),
        ],
        "related_words": ["the-rocket", "red-rocket", "vomit-comet"],
    },
    {
        "slug": "parks",
        "title": "Toronto Parks & Green Space: Islands, High Park & the Don Valley",
        "kicker": "13% of the city is parkland",
        "h1": "Toronto Parks & Green Space",
        "dek": "A car-free island park in Lake Ontario, a 400-acre park with an endangered oak savannah, and a converted brick quarry turned environmental centre — Toronto's green space is stranger and better than its skyline suggests.",
        "meta_desc": "A guide to Toronto's parks and green space: Toronto Islands, High Park, and the Don Valley / Evergreen Brick Works — history and what makes each one distinct.",
        "keywords": "Toronto parks, Toronto Islands, High Park Toronto, Don Valley, Evergreen Brick Works, Toronto green space",
        "hero_img": "High_Park_Toronto_October_2012.jpg",
        "hero_alt": "High Park in Toronto in autumn",
        "hero_credit": "High Park — Benson Kua, CC BY-SA 2.0",
        "sections": [
            (None, '<p>Parks and green space cover roughly 13% of Toronto\'s land area — over 8,000 hectares, ranging from formal Victorian-designed lawns to actual Carolinian forest.</p>'),
            ("Toronto Islands", '<p>A car-free archipelago of small islands just offshore in Lake Ontario, reachable only by ferry (or, in recent years, a pedestrian/cyclist bridge to one island), with beaches, historic cottages, and the best unobstructed view of the Toronto skyline anywhere.</p>' + figure("Toronto_skyline_toronto_islands_b.JPG", "The Toronto skyline seen from the Toronto Islands", "Toronto skyline from the Toronto Islands — Wikimedia Commons, Creative Commons licensed")),
            ("High Park", '<p>At nearly 400 acres, Toronto\'s largest and best-known park, donated to the city in 1873 by architect John George Howard and opened in 1876. It contains a rare and endangered black oak savannah ecosystem, a small zoo, sports fields, and — every spring — some of the city\'s most-photographed cherry blossoms.</p>'),
            ("The Don Valley and Evergreen Brick Works", '<p>The Don River valley cuts a genuinely wild green corridor through the middle of the city. Its most distinctive landmark is the <strong>Evergreen Brick Works</strong>: a former industrial quarry and brick factory — the same one that supplied the bricks for Casa Loma, Massey Hall and the Ontario Legislature — converted since 2010 into Canada\'s first large-scale community environmental centre.</p>'),
        ],
        "sources": [
            ("Wikipedia — High Park", "https://en.wikipedia.org/wiki/High_Park"),
            ("historyoftoronto.ca — A Comprehensive Guide to Toronto Parks", "https://historyoftoronto.ca/blog/a-comprehensive-guide-to-toronto-parks-exploring-the-green-oasis-of-canadas-largest-city"),
        ],
        "related_words": [],
    },
    {
        "slug": "media",
        "title": "Toronto Media & Entertainment: Hollywood North and Beyond",
        "kicker": "Third-largest film production centre in North America",
        "h1": "Toronto Media & Entertainment",
        "dek": "Toronto has been a major film and TV production centre since the late 1970s — and, separately, the launchpad for some of the most influential music of the streaming era.",
        "meta_desc": "How Toronto became Hollywood North: the film and TV production industry's history, scale, and infrastructure, plus the city's outsized influence on modern music.",
        "keywords": "Hollywood North Toronto, Toronto film industry, Toronto TV production, Toronto music scene, OVO Drake Toronto",
        "hero_img": "Toronto-CN-tower-and-Canadian-flag-skyline.jpg",
        "hero_alt": "The Toronto skyline and CN Tower",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto has carried the nickname "Hollywood North" since the late 1970s — and unlike a lot of city nicknames, this one is backed by genuinely large numbers.</p>'),
            ("A production centre since the 1970s", '<p>By 1979, Toronto\'s mayor was already announcing that Canada had become the third-largest movie production centre in North America, after Los Angeles and New York. The city is home to Pinewood Toronto Studios, Canada\'s largest film studio, and in 2023 alone, film and TV production contributed roughly $3.15 billion to Ontario\'s economy and close to 46,000 direct and spin-off jobs.</p>'),
            ("Why Toronto works for film and TV", '<p>Competitive tax incentives, a deep pool of skilled crew, and a downtown that can plausibly stand in for New York, Chicago or a generic American city on camera — all of which is exactly why so many productions shoot in Toronto without ever setting the story there.</p>'),
            ("Music: from a hip-hop and R&B hub to global reach", '<p>Toronto\'s Caribbean-rooted hip-hop scene — the same cultural current documented throughout the slang in this dictionary — produced an outsized share of 2010s-2020s global pop and R&B, led most visibly by Drake\'s <a href="../words/ovo.html">OVO</a> label and The Weeknd. TIFF (see our <a href="festivals.html">festivals guide</a>) and the wider music/film ecosystem reinforce each other; a lot of the same city infrastructure supports both.</p>'),
        ],
        "sources": [
            ("Wikipedia — Hollywood North", "https://en.wikipedia.org/wiki/Hollywood_North"),
            ("Toronto Global — What Makes Toronto \"Hollywood North\"?", "https://torontoglobal.ca/our-industries/what-makes-toronto-hollywood-north/"),
        ],
        "related_words": ["ovo", "we-the-north"],
    },
    {
        "slug": "economy",
        "title": "Toronto's Economy: Bay Street & Canada's Financial Capital",
        "kicker": "Five bank towers, one stock exchange",
        "h1": "Toronto's Economy: Bay Street",
        "dek": "Toronto has been Canada's financial capital since the 1970s, when Bay Street took that role from Montreal's St. James Street — here's what actually sits in the Financial District.",
        "meta_desc": "A guide to Toronto's Financial District and Bay Street: Canada's five major banks, the Toronto Stock Exchange, and how Toronto became the country's financial capital.",
        "keywords": "Bay Street Toronto, Toronto Financial District, Toronto Stock Exchange, Toronto economy, Canada financial capital",
        "hero_img": "Bay_Street,_Financial_District,_Toronto,_Ontario_(29708936890).jpg",
        "hero_alt": "Bay Street in Toronto's Financial District",
        "hero_credit": "Bay Street, Financial District — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>"Bay Street" functions the way "Wall Street" does in the U.S. — a specific street that\'s become shorthand for an entire national industry.</p>'),
            ("Canada's financial capital since the 1970s", '<p>Bay Street became the centre of Canadian finance in the 1970s, taking over from Montreal\'s St. James Street. It\'s now home to the headquarters of five of Canada\'s major banks — Bank of Montreal, Scotiabank, CIBC, TD Bank and RBC — plus the Toronto Stock Exchange (TSX), one of the world\'s largest, located just a block away at York and King.</p>'),
            ("What\'s actually downtown", '<p>Beyond the banks: a dense cluster of law firms, insurance companies, pension funds and accounting firms, all within walking distance of Union Station — which is exactly why the Financial District\'s skyline (and the <a href="landmarks.html">PATH network</a> underneath it) is as dense as it is.</p>'),
        ],
        "sources": [
            ("Wikipedia — Bay Street", "https://en.wikipedia.org/wiki/Bay_Street"),
            ("Wikipedia — Financial District, Toronto", "https://en.wikipedia.org/wiki/Financial_District,_Toronto"),
        ],
        "related_words": [],
    },
    {
        "slug": "education",
        "title": "Toronto's Universities: U of T, York, and TMU",
        "kicker": "Where the MTE research happens",
        "h1": "Toronto's Universities",
        "dek": "Three major universities, three very different founding stories — and one of them is where the academic research behind this entire dictionary actually comes from.",
        "meta_desc": "A guide to Toronto's major universities: the University of Toronto (1827), York University (1959), and Toronto Metropolitan University — including where Multicultural Toronto English is actually researched.",
        "keywords": "University of Toronto history, York University Toronto, Toronto Metropolitan University, TMU Ryerson, Toronto universities",
        "hero_img": "Toronto_skyline_(2012).jpg",
        "hero_alt": "The Toronto skyline",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto is home to three major universities, each with a genuinely different origin story.</p>'),
            ("University of Toronto (chartered 1827)", '<p>Founded as the Anglican-affiliated King\'s College at York, chartered in 1827 but not actually established until 1843 — making it one of the oldest universities in Canada. It later added suburban campuses at Scarborough (1964) and Mississauga (1966). Its Mississauga campus, U of T Mississauga (UTM), is where linguist <strong>Dr. Derek Denis</strong> researches Multicultural Toronto English — the academic term for the vocabulary this entire dictionary documents. See our <a href="../history.html#mte">history of Toronto slang</a> for that research directly.</p>'),
            ("York University (founded 1959)", '<p>Founded in 1959 in response to Toronto\'s rapid post-war growth, initially affiliated with the University of Toronto until becoming fully independent in 1965. Its main Keele campus opened that same year, alongside the smaller downtown Glendon campus.</p>'),
            ("Toronto Metropolitan University (founded 1948 as Ryerson)", '<p>Founded in 1948 as the Ryerson Institute of Technology to meet post-war demand for skilled trades training, on the site of Ontario\'s first teacher training college. It gained degree-granting authority in 1971 and rebranded as Toronto Metropolitan University (TMU) in 2022.</p>'),
        ],
        "sources": [
            ("The Canadian Encyclopedia — University of Toronto", "https://www.thecanadianencyclopedia.ca/en/article/university-of-toronto"),
            ("The Canadian Encyclopedia — York University", "https://www.thecanadianencyclopedia.ca/en/article/york-university"),
            ("Toronto Metropolitan University — History", "https://www.torontomu.ca/about/history/"),
        ],
        "related_words": ["mans"],
    },
    {
        "slug": "nicknames",
        "title": "Every Toronto Nickname Explained: The Six, Hogtown, T.O. & More",
        "kicker": "One city, half a dozen names",
        "h1": "Every Toronto Nickname, Explained",
        "dek": "Toronto has accumulated more nicknames than most cities its size — some affectionate, some originally insults the city decided to keep anyway.",
        "meta_desc": "Every major Toronto nickname explained: The Six / 6ix, Hogtown, Toronto the Good, the Big Smoke, T.O. and T-Dot — where each one actually comes from.",
        "keywords": "Toronto nicknames, why is Toronto called the six, Toronto the Good, Big Smoke Toronto, T.O. T-Dot meaning",
        "hero_img": "Toronto-CN-tower-and-Canadian-flag-skyline.jpg",
        "hero_alt": "The Toronto skyline",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Few cities collect nicknames the way Toronto has — partly civic pride, partly self-deprecation, and at least twice, an insult the city simply decided to keep.</p>'),
            ("The Six / 6ix", '<p>The newest and now most globally recognized nickname, referring to the 1998 amalgamation of six municipalities into one Toronto, popularized by Drake\'s 2015 album <em>Views From The 6</em> after Toronto rapper Jimmy Prime used it in street culture first. Full dictionary entry: <a href="../words/the-six.html">The Six / The 6ix</a>.</p>'),
            ("Hogtown", '<p>A 19th-century nickname with two competing origin stories — a political insult about Toronto politicians "hogging" the provincial legislature, and the city\'s genuinely massive meatpacking industry. Toronto embraced it rather than fighting it. Full entry: <a href="../words/hogtown.html">Hogtown</a>.</p>'),
            ("Toronto the Good", '<p>Coined by 19th-century mayor William Howland, who campaigned against gambling and public drinking while promoting a strict Christian moral code. The nickname stuck — but is now mostly used sarcastically, given how far the modern city is from Howland\'s vision.</p>'),
            ("The Big Smoke", '<p>Popularized by Maclean\'s columnist Allan Fotheringham, who borrowed a term Aboriginal Australians used for Australian cities to describe Toronto as all reputation and "smoke and mirrors." A competing, less cynical theory ties it to the literal industrial smoke that hung over the city in the early 1900s.</p>'),
            ("T.O. and T-Dot", '<p>Straightforward abbreviation-era nicknames, modeled on "NY" for New York and "LA" for Los Angeles. Full entries: <a href="../words/t-dot.html">T Dot / T.O.</a> and <a href="../words/the-dot.html">The Dot</a>.</p>'),
        ],
        "sources": [
            ("WorldAtlas — Why is Toronto Called \"the Big Smoke\"?", "https://www.worldatlas.com/articles/why-is-toronto-the-big-smoke.html"),
            ("Reviewlution — Why is Toronto Called the Six?", "https://reviewlution.ca/resources/why-is-toronto-called-the-six/"),
            ("Barry Popik — Big Smoke (Toronto, Canada nickname)", "https://barrypopik.com/blog/big_smoke_toronto1"),
        ],
        "related_words": ["the-six", "hogtown", "t-dot", "the-dot"],
    },
    {
        "slug": "indigenous-history",
        "title": "Toronto's Indigenous History: Tkaronto & the Dish With One Spoon",
        "kicker": "Before 1793",
        "h1": "Toronto's Indigenous History",
        "dek": "Toronto's own history — and even its name — starts long before York was founded in 1793. The land has been home to Indigenous peoples for over 10,000 years, and \"Toronto\" itself comes from a Mohawk word for a place well north of the modern city.",
        "meta_desc": "Toronto's Indigenous history before European settlement: the Wendat, Haudenosaunee and Anishinaabe peoples, the Dish With One Spoon treaty, the Toronto Purchase, and the real origin of the name Toronto.",
        "keywords": "Toronto Indigenous history, meaning of the word Toronto, Tkaronto, Dish With One Spoon, Toronto Purchase, Mississaugas of the Credit",
        "hero_img": "Toronto_skyline_toronto_islands_b.JPG",
        "hero_alt": "The Toronto skyline seen from the Toronto Islands",
        "hero_credit": "Toronto skyline from the Toronto Islands — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Our <a href="history.html">history of Toronto</a> page, like most accounts, starts the clock at the 1793 founding of York. That\'s the origin of the current city government — it is not the origin of the place. People have lived on this land for more than 10,000 years, and the name "Toronto" itself predates any European settlement by centuries.</p>'),
            ("Where the name actually comes from", '<p>"Toronto" is widely traced to <em>tkaronto</em>, a Mohawk word meaning roughly "where there are trees standing in the water" — originally describing a narrows between Lake Simcoe and Lake Couchiching, well north of the modern city, where the Wendat and later Haudenosaunee drove stakes into the water to build fish weirs. The name migrated south over generations of maps and trade routes until it settled on the site of the current city, long before Simcoe founded York in 1793 and even survived his attempt to rename the place. This is also, distantly, the same root behind local slang like <a href="../words/t-dot.html">T Dot</a> and <a href="../words/the-dot.html">the Dot</a> — abbreviations of a name that was already secondhand when the British arrived.</p>'),
            ("The peoples who were here", '<p>Before sustained European contact, the region was home to the <strong>Wendat (Huron)</strong>, followed by the <strong>Haudenosaunee Confederacy</strong>, and by the 17th–18th centuries the <strong>Mississaugas of the Credit</strong>, an Anishinaabe people who remain the most direct historical stewards of the land the city now sits on. Archaeological sites around present-day Toronto — including village sites near the Humber River, a historic carrying-place trail connecting Lake Ontario to Lake Simcoe — show continuous Indigenous settlement stretching back well over 10,000 years.</p>'),
            ("The Dish With One Spoon", '<p>Long before any treaty involving the British Crown, the Haudenosaunee and Anishinaabe peoples of the region were themselves party to the <strong>Dish With One Spoon</strong> covenant — an agreement to share the territory and its resources peacefully, take only what is needed, and keep the "dish" (the land) clean for those who\'d use it after. It\'s still invoked today, including by the City of Toronto itself, as the founding relationship underlying the land the city occupies.</p>'),
            ("The Toronto Purchase (1787, and its 200-year aftermath)", '<p>In 1787, the British Crown negotiated a land agreement with the Mississaugas of the Credit for territory including what is now downtown Toronto — the <strong>Toronto Purchase</strong>. The original document was later found to be invalid (it left the actual boundaries and price blank), and the Mississaugas of the Credit spent roughly two centuries pursuing a formal claim over the shortfall. In 2010, the federal government settled the claim for $145 million, one of the largest specific land-claim settlements in Canadian history at the time — a rare case where a founding-era land deal was actually revisited and compensated in the modern era rather than simply left as historical footnote.</p>'),
        ],
        "sources": [
            ("City of Toronto — Indigenous History of Toronto", "https://www.toronto.ca/city-government/accessibility-human-rights/indigenous-affairs-office/indigenous-history-of-toronto/"),
            ("Wikipedia — Toronto Purchase", "https://en.wikipedia.org/wiki/Toronto_Purchase"),
            ("Wikipedia — Etymology of Toronto", "https://en.wikipedia.org/wiki/Toronto#Etymology"),
            ("Mississaugas of the Credit First Nation — Our History", "https://mncfn.ca/about-mncfn/"),
        ],
        "related_words": ["t-dot", "the-dot"],
    },
    {
        "slug": "weather",
        "title": "Toronto Weather & Climate: Brutal Winters, Humid Summers",
        "kicker": "Four seasons, all of them extreme",
        "h1": "Toronto Weather & Climate",
        "dek": "Toronto runs a genuine humid continental climate — meaning real winters and real summers, not the mild in-between some people expect from a lake city.",
        "meta_desc": "A guide to Toronto's climate: cold snowy winters, hot humid summers, why Lake Ontario moderates temperatures near the shore, and how the city handles snow removal.",
        "keywords": "Toronto weather, Toronto climate, Toronto winter, how cold does it get in Toronto, Toronto snow",
        "hero_img": "Toronto_skyline_(2012).jpg",
        "hero_alt": "The Toronto skyline",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto sits at the humid-continental/humid-subtropical boundary, which in practice means one thing: no mild in-between season carries the year. Winters are genuinely cold, summers are genuinely hot and humid, and the lake at the city\'s doorstep changes both more than people expect.</p>'),
            ("Winter", '<p>Average January highs sit around -1°C with lows near -6°C, but wind chill regularly pushes the felt temperature well below -20°C during cold snaps, and the city sees meaningful lake-effect snow squalls off Lake Ontario. Toronto\'s PATH network (see our <a href="transit.html">transit guide</a>) exists largely because of exactly this weather — it lets downtown workers avoid the worst of it entirely.</p>'),
            ("Summer", '<p>Summers run hot and notably humid for a Canadian city, with July highs averaging around 27°C but humidex values that regularly push the "feels like" temperature into the mid-30s or higher. The city\'s Beaches and Toronto Islands (see our <a href="parks.html">parks guide</a>) become genuinely essential rather than decorative once summer humidity sets in.</p>'),
            ("The lake effect", '<p>Lake Ontario moderates temperatures right along the shoreline — downtown and the waterfront run slightly cooler in summer and slightly milder in winter than inland areas like Vaughan or Brampton just a short drive north, thanks to the lake\'s thermal mass. That same lake is also the source of the heavy, sudden snow squalls that can dump a foot of snow on the city in an afternoon while areas further inland see almost nothing.</p>'),
            ("Snow removal, seriously", '<p>Toronto\'s Combined Heavy Equipment/Winter Operations budget is a genuinely major line item — snow clearing across the city\'s streets, sidewalks and bike lanes runs into the tens of millions of dollars in a typical winter, and a bad one draws real political heat when it goes slowly. It\'s one of the most consistently discussed municipal issues every winter, alongside TTC delays.</p>'),
        ],
        "sources": [
            ("Environment and Climate Change Canada — Toronto Climate Normals", "https://climate.weather.gc.ca/climate_normals/index_e.html"),
            ("Wikipedia — Climate of Toronto", "https://en.wikipedia.org/wiki/Toronto#Climate"),
            ("City of Toronto — Winter Operations", "https://www.toronto.ca/services-payments/streets-parking-transportation/road-maintenance/winter-maintenance/"),
        ],
        "related_words": [],
    },
    {
        "slug": "architecture",
        "title": "Toronto Architecture: Bay-and-Gable Houses & the Modern Skyline",
        "kicker": "Victorian rowhouses to glass towers",
        "h1": "Toronto Architecture",
        "dek": "A style found almost nowhere else — the Victorian bay-and-gable rowhouse — sitting a short walk from one of the tallest, densest condo skylines in North America.",
        "meta_desc": "A guide to Toronto's architecture: the city's distinctive Victorian bay-and-gable rowhouses, the modern condo boom, and how the two eras sit side by side.",
        "keywords": "Toronto architecture, bay and gable houses Toronto, Toronto Victorian houses, Toronto condo boom, Cabbagetown architecture",
        "hero_img": "Houses_in_Cabbagetown_Toronto.jpg",
        "hero_alt": "Victorian bay-and-gable houses in Cabbagetown, Toronto",
        "hero_credit": "Bay-and-gable houses, Cabbagetown — David (bootbearwdc), CC BY 2.0",
        "sections": [
            (None, '<p>Toronto\'s built environment runs on two very different clocks at once: a 19th-century residential style found almost nowhere outside the city, and one of the fastest, tallest condo booms in North America layered right on top of it.</p>'),
            ("The bay-and-gable house", '<p>Walk through Cabbagetown, Riverdale, Parkdale or the Annex and the dominant house style is the <strong>bay-and-gable</strong>: a narrow Victorian rowhouse with a projecting bay window topped by a steep, pointed gable roof, usually in red brick. It emerged in Toronto specifically in the late 19th century as a way to maximize light and interior space on narrow urban lots, and while similar bay windows exist elsewhere, the sheer concentration of this exact style is considered distinctly Torontonian — architectural historians treat it as close to a local vernacular style in its own right.</p>' + figure("Cabbagetown_houses.jpg", "Rows of Victorian bay-and-gable houses in Cabbagetown, Toronto", "Cabbagetown houses — David (bootbearwdc), CC BY 2.0")),
            ("Cabbagetown: the largest Victorian district in North America", '<p>The Cabbagetown neighbourhood, just east of downtown, is frequently cited as the largest continuous area of preserved Victorian housing anywhere in North America — a legacy of 19th-century working-class Irish immigrant settlement (the name reportedly comes from residents growing cabbages on their front lawns) followed by a wave of restoration and gentrification starting in the 1970s.</p>'),
            ("The modern skyline", '<p>Since the early 2000s, Toronto has run one of the largest condo construction booms of any city on the continent, driven by high housing demand and a downtown that\'s been actively encouraged to build up rather than out. The result is a skyline dominated by the CN Tower (see our <a href="landmarks.html">landmarks guide</a>) surrounded by an ever-denser cluster of glass residential towers — a contrast that puts 130-year-old bay-and-gable rowhouses a few blocks from buildings that didn\'t exist a decade ago.</p>'),
        ],
        "sources": [
            ("Wikipedia — Bay-and-gable", "https://en.wikipedia.org/wiki/Bay-and-gable"),
            ("Wikipedia — Cabbagetown, Toronto", "https://en.wikipedia.org/wiki/Cabbagetown,_Toronto"),
            ("Toronto Preservation Board / heritage planning materials on Victorian residential architecture", "https://www.toronto.ca/city-government/planning-development/heritage-preservation/"),
        ],
        "related_words": [],
    },
    {
        "slug": "art",
        "title": "Toronto Art & Public Art: the AGO and Graffiti Alley",
        "kicker": "From the AGO to the alley behind Queen West",
        "h1": "Toronto Art & Public Art",
        "dek": "One of North America's largest art museums, and — a few blocks away — one of the most photographed legal graffiti strips in the country.",
        "meta_desc": "A guide to Toronto's art scene: the Art Gallery of Ontario (AGO), Graffiti Alley near Queen West, and the city's public street art culture.",
        "keywords": "Art Gallery of Ontario, AGO Toronto, Graffiti Alley Toronto, Toronto street art, Toronto public art",
        "hero_img": "Art_Gallery_of_Ontario_(24409138225).jpg",
        "hero_alt": "The Art Gallery of Ontario building in Toronto",
        "hero_credit": "Art Gallery of Ontario — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto\'s art scene spans both ends of the formality spectrum at once: a major international museum downtown, and a genuinely lawless-looking laneway of legal graffiti a short walk from it.</p>'),
            ("The Art Gallery of Ontario (AGO)", '<p>One of the largest art museums in North America by exhibition space, holding a collection of roughly 120,000 works spanning European masters, a major Group of Seven and Canadian collection, and significant Indigenous and contemporary art. Its current building — a dramatic titanium-and-glass renovation completed in 2008 — was designed by Toronto-born architect <strong>Frank Gehry</strong>, his first major project in his home city.</p>'),
            ("Graffiti Alley", '<p>A stretch of laneway running roughly parallel to Queen Street West, officially sanctioned for street art since the 1970s and now one of the most consistently repainted, photographed stretches of public art in the city — a rotating, unofficial open-air gallery rather than a single fixed mural. It\'s become enough of a landmark in its own right that it regularly turns up as a filming location and photo backdrop, feeding back into Toronto\'s <a href="media.html">Hollywood North</a> production scene.</p>'),
            ("Public art beyond the two big names", '<p>Beyond the AGO and Graffiti Alley, Toronto runs a formal public art program requiring large new developments to fund public art installations, which is why the city\'s newer condo neighbourhoods — Liberty Village, CityPlace, the waterfront — tend to have a noticeably higher density of sculpture and installation art than older, established neighbourhoods.</p>'),
        ],
        "sources": [
            ("Art Gallery of Ontario — About the AGO", "https://ago.ca/about-ago"),
            ("Wikipedia — Art Gallery of Ontario", "https://en.wikipedia.org/wiki/Art_Gallery_of_Ontario"),
            ("blogTO — Graffiti Alley Toronto", "https://www.blogto.com/toronto/graffiti_alley/"),
        ],
        "related_words": [],
    },
    {
        "slug": "waterfront",
        "title": "Toronto's Waterfront: Harbourfront, Sugar Beach & the Islands",
        "kicker": "630 km² of city, and a lakefront it's still rebuilding",
        "h1": "Toronto's Waterfront",
        "dek": "A former industrial shipping and rail strip along Lake Ontario, being rebuilt piece by piece into parks, beaches — including a pink-umbrella \"urban beach\" — and public space.",
        "meta_desc": "A guide to Toronto's waterfront: Harbourfront Centre, Sugar Beach, the Toronto Islands, and the decades-long revitalization turning the old industrial shoreline into public space.",
        "keywords": "Toronto waterfront, Harbourfront Centre, Sugar Beach Toronto, Toronto Islands, Toronto waterfront revitalization",
        "hero_img": "Harbourfront,_Toronto,_Ontario_from_CN_Tower_(21652107550).jpg",
        "hero_alt": "Toronto's Harbourfront and waterfront seen from above",
        "hero_credit": "Toronto Harbourfront — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>For most of the 20th century, Toronto\'s Lake Ontario shoreline was industrial and inaccessible — rail yards, warehouses and shipping infrastructure, not parkland. What exists today is the product of a decades-long, still-ongoing revitalization.</p>'),
            ("Harbourfront Centre", '<p>A cultural and recreational precinct along the central waterfront, developed starting in the 1970s on former industrial and port land. It now hosts year-round festivals, an outdoor skating rink in winter, art studios, a theatre, and direct water access — the anchor of Toronto\'s public waterfront identity.</p>'),
            ("Sugar Beach", '<p>An artificial "urban beach" opened in 2010 on the site of a former parking lot next to the still-operating Redpath Sugar refinery (the source of its name and its sugar-white sand). It\'s known for its rows of oversized pink umbrellas and is one of the clearest symbols of the waterfront\'s shift from industrial to public space — a functioning beach with real sand, a stone\'s throw from downtown office towers.</p>' + figure("Sugar_Beach_Toronto_-_2010_(cropped).jpg", "Sugar Beach in Toronto, with its pink umbrellas along Lake Ontario", "Sugar Beach — Wikimedia Commons, Creative Commons licensed")),
            ("The Toronto Islands", '<p>Covered in more depth in our <a href="parks.html">parks guide</a> — a car-free archipelago just offshore, reachable by ferry, and the best vantage point in the city for looking back at the skyline it fronts.</p>'),
            ("An ongoing project", '<p>Waterfront Toronto, the tri-government agency overseeing the revitalization, continues major projects along the eastern waterfront, including flood protection and new parkland in the Port Lands — one of the largest urban land redevelopment projects underway anywhere in North America.</p>'),
        ],
        "sources": [
            ("Waterfront Toronto — About", "https://www.waterfrontoronto.ca/explore-projects"),
            ("Wikipedia — Harbourfront, Toronto", "https://en.wikipedia.org/wiki/Harbourfront,_Toronto"),
            ("blogTO — Sugar Beach Toronto", "https://www.blogto.com/sports_play/sugar_beach/"),
        ],
        "related_words": [],
    },
    {
        "slug": "lgbtq-village",
        "title": "Church-Wellesley Village: Toronto's LGBTQ+ History",
        "kicker": "One of North America's oldest gay villages",
        "h1": "Church-Wellesley Village",
        "dek": "Toronto's LGBTQ+ neighbourhood has roots going back to the 1970s, a defining act of resistance in 1981, and now one of the largest Pride festivals in the world.",
        "meta_desc": "The history of Toronto's Church-Wellesley Village: its 1970s origins, the 1981 bathhouse raids that galvanized the community, and Toronto Pride, now one of the largest Pride festivals worldwide.",
        "keywords": "Church-Wellesley Village Toronto, Toronto Pride history, Toronto gay village, 1981 bathhouse raids Toronto, Toronto LGBTQ history",
        "hero_img": "Pride_parade_Toronto_2011.jpg",
        "hero_alt": "Crowds at the Toronto Pride parade",
        "hero_credit": "Toronto Pride parade, 2011 — Kitty Rainbow, CC BY 2.0",
        "sections": [
            (None, '<p>Centred on Church Street between Wellesley and Alexander, the <strong>Church-Wellesley Village</strong> (often just "the Village") has been the recognized centre of Toronto\'s LGBTQ+ community since the 1970s, and is counted among the oldest continuously existing gay villages in North America.</p>'),
            ("Origins in the 1970s", '<p>The neighbourhood\'s identity took shape through the 1970s as LGBTQ+-owned bars, bathhouses and community organizations concentrated along Church Street, in a city and country where being openly gay carried real legal and social risk — homosexuality had only been decriminalized in Canada in 1969.</p>'),
            ("The 1981 bathhouse raids", '<p>On February 5, 1981, Toronto police raided four gay bathhouses simultaneously in a coordinated operation, arresting roughly 300 men — at the time the largest mass arrest in Canada since the 1970 October Crisis. The raids, widely seen as targeted harassment rather than legitimate policing, triggered immediate mass protests the following night and are now generally regarded as Toronto\'s equivalent of the Stonewall riots: the event that galvanized the city\'s LGBTQ+ community into sustained organized activism, and directly shaped the Village that exists today.</p>'),
            ("Toronto Pride today", '<p>What began as small community marches grew into <strong>Toronto Pride</strong>, now one of the largest Pride festivals in the world, drawing over a million attendees across a multi-day festival and parade each June, centred on and around the Village. In 2014, Toronto hosted WorldPride, only the third city ever to do so.</p>'),
            ("The Village as a neighbourhood", '<p>Beyond Pride itself, the Village remains a functioning residential and commercial neighbourhood — bars, community health services, and Canada\'s largest LGBTQ+ community centre, The 519, all concentrated within a few blocks, a level of institutional density that makes it more than a once-a-year festival site.</p>'),
        ],
        "sources": [
            ("The Canadian Encyclopedia — Toronto Bathhouse Raids", "https://www.thecanadianencyclopedia.ca/en/article/torontos-bathhouse-raids"),
            ("Wikipedia — Church and Wellesley", "https://en.wikipedia.org/wiki/Church_and_Wellesley"),
            ("Pride Toronto — About", "https://www.pridetoronto.com/about-pride-toronto/"),
        ],
        "related_words": [],
    },
    {
        "slug": "medical-history",
        "title": "Toronto's Medical History: Where Insulin Was Discovered",
        "kicker": "A Nobel Prize, 100+ years ago",
        "h1": "Toronto's Medical History",
        "dek": "One of the most consequential medical discoveries of the 20th century happened in a University of Toronto lab in the summer of 1921 — and Toronto's hospitals have stayed near the centre of Canadian medicine ever since.",
        "meta_desc": "Toronto's medical history: the 1921 discovery of insulin at the University of Toronto by Banting and Best, the 1923 Nobel Prize, and the city's hospital and research institutions today.",
        "keywords": "insulin discovery Toronto, Banting and Best, University of Toronto insulin, Toronto General Hospital, SickKids history",
        "hero_img": "Banting_and_Best.jpg",
        "hero_alt": "Frederick Banting and Charles Best, who discovered insulin in Toronto in 1921",
        "hero_credit": "Banting and Best — Star Weekly Magazine, 1963, public domain",
        "sections": [
            (None, '<p>Toronto\'s reputation as a finance and entertainment hub tends to overshadow a quieter fact: one of the most consequential medical breakthroughs of the last century happened here, in a University of Toronto laboratory, in a single summer.</p>'),
            ("The discovery (May–July 1921)", '<p>On May 17, 1921, <strong>Frederick Banting</strong> and his student assistant <strong>Charles Best</strong> began a summer research project in the laboratory of Scottish physiologist <strong>J.J.R. Macleod</strong> at the University of Toronto, testing a theory about the pancreas and diabetes. On July 27, 1921, they successfully isolated <strong>insulin</strong> for the first time — a hormone that, once purified with the help of biochemist <strong>James Collip</strong>, turned a type 1 diabetes diagnosis from a near-certain death sentence into a manageable chronic condition.</p>'),
            ("First treatment, and the Nobel Prize", '<p>On January 11, 1922, 14-year-old <strong>Leonard Thompson</strong> became the first person treated with the new extract at Toronto General Hospital. The results were dramatic enough that news spread worldwide within months. Banting and Macleod were awarded the <strong>1923 Nobel Prize in Physiology or Medicine</strong> — Banting split his share of the prize money with Best, and Macleod split his with Collip, in recognition that the discovery was a team effort the Nobel committee\'s two-person rule couldn\'t fully capture.</p>'),
            ("Toronto's hospital and research corridor today", '<p>The University Avenue corridor between Queen\'s Park and downtown — sometimes called Toronto\'s Discovery District — remains one of the densest concentrations of hospitals and biomedical research anywhere in North America, anchored by <strong>Toronto General Hospital</strong>, <strong>The Hospital for Sick Children (SickKids)</strong>, one of the world\'s leading pediatric research hospitals, and <strong>MaRS Discovery District</strong>, a modern innovation hub built, fittingly, on the same site where insulin was first administered to patients. See our <a href="tech-scene.html">Toronto tech scene guide</a> for how that same corridor evolved into a startup hub.</p>'),
        ],
        "sources": [
            ("Heritage U of T — Discovery of Insulin at University of Toronto", "https://heritage.utoronto.ca/exhibits/insulin"),
            ("NobelPrize.org — The 'Miracle' Discovery That Reversed the Diabetes Death Sentence", "https://www.nobelprize.org/the-miracle-discovery-that-reversed-the-diabetes-death-sentence/"),
            ("Diabetologia — The Discovery of Insulin in Toronto", "https://link.springer.com/article/10.1007/s00125-020-05371-6"),
        ],
        "related_words": ["mans"],
    },
    {
        "slug": "tech-scene",
        "title": "Toronto's Tech Scene: Silicon Valley North",
        "kicker": "More tech workers than LA or Seattle",
        "h1": "Toronto's Tech Scene",
        "dek": "Toronto has quietly become one of North America's largest tech hubs — enough that it's earned the nickname \"Silicon Valley North,\" built on a deep AI research bench and a startup ecosystem that grew out of the same university corridor that discovered insulin.",
        "meta_desc": "A guide to Toronto's tech industry: why it's called Silicon Valley North, the MaRS Discovery District, and the city's AI research strength centred on the University of Toronto.",
        "keywords": "Toronto tech scene, Silicon Valley North, MaRS Discovery District, Toronto AI research, Toronto startup ecosystem",
        "hero_img": "Toronto-CN-tower-and-Canadian-flag-skyline.jpg",
        "hero_alt": "The Toronto skyline and CN Tower",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Long before "Silicon Valley North" became a talking point, Toronto already had the raw ingredients: a major research university, a dense financial sector willing to fund things, and — increasingly — more tech workers than Chicago, Los Angeles, Seattle or Washington, D.C., trailing only the Bay Area and New York in North America.</p>'),
            ("MaRS Discovery District", '<p>Founded in 2000 on University Avenue, <strong>MaRS Discovery District</strong> is now North America\'s largest urban innovation hub — a 1.5 million square foot complex supporting over 1,200 startups, with a stated mission of connecting publicly funded research to venture capital and commercial partners. Its location isn\'t an accident: it sits on the same University Avenue site where insulin was first administered to patients in 1922 — see our <a href="medical-history.html">medical history guide</a> for that story.</p>'),
            ("An AI research bench most cities can\'t match", '<p>The University of Toronto\'s computer science department, home to deep-learning pioneer <strong>Geoffrey Hinton</strong> for decades, is one of the reasons Toronto punches above its weight in AI research specifically — the Vector Institute, a dedicated AI research institute, was built directly on top of that academic strength, and has helped anchor a wave of AI startups and corporate research labs in the city.</p>'),
            ("Homegrown companies and outside investment", '<p>The city\'s most visible tech success story, e-commerce platform <strong>Shopify</strong>, is headquartered in Ottawa but has a major Toronto presence; BlackBerry-maker Research In Motion, co-founded by Waterloo-area entrepreneurs Mike Lazaridis and Jim Balsillie, is part of the same wider Ontario tech corridor. International investment has followed: Toronto\'s tech sector has repeatedly out-added jobs compared to Silicon Valley and New York City combined in recent growth cycles, driven partly by comparatively lower costs and Canada\'s more accessible skilled-worker immigration pathways.</p>'),
        ],
        "sources": [
            ("MaRS Discovery District — Our Story", "https://www.marsdd.com/our-story/"),
            ("MIT Technology Review — Toronto Would Like to Be Seen as the Nice Person's Silicon Valley", "https://www.technologyreview.com/2020/06/17/1003314/toronto-would-like-to-be-seen-as-the-nice-persons-silicon-valley-if-thats-not-too-much-trouble/"),
            ("Wikipedia — MaRS Discovery District", "https://en.wikipedia.org/wiki/MaRS_Discovery_District"),
        ],
        "related_words": [],
    },
    {
        "slug": "public-library",
        "title": "Toronto Public Library: The Busiest Library System on Earth",
        "kicker": "100 branches, 26 million checkouts a year",
        "h1": "Toronto Public Library",
        "dek": "Toronto runs the busiest urban public library system in the world — more circulation per capita than any other city, spread across 100 branches, and free to use for everyone.",
        "meta_desc": "A guide to the Toronto Public Library: its 1884 founding, the 1998 amalgamation into one system, and how it became the busiest urban public library system in the world.",
        "keywords": "Toronto Public Library, busiest library in the world, Toronto Reference Library, TPL history, Toronto library branches",
        "hero_img": "Toronto_Public_Library_Runnymede_Branch_(4994916241).jpg",
        "hero_alt": "A Toronto Public Library branch building",
        "hero_credit": "Toronto Public Library, Runnymede Branch — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>It\'s an easy fact to miss next to the skyline and the sports teams, but Toronto genuinely runs the <strong>busiest urban public library system in the world</strong> — more circulation per capita than any other major city\'s library system, anywhere.</p>'),
            ("From a Mechanics\' Institute to one city system", '<p>The library\'s roots go back to 1830 and the York Mechanics\' Institute; the modern Toronto Public Library was formally established in 1884, with James Bain as its first chief librarian. Like so much else in this city\'s civic history, it existed for most of the 20th century as several separate systems — one per former municipality — until the 1998 amalgamation of Toronto merged seven library boards into the single system that exists today, the largest public library system in North America.</p>'),
            ("The numbers", '<p>As of the early 2020s: 100 branches, close to a million cardholders, a collection of roughly 10.6 million items, and circulation north of 26 million items a year — serving a population of about 3 million people. The system\'s 100th branch opened in Scarborough City Centre in 2014.</p>'),
            ("More than just books", '<p>Every branch is free to join and use regardless of residency status, and the system has leaned hard into being a genuine public commons — maker spaces, free Wi-Fi and computer access, newcomer settlement services, and a well-used digital lending catalogue sit alongside the physical stacks. The flagship <strong>Toronto Reference Library</strong> on Yonge Street, a dramatic 1977 atrium building designed by Raymond Moriyama, is itself a minor architectural landmark in its own right.</p>'),
        ],
        "sources": [
            ("Toronto Public Library — History of Toronto Public Library", "https://tpl.ca/about-the-library/library-history/"),
            ("Wikipedia — Toronto Public Library", "https://en.wikipedia.org/wiki/Toronto_Public_Library"),
            ("Active History — A History of the Toronto Public Library in Four Buildings", "https://activehistory.ca/blog/2020/09/02/a-history-of-the-toronto-public-library-in-four-buildings/"),
        ],
        "related_words": [],
    },
    {
        "slug": "housing",
        "title": "Toronto Housing & Cost of Living: Why It's So Expensive",
        "kicker": "A 1% vacancy rate, explained",
        "h1": "Toronto Housing & Cost of Living",
        "dek": "Toronto is consistently ranked among the least affordable housing markets in North America. Here's the actual mechanics of why — not just \"demand,\" but specific policy and supply decisions that got the city here.",
        "meta_desc": "Why Toronto housing is so expensive: rental vacancy rates, the condo-over-rental building boom, population growth, and what typical rent and home prices actually look like.",
        "keywords": "Toronto housing costs, Toronto rent prices, why is Toronto so expensive, Toronto housing crisis, Toronto cost of living",
        "hero_img": "Toronto_skyline_(2012).jpg",
        "hero_alt": "The Toronto skyline",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto shows up near the top of almost every "least affordable city in North America" ranking, and it\'s not a mysterious phenomenon — it\'s a specific, documentable mismatch between how fast the city has grown and how it has (and hasn\'t) built housing to match.</p>'),
            ("What things actually cost", '<p>As of the mid-2020s, a typical one-bedroom apartment in Toronto rents for upward of $2,400 a month, with two-bedrooms regularly exceeding $3,200; the average home purchase price sits above $1.1 million. Renting the average one-bedroom for a year runs well past the conventional benchmark that housing shouldn\'t exceed 30% of income for a typical local salary.</p>'),
            ("The vacancy-rate problem", '<p>Toronto\'s purpose-built rental vacancy rate has hovered around 1% for years — a genuinely extreme level of scarcity by North American standards, where 5% is often considered a healthy, balanced market. A market that tight puts sustained upward pressure on rent regardless of what else is happening in the economy.</p>'),
            ("Condos instead of rentals", '<p>A meaningful part of the story is policy-driven: Ontario\'s 2017 Rental Fairness Act extended rent control to all units, a tenant-friendly move that had a side effect developers responded to by building more condos for individual sale and fewer purpose-built rental buildings, since condos aren\'t subject to the same rent-control exposure. The result was more housing supply overall but proportionally less of it available specifically as long-term rental stock.</p>'),
            ("Population growth outpacing supply", '<p>Ontario has recently posted the highest population growth rate among G7 economies, and the Toronto region absorbs a large share of that growth. New housing supply, constrained by zoning, approvals timelines and construction capacity, has consistently lagged behind — the basic supply-and-demand mismatch underneath all the specific policy details.</p>'),
        ],
        "sources": [
            ("Royal York Property Management — What Is the Cost of Living in Toronto and Why Is It So High?", "https://royalyorkpropertymanagement.ca/news-article/what-is-the-cost-of-living-in-toronto-and-why-is-it-so-high"),
            ("The Green Line — Toronto's High Rent and Housing Costs Have Created a Crisis", "https://thegreenline.to/issue/toronto-housing-crisis/"),
        ],
        "related_words": ["gta"],
    },
    {
        "slug": "cne",
        "title": "The CNE: The Canadian National Exhibition, Toronto's Annual Fair",
        "kicker": "1.4 million visitors, 18 days a year",
        "h1": "The CNE (\"The Ex\")",
        "dek": "Toronto's end-of-summer ritual: an agricultural fair turned mega-event, running every year for 18 days leading up to Labour Day since 1879.",
        "meta_desc": "A guide to the Canadian National Exhibition (the CNE, or \"the Ex\") in Toronto: its 1879 founding, what it is today, and why it's still an end-of-summer tradition.",
        "keywords": "CNE Toronto, Canadian National Exhibition, the Ex Toronto, CNE history, Toronto end of summer fair",
        "hero_img": "Canadian_National_Exhibition_(CNE)_fireworks_(17419476860).jpg",
        "hero_alt": "Fireworks over the Canadian National Exhibition in Toronto",
        "hero_credit": "CNE fireworks — Wikimedia Commons, CC BY-SA 2.0",
        "sections": [
            (None, '<p>Locals just call it <strong>the Ex</strong>. Officially the <strong>Canadian National Exhibition</strong>, it\'s Toronto\'s single biggest recurring annual event, and one most Torontonians have a strong, specific opinion about (usually the food).</p>'),
            ("From agricultural fair to mega-event (1879–present)", '<p>The CNE traces back to a travelling agricultural fair that circulated among towns in what\'s now southern Ontario through the 1840s. The City of Toronto leased lakefront land as a permanent fairground in 1878 and held its first exhibition on the site the following year, drawing roughly 100,000 visitors at 25 cents admission. Newspapers began calling it the "Canadian National Exhibition" by 1904, and the name stuck.</p>'),
            ("What it is today", '<p>The modern CNE runs for 18 days leading up to and including Labour Day each September, drawing more than 1.4 million visitors annually to Exhibition Place on the western waterfront — making it one of the largest annual fairs in North America. Expect a midway with rides, agricultural and livestock displays that echo its original purpose, an air show over the lake, and a genuinely enormous, genuinely unhinged food lineup that\'s become a bigger draw than the rides for a lot of attendees.</p>'),
            ("Exhibition Place: more than one event", '<p>The CNE\'s permanent home, <strong>Exhibition Place</strong>, hosts events year-round beyond the fair itself, including concerts and the Coca-Cola Coliseum. It\'s also, not coincidentally, close to the same waterfront corridor covered in our <a href="waterfront.html">waterfront guide</a>.</p>'),
        ],
        "sources": [
            ("Wikipedia — Canadian National Exhibition", "https://en.wikipedia.org/wiki/Canadian_National_Exhibition"),
            ("The Canadian Encyclopedia — Canadian National Exhibition", "https://www.thecanadianencyclopedia.ca/en/article/canadian-national-exhibition"),
            ("The Ex — Our Organization", "https://www.theex.com/our-organization/"),
        ],
        "related_words": [],
    },
    {
        "slug": "famous-torontonians",
        "title": "Famous People From Toronto: Musicians, Writers & Scientists",
        "kicker": "From Nobel laureates to Drake",
        "h1": "Famous People From Toronto",
        "dek": "A city that produced a Nobel Prize-winning medical discovery and a generation-defining rap career has a longer list of notable natives than its music-scene reputation alone suggests.",
        "meta_desc": "Notable people from Toronto: musicians like Drake and The Weeknd, writer Margaret Atwood, insulin co-discoverer Frederick Banting, and more — who they are and what they're known for.",
        "keywords": "famous people from Toronto, celebrities from Toronto, notable Torontonians, Drake Toronto, Margaret Atwood Toronto",
        "hero_img": "Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg",
        "hero_alt": "Nathan Phillips Square and Toronto City Hall",
        "hero_credit": "Nathan Phillips Square, Toronto City Hall — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto\'s cultural export list runs a lot deeper than the music industry, though the music industry is genuinely where it\'s most dominant. A sample of who actually comes from here.</p>'),
            ("Music", '<p><strong>Drake</strong> (Aubrey Graham) is the most globally recognizable name to come out of the city\'s music scene, and did more than any single figure to popularize Toronto\'s own slang and nicknames worldwide — see our <a href="nicknames.html">nicknames guide</a> for the direct line from his work to "The Six." <strong>The Weeknd</strong> (Abel Tesfaye), who grew up in Scarborough and got his start in Parkdale, and electronic producer <strong>deadmau5</strong> (Joel Zimmerman) round out a music scene detailed further in our <a href="media.html">media and entertainment guide</a>.</p>'),
            ("Literature", '<p><strong>Margaret Atwood</strong>, author of <em>The Handmaid\'s Tale</em> and one of the most internationally recognized living Canadian writers, has lived and worked in Toronto for most of her career.</p>'),
            ("Science", '<p><strong>Sir Frederick Banting</strong>, who co-discovered insulin at the University of Toronto in 1921 and won the Nobel Prize in 1923, is arguably the most consequential name on this list by real-world impact — see our full <a href="medical-history.html">medical history guide</a>. More recently, U of T computer scientist <strong>Geoffrey Hinton</strong> has become one of the most cited researchers behind the current era of AI, discussed further in our <a href="tech-scene.html">tech scene guide</a>.</p>'),
            ("Business and architecture", '<p><strong>Mike Lazaridis</strong> and <strong>Jim Balsillie</strong>, co-founders of Research In Motion (BlackBerry), came out of the same wider southern-Ontario tech corridor as Toronto\'s current startup scene. Architect <strong>Frank Gehry</strong>, designer of the Guggenheim Museum Bilbao, was born and raised in Toronto — and returned decades later to design the current Art Gallery of Ontario building, covered in our <a href="art.html">art guide</a>.</p>'),
        ],
        "sources": [
            ("Wikipedia — List of people from Toronto", "https://en.wikipedia.org/wiki/List_of_people_from_Toronto"),
            ("Heritage U of T — Discovery of Insulin at University of Toronto", "https://heritage.utoronto.ca/exhibits/insulin"),
        ],
        "related_words": ["we-the-north", "ovo"],
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
