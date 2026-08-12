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
    {
        "slug": "airports",
        "title": "Toronto's Airports: Pearson vs. Billy Bishop",
        "kicker": "One giant, one tiny, both busy",
        "h1": "Toronto's Airports",
        "dek": "Canada's busiest airport, and — a fraction of its size but a straight shot to the downtown core — the small island airport most first-time visitors don't know exists.",
        "meta_desc": "A guide to Toronto's two airports: Toronto Pearson International Airport, Canada's busiest, and Billy Bishop Toronto City Airport on the Toronto Islands.",
        "keywords": "Toronto Pearson Airport, Billy Bishop Airport, Toronto Island Airport, Toronto airports guide, YYZ YTZ",
        "hero_img": "Toronto_Pearson_Airport-Terminal_1.JPG",
        "hero_alt": "Terminal 1 at Toronto Pearson International Airport",
        "hero_credit": "Toronto Pearson Airport, Terminal 1 — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto runs two airports with almost nothing in common except the city they serve — one a sprawling international hub, the other a small island strip a ferry ride from downtown.</p>'),
            ("Toronto Pearson International Airport (YYZ)", '<p>Canada\'s largest and busiest airport by a wide margin, serving more than 35 million passengers a year and ranking among the busiest in the world. It traces back to 1937, when the Toronto Harbour Commission built Malton Airport northwest of the city as a secondary airfield to the existing downtown airport — Malton ended up eclipsing it entirely and was later renamed for Lester B. Pearson, Canada\'s 14th prime minister and a Nobel Peace Prize laureate.</p>'),
            ("Billy Bishop Toronto City Airport (YTZ)", '<p>A much smaller airport on the Toronto Islands, established in 1939 and named for World War I flying ace William Avery Bishop, a Victoria Cross recipient. It handles close to 2.8 million passengers a year on short-haul and regional routes, with the appeal being pure convenience — a pedestrian tunnel connects it directly to the mainland, putting it a 10-minute ride from the Financial District, versus 30–45 minutes from Pearson.</p>'),
            ("Two very different flight experiences", '<p>Pearson is the default for almost all international and long-haul travel and has direct connections to destinations worldwide; Billy Bishop is largely a domestic and short-haul U.S. option, historically dominated by Porter Airlines, which built its entire brand around the small island airport\'s downtown convenience.</p>'),
        ],
        "sources": [
            ("Wikipedia — History of Toronto Pearson International Airport", "https://en.wikipedia.org/wiki/History_of_Toronto_Pearson_International_Airport"),
            ("Billy Bishop Toronto City Airport — History of the Airport", "https://www.billybishopairport.com/the-airport/history-of-the-airport/"),
            ("Wikipedia — List of the busiest airports in Canada", "https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_Canada"),
        ],
        "related_words": [],
    },
    {
        "slug": "government",
        "title": "Toronto's City Government: Mayors, City Hall & How It's Run",
        "kicker": "One council, 25 wards, one very online mayoralty",
        "h1": "Toronto's City Government",
        "dek": "How Toronto is actually governed post-amalgamation — the mayor and city council system, the architecture of City Hall itself, and the mayoralty that briefly made the city a global punchline.",
        "meta_desc": "A guide to Toronto's city government: the mayor-council system since the 1998 amalgamation, City Hall's architecture, and the history of the office including the Rob Ford era.",
        "keywords": "Toronto city government, Toronto mayor history, Toronto City Hall, Rob Ford mayor, Mel Lastman, Toronto city council",
        "hero_img": "Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg",
        "hero_alt": "Toronto City Hall and Nathan Phillips Square",
        "hero_credit": "Toronto City Hall, Nathan Phillips Square — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Toronto is governed by an elected mayor and a city council, currently 25 councillors representing individual wards, under a structure that dates only to the 1998 amalgamation covered in our <a href="history.html">history guide</a> — before that, six separate municipal governments ran the constituent cities that now make up Toronto.</p>'),
            ("City Hall itself", '<p>The current, unmistakably modernist Toronto City Hall — two curved towers wrapped around a domed council chamber — opened in 1965, the winning entry in an international design competition won by Finnish architect Viljo Revell. It replaced what\'s now called <strong>Old City Hall</strong>, a Romanesque Revival building from 1899 a block away that still stands and now serves mainly as a courthouse. The plaza in front of the new City Hall, Nathan Phillips Square, hosts the city\'s outdoor skating rink each winter and the annual raising of the Toronto sign.</p>'),
            ("Mel Lastman: the first post-amalgamation mayor", '<p><strong>Mel Lastman</strong>, previously mayor of the suburban city of North York for 25 years, became Toronto\'s first mayor under the new amalgamated system in 1998, serving until 2003 — a genuinely awkward transition period stitching six formerly independent city bureaucracies into one.</p>'),
            ("Rob Ford (2010–2014)", '<p>Toronto\'s best-known mayor internationally, for reasons the city would probably prefer otherwise. Rob Ford\'s single term became a global media story after a 2013 video surfaced showing him smoking crack cocaine, part of a wider substance-abuse scandal that led city council to strip most of his mayoral powers while he remained formally in office. It\'s a genuinely unusual chapter in Canadian municipal politics, and remains the single most-referenced fact about Toronto city government outside Canada.</p>'),
            ("Since then", '<p>John Tory served as mayor from 2014 to 2023, followed by Olivia Chow, elected in a 2023 by-election after Tory\'s resignation — a far lower-drama stretch of the office than the Ford years, focused mostly on transit funding and the housing pressures covered in our <a href="housing.html">housing guide</a>.</p>'),
        ],
        "sources": [
            ("Wikipedia — Mayor of Toronto", "https://en.wikipedia.org/wiki/Mayor_of_Toronto"),
            ("Wikipedia — Mayoralty of Rob Ford", "https://en.wikipedia.org/wiki/Mayoralty_of_Rob_Ford"),
            ("Wikipedia — Toronto City Hall", "https://en.wikipedia.org/wiki/Toronto_City_Hall"),
        ],
        "related_words": [],
    },
    {
        "slug": "comedy",
        "title": "Toronto's Comedy Scene: Second City, SCTV & Its Famous Alumni",
        "kicker": "Where a huge chunk of North American comedy trained",
        "h1": "Toronto's Comedy Scene",
        "dek": "A Chicago import that put down roots in an old firehouse in 1973 turned into one of the most influential comedy pipelines in North America — Toronto's Second City and SCTV.",
        "meta_desc": "The history of Toronto's comedy scene: Second City Toronto's 1973 founding, the SCTV television series, and the long list of major comedians who came out of both.",
        "keywords": "Second City Toronto, SCTV history, Toronto comedy scene, John Candy, Mike Myers Toronto, Toronto comedians",
        "hero_img": "Toronto-CN-tower-and-Canadian-flag-skyline.jpg",
        "hero_alt": "The Toronto skyline and CN Tower",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto\'s comedy pedigree rivals its music scene for sheer output — anchored by one institution that\'s been training performers here since 1973.</p>'),
            ("Second City Toronto (founded 1973)", '<p>The Chicago-born improv theatre <strong>Second City</strong> opened a Toronto branch in 1973, settling into a permanent home in a converted old firehouse the following year. Its first Toronto cast included <strong>Dan Aykroyd</strong>, <strong>Gilda Radner</strong> and <strong>Joe Flaherty</strong>; <strong>John Candy</strong> joined in 1973 at age 26. Since then, hundreds of performers have trained there, including <strong>Mike Myers</strong>, <strong>Eugene Levy</strong>, <strong>Catherine O\'Hara</strong> and <strong>Martin Short</strong>.</p>'),
            ("SCTV (1976–1984)", '<p>Second City\'s Toronto cast spun off into <strong>SCTV</strong>, a sketch series built around a fictional small-town TV station, first produced for Global Television in 1976. Over seven years and 185 episodes it earned 13 Emmy nominations and gave the world <em>The Great White North</em>, Rick Moranis and Dave Thomas\'s Bob and Doug McKenzie sketches — a deliberately exaggerated parody of Canadian identity that, ironically, ended up shaping how a lot of people outside Canada actually picture it.</p>'),
            ("The alumni network today", '<p>The through-line from 1970s Second City Toronto to the current landscape of American film and television comedy is genuinely direct — a huge share of SNL writers, showrunners and film comedy leads over the past four decades trace back to this one Toronto stage. See our <a href="famous-torontonians.html">famous Torontonians guide</a> and <a href="media.html">media and entertainment guide</a> for how this connects to the rest of the city\'s outsized entertainment-industry footprint.</p>'),
        ],
        "sources": [
            ("Wikipedia — Second City Television", "https://en.wikipedia.org/wiki/Second_City_Television"),
            ("Canada's Walk of Fame — SCTV", "https://www.canadaswalkoffame.com/inductees/sctv/"),
            ("CBC Comedy — What It Takes to Be First at The Second City", "https://www.cbc.ca/comedy/what-it-takes-to-be-first-at-the-second-city-1.5381106"),
        ],
        "related_words": [],
    },
    {
        "slug": "zoo-science-centre",
        "title": "Toronto Zoo & the Ontario Science Centre",
        "kicker": "3,800 animals, and a closed Brutalist landmark",
        "h1": "Toronto Zoo & the Ontario Science Centre",
        "dek": "One of the largest zoos in the world by area, and a beloved Brutalist science museum the province abruptly closed in 2024 — two very different fates for two of Toronto's classic family attractions.",
        "meta_desc": "A guide to the Toronto Zoo, one of the world's largest zoos by area, and the Ontario Science Centre, a 1969 Brutalist landmark closed by the province in 2024.",
        "keywords": "Toronto Zoo history, Ontario Science Centre closure, Toronto family attractions, Toronto Zoo facts",
        "hero_img": "Kesho_Park_at_the_Toronto_Zoo_(3354803789).jpg",
        "hero_alt": "Kesho Park at the Toronto Zoo",
        "hero_credit": "Kesho Park, Toronto Zoo — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Two of Toronto\'s classic family-outing institutions, both born out of 1960s civic ambition — one still going strong, the other now a genuine architectural loss.</p>'),
            ("Toronto Zoo", '<p>Opened August 15, 1974 as the Metropolitan Toronto Zoo (renamed simply Toronto Zoo in 1998, matching the wider amalgamation), replacing an older, cramped municipal zoo in Riverdale Park. At 287 hectares (710 acres), it\'s one of the largest zoos in the world by land area, home to roughly 3,800 animals across nearly 450 species, laid out in geographic zones connected by a monorail.</p>'),
            ("Ontario Science Centre (1969–2024)", '<p>A hands-on science and technology museum in Flemingdon Park, founded in 1964 and opened to the public in 1969 — an example of ambitious Brutalist civic architecture, its buildings and exhibit halls connected by bridges and escalators across a ravine site. It housed Ontario\'s only IMAX Dome theatre starting in 1996. In June 2024, the provincial government abruptly and permanently closed the building, citing deteriorating infrastructure and a risk of roof failure under snow load — a closure that drew significant public backlash and remains a genuinely contested local story.</p>'),
            ("What\'s left", '<p>With the Science Centre shuttered, the Toronto Zoo — alongside <a href="parks.html">High Park and the Toronto Islands</a> — remains one of the city\'s most reliable large-scale family attractions, and the province has said a scaled-down science centre replacement is planned for Ontario Place on the waterfront, though that project remains years out.</p>'),
        ],
        "sources": [
            ("Toronto Zoo — Fifty Timeline", "https://www.torontozoo.com/history"),
            ("Wikipedia — Ontario Science Centre", "https://en.wikipedia.org/wiki/Ontario_Science_Centre"),
            ("Britannica — Toronto Zoo", "https://www.britannica.com/place/Toronto-Zoo"),
        ],
        "related_words": [],
    },
    {
        "slug": "craft-beer",
        "title": "Toronto's Craft Beer Scene: 70+ Independent Breweries",
        "kicker": "From one 1985 brewery to a whole neighbourhood of them",
        "h1": "Toronto's Craft Beer Scene",
        "dek": "A city that drank mostly big-brand beer for most of the 20th century now supports more than 70 independent breweries — the modern craft scene traces back to a single 1985 opening.",
        "meta_desc": "A guide to Toronto's craft beer scene: how it started with Upper Canada Brewing Co. in 1985, key breweries like Steam Whistle and Mill Street, and the city's 70+ independent breweries today.",
        "keywords": "Toronto craft beer, Toronto breweries, Steam Whistle Brewing, Mill Street Brewery, Toronto beer scene history",
        "hero_img": "Toronto_Railway_Museum_and_Steam_Whistle_Brewery_are_located_in_the_Roundhouse_Park_(27622030420).jpg",
        "hero_alt": "Steam Whistle Brewery at Roundhouse Park in Toronto",
        "hero_credit": "Steam Whistle Brewery, Roundhouse Park — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto drank mostly the same handful of big national beer brands for most of the 20th century. That changed starting in a single year — 1985 — and hasn\'t really stopped since.</p>'),
            ("The craft renaissance starts in 1985", '<p>The modern rebirth of small independent brewing in Toronto is generally traced to <strong>Upper Canada Brewing Co.</strong>, which opened in 1985. A wave followed quickly after: Amsterdam Brasserie and Brewpub (1986), C\'est What (1988), and the Granite Brewery (1991), each pushing further from the mass-market lagers that had dominated for decades.</p>'),
            ("Steam Whistle and Mill Street", '<p>Two names now synonymous with Toronto craft beer: <strong>Steam Whistle Brewing</strong>, founded in 1998 and based in the historic John Street Roundhouse at Roundhouse Park near the CN Tower, and <strong>Mill Street Brewery</strong>, founded in 2002 in the <a href="waterfront.html">Distillery District</a>\'s restored Victorian industrial buildings — both choosing genuinely historic industrial spaces as home rather than generic retail units, which became something of a pattern for the scene.</p>'),
            ("Where it stands now", '<p>Toronto is now home to more than 70 independent breweries, one of the highest concentrations of any Canadian city, spanning everything from Bellwoods Brewery\'s inventive sours in Trinity Bellwoods to large-scale operations like Amsterdam\'s Leaside facility. It sits alongside the <a href="food.html">wider food scene guide</a> as one of the more visibly changed parts of Toronto\'s culture over the last two decades.</p>'),
        ],
        "sources": [
            ("City of Toronto — Made in Toronto: Whiskey and Beer", "https://www.toronto.ca/explore-enjoy/history-art-culture/online-exhibits/web-exhibits/web-exhibits-culture-people/made-in-toronto-whiskey-and-beer/"),
            ("Ecotone — A Taste of History: Toronto's Craft Breweries", "https://ecotone.ca/a-taste-of-history-torontos-craft-breweries/"),
            ("Wikipedia — Steam Whistle Brewing", "https://en.wikipedia.org/wiki/Steam_Whistle_Brewing"),
        ],
        "related_words": [],
    },
    {
        "slug": "safety",
        "title": "Is Toronto Safe? Crime Rates & Safety Guide",
        "kicker": "6th safest major city in the world, per The Economist",
        "h1": "Is Toronto Safe?",
        "dek": "Toronto's reputation is safer than its headlines sometimes suggest — the actual crime statistics put it well below the Canadian national average and among the safest big cities in North America.",
        "meta_desc": "Is Toronto safe? A look at the actual crime statistics: how Toronto compares to the Canadian national average and other major North American cities.",
        "keywords": "is Toronto safe, Toronto crime rate, Toronto crime statistics, Toronto safety compared to other cities",
        "hero_img": "City_Hall,_Toronto,_Ontario.jpg",
        "hero_alt": "Toronto City Hall",
        "hero_credit": "Toronto City Hall — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>A common question from anyone considering a visit or a move: is Toronto actually safe? The honest, statistics-backed answer is yes, comparatively — though "comparatively" is doing real work in that sentence, and it\'s worth looking at the actual numbers rather than headlines.</p>'),
            ("How Toronto ranks globally", '<p>In 2024, The Economist\'s Safe Cities Index ranked Toronto the <strong>6th safest major city in the world</strong> and the safest major city in North America — ahead of most large U.S. and European cities on the index\'s combined measure of digital, health, infrastructure and personal security.</p>'),
            ("Toronto vs. the rest of Canada", '<p>Toronto recorded 2,977 police-reported Criminal Code incidents per 100,000 people in 2023 — well below the national Canadian average of 5,668, and lower than both Montreal (5,074) and notably Vancouver (7,545). Its homicide rate, around 2.1 per 100,000 in 2024, sits close to the national rate and far below cities like Winnipeg.</p>'),
            ("Toronto vs. U.S. cities", '<p>Compared to peer-sized American cities, Toronto\'s violent crime and homicide rates run substantially lower than New York\'s or Los Angeles\'s, a gap partly attributable to Canada\'s stricter gun-control regime. Property crime is one of the few categories where Toronto has recently run comparable to or higher than some U.S. peer cities.</p>'),
            ("What this means practically", '<p>Like any large city, safety in Toronto varies meaningfully by neighbourhood and time of day — see our <a href="neighbourhoods.html">general neighbourhoods guide</a> for the lay of the land. But at the city-wide level, the data consistently supports Toronto\'s general reputation as unusually safe for a city of its size.</p>'),
        ],
        "sources": [
            ("Wikipedia — Crime in Toronto", "https://en.wikipedia.org/wiki/Crime_in_Toronto"),
            ("Statistics Canada — Safe Cities Profile Series: Toronto", "https://www150.statcan.gc.ca/n1/pub/85-002-x/2020001/article/00001/toronto-eng.htm"),
            ("Kruse Law — Crime Rate Statistics in Toronto", "https://www.kruselaw.ca/blog/crime-rate-statistics-in-toronto-2025/"),
        ],
        "related_words": [],
    },
    {
        "slug": "ethnic-enclaves",
        "title": "Toronto's Ethnic Enclaves: Chinatown, Little Italy, Greektown & More",
        "kicker": "A world tour, one streetcar ride apart",
        "h1": "Toronto's Ethnic Enclaves",
        "dek": "Beyond the general neighbourhood map, Toronto has a specific set of streets that function as living cultural districts — three separate Chinatowns, a Greektown that was once the largest in North America, and more.",
        "meta_desc": "A guide to Toronto's ethnic enclaves: Chinatown on Spadina, Little Italy on College Street, Greektown on the Danforth, Little India, and Little Portugal — history and what's there today.",
        "keywords": "Toronto Chinatown, Little Italy Toronto, Greektown Danforth, Little India Toronto, Little Portugal Toronto, Toronto ethnic neighbourhoods",
        "hero_img": "Chinatown_toronto_spadina_avenue.JPG",
        "hero_alt": "Chinatown along Spadina Avenue in Toronto",
        "hero_credit": "Chinatown, Spadina Avenue — Wikimedia Commons, CC BY-SA",
        "sections": [
            (None, '<p>Our general <a href="neighbourhoods.html">neighbourhoods guide</a> covers the city\'s broad geography. This is the more specific layer underneath it — commercial strips that function as living cultural districts, each with its own settlement history.</p>'),
            ("Chinatown (actually three of them)", '<p>Toronto doesn\'t have one Chinatown — it has three, plus several smaller nodes people casually call by the same name. The downtown Chinatown along <strong>Spadina Avenue</strong> is the best known, and it has its own layered history: the site was a Jewish immigrant district before it became predominantly Chinese, first through immigration from southern China and Hong Kong and, more recently, mainland China.</p>'),
            ("Little Italy", '<p>Centred on College Street between Ossington and Bathurst, Little Italy formed in the early 20th century and grew substantially after both world wars as Italian immigration to Toronto accelerated. It remains one of the city\'s most concentrated restaurant-and-café strips, and hosts a large public screening party during the FIFA World Cup whenever Italy plays.</p>'),
            ("Greektown (the Danforth)", '<p>Through the 1970s and 80s, the Danforth was regarded as the largest Greektown in North America — one estimate from 1976 put roughly 65,000 Greek residents in the surrounding area, though the strip has always shared space with Estonian, Lithuanian, Italian, Chinese and Finnish communities too. It\'s now also home to Toronto\'s <a href="festivals.html">Taste of the Danforth</a> street festival each August.</p>'),
            ("Little India and Little Portugal", '<p><strong>Little India</strong>, also known as the Gerrard India Bazaar on Gerrard Street East, traces back to one businessman opening a South Asian movie theatre and building a commercial strip around it. <strong>Little Portugal</strong>, around Dundas Street West, formed alongside Little Italy as part of the same mid-20th-century wave of Southern European immigration to west-end Toronto.</p>'),
        ],
        "sources": [
            ("Wikipedia — Chinatown, Toronto", "https://en.wikipedia.org/wiki/Chinatown,_Toronto"),
            ("Wikipedia — Greektown, Toronto", "https://en.wikipedia.org/wiki/Greektown,_Toronto"),
            ("Prepare for Canada — Toronto Neighbourhoods: Ethnic Enclaves to Discover", "https://prepareforcanada.com/living/housing/toronto-neighbourhoods-ethnic-enclaves-to-discover"),
        ],
        "related_words": [],
    },
    {
        "slug": "ravines",
        "title": "Toronto's Ravine System: The World's Largest Urban Ravine Network",
        "kicker": "150 ravines, 1,200+ km of edges",
        "h1": "Toronto's Ravine System",
        "dek": "Hidden beneath the street grid is the largest ravine system of any city in the world — 30 times the size of New York's Central Park, and within a 10-minute walk of nearly a third of Toronto residents.",
        "meta_desc": "A guide to the Toronto ravine system: the largest urban ravine network in the world, formed 12,000 years ago, protecting over 110 square kilometres of the city.",
        "keywords": "Toronto ravine system, Toronto ravines, largest urban ravine network, Toronto hidden nature, Don Valley ravines",
        "hero_img": "East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg",
        "hero_alt": "A pedestrian bridge over the Don River in a Toronto ravine",
        "hero_credit": "East Don Parkland — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Most visitors never see it, because it\'s built to be invisible from street level — but Toronto sits on top of the largest ravine system of any city in the world, a hidden second landscape running underneath the grid.</p>'),
            ("The scale of it", '<p>The system includes at least 150 individual ravines, protected under the city\'s Ravine and Natural Feature Protection Bylaw across roughly 110 square kilometres (42 sq mi) of public and private land — about 30 times the area of New York\'s Central Park. Measured by edge length rather than area, the ravines add up to more than 1,200 kilometres, roughly ten times longer than Toronto\'s actual Lake Ontario waterfront. Close to a third of the city\'s population lives within a 10-minute walk of one.</p>'),
            ("How old it is", '<p>The river valleys that became these ravines started forming around 12,000 years ago, as glaciers retreated at the end of the last ice age. Archaeological evidence shows humans occupying parts of the ravine system as early as roughly 9,000 BCE — making it, in a real sense, the oldest continuously used part of the city\'s landscape, well predating even the <a href="indigenous-history.html">Indigenous history</a> covered in our other guide.</p>'),
            ("What they actually do", '<p>Beyond recreation — over a million people a year use the ravines to hike, bike and explore — they function as a working watershed system: filtering and slowing stormwater, supporting biodiversity that can\'t survive on the paved surface above, and measurably reducing urban heat. The most developed and accessible stretch is the <a href="parks.html">Don Valley</a>, but the system extends into ravines across almost every part of the city, including many with no formal park designation at all.</p>'),
        ],
        "sources": [
            ("Wikipedia — Toronto ravine system", "https://en.wikipedia.org/wiki/Toronto_ravine_system"),
            ("Curiocity — Toronto Is Home to the Largest Ravine System in the World", "https://curiocity.com/toronto-ravine-system-largest-in-the-world/"),
            ("City of Toronto — Ravine Strategy", "https://www.toronto.ca/city-government/accountability-operations-customer-service/long-term-vision-plans-and-strategies/ravine-strategy/"),
        ],
        "related_words": [],
    },
    {
        "slug": "newspapers",
        "title": "Toronto's Newspapers: The Globe and Mail, Toronto Star & National Post",
        "kicker": "Three mastheads, one very old rivalry",
        "h1": "Toronto's Newspapers",
        "dek": "Canada's national newspaper industry is disproportionately headquartered in Toronto — including one paper whose roots trace back to 1844, and a lost-jobs labour dispute that accidentally created another.",
        "meta_desc": "A guide to Toronto's major newspapers: The Globe and Mail's 1844 origins, the Toronto Star's founding by laid-off printers in 1892, and the National Post's 1998 launch.",
        "keywords": "Globe and Mail history, Toronto Star history, National Post history, Toronto newspapers, Canadian newspaper industry Toronto",
        "hero_img": "Toronto_skyline_(2012).jpg",
        "hero_alt": "The Toronto skyline",
        "hero_credit": "Toronto skyline — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Canada\'s newspaper industry is unusually concentrated in Toronto, and the three biggest national and metro papers all have genuinely distinct, occasionally accidental, origin stories.</p>'),
            ("The Globe and Mail (roots to 1844)", '<p>The Globe and Mail\'s lineage traces back to <strong>The Globe</strong>, founded in 1844 by Scottish immigrant George Brown, who later became a Father of Confederation. A rival, <strong>The Empire</strong>, was founded in 1887 by then–prime minister John A. Macdonald and later merged into <strong>The Mail and Empire</strong>. In 1936, The Globe and The Mail and Empire merged into the paper that exists today, now generally regarded as Canada\'s paper of record.</p>'),
            ("Toronto Star (founded 1892, by accident)", '<p>The Toronto Star started life as the <strong>Evening Star</strong> in 1892, founded by 25 printers who had just lost their jobs in a labour dispute — not exactly a boardroom business plan. It changed hands repeatedly until 1899, when publisher <strong>Joseph E. Atkinson</strong> took over, renamed it the Toronto Daily Star, and grew its circulation from 7,000 to 40,000 within five years.</p>'),
            ("National Post (1998)", '<p>The newest of the three, founded in 1998 by media magnate <strong>Conrad Black</strong> as a deliberate national competitor to The Globe and Mail, built out of what had been a Toronto business paper. Black sold it to CanWest Global in 2000–2001, and it has changed hands several more times since.</p>'),
        ],
        "sources": [
            ("Wikipedia — The Globe and Mail", "https://en.wikipedia.org/wiki/The_Globe_and_Mail"),
            ("Britannica — The Toronto Star", "https://www.britannica.com/topic/The-Toronto-Star"),
            ("Wikipedia — National Post", "https://en.wikipedia.org/wiki/National_Post"),
        ],
        "related_words": [],
    },
    {
        "slug": "cycling",
        "title": "Cycling in Toronto: Bike Lanes and a 120-Year Fight for Them",
        "kicker": "The Bloor bike lane took over a century",
        "h1": "Cycling in Toronto",
        "dek": "Toronto cyclists were lobbying City Hall for better infrastructure in 1896. The Bloor Street bike lane — arguably the city's flagship piece of cycling infrastructure — didn't open until 2016.",
        "meta_desc": "A guide to cycling in Toronto: the century-long fight for bike lanes on Bloor Street, the modern protected bike lane network, and Bike Share Toronto.",
        "keywords": "Toronto bike lanes, Bloor Street bike lane history, cycling in Toronto, Bike Share Toronto, Toronto cycling infrastructure",
        "hero_img": "Toronto_Protected_Bike_Lanes.jpg",
        "hero_alt": "A protected bike lane in Toronto",
        "hero_credit": "Protected bike lane, Toronto — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto\'s relationship with the bicycle is much older than the current bike lane debates suggest — and the timeline of one specific street, Bloor, tells the whole story in miniature.</p>'),
            ("An unexpectedly old fight", '<p>On February 15, 1896, Toronto bicycle club representatives met at the Athenaeum Club to lobby City Hall for a citywide cycling plan. Cycling\'s early-20th-century popularity decline cost advocates their political leverage for decades — a 1978 city-commissioned study considered a bike lane on Bloor and instead recommended a wider curb lane on the parallel Harbord Street; a 1990s study again flagged Bloor-Danforth as an ideal cross-town cycling route and again went nowhere.</p>'),
            ("Bells on Bloor and the eventual win", '<p>Modern grassroots pressure picked up with <strong>Bells on Bloor</strong>, formed in 2007, which organized annual "pedal-powered" bike parades down the street to demonstrate demand — 500 riders at the first parade in 2007, roughly 2,000 by 2009. A pilot protected bike lane finally opened along Bloor from Shaw Street to Avenue Road in August 2016, roughly 120 years after that first 1896 meeting, physically separated from traffic by posts and parked cars.</p>'),
            ("The network and bike share today", '<p>Toronto now runs a growing network of protected and painted bike lanes across the downtown core and select arterial roads, alongside <strong>Bike Share Toronto</strong>, a public docked bike-share system with stations concentrated downtown and expanding outward. Debates over new lane installations remain a genuinely recurring, often contentious item at city council — a modern echo of the same fight that started in 1896.</p>'),
        ],
        "sources": [
            ("NOW Magazine — Bloor Bike Lanes: 120 Years in the Making", "https://nowtoronto.com/news/bloor-bike-lanes-120-years-in-the-making/"),
            ("Toronto Community Bikeways Coalition — Short History of Bike Lanes on Bloor", "https://www.communitybikewaysto.ca/short-history-of-bike-lanes-on-bloor"),
            ("Toronto Life — Dividing Line: How the Bloor Street Bike Lane Turned the City Into a Battlefield", "https://torontolife.com/deep-dives/dividing-line-bloor-street-bike-lane-turned-toronto-into-a-battlefield/"),
        ],
        "related_words": [],
    },
    {
        "slug": "religion",
        "title": "Religious Diversity in Toronto: Faiths, Temples & Houses of Worship",
        "kicker": "From a mostly-Presbyterian city to every faith on Earth",
        "h1": "Religious Diversity in Toronto",
        "dek": "Toronto's 19th-century religious makeup was overwhelmingly Protestant. The modern city holds functioning places of worship for nearly every major world religion — often inside buildings originally built for a completely different faith.",
        "meta_desc": "A guide to religious diversity in Toronto: its 19th-century Protestant-majority history, how immigration reshaped it, and the city's mosques, synagogues, temples and churches today.",
        "keywords": "Toronto religious diversity, Toronto places of worship, Toronto mosques synagogues temples, multi-faith Toronto history",
        "hero_img": "Ismaili_Centre,_Toronto_-_Prayer_hall.jpg",
        "hero_alt": "The prayer hall of the Ismaili Centre in Toronto",
        "hero_credit": "Ismaili Centre, Toronto, prayer hall — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Toronto\'s reputation as one of the most religiously diverse cities in the world is a relatively recent development — as recently as the mid-19th century, its religious makeup looked nothing like it does today.</p>'),
            ("A mostly-Protestant 19th-century city", '<p>In 1851, Protestants made up roughly 73% of Toronto\'s population, with Roman Catholics at about 25% and only small numbers of Jews, Unitarians and freethinkers rounding out the rest — part of why the city earned the nickname <a href="nicknames.html">Toronto the Good</a>, a Protestant-inflected moral reputation that stuck for decades.</p>'),
            ("Immigration reshaped it, building by building", '<p>Waves of immigration through the 20th century transformed both the city\'s religious makeup and, often literally, its buildings. Eastern European Jewish immigrants built the <strong>Kiever Synagogue</strong> in west Toronto in the 1920s; a Presbyterian church near High Park, built in 1930, was purchased and converted in 1969 into the <strong>Jami Mosque</strong>; <strong>Santa Inês</strong>, built in 1913 to serve an Italian Catholic community, now primarily serves a Portuguese congregation — a pattern of a single building serving several different faith communities in succession, decade after decade, as the surrounding neighbourhood\'s <a href="ethnic-enclaves.html">immigrant population</a> changed.</p>'),
            ("Toronto today", '<p>The modern city holds functioning houses of worship for Christianity in all its denominations, Islam, Judaism, Hinduism, Sikhism, Buddhism, the Baha\'i Faith and more, many of which — mosques especially — double as genuine community centres running settlement services, youth programs and social events well beyond religious observance itself.</p>'),
        ],
        "sources": [
            ("City of Toronto — Spiritual Toronto", "https://www.toronto.ca/explore-enjoy/history-art-culture/museums/virtual-exhibits/textures-of-a-lost-toronto/spiritual-toronto/"),
            ("Ontario Heritage Trust — Ontario's Rich Religious Heritage", "https://www.heritagetrust.on.ca/heritagematters/articles/ontarios-rich-religious-heritage"),
        ],
        "related_words": [],
    },
    {
        "slug": "coffee-culture",
        "title": "Toronto's Coffee Culture: The Rise of Third-Wave Cafés",
        "kicker": "From diner coffee to single-origin pour-overs",
        "h1": "Toronto's Coffee Culture",
        "dek": "Toronto's independent café scene took off precisely when the big chains stumbled — a 2008–09 recession that hit Starbucks hard cleared space for a wave of Toronto-grown, barista-driven coffee shops.",
        "meta_desc": "A guide to Toronto's coffee culture: the shift from chain coffee to third-wave independent cafés, key shops like Sam James Coffee Bar, and the city's café scene today.",
        "keywords": "Toronto coffee culture, Toronto independent cafes, third wave coffee Toronto, best coffee shops Toronto history",
        "hero_img": "The_Only_Cafe,_Danforth_Avenue,_Toronto,_Canada,_May_2014.jpg",
        "hero_alt": "The Only Cafe on Danforth Avenue in Toronto",
        "hero_credit": "The Only Cafe, Danforth Avenue — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Toronto\'s coffee scene followed the same three-wave pattern as the rest of North America — mass-market chains, then independent cafés, then a more deliberate, craft-focused "third wave" — but the timing of that last shift here was shaped by a very specific economic moment.</p>'),
            ("The chain-coffee slowdown that created an opening", '<p>In 2008 and 2009, as recession hit, Starbucks closed close to 1,000 locations worldwide and shifted toward fully automatic espresso machines, while Second Cup — the dominant Canadian chain — struggled too. That retreat by the big players cleared real commercial space and customer attention for a wave of Toronto-founded independents just as third-wave, barista-driven coffee culture was arriving from the U.S. West Coast.</p>'),
            ("The independents that defined it", '<p>A run of now-established Toronto cafés opened in quick succession through this window: <strong>Cherry Bomb</strong> (2005), <strong>Manic</strong> (2007), <strong>Lit</strong> (2008), and <strong>Sam James Coffee Bar</strong> (2009), which grew into one of the city\'s most recognized coffee names. <strong>JetFuel</strong>, on the Cabbagetown-adjacent stretch near <a href="architecture.html">Cabbagetown</a>, predates all of them — open since 1992 with no printed menu, baristas making drinks to order.</p>'),
            ("What third wave actually means", '<p>Third-wave coffee treats the drink as an artisanal product rather than a commodity — emphasis on bean origin, ethical sourcing, roast quality and precise brewing, often with shops roasting their own beans or partnering directly with small-batch roasters. That ethos is now the default expectation at Toronto\'s better-known independent cafés, spread across neighbourhoods from Ossington to the Danforth.</p>'),
        ],
        "sources": [
            ("Foodism — Brewing a Cup of Toronto's Coffee Scene", "https://foodism.ca/culture/toronto-coffee/"),
            ("Foodism — Sacred Grounds: The Rise of Toronto's Third-Wave Craft Coffee Scene", "https://foodism.ca/culture/sacred-grounds-craft-coffee/"),
            ("Canadian Barista Institute — History of the Third Wave Coffee Movement in Canada", "https://canadianbaristainstitute.com/en-us/blogs/news/defining-third-wave-coffee-movement-and-documenting-its-origins-in-canada"),
        ],
        "related_words": [],
    },
    {
        "slug": "union-station",
        "title": "Union Station Toronto: History of a 1927 Beaux-Arts Landmark",
        "kicker": "Every commuter train in the region, one roof",
        "h1": "Union Station",
        "dek": "Toronto's grand 1927 train hall is the single busiest piece of transportation infrastructure in the country — over a quarter million people a day pass through it, more than through Pearson Airport.",
        "meta_desc": "The history of Toronto's Union Station: its 1927 Beaux-Arts construction, the historic train shed, and its role today as Canada's busiest transportation hub.",
        "keywords": "Union Station Toronto history, Toronto Union Station architecture, busiest train station Canada, Union Station Great Hall",
        "hero_img": "Union_Station_grand_hall.jpg",
        "hero_alt": "The Great Hall inside Toronto's Union Station",
        "hero_credit": "Union Station Great Hall — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>More people pass through Union Station on an average weekday than through Toronto Pearson Airport — a fact that surprises a lot of visitors, given how much less attention the building gets internationally.</p>'),
            ("A grand building for a growing city (opened 1927)", '<p>The current Union Station opened in 1927, jointly commissioned by the Canadian Pacific Railway and Grand Trunk Railway and designed in the Beaux-Arts style by a team including Toronto architect John M. Lyle. Its Great Hall runs 79 metres long with a 27-metre coffered ceiling, built to project the confidence of a city that had just spent decades <a href="history.html">growing rapidly on the back of the railway</a>.</p>'),
            ("The train shed", '<p>Behind the Great Hall, the Union Station Train Shed, built 1929–30, uses a "Bush shed" design — smoke ducts positioned directly above the tracks that vent locomotive exhaust upward while keeping platforms below relatively clear, a clever piece of pre-diesel railway engineering that\'s still functionally intact today.</p>'),
            ("A 2010s restoration", '<p>A major restoration and revitalization project, starting around 2010, cleaned and repaired the facade, restored the historic concourse and VIA Rail waiting rooms, and added new retail concourses beneath the station without altering the protected heritage spaces above.</p>'),
            ("The hub it is today", '<p>Union Station is now the meeting point for Toronto\'s TTC subway, <a href="go-transit.html">GO Transit\'s regional rail network</a>, VIA Rail\'s national intercity trains, and the UP Express airport link to Pearson — arguably the single most load-bearing piece of infrastructure in the whole region, all funnelled through one 1927 building.</p>'),
        ],
        "sources": [
            ("City of Toronto — History of Union Station", "https://www.toronto.ca/services-payments/venues-facilities-bookings/booking-city-facilities/union-station/history-of-union-station/"),
            ("GO Transit — Union Station: History, Facts & Map", "https://www.gotransit.com/en/find-a-station/un/union-station-history-facts-and-map"),
            ("Toronto Railway Historical Association — Union Station (1927)", "https://www.trha.ca/trha/history/stations/toronto-union-station-1927/"),
        ],
        "related_words": ["t-dot"],
    },
    {
        "slug": "go-transit",
        "title": "GO Transit: Toronto's Regional Rail and Bus Network",
        "kicker": "One line in 1967, a whole region now",
        "h1": "GO Transit",
        "dek": "Where the TTC ends, GO Transit picks up — the regional rail and bus system that stitches Toronto to its surrounding commuter belt, running since a single experimental line in 1967.",
        "meta_desc": "A guide to GO Transit: North America's first modern regional rail service, launched in 1967, and how it connects Toronto to the wider Greater Golden Horseshoe region today.",
        "keywords": "GO Transit history, GO Train Toronto, Toronto regional rail, PRESTO card, Toronto commuter rail",
        "hero_img": "GO_Transit_MP40-3C_602_Oshawa_Turnaround_Rushhour.JPG",
        "hero_alt": "A GO Transit train at Oshawa GO Station",
        "hero_credit": "GO Transit train, Oshawa — Wikimedia Commons, CC BY 3.0",
        "sections": [
            (None, '<p>Our <a href="transit.html">TTC guide</a> covers getting around inside Toronto. GO Transit is the layer above that — the regional system that connects the city to the much larger commuter region surrounding it, formally called the Greater Golden Horseshoe.</p>'),
            ("A 1967 experiment that stuck", '<p>GO Transit launched on May 23, 1967 with a single rail line along the Lakeshore corridor between Pickering and Hamilton — one of the first modern regional commuter rail services anywhere in North America, and originally planned as a three-year pilot project. It proved popular enough that it never shut down, and instead kept expanding.</p>'),
            ("The network today", '<p>GO Transit now runs seven rail lines and an extensive bus network reaching well beyond the old Metro Toronto boundary, into Hamilton, Kitchener-Waterloo, Barrie and Niagara. It\'s paid for with the same <strong>PRESTO</strong> fare card used across most GTA transit systems, letting a single tap-in cover a trip that starts on a GO train and ends on a TTC streetcar.</p>'),
            ("The next big expansion: the Eglinton Crosstown", '<p>The <strong>Eglinton Crosstown LRT</strong>, a roughly 19-kilometre light rail line running largely underground across midtown Toronto, has been under construction since 2011 as one of the largest transit expansions in the city\'s history — intended to relieve pressure on the subway\'s east-west capacity, though its opening has faced repeated delays.</p>'),
        ],
        "sources": [
            ("GO Transit — Union Station: History, Facts & Map", "https://www.gotransit.com/en/find-a-station/un/union-station-history-facts-and-map"),
            ("Metrolinx — About GO Transit", "https://www.gotransit.com/en/about-us"),
            ("Wikipedia — Eglinton Crosstown", "https://en.wikipedia.org/wiki/Eglinton_Crosstown"),
        ],
        "related_words": [],
    },
    {
        "slug": "ontario-place",
        "title": "Ontario Place: History, Closure & the Redevelopment Controversy",
        "kicker": "A 1971 futurist landmark, currently a live political fight",
        "h1": "Ontario Place",
        "dek": "A Modernist waterfront park that drew millions of visitors a year in the 1970s, closed its main attractions in 2012, and is now the site of one of Toronto's most contested current redevelopment fights.",
        "meta_desc": "The history of Ontario Place: its 1971 opening as a Modernist waterfront park, its 2012 closure, and the ongoing controversy over its redevelopment into a private spa.",
        "keywords": "Ontario Place history, Ontario Place closure, Ontario Place spa controversy, Ontario Place redevelopment, Therme Toronto",
        "hero_img": "Ontario_Place,_Toronto,_Canada_(21653132619).jpg",
        "hero_alt": "Ontario Place on Toronto's waterfront",
        "hero_credit": "Ontario Place — Wikimedia Commons, CC BY-SA 2.0",
        "sections": [
            (None, '<p>Few Toronto landmarks have swung from beloved to abandoned to politically radioactive quite like Ontario Place — a genuinely striking piece of 1970s design that\'s currently at the centre of a real, ongoing fight over what the waterfront is for.</p>'),
            ("A Modernist showpiece (opened 1971)", '<p>Ontario Place opened in 1971 as the provincial government\'s answer to Montreal\'s Expo 67 — a cluster of futuristic pod-shaped pavilions built out over the lake on artificial landscaped islands, designed by architect Eberhard Zeidler with landscape by Michael Hough, and home to the world\'s first permanent IMAX theatre. It drew more than two million visitors a year in its early decades.</p>'),
            ("Decline and closure (2012)", '<p>Rising operating costs led to a slow retreat: individual attractions closed through the 1990s and 2000s until the site\'s main attractions shut entirely in 2012, leaving most of the park unused for the following decade, even as its Modernist landscape design earned growing architectural-preservation recognition.</p>'),
            ("The current redevelopment fight", '<p>In 2019 the Ontario government announced plans to redevelop the site, culminating in a 95-year lease to Austrian company <strong>Therme</strong> to build a large indoor waterpark and spa on part of the property. The plan has drawn sustained public protest and legal challenges, and in a 2024 report the province\'s auditor general found the bidding process that selected Therme was "not fair, transparent or accountable" — while the public price tag for supporting infrastructure has grown substantially past its original estimate. As of the mid-2020s, the dispute over the site\'s future remains unresolved and genuinely contested, unlike most of the settled history covered elsewhere in this guide.</p>'),
        ],
        "sources": [
            ("Wikipedia — Ontario Place", "https://en.wikipedia.org/wiki/Ontario_Place"),
            ("CBC News — Ontario Place Redevelopment Not 'Fair, Transparent or Accountable,' Auditor General Finds", "https://www.cbc.ca/news/canada/toronto/ontario-auditor-general-setup-1.7399052"),
            ("Toronto Life — A Nostalgic Tour of the Glory Years of Ontario Place", "https://torontolife.com/city/ontario-place-history-archival-photos/"),
        ],
        "related_words": [],
    },
    {
        "slug": "extreme-weather",
        "title": "Toronto's Worst Storms: Hurricane Hazel, the 2013 Flood & Ice Storm",
        "kicker": "81 deaths in one October night, 1954",
        "h1": "Toronto's Worst Storms",
        "dek": "Our general climate guide covers Toronto's normal weather. This is the abnormal side of it — a 1954 hurricane that reshaped the city's relationship to its own rivers, and a single year, 2013, that delivered a record flood and a historic ice storm five months apart.",
        "meta_desc": "Toronto's most severe historical weather events: the 1954 Hurricane Hazel flood that killed 81 people, the July 2013 record flash flood, and the December 2013 ice storm.",
        "keywords": "Hurricane Hazel Toronto, Toronto 2013 flood, Toronto ice storm 2013, worst storms in Toronto history",
        "hero_img": "Tree_falls_on_vehicle_-_Toronto_Ice_Storm_2013.jpg",
        "hero_alt": "Storm damage from the 2013 Toronto ice storm",
        "hero_credit": "Toronto Ice Storm, 2013 — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Our <a href="weather.html">weather guide</a> covers what a normal year in Toronto looks like. This page is about the exceptions — the storms severe enough to actually change how the city is built and governed.</p>'),
            ("Hurricane Hazel (October 1954)", '<p>The single deadliest weather event in Toronto\'s history. Hurricane Hazel reached the city on October 15–16, 1954, dropping enormous rainfall onto already-saturated ground and causing catastrophic flooding along the Humber River and Etobicoke Creek. It killed 81 people across the region and caused roughly $137 million in 1954 dollars in damage (well over a billion dollars today), leaving about 4,000 people homeless; 35 people died on a single street, Raymore Drive in Weston, when homes were swept away. In its aftermath, the province banned residential development along Toronto\'s river valleys — a direct reason so much of the <a href="ravines.html">ravine and river-valley system</a> covered elsewhere in this guide is parkland today rather than housing.</p>'),
            ("The July 2013 flash flood", '<p>On July 8, 2013, Toronto recorded 126 mm of rain in a single day — the most rainfall the city had ever measured in one day, more than a typical month\'s worth of July rain falling in a few hours. The flooding knocked out power to over 300,000 customers and stranded roughly 1,400 GO Transit passengers on a train sitting in floodwater for hours.</p>'),
            ("The December 2013 ice storm", '<p>Just over five months later, an ice storm hit the city on December 21–22, 2013, coating trees and power lines in ice heavy enough to snap branches and topple lines across the region, leaving hundreds of thousands of customers without power — some for over a week, through the days leading into Christmas. Environment Canada ranked the two 2013 Toronto storms among the top weather stories in the country that year.</p>'),
        ],
        "sources": [
            ("Wikipedia — Effects of Hurricane Hazel in Canada", "https://en.wikipedia.org/wiki/Effects_of_Hurricane_Hazel_in_Canada"),
            ("The Canadian Encyclopedia — Hurricane Hazel", "https://www.thecanadianencyclopedia.ca/en/article/hurricane-hazel"),
            ("CBC News — A Decade Ago, Toronto Was Underwater", "https://www.cbc.ca/news/canada/toronto/10-years-after-historic-floods-in-toronto-city-reflects-on-whats-changed-1.6898788"),
        ],
        "related_words": [],
    },
    {
        "slug": "cocktail-scene",
        "title": "Toronto's Cocktail & Distillery Scene",
        "kicker": "From the largest distillery in the British Empire to craft gin",
        "h1": "Toronto's Cocktail & Distillery Scene",
        "dek": "The same Victorian-era industrial site that once housed the British Empire's largest distillery is now home to some of the city's best bars — and a new generation of small-batch Toronto distilleries.",
        "meta_desc": "A guide to Toronto's cocktail and distillery scene: the Gooderham and Worts distillery history, the modern Distillery District bar scene, and craft distilleries operating in the city today.",
        "keywords": "Toronto cocktail bars, Toronto craft distilleries, Gooderham and Worts, Distillery District bars, Toronto gin whisky",
        "hero_img": "The_Boiler_House,_Distillery_district._Toronto._(5617418107).jpg",
        "hero_alt": "The Boiler House building in Toronto's Distillery District",
        "hero_credit": "The Boiler House, Distillery District — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Long before the <a href="craft-beer.html">craft beer boom</a>, Toronto\'s biggest claim to drinks-industry fame was distilling, not brewing — and the industrial site behind that history is now the anchor of the city\'s cocktail scene too.</p>'),
            ("Gooderham and Worts: once the largest in the Empire", '<p>Founded in 1832, the Gooderham and Worts distillery grew through the 19th century into the largest distillery in the British Empire at its peak, its Victorian industrial buildings now preserved as the <a href="neighbourhoods.html">Distillery District</a>. Production wound down through the 20th century, and the site was redeveloped starting in 2001 into the pedestrian-only historic district that exists today.</p>'),
            ("The modern cocktail bar scene", '<p>Toronto\'s serious cocktail bars are spread well beyond the Distillery District itself — a scene shaped by the same broader craft-beverage culture documented in our <a href="craft-beer.html">craft beer guide</a> and <a href="coffee-culture.html">coffee culture guide</a>: an emphasis on house-made syrups and bitters, classic technique, and increasingly, ingredients sourced from Ontario producers rather than imported spirits alone.</p>'),
            ("A new wave of small distilleries", '<p>A newer generation of small-batch Ontario distilleries — including Toronto-area operations like Spirit of York and Junction Craft Distillery — now produce gin, whisky and vodka using largely local grain, part of the same craft-production shift that transformed the city\'s beer and coffee scenes over the same period.</p>'),
        ],
        "sources": [
            ("Wikipedia — Gooderham and Worts", "https://en.wikipedia.org/wiki/Gooderham_and_Worts"),
            ("Wikipedia — Distillery District", "https://en.wikipedia.org/wiki/Distillery_District"),
        ],
        "related_words": [],
    },
    {
        "slug": "broadcasting",
        "title": "Toronto Broadcasting History: CFRB, CityTV & MuchMusic",
        "kicker": "The world's first all-electric radio station started here",
        "h1": "Toronto Broadcasting History",
        "dek": "Toronto's broadcasting industry produced a genuine world-first in 1927, reinvented local television in 1972, and gave Canada its own answer to MTV in 1984 — a throughline most people don't realize connects three completely different eras.",
        "meta_desc": "The history of broadcasting in Toronto: CFRB, the world's first all-electric radio station (1927); Citytv's 1972 launch under Moses Znaimer; and MuchMusic's 1984 debut.",
        "keywords": "CFRB history, Citytv history Moses Znaimer, MuchMusic history, Toronto broadcasting history, CBC Toronto",
        "hero_img": "Bell_Media_Queen_Street,_Toronto,_Ontario_(29709430050).jpg",
        "hero_alt": "A Toronto broadcast media building on Queen Street",
        "hero_credit": "Bell Media, Queen Street, Toronto — Wikimedia Commons, Creative Commons licensed",
        "sections": [
            (None, '<p>Our <a href="media.html">media and entertainment guide</a> covers Toronto\'s film and music industries. This is the broadcasting side specifically — radio and television — where the city produced a genuine engineering first and, decades later, reinvented what local TV could look like.</p>'),
            ("CFRB (1927): a world first", '<p><strong>CFRB</strong> went on air on February 19, 1927, launched by Edward "Ted" Rogers Sr. — founder of what became Rogers Communications — using a transmitter of his own design that made CFRB the world\'s first all-electric radio station, eliminating the noisy batteries every other station still relied on. It later moved to the 1010 AM frequency it still broadcasts on today.</p>'),
            ("Citytv (1972): reinventing local television", '<p>Moses Znaimer and a group of partners launched Citytv on September 28, 1972, as Canada\'s first commercial UHF television station — deliberately scrappy, low-budget and street-level in a way conventional broadcasters weren\'t, with reporters using handheld cameras well before that was standard practice anywhere in North American local news.</p>'),
            ("MuchMusic (1984): Canada\'s own MTV", '<p>Building directly on Citytv\'s infrastructure and philosophy, Znaimer and producer John Martin launched <strong>MuchMusic</strong> on August 31, 1984 — a 24-hour music video channel that became a genuine cultural institution for a generation of Canadian viewers, and a launching pad for Canadian musicians the way MTV was in the U.S.</p>'),
            ("CBC in Toronto", '<p>The Canadian Broadcasting Corporation, Canada\'s public broadcaster, was founded nationally in 1936 and has run major English-language television and radio operations from Toronto for decades, based since 1992 at the Canadian Broadcasting Centre on Front Street — a short walk from Union Station.</p>'),
        ],
        "sources": [
            ("Wikipedia — CFRB", "https://en.wikipedia.org/wiki/CFRB_1010"),
            ("The Canadian Encyclopedia — Moses Znaimer", "https://www.thecanadianencyclopedia.ca/en/article/moses-znaimer"),
            ("The Canadian Encyclopedia — MuchMusic", "https://www.thecanadianencyclopedia.ca/en/article/muchmusic-emc"),
        ],
        "related_words": [],
    },
    {
        "slug": "scarborough",
        "title": "Scarborough: History of Toronto's Largest Former Borough",
        "kicker": "Named for a coastline in Yorkshire, England",
        "h1": "Scarborough",
        "dek": "From a rural township of 3,000 people to a district that tripled its population between 1955 and 1970 — the deep history behind the part of the city locals just call \"Scarbs.\"",
        "meta_desc": "The history of Scarborough, Toronto: its 1793 naming after the English coastal town, explosive postwar population growth, the Golden Mile, and its 1998 amalgamation into Toronto.",
        "keywords": "Scarborough Toronto history, Scarborough Bluffs, Golden Mile Scarborough, why is Scarborough called Scarborough, Scarborough amalgamation",
        "hero_img": "Scarborough_Bluffs,_May_4_2026_(07).jpg",
        "hero_alt": "The Scarborough Bluffs along Lake Ontario",
        "hero_credit": "Scarborough Bluffs — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Our slang-focused <a href="../neighbourhoods.html">Toronto Slang By Neighbourhood</a> page covers why Scarborough matters to this dictionary specifically. This page is the wider story: the actual history of the place itself, the largest of the six former municipalities that merged into Toronto in 1998.</p>'),
            ("Where the name comes from", '<p>The first European settlers arrived in 1791, and the area was initially referred to informally as Glasgow. It was Elizabeth Simcoe, wife of Upper Canada\'s first Lieutenant Governor, who renamed it Scarborough — the dramatic <strong>Scarborough Bluffs</strong> along the Lake Ontario shoreline reminded her of the cliffs at Scarborough, a coastal town in Yorkshire, England.</p>'),
            ("A century of farmland, then explosive growth", '<p>The Township of Scarborough was incorporated in 1850 with a population of just 3,000, and stayed mostly rural — farms, mills along the Rouge River and Highland Creek — for the following century. That changed abruptly after the Second World War: Scarborough\'s population doubled from 48,000 to 110,000 between 1950 and 1955 alone, then roughly tripled again by 1970, one of the fastest sustained growth rates of any part of the region.</p>'),
            ("The Golden Mile", '<p>A stretch of Eglinton Avenue East became the <strong>Golden Mile</strong>, one of Canada\'s first model industrial parks, after Scarborough township reeve Oliver Crockford negotiated the purchase of a former military munitions site from the federal government in the late 1940s for a bargain $350,000 — turning it into a major manufacturing corridor that anchored the local economy for decades.</p>'),
            ("From township to city to borough of Toronto", '<p>Scarborough was reconstituted as a borough in 1967 and became a city in its own right in 1983, before amalgamating with Toronto in 1998 along with East York, Etobicoke, York and North York — see our <a href="history.html">full amalgamation history</a> for the wider context.</p>'),
        ],
        "sources": [
            ("Wikipedia — Scarborough, Ontario", "https://en.wikipedia.org/wiki/Scarborough,_Ontario"),
            ("Heritage Toronto — Golden Mile Industry & Manufacturing", "https://www.heritagetoronto.org/explore/scarborough-history-golden-mile/golden-mile-industry-manufacturing/"),
            ("City of Toronto — Scarborough Before the Civic Centre", "https://www.toronto.ca/explore-enjoy/history-art-culture/online-exhibits/web-exhibits/web-exhibits-local-government/albert-campbells-dream-a-new-scarborough-civic-centre/scarborough-before-the-civic-centre/"),
        ],
        "related_words": ["scarbs", "brodie", "roadman"],
    },
    {
        "slug": "etobicoke",
        "title": "Etobicoke: Toronto's West-End Former City",
        "kicker": "The Kingsway to Rexdale, in one borough",
        "h1": "Etobicoke",
        "dek": "From a rural township incorporated in 1850 to a postwar suburb that grew from under 40,000 people to over 200,000 in two decades — Toronto's affluent-to-working-class west end former city.",
        "meta_desc": "The history of Etobicoke, Toronto: its 1850 incorporation, rapid postwar suburban growth, and its range from the affluent Kingsway to Rexdale, before its 1998 amalgamation into Toronto.",
        "keywords": "Etobicoke history, Etobicoke Toronto, Kingsway Etobicoke, Rexdale Etobicoke, Etobicoke amalgamation",
        "hero_img": "Humber_Bay_Arch_Bridge_at_Night_1.jpg",
        "hero_alt": "The Humber Bay Arch Bridge in Etobicoke",
        "hero_credit": "Humber Bay Arch Bridge, Etobicoke — Wikimedia Commons, CC BY-SA 2.0",
        "sections": [
            (None, '<p>Etobicoke — the name comes from an Ojibwe word generally translated as "place where the alders grow" — is Toronto\'s westernmost former city, running from the Humber River to the Mississauga border, and one of the widest-ranging in character of the six pre-amalgamation municipalities.</p>'),
            ("From township to postwar boom", '<p>The Township of Etobicoke was incorporated on January 21, 1850. Like most of what\'s now Toronto\'s inner suburbs, it stayed largely rural until after the Second World War, when its population exploded from under 40,000 to more than 200,000 within two decades — the same broad postwar suburbanization wave documented across our other <a href="scarborough.html">former-municipality guides</a>.</p>'),
            ("From the Kingsway to Rexdale", '<p>Few former cities in the region span as wide a range as Etobicoke does. <strong>The Kingsway</strong> and <strong>Markland Wood</strong> are among the most affluent residential areas in the city; <strong>Rexdale</strong>, in the north, has a very different profile and history — see our <a href="../neighbourhoods.html">Toronto slang by neighbourhood</a> guide for its specific role in the Somali- and Caribbean-rooted vocabulary this whole dictionary documents.</p>'),
            ("What\'s there today", '<p>Etobicoke is home to Humber College, Woodbine Racetrack, Sherway Gardens shopping centre, and a significant share of <a href="airports.html">Toronto Pearson Airport</a>\'s surrounding lands. It became a borough in 1967, a city in 1983, and merged into Toronto in the 1998 amalgamation along with the five other former municipalities.</p>'),
        ],
        "sources": [
            ("Wikipedia — Etobicoke", "https://en.wikipedia.org/wiki/Etobicoke"),
            ("City of Toronto — Etobicoke: A Modern Suburb", "https://www.toronto.ca/explore-enjoy/history-art-culture/online-exhibits/web-exhibits/web-exhibits-community-neighbourhoods/etobicoke-a-modern-suburb/"),
            ("Etobicoke Historical Society — Brief History of Etobicoke", "https://www.etobicokehistorical.com/brief-history-of-etobicoke.html"),
        ],
        "related_words": ["rexdale", "wallahi"],
    },
    {
        "slug": "north-york",
        "title": "North York: The Suburb One Mayor Turned Into a Downtown",
        "kicker": "25 years, one mayor, one new skyline",
        "h1": "North York",
        "dek": "Almost single-handedly reshaped by one 25-year mayor, North York built its own downtown along Yonge Street — complete with its own city hall, square and skyline — before merging into Toronto in 1998.",
        "meta_desc": "The history of North York, Toronto: Mel Lastman's 25-year mayoralty, the $4-billion Yonge Street redevelopment, Mel Lastman Square, and its 1998 amalgamation into Toronto.",
        "keywords": "North York history, Mel Lastman, Mel Lastman Square, North York Yonge Street, North York amalgamation",
        "hero_img": "MelLastmanSquare_-_2015June03.jpg",
        "hero_alt": "Mel Lastman Square in North York",
        "hero_credit": "Mel Lastman Square, North York — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Of all six former municipalities that merged into Toronto in 1998, North York has the most direct link to a single person — mayor <strong>Mel Lastman</strong>, who ran it for a genuinely unusual 25 consecutive years and used that time to build it a downtown from close to nothing.</p>'),
            ("Mel Lastman\'s 25-year mayoralty (1972–1997)", '<p>Lastman served as mayor of North York from 1972 to 1997, and used that long tenure to push through roughly $4 billion in redevelopment along north Yonge Street — a deliberate effort to give a suburban municipality its own genuine downtown rather than leaving it purely residential. North York was upgraded from a borough to a full city in 1979, with its new civic offices anchoring the project.</p>'),
            ("Mel Lastman Square", '<p>The centrepiece, <strong>Mel Lastman Square</strong>, opened June 16, 1989 — a 20,000-square-foot public space with an amphitheatre, fountains and a reflecting pool that becomes an outdoor skating rink in winter, sitting alongside North York Civic Centre, the North York Central Library and an arts centre, all built on the same stretch of Yonge Street through the 1970s and 80s.</p>'),
            ("From North York\'s mayor to Toronto\'s mayor", '<p>When the 1998 amalgamation merged North York into the new City of Toronto (see our <a href="history.html">full amalgamation history</a>), Mel Lastman went on to become the first mayor of the newly unified megacity — a fitting cap to a career spent building a downtown for a suburb that, within a year, would no longer technically be one.</p>'),
        ],
        "sources": [
            ("North York Historical Society — NYHS Remembers Mel Lastman (1933–2021)", "https://nyhs.ca/local-history-articles/nyhs-remembers-mel-lastman-1933-2021/"),
            ("Wikipedia — Mel Lastman Square", "https://en.wikipedia.org/wiki/Mel_Lastman_Square"),
            ("Wikipedia — North York City Centre", "https://en.wikipedia.org/wiki/North_York_City_Centre"),
        ],
        "related_words": [],
    },
    {
        "slug": "mississauga",
        "title": "Mississauga: How \"Sauga\" Became Canada's Sixth-Largest City",
        "kicker": "36 years, one mayor, one bedroom community turned metropolis",
        "h1": "Mississauga",
        "dek": "In 1975 it had 235,000 people. Under one mayor's 36-year tenure, it grew into Canada's sixth-largest city — the fuller story behind the place Toronto slang just calls \"Sauga.\"",
        "meta_desc": "The history of Mississauga, Ontario: Hazel McCallion's 36-year mayoralty, the growth of Square One, and how a bedroom community became Canada's sixth-largest city.",
        "keywords": "Mississauga history, Hazel McCallion, Square One Mississauga, why is Mississauga called Sauga, Mississauga population growth",
        "hero_img": "Absolute_Towers_Mississauga._South-west_view.jpg",
        "hero_alt": "The Absolute World towers in Mississauga, Ontario",
        "hero_credit": "Absolute World towers, Mississauga — Wikimedia Commons, CC BY-SA 4.0",
        "sections": [
            (None, '<p>Our dictionary entry for <a href="../words/sauga.html">Sauga</a> covers the slang side of this. This page is the fuller story: how a separate city west of Toronto — genuinely distinct from the amalgamated municipalities covered elsewhere in this guide — grew into one of the largest cities in the country in living memory.</p>'),
            ("From bedroom community to Canada\'s 6th-largest city", '<p>Mississauga was incorporated as a city in 1974, one year after its future downtown anchor, <strong>Square One</strong> shopping centre, opened in 1973. It had roughly 235,000 residents in 1975; by the time long-serving mayor Hazel McCallion retired in 2014, that number had roughly tripled to nearly 750,000, making Mississauga Canada\'s sixth-largest city — a growth rate that reshaped what had been countryside and small villages into continuous suburban development.</p>'),
            ("Hazel McCallion\'s 36 years", '<p><strong>Hazel McCallion</strong> was first elected mayor in 1978 and didn\'t retire until 2014 — 36 consecutive years, presiding directly over Mississauga\'s transformation from bedroom community to a genuine city with its own downtown, business parks and skyline, and earning a reputation as one of the most dominant local political figures in Canadian municipal history.</p>'),
            ("Not part of Toronto — on purpose", '<p>Unlike Scarborough, Etobicoke or North York, Mississauga was never absorbed into Toronto\'s 1998 amalgamation — it remains, deliberately, a separate city in Peel Region, which is exactly why Toronto slang treats "Sauga" as its own distinct identity rather than just another Toronto neighbourhood; see our <a href="../neighbourhoods.html">slang neighbourhoods guide</a> for that distinction in more detail. <a href="airports.html">Toronto Pearson Airport</a> is also technically located within Mississauga\'s borders, not Toronto\'s.</p>'),
        ],
        "sources": [
            ("The Canadian Encyclopedia — Mississauga", "https://www.thecanadianencyclopedia.ca/en/article/mississauga"),
            ("Storeys — The Mixed Legacy Hazel McCallion Leaves Behind in Mississauga", "https://storeys.com/hazel-mccallion-death-legacy-mississauga/"),
            ("Heritage Mississauga — Square One", "https://heritagemississauga.com/business/the-rise-of-the-shopping-centre/square-one/"),
        ],
        "related_words": ["sauga", "905", "gta"],
    },
    {
        "slug": "brampton",
        "title": "Brampton: From \"Flower Town\" to the Centre of Punjabi Canada",
        "kicker": "140 greenhouses, then a whole new identity",
        "h1": "Brampton",
        "dek": "Once North America's largest flower-growing business, later one of the fastest-growing cities in Canada and now home to one of the largest Punjabi and Sikh communities outside South Asia.",
        "meta_desc": "The history of Brampton, Ontario: its 19th-century \"Flower City\" greenhouse industry and its transformation into a major centre of Punjabi-Canadian and Sikh community life.",
        "keywords": "Brampton history, why is Brampton called Flower City, Brampton Punjabi community, Brampton Sikh population, Brampton Ontario growth",
        "hero_img": "Brampton_City_Hall_West_Tower_(37520691101).jpg",
        "hero_alt": "Brampton City Hall's west tower",
        "hero_credit": "Brampton City Hall — Wikimedia Commons, CC BY 2.0",
        "sections": [
            (None, '<p>Brampton, immediately northwest of Toronto in Peel Region, has had two almost entirely unrelated identities a century apart — a 19th-century flower-growing capital, and a modern hub of one of the largest Punjabi diaspora communities anywhere outside South Asia.</p>'),
            ("The Flower City", '<p>Brampton\'s original nickname, "the Flower Town of Canada," traces to 1863, when Edward Dale founded a nursery that grew into <strong>Dale Estate</strong>, at its peak the largest flower-growing business in North America with 140 greenhouses producing orchids, carnations, lilies and more for export worldwide. The city formally adopted the Flower City identity in 1963; the business itself, hurt by rising fuel costs and a shrinking market, closed in 1980.</p>'),
            ("Rapid modern growth", '<p>Brampton has more recently posted the highest population growth rate of any of Canada\'s 25 largest cities, reaching 656,480 residents as of the 2021 census — a 10.6% jump in five years alone, driven substantially by immigration.</p>'),
            ("The centre of Punjabi Canada", '<p>Postwar changes to Canadian immigration policy removed earlier discriminatory restrictions on South Asian immigration, and Brampton — with its growing economy, job opportunities and, over time, an established Punjabi social network — became a primary destination. Sikhs alone make up roughly a fifth of Brampton\'s population today, alongside large Hindu and Muslim South Asian communities, visible in the city\'s density of gurdwaras, temples, sweet shops and Punjabi-language businesses — a newer, parallel chapter to the <a href="ethnic-enclaves.html">ethnic-enclave history</a> covered elsewhere in this guide.</p>'),
        ],
        "sources": [
            ("Bramptonist — How Brampton Got Its Rep as Flower City", "https://bramptonist.com/brampton-got-rep-flower-city/"),
            ("The Newcomer — Punjabi Sikhs in Brampton", "https://thenewcomer.ca/arts-culture-history/punjabi-sikhs-in-brampton/"),
            ("Wikipedia — Brampton", "https://en.wikipedia.org/wiki/Brampton"),
        ],
        "related_words": ["905", "gta"],
    },
    {
        "slug": "vaughan",
        "title": "Vaughan: Canada's Wonderland and the Subway That Followed It",
        "kicker": "A theme park first, a downtown 36 years later",
        "h1": "Vaughan",
        "dek": "Canada's largest theme park put Vaughan on the map in 1981. It took until 2017 for the subway — and a real downtown — to catch up.",
        "meta_desc": "The history of Vaughan, Ontario: Canada's Wonderland's 1981 opening, and the 2017 subway extension and Vaughan Metropolitan Centre that gave the city its first real downtown.",
        "keywords": "Vaughan history, Canada's Wonderland history, Vaughan Metropolitan Centre, Vaughan subway extension, Vaughan Ontario growth",
        "hero_img": "WindSeeker_at_Canada's_Wonderland,_August_2018_(3).jpg",
        "hero_alt": "The WindSeeker ride at Canada's Wonderland in Vaughan",
        "hero_credit": "Canada's Wonderland, Vaughan — Wikimedia Commons, CC BY-SA 3.0",
        "sections": [
            (None, '<p>Vaughan, north of Toronto in York Region, spent decades known almost entirely for one thing before a 21st-century transit project finally gave it a second identity.</p>'),
            ("Canada\'s Wonderland (1981)", '<p><strong>Canada\'s Wonderland</strong> opened on May 23, 1981, built by the Taft Broadcasting Company and Great-West Life Assurance — Canada\'s first major theme park and still its largest, marked at opening with 10,000 helium balloons, 13 parachutists and 350 white doves. It remains one of the region\'s biggest tourist draws and a formative summer destination for generations of GTA kids.</p>'),
            ("A subway extension changes the city\'s shape (2017)", '<p>For most of its history Vaughan had no real downtown to speak of — that changed with the <strong>Toronto–York Spadina Subway Extension</strong>, which brought Line 1 north of Steeles Avenue for the first time. The Vaughan Metropolitan Centre station opened December 17, 2017, immediately spurring a wave of high-rise residential and office construction around it — a deliberate, planned downtown built around a single subway stop, similar in spirit to how <a href="north-york.html">North York built its own downtown</a> around Yonge Street decades earlier.</p>'),
            ("What Vaughan looks like today", '<p>The city now runs on two distinct identities at once: the established tourist-and-suburban-family draw of Canada\'s Wonderland in the north, and a genuinely new, still-developing high-density downtown at the Vaughan Metropolitan Centre in the south — a rare case of a GTA suburb building a downtown core from scratch rather than growing one organically over a century.</p>'),
        ],
        "sources": [
            ("Six Flags — The History of Canada's Wonderland: From Opening Day to Today", "https://www.sixflags.com/blog/media-center/history-of-canadas-wonderland"),
            ("Wikipedia — Vaughan Metropolitan Centre station", "https://en.wikipedia.org/wiki/Vaughan_Metropolitan_Centre_station"),
            ("Wikipedia — Vaughan", "https://en.wikipedia.org/wiki/Vaughan"),
        ],
        "related_words": ["905", "gta"],
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
