# Sources & Credits

## How this dictionary was built

`api.urbandictionary.com` and most slang/culture publications (Urban
Dictionary, Wikipedia, CBC, Narcity, Vice, etc.) aren't reachable as live
scrape targets from this build environment's network policy. Instead, every
entry in `data/terms.json` was compiled through targeted research against
published, citable sources on Toronto and GTA slang, then written up by hand
in a consistent dictionary format (term, definition, origin, example).

If you want to extend this into an actual live scraper (e.g. hitting the
Urban Dictionary API for definitions + vote counts on a fixed seed list of
Toronto terms), that's a natural next step — see "Extending the dataset"
below.

## Research sources consulted

- [CBC Toronto — "Wallahi, it's not just Toronto slang anymore"](https://www.cbc.ca/news/canada/toronto/toronto-slang-1.5320157)
- [Narcity — Toronto Slang: The Ultimate Guide](https://www.narcity.com/toronto/toronto-slang-words)
- [The Queen's Journal — The Toronto slang dictionary](https://www.queensjournal.ca/the-toronto-slang-dictionary/)
- [Wikipedia — Toronto slang](https://en.wikipedia.org/wiki/Toronto_slang)
- [Wiktionary — Category: Multicultural Toronto English](https://en.wiktionary.org/wiki/Category:Multicultural_Toronto_English)
- [Canadian Language Museum — A Dictionary of English in Multicultural Toronto (PDF)](https://languagemuseum.ca/wp-content/uploads/2024/05/A-Dictionary-of-English-in-Multicultural-Toronto.pdf)
- [U of T Magazine — Do You Know Toronto Slang?](https://magazine.utoronto.ca/research-ideas/culture-society/do-you-know-toronto-slang/)
- [Vice — Toronto's Slang Isn't 'New.' It's Black.](https://www.vice.com/en/article/drake-torontos-slang-isnt-new-its-black/)
- [slanginsights.com — Toronto Slang: Common Words, Meanings, and Real-Life Examples](https://slanginsights.com/toronto-slang/)
- [BlogTO — How Toronto got the nickname Hogtown](https://www.blogto.com/city/2013/10/how_toronto_got_the_nickname_hogtown/)
- [The Globe and Mail — We The 6: Why the name Drake gave us is here to stay](https://www.theglobeandmail.com/news/toronto/we-the-6-why-the-name-drake-gave-us-is-here-to-stay/article25421112/)
- [DCHP-3 (UBC) — Hogtown](https://dchp.arts.ubc.ca/entries/Hogtown)
- Additional context from Wikipedia entries on the Don Valley Parkway, Gardiner Expressway, Steeles Avenue, and Jane and Finch.

Slang is alive and contested — spellings, exact origins and "who really
started it" are debated even among the sources above. Where a term's roots
are widely credited to a specific community (Jamaican Patois, Somali, Arabic,
etc.), that's noted in the `origin` field, with respect to the communities
that actually built this vocabulary before it went mainstream.

## Photography

All background/section imagery is real, unedited photography of Toronto,
sourced from Wikimedia Commons under Creative Commons licenses. Full credit
and license for each image:

| Image | Credit | Used on | Source |
|---|---|---|---|
| Toronto Pearson Airport-Terminal 1.JPG | Toronto Pearson Airport, Terminal 1 — Wikimedia Commons, Creative Commons licensed | airports | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Pearson_Airport-Terminal_1.JPG) |
| Ajax Waterfront Park (cropped).jpg | Ajax Waterfront Park — Wikimedia Commons, CC BY 4.0 | ajax | [File page](https://commons.wikimedia.org/wiki/File:Ajax_Waterfront_Park_%28cropped%29.jpg) |
| Houses in Cabbagetown Toronto.jpg | Bay-and-gable houses, Cabbagetown — David (bootbearwdc), CC BY 2.0 | architecture | [File page](https://commons.wikimedia.org/wiki/File:Houses_in_Cabbagetown_Toronto.jpg) |
| Bmo field (8820851518).jpg | BMO Field, Toronto — Wikimedia Commons, CC BY 2.0 | argonauts-grey-cup | [File page](https://commons.wikimedia.org/wiki/File:Bmo_field_%288820851518%29.jpg) |
| Art Gallery of Ontario (24409138225).jpg | Art Gallery of Ontario — Wikimedia Commons, Creative Commons licensed | art | [File page](https://commons.wikimedia.org/wiki/File:Art_Gallery_of_Ontario_%2824409138225%29.jpg) |
| Avro Arrow rollout.jpg | Avro Arrow rollout — Wikimedia Commons, public domain | avro-arrow | [File page](https://commons.wikimedia.org/wiki/File:Avro_Arrow_rollout.jpg) |
| First Canadian Place, Toronto, Ontario (29889104772).jpg | First Canadian Place, Toronto — Wikimedia Commons, CC BY-SA 2.0 | banks | [File page](https://commons.wikimedia.org/wiki/File:First_Canadian_Place%2C_Toronto%2C_Ontario_%2829889104772%29.jpg) |
| Prince Edward Viaduct (4672897942).jpg | Prince Edward Viaduct — Wikimedia Commons, CC BY-SA 2.0 | bloor-viaduct | [File page](https://commons.wikimedia.org/wiki/File:Prince_Edward_Viaduct_%284672897942%29.jpg) |
| Toronto Blue Jays 1992 and 1993 World Series Rings, Canadian Baseball Hall of Fame, St. Marys Ontario 2945 (4871386541).jpg | Blue Jays World Series rings, Canadian Baseball Hall of Fame — Wikimedia Commons, Creative Commons licensed | blue-jays-1992 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Blue_Jays_1992_and_1993_World_Series_Rings%2C_Canadian_Baseball_Hall_of_Fame%2C_St._Marys_Ontario_2945_%284871386541%29.jpg) |
| Brampton City Hall West Tower (37520691101).jpg | Brampton City Hall — Wikimedia Commons, CC BY 2.0 | brampton | [File page](https://commons.wikimedia.org/wiki/File:Brampton_City_Hall_West_Tower_%2837520691101%29.jpg) |
| Bell Media Queen Street, Toronto, Ontario (29709430050).jpg | Bell Media, Queen Street, Toronto — Wikimedia Commons, Creative Commons licensed | broadcasting, much-music-awards | [File page](https://commons.wikimedia.org/wiki/File:Bell_Media_Queen_Street%2C_Toronto%2C_Ontario_%2829709430050%29.jpg) |
| Spencer Smith Park in Burlington, Ontario.jpg | Spencer Smith Park, Burlington — Wikimedia Commons, Creative Commons licensed | burlington | [File page](https://commons.wikimedia.org/wiki/File:Spencer_Smith_Park_in_Burlington%2C_Ontario.jpg) |
| Canadian Broadcasting Centre, Corner of John and Front Street, Toronto, Ontario (29920113811).jpg | Canadian Broadcasting Centre, Toronto — Wikimedia Commons, Creative Commons licensed | canadian-screen-awards | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Broadcasting_Centre%2C_Corner_of_John_and_Front_Street%2C_Toronto%2C_Ontario_%2829920113811%29.jpg) |
| Casa Loma, Toronto, Ontario (29709454210).jpg | Casa Loma — Wikimedia Commons, CC BY-SA 2.0 | casa-loma | [File page](https://commons.wikimedia.org/wiki/File:Casa_Loma%2C_Toronto%2C_Ontario_%2829709454210%29.jpg) |
| Canadian Broadcasting Centre, Toronto, Ontario (29968452336).jpg | Canadian Broadcasting Centre, Toronto — Wikimedia Commons, Creative Commons licensed | cbc-toronto | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Broadcasting_Centre%2C_Toronto%2C_Ontario_%2829968452336%29.jpg) |
| Graves of Frederick Grant Banting (1891–1941) and Henrietta Elizabeth Ball Banting (1912–1976) at Mount Pleasant Cemetery, Toronto.jpg | Frederick Banting's grave, Mount Pleasant Cemetery — Wikimedia Commons, CC BY 4.0 | cemeteries | [File page](https://commons.wikimedia.org/wiki/File:Graves_of_Frederick_Grant_Banting_%281891%E2%80%931941%29_and_Henrietta_Elizabeth_Ball_Banting_%281912%E2%80%931976%29_at_Mount_Pleasant_Cemetery%2C_Toronto.jpg) |
| CN Tower, Toronto, Ontario (29969151776).jpg | The CN Tower — Wikimedia Commons, CC BY-SA 2.0 | cn-tower | [File page](https://commons.wikimedia.org/wiki/File:CN_Tower%2C_Toronto%2C_Ontario_%2829969151776%29.jpg) |
| Canadian National Exhibition (CNE) fireworks (17419476860).jpg | CNE fireworks — Wikimedia Commons, CC BY-SA 2.0 | cne | [File page](https://commons.wikimedia.org/wiki/File:Canadian_National_Exhibition_%28CNE%29_fireworks_%2817419476860%29.jpg) |
| The Boiler House, Distillery district. Toronto. (5617418107).jpg | The Boiler House, Distillery District — Wikimedia Commons, Creative Commons licensed | cocktail-scene | [File page](https://commons.wikimedia.org/wiki/File:The_Boiler_House%2C_Distillery_district._Toronto._%285617418107%29.jpg) |
| The Only Cafe, Danforth Avenue, Toronto, Canada, May 2014.jpg | The Only Cafe, Danforth Avenue — Wikimedia Commons, Creative Commons licensed | coffee-culture | [File page](https://commons.wikimedia.org/wiki/File:The_Only_Cafe%2C_Danforth_Avenue%2C_Toronto%2C_Canada%2C_May_2014.jpg) |
| Toronto Railway Museum and Steam Whistle Brewery are located in the Roundhouse Park (27622030420).jpg | Steam Whistle Brewery, Roundhouse Park — Wikimedia Commons, Creative Commons licensed | craft-beer | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Railway_Museum_and_Steam_Whistle_Brewery_are_located_in_the_Roundhouse_Park_%2827622030420%29.jpg) |
| Toronto Protected Bike Lanes.jpg | Protected bike lane, Toronto — Wikimedia Commons, Creative Commons licensed | cycling | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Protected_Bike_Lanes.jpg) |
| De Havilland Canada DHC-2 Beaver. (8107669296).jpg | De Havilland Canada DHC-2 Beaver — Wikimedia Commons, public domain | de-havilland-canada | [File page](https://commons.wikimedia.org/wiki/File:De_Havilland_Canada_DHC-2_Beaver._%288107669296%29.jpg) |
| GM Canada Oshawa - Flickr - Stradablog.jpg | GM Canada, Oshawa — Wikimedia Commons, CC BY 2.0 | durham-region | [File page](https://commons.wikimedia.org/wiki/File:GM_Canada_Oshawa_-_Flickr_-_Stradablog.jpg) |
| Leaside Bridge, construction (29661028238).jpg | Leaside Bridge under construction — Wikimedia Commons, CC BY 2.0 | east-york | [File page](https://commons.wikimedia.org/wiki/File:Leaside_Bridge%2C_construction_%2829661028238%29.jpg) |
| 1918eatonssantaclausparade.jpg | Eaton's Santa Claus Parade, 1918 — Archives of Ontario, public domain | eatons-simpsons | [File page](https://commons.wikimedia.org/wiki/File:1918eatonssantaclausparade.jpg) |
| Bay Street, Financial District, Toronto, Ontario (29708936890).jpg | Bay Street, Financial District — Wikimedia Commons, Creative Commons licensed | economy | [File page](https://commons.wikimedia.org/wiki/File:Bay_Street%2C_Financial_District%2C_Toronto%2C_Ontario_%2829708936890%29.jpg) |
| Chinatown toronto spadina avenue.JPG | Chinatown, Spadina Avenue — Wikimedia Commons, CC BY-SA | ethnic-enclaves, chinese-head-tax | [File page](https://commons.wikimedia.org/wiki/File:Chinatown_toronto_spadina_avenue.JPG) |
| Humber Bay Arch Bridge at Night 1.jpg | Humber Bay Arch Bridge, Etobicoke — Wikimedia Commons, CC BY-SA 2.0 | etobicoke | [File page](https://commons.wikimedia.org/wiki/File:Humber_Bay_Arch_Bridge_at_Night_1.jpg) |
| Coca-Cola Coliseum, Exhibition Place, Toronto, Ontario (29901775271).jpg | Coca-Cola Coliseum, Exhibition Place — Wikimedia Commons, CC BY-SA 2.0 | exhibition-place | [File page](https://commons.wikimedia.org/wiki/File:Coca-Cola_Coliseum%2C_Exhibition_Place%2C_Toronto%2C_Ontario_%2829901775271%29.jpg) |
| Tree falls on vehicle - Toronto Ice Storm 2013.jpg | Toronto Ice Storm, 2013 — Wikimedia Commons, Creative Commons licensed | extreme-weather | [File page](https://commons.wikimedia.org/wiki/File:Tree_falls_on_vehicle_-_Toronto_Ice_Storm_2013.jpg) |
| Toronto Nathan Phillips Square and Toronto City Hall (29944923803).jpg | Nathan Phillips Square, Toronto City Hall — Wikimedia Commons, CC BY 2.0 | famous-torontonians, government, homelessness +1 more | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_%2829944923803%29.jpg) |
| Caribana Toronto 2011 (2).jpg | Caribana Toronto — Ruth Choi, CC BY-SA 2.0 | festivals | [File page](https://commons.wikimedia.org/wiki/File:Caribana_Toronto_2011_%282%29.jpg) |
| St Lawrence Market, Toronto, West partial view 20170417 1.jpg | St. Lawrence Market — Wikimedia Commons, Creative Commons licensed | food | [File page](https://commons.wikimedia.org/wiki/File:St_Lawrence_Market%2C_Toronto%2C_West_partial_view_20170417_1.jpg) |
| Gardiner Expressway, Toronto, Ontario (29968916176).jpg | Gardiner Expressway — Wikimedia Commons, CC BY-SA 2.0 | gardiner-dvp | [File page](https://commons.wikimedia.org/wiki/File:Gardiner_Expressway%2C_Toronto%2C_Ontario_%2829968916176%29.jpg) |
| GO Transit MP40-3C 602 Oshawa Turnaround Rushhour.JPG | GO Transit train, Oshawa — Wikimedia Commons, CC BY 3.0 | go-transit | [File page](https://commons.wikimedia.org/wiki/File:GO_Transit_MP40-3C_602_Oshawa_Turnaround_Rushhour.JPG) |
| Entrance to McMichael Gallery in Kleinburg, Ontario, Canada (8203976920).jpg | McMichael Canadian Art Collection, Kleinburg — Wikimedia Commons, Creative Commons licensed | group-of-seven | [File page](https://commons.wikimedia.org/wiki/File:Entrance_to_McMichael_Gallery_in_Kleinburg%2C_Ontario%2C_Canada_%288203976920%29.jpg) |
| Cherry Blossom in High Park 69.jpg | Cherry blossoms, High Park — Wikimedia Commons, CC BY-SA 4.0 | high-park | [File page](https://commons.wikimedia.org/wiki/File:Cherry_Blossom_in_High_Park_69.jpg) |
| Toronto skyline (2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | history, education, weather +7 more | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_%282012%29.jpg) |
| Toronto General Hospital, Toronto, Ontario (30003270175).jpg | Toronto General Hospital — Wikimedia Commons, Creative Commons licensed | hospitals, stem-cell-discovery, cystic-fibrosis-gene | [File page](https://commons.wikimedia.org/wiki/File:Toronto_General_Hospital%2C_Toronto%2C_Ontario_%2830003270175%29.jpg) |
| Cinesphere, at Ontario Place, in 2012, when it was closed for several years (7157561345).jpg | Cinesphere, Ontario Place — Wikimedia Commons, Creative Commons licensed | imax-toronto | [File page](https://commons.wikimedia.org/wiki/File:Cinesphere%2C_at_Ontario_Place%2C_in_2012%2C_when_it_was_closed_for_several_years_%287157561345%29.jpg) |
| Toronto skyline toronto islands b.JPG | Toronto skyline from the Toronto Islands — Wikimedia Commons, Creative Commons licensed | indigenous-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_toronto_islands_b.JPG) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | CN Tower and Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | landmarks, media, nicknames +5 more | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| LCBO at Parkway Mall.jpg | LCBO, Parkway Mall — Wikimedia Commons, CC BY-SA 4.0 | lcbo-history | [File page](https://commons.wikimedia.org/wiki/File:LCBO_at_Parkway_Mall.jpg) |
| Pride parade Toronto 2011.jpg | Toronto Pride parade, 2011 — Kitty Rainbow, CC BY 2.0 | lgbtq-village | [File page](https://commons.wikimedia.org/wiki/File:Pride_parade_Toronto_2011.jpg) |
| Worlds Biggest Bookstore.jpg | World's Biggest Bookstore, Toronto — Ian Muttoo, CC BY-SA 2.0 | literary-scene | [File page](https://commons.wikimedia.org/wiki/File:Worlds_Biggest_Bookstore.jpg) |
| AirCanadaCentre.jpg | Scotiabank Arena (formerly Air Canada Centre) — Wikimedia Commons, CC BY 2.0 | maple-leafs-1967 | [File page](https://commons.wikimedia.org/wiki/File:AirCanadaCentre.jpg) |
| Downtown Markham (Rougeside Promenade) Centre-ville de Markham (Rougeside Promenade) (38469952964).jpg | Downtown Markham — Wikimedia Commons, CC BY 2.0 | markham | [File page](https://commons.wikimedia.org/wiki/File:Downtown_Markham_%28Rougeside_Promenade%29_Centre-ville_de_Markham_%28Rougeside_Promenade%29_%2838469952964%29.jpg) |
| Massey Hall August 2017 02.jpg | Massey Hall — Wikimedia Commons, CC BY-SA 4.0 | massey-hall | [File page](https://commons.wikimedia.org/wiki/File:Massey_Hall_August_2017_02.jpg) |
| Banting and Best.jpg | Banting and Best — Star Weekly Magazine, 1963, public domain | medical-history | [File page](https://commons.wikimedia.org/wiki/File:Banting_and_Best.jpg) |
| Niagara Escarpment from above Rattlesnake Point, Milton, Ontario.jpg | Niagara Escarpment, Rattlesnake Point, Milton — Wikimedia Commons, CC BY-SA 4.0 | milton | [File page](https://commons.wikimedia.org/wiki/File:Niagara_Escarpment_from_above_Rattlesnake_Point%2C_Milton%2C_Ontario.jpg) |
| Absolute Towers Mississauga. South-west view.jpg | Absolute World towers, Mississauga — Wikimedia Commons, CC BY-SA 4.0 | mississauga | [File page](https://commons.wikimedia.org/wiki/File:Absolute_Towers_Mississauga._South-west_view.jpg) |
| Kensington Market Toronto August 2017 03.jpg | Kensington Market — Arild Vågen, CC BY-SA 4.0 | neighbourhoods, multiculturalism, kensington-market | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Old Town Hall-460 Botsford Street-Newmarket-Ontario-HPC6381-20200905.jpg | Old Town Hall, Newmarket — Wikimedia Commons, CC BY-SA 4.0 | newmarket | [File page](https://commons.wikimedia.org/wiki/File:Old_Town_Hall-460_Botsford_Street-Newmarket-Ontario-HPC6381-20200905.jpg) |
| MelLastmanSquare - 2015June03.jpg | Mel Lastman Square, North York — Wikimedia Commons, CC BY-SA 4.0 | north-york | [File page](https://commons.wikimedia.org/wiki/File:MelLastmanSquare_-_2015June03.jpg) |
| Oakville Harbour Pier (1).JPG | Oakville Harbour — Wikimedia Commons, public domain (CC0) | oakville | [File page](https://commons.wikimedia.org/wiki/File:Oakville_Harbour_Pier_%281%29.JPG) |
| Sharp Centre for Design.jpg | Sharp Centre for Design, OCAD University — Wikimedia Commons, Creative Commons licensed | ocad-university | [File page](https://commons.wikimedia.org/wiki/File:Sharp_Centre_for_Design.jpg) |
| Ontario Place, Toronto, Canada (21653132619).jpg | Ontario Place — Wikimedia Commons, CC BY-SA 2.0 | ontario-place | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Place%2C_Toronto%2C_Canada_%2821653132619%29.jpg) |
| Law Society of Upper Canada, Osgoode Hall, Toronto, Ontario (21814316256).jpg | Osgoode Hall — Wikimedia Commons, Creative Commons licensed | osgoode-hall | [File page](https://commons.wikimedia.org/wiki/File:Law_Society_of_Upper_Canada%2C_Osgoode_Hall%2C_Toronto%2C_Ontario_%2821814316256%29.jpg) |
| High Park Toronto October 2012.jpg | High Park — Benson Kua, CC BY-SA 2.0 | parks | [File page](https://commons.wikimedia.org/wiki/File:High_Park_Toronto_October_2012.jpg) |
| Path... (1889799985).jpg | Toronto PATH tunnel — Wikimedia Commons, CC BY 2.0 | path | [File page](https://commons.wikimedia.org/wiki/File:Path..._%281889799985%29.jpg) |
| Four-Seasons-Centre.JPG | Four Seasons Centre — Wikimedia Commons, CC BY-SA 1.0 | performing-arts | [File page](https://commons.wikimedia.org/wiki/File:Four-Seasons-Centre.JPG) |
| Pickering Nuclear Generating Station at Beachfront Park, June 6 2026 (03) (5-3 cropped).jpg | Pickering Nuclear Generating Station — Wikimedia Commons, CC BY-SA 4.0 | pickering | [File page](https://commons.wikimedia.org/wiki/File:Pickering_Nuclear_Generating_Station_at_Beachfront_Park%2C_June_6_2026_%2803%29_%285-3_cropped%29.jpg) |
| YRT PRESTO tap device at Finch station.png | PRESTO tap device, Finch station — Wikimedia Commons, CC BY-SA 4.0 | presto-card | [File page](https://commons.wikimedia.org/wiki/File:YRT_PRESTO_tap_device_at_Finch_station.png) |
| Toronto Public Library Runnymede Branch (4994916241).jpg | Toronto Public Library, Runnymede Branch — Wikimedia Commons, CC BY 2.0 | public-library | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Public_Library_Runnymede_Branch_%284994916241%29.jpg) |
| Ontario Government Buildings.JPG | Ontario Legislative Building, Queen's Park — Wikimedia Commons, Creative Commons licensed | queens-park | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Government_Buildings.JPG) |
| Canadian Pacific Railway Building plaque 69 Yonge Street Toronto ON M5E 1J1 Canada.jpg | Canadian Pacific Railway Building plaque, Toronto — Wikimedia Commons, CC BY-SA 4.0 | railways | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Pacific_Railway_Building_plaque_69_Yonge_Street_Toronto_ON_M5E_1J1_Canada.jpg) |
| Toronto Raptors 2019 parade photo by Djuradj Vujcic.jpg | Toronto Raptors championship parade, 2019 — Djuradj Vujcic, CC BY 2.0 | raptors-2019 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Raptors_2019_parade_photo_by_Djuradj_Vujcic.jpg) |
| East Don Parkland - Pedestrian bridge over the Don River - 20200529.jpg | East Don Parkland — Wikimedia Commons, CC BY-SA 4.0 | ravines | [File page](https://commons.wikimedia.org/wiki/File:East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg) |
| Ismaili Centre, Toronto - Prayer hall.jpg | Ismaili Centre, Toronto, prayer hall — Wikimedia Commons, CC BY-SA 4.0 | religion | [File page](https://commons.wikimedia.org/wiki/File:Ismaili_Centre%2C_Toronto_-_Prayer_hall.jpg) |
| Town of Richmond Hill.JPG | Richmond Hill, Ontario — Wikimedia Commons, Creative Commons licensed | richmond-hill | [File page](https://commons.wikimedia.org/wiki/File:Town_of_Richmond_Hill.JPG) |
| Michael Lee-Chin Crystal, Daniel Libeskind, 2007 - Royal Ontario Museum, Toronto (1277497687).jpg | Michael Lee-Chin Crystal, ROM — Wikimedia Commons, CC BY-SA 2.0 | rom | [File page](https://commons.wikimedia.org/wiki/File:Michael_Lee-Chin_Crystal%2C_Daniel_Libeskind%2C_2007_-_Royal_Ontario_Museum%2C_Toronto_%281277497687%29.jpg) |
| City Hall, Toronto, Ontario.jpg | Toronto City Hall — Wikimedia Commons, CC BY 2.0 | safety | [File page](https://commons.wikimedia.org/wiki/File:City_Hall%2C_Toronto%2C_Ontario.jpg) |
| Scarborough Bluffs, May 4 2026 (07).jpg | Scarborough Bluffs — Wikimedia Commons, CC BY-SA 4.0 | scarborough | [File page](https://commons.wikimedia.org/wiki/File:Scarborough_Bluffs%2C_May_4_2026_%2807%29.jpg) |
| Flight stop.jpg | Flight Stop, Toronto Eaton Centre — Wikimedia Commons, Creative Commons licensed | shopping-malls | [File page](https://commons.wikimedia.org/wiki/File:Flight_stop.jpg) |
| 299 Queen Street West, Toronto, Ontario, Canada.jpg | 299 Queen Street West, Toronto — Wikimedia Commons, CC BY 2.0 | speakers-corner | [File page](https://commons.wikimedia.org/wiki/File:299_Queen_Street_West%2C_Toronto%2C_Ontario%2C_Canada.jpg) |
| Rogers Centre, Toronto, Ontario (21652480228).jpg | Rogers Centre — Wikimedia Commons, Creative Commons licensed | sports, rogers-centre, blue-jays-founding | [File page](https://commons.wikimedia.org/wiki/File:Rogers_Centre%2C_Toronto%2C_Ontario_%2821652480228%29.jpg) |
| Toronto - ON - St Lawrence Market.jpg | St. Lawrence Market — Wikimedia Commons, Creative Commons licensed | st-lawrence-market | [File page](https://commons.wikimedia.org/wiki/File:Toronto_-_ON_-_St_Lawrence_Market.jpg) |
| Pillar at Museum Station, TTC, Toronto -e.jpg | Pillar at Museum Station, TTC — Wikimedia Commons, Creative Commons licensed | subway-art | [File page](https://commons.wikimedia.org/wiki/File:Pillar_at_Museum_Station%2C_TTC%2C_Toronto_-e.jpg) |
| TIFF Bell Lightbox Founder Lounge 2023.jpg | TIFF Bell Lightbox — Wikimedia Commons, CC BY 4.0 | tiff-lightbox | [File page](https://commons.wikimedia.org/wiki/File:TIFF_Bell_Lightbox_Founder_Lounge_2023.jpg) |
| Toronto Harbour from Harbour Square Park.jpg | Toronto Harbour — Wikimedia Commons, CC BY-SA 4.0 | toronto-harbour | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Harbour_from_Harbour_Square_Park.jpg) |
| Manhole cover reading Toronto Hydro Electric System, Toronto, Ontario, 2025-08-25.jpg | Toronto Hydro Electric System manhole cover — Wikimedia Commons, CC BY-SA 4.0 | toronto-hydro | [File page](https://commons.wikimedia.org/wiki/File:Manhole_cover_reading_Toronto_Hydro_Electric_System%2C_Toronto%2C_Ontario%2C_2025-08-25.jpg) |
| Jack-Layton-Ferry-Terminal-2025-04-09.jpg | Jack Layton Ferry Terminal, Toronto — Wikimedia Commons, CC BY-SA 4.0 | toronto-islands-ferry | [File page](https://commons.wikimedia.org/wiki/File:Jack-Layton-Ferry-Terminal-2025-04-09.jpg) |
| Toronto Star Building 1929.JPG | Old Toronto Star Building, 1929 — Wikimedia Commons, public domain | toronto-star-legacy | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Star_Building_1929.JPG) |
| CLRV TTC Streetcar No 4004 (8063115473).jpg | TTC streetcar — Peter Broster, CC BY 2.0 | transit | [File page](https://commons.wikimedia.org/wiki/File:CLRV_TTC_Streetcar_No_4004_%288063115473%29.jpg) |
| Union Station grand hall.jpg | Union Station Great Hall — Wikimedia Commons, CC BY 2.0 | union-station | [File page](https://commons.wikimedia.org/wiki/File:Union_Station_grand_hall.jpg) |
| WindSeeker at Canada's Wonderland, August 2018 (3).jpg | Canada's Wonderland, Vaughan — Wikimedia Commons, CC BY-SA 3.0 | vaughan | [File page](https://commons.wikimedia.org/wiki/File:WindSeeker_at_Canada%27s_Wonderland%2C_August_2018_%283%29.jpg) |
| RC Harris Water Treatment Plant 2009.jpg | R.C. Harris Water Treatment Plant — Wikimedia Commons, CC BY 2.0 | water-treatment | [File page](https://commons.wikimedia.org/wiki/File:RC_Harris_Water_Treatment_Plant_2009.jpg) |
| Harbourfront, Toronto, Ontario from CN Tower (21652107550).jpg | Toronto Harbourfront — Wikimedia Commons, Creative Commons licensed | waterfront | [File page](https://commons.wikimedia.org/wiki/File:Harbourfront%2C_Toronto%2C_Ontario_from_CN_Tower_%2821652107550%29.jpg) |
| Remembrance Day 2014 in Whitby, Ontario.jpg | Downtown Whitby — Wikimedia Commons, CC BY 2.0 | whitby | [File page](https://commons.wikimedia.org/wiki/File:Remembrance_Day_2014_in_Whitby%2C_Ontario.jpg) |
| Toronto Nathan Phillips Square Christmas tree (16103747613).jpg | Nathan Phillips Square Christmas tree — Wikimedia Commons, Creative Commons licensed | winter-festivals | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_Christmas_tree_%2816103747613%29.jpg) |
| Woodbine Racetrack.jpg | Woodbine Racetrack — Wikimedia Commons, CC BY-SA 4.0 | woodbine-racetrack | [File page](https://commons.wikimedia.org/wiki/File:Woodbine_Racetrack.jpg) |
| Weston Park 2018 07.jpg | Weston Park, Toronto — Wikimedia Commons, CC BY-SA 4.0 | york | [File page](https://commons.wikimedia.org/wiki/File:Weston_Park_2018_07.jpg) |
| Kesho Park at the Toronto Zoo (3354803789).jpg | Kesho Park, Toronto Zoo — Wikimedia Commons, CC BY 2.0 | zoo-science-centre | [File page](https://commons.wikimedia.org/wiki/File:Kesho_Park_at_the_Toronto_Zoo_%283354803789%29.jpg) |

Images are loaded directly from Wikimedia Commons via `Special:FilePath`
(a stable MediaWiki redirect to the current full-resolution file) rather than
bundled into the repo, so credit and licensing always stay attached to the
original file page. The table above is generated straight from each page's
`hero_img`/`hero_credit` fields in `scripts/build_guide.py` (dedup'd by
filename), so it stays accurate as long as every new `PAGES` entry sets both
fields — no need to hand-maintain it separately.

## Extending the dataset

`data/terms.json` is a plain array — add an entry with `term`, `slug`,
`categories`, `origin`, `definition` and `example`, then run
`python3 scripts/build.py` to regenerate the static term cards in
`index.html` (the dictionary page is pre-rendered HTML for search engines
and no-JS visitors, not built client-side — see `README.md`). To pull real Urban Dictionary
definitions and vote counts programmatically for a seed list of terms (this
environment's network policy blocks `api.urbandictionary.com`, but most
local/CI environments won't), the endpoint is:

```
GET https://api.urbandictionary.com/v0/define?term=<term>
```

which returns `definition`, `example`, `thumbs_up`, `thumbs_down` and
`permalink` per submitted definition.
