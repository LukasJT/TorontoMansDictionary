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
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | 2003-blackout-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Kensington_Market_Toronto_August_2017_03.jpg | Kensington Market, Toronto — Arild Vågen, CC BY-SA 4.0 (illustrative of Toronto's multiculturalism; no free-license photo of a specific LINC or adult ESL classroom could be verified) | adult-esl-toronto | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | agincourt-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Pearson_Airport-Terminal_1.JPG | Toronto Pearson Airport, Terminal 1 — Wikimedia Commons, Creative Commons licensed | airports | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Pearson_Airport-Terminal_1.JPG) |
| Ajax_Waterfront_Park_(cropped).jpg | Ajax Waterfront Park — Wikimedia Commons, CC BY 4.0 | ajax | [File page](https://commons.wikimedia.org/wiki/File:Ajax_Waterfront_Park_(cropped).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | alderwood | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | alexandra-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | allan-gardens | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Houses_in_Cabbagetown_Toronto.jpg | Bay-and-gable houses, Cabbagetown — David (bootbearwdc), CC BY 2.0 | architecture | [File page](https://commons.wikimedia.org/wiki/File:Houses_in_Cabbagetown_Toronto.jpg) |
| Bmo_field_(8820851518).jpg | BMO Field, Toronto — Wikimedia Commons, CC BY 2.0 | argonauts-grey-cup | [File page](https://commons.wikimedia.org/wiki/File:Bmo_field_(8820851518).jpg) |
| Art_Gallery_of_Ontario_(24409138225).jpg | Art Gallery of Ontario — Wikimedia Commons, Creative Commons licensed | art | [File page](https://commons.wikimedia.org/wiki/File:Art_Gallery_of_Ontario_(24409138225).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | ashbridges-bay | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Aura_Condo_at_College_Park,_Toronto_Ontario.JPG | Aura, College Park, Toronto — Wikimedia Commons, Creative Commons licensed | aura-college-park | [File page](https://commons.wikimedia.org/wiki/File:Aura_Condo_at_College_Park,_Toronto_Ontario.JPG) |
| Downtown_Aurora,_Ontario_(18545289314).jpg | Downtown Aurora, Ontario — Reg Natarajan, Wikimedia Commons, Creative Commons licensed | aurora | [File page](https://commons.wikimedia.org/wiki/File:Downtown_Aurora,_Ontario_(18545289314).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | automotive-building-cne | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Avro_Arrow_rollout.jpg | Avro Arrow rollout — Wikimedia Commons, public domain | avro-arrow | [File page](https://commons.wikimedia.org/wiki/File:Avro_Arrow_rollout.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | balmy-beach | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| First_Canadian_Place,_Toronto,_Ontario_(29889104772).jpg | First Canadian Place, Toronto — Wikimedia Commons, CC BY-SA 2.0 | banks | [File page](https://commons.wikimedia.org/wiki/File:First_Canadian_Place,_Toronto,_Ontario_(29889104772).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | barbara-hall | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | barenaked-ladies | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Keds_basketball_sneakers,_1929_-_Bata_Shoe_Museum_-_DSC00724.JPG | Bata Shoe Museum, Toronto — Wikimedia Commons, Creative Commons licensed | bata-shoe-museum | [File page](https://commons.wikimedia.org/wiki/File:Keds_basketball_sneakers,_1929_-_Bata_Shoe_Museum_-_DSC00724.JPG) |
| Toronto_Pride_Parade_2007.jpg | Toronto Pride Parade — Wikimedia Commons, Creative Commons licensed (a later Pride parade, shown to represent the raids' legacy; no free-license photo of the 1981 raids or protest march itself could be verified) | bathhouse-raids-1981 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Pride_Parade_2007.jpg) |
| Osgoode_Hall,_courtroom_-2.jpg | Osgoode Hall courtroom — Padraic, Wikimedia Commons, CC BY-SA | bedford-v-canada | [File page](https://commons.wikimedia.org/wiki/File:Osgoode_Hall,_courtroom_-2.jpg) |
| Beltline_Bridge.jpg | Beltline Trail bridge, Toronto — Wikimedia Commons, Creative Commons licensed | beltline-trail | [File page](https://commons.wikimedia.org/wiki/File:Beltline_Bridge.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | berczy-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| TD_Bike_Share_Toronto_at_Carlton_and_Sherbourne.JPG | Bike Share Toronto, Carlton and Sherbourne — Wikimedia Commons, Creative Commons licensed | bike-share-toronto | [File page](https://commons.wikimedia.org/wiki/File:TD_Bike_Share_Toronto_at_Carlton_and_Sherbourne.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | billy-bishop-airport | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Black_Creek_Pioneer_Village.jpg | Black Creek Pioneer Village, Toronto — Wikimedia Commons, Creative Commons licensed | black-creek-pioneer-village | [File page](https://commons.wikimedia.org/wiki/File:Black_Creek_Pioneer_Village.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | black-creek-waterway | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | black-toronto-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | bloor-bike-lane-pilot | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Prince_Edward_Viaduct_(4672897942).jpg | Prince Edward Viaduct — Wikimedia Commons, CC BY-SA 2.0 | bloor-viaduct | [File page](https://commons.wikimedia.org/wiki/File:Prince_Edward_Viaduct_(4672897942).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | bloor-west-village | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Blue_Jays_1992_and_1993_World_Series_Rings,_Canadian_Baseball_Hall_of_Fame,_St._Marys_Ontario_2945_(4871386541).jpg | Blue Jays World Series rings, Canadian Baseball Hall of Fame — Wikimedia Commons, Creative Commons licensed | blue-jays-1992 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Blue_Jays_1992_and_1993_World_Series_Rings,_Canadian_Baseball_Hall_of_Fame,_St._Marys_Ontario_2945_(4871386541).jpg) |
| Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg | Rogers Centre — Wikimedia Commons, Creative Commons licensed | blue-jays-founding | [File page](https://commons.wikimedia.org/wiki/File:Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | board-game-cafes | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| GO_Transit_Bombardier_Bilevel_CEM_322.JPG | GO Transit bi-level rail car — Wikimedia Commons, CC BY-SA 3.0 | bombardier-toronto | [File page](https://commons.wikimedia.org/wiki/File:GO_Transit_Bombardier_Bilevel_CEM_322.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | boyd-gang | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | bradford-west-gwillimbury | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Brampton_City_Hall_West_Tower_(37520691101).jpg | Brampton City Hall — Wikimedia Commons, CC BY 2.0 | brampton | [File page](https://commons.wikimedia.org/wiki/File:Brampton_City_Hall_West_Tower_(37520691101).jpg) |
| Bell_Media_Queen_Street,_Toronto,_Ontario_(29709430050).jpg | Bell Media, Queen Street, Toronto — Wikimedia Commons, Creative Commons licensed | broadcasting | [File page](https://commons.wikimedia.org/wiki/File:Bell_Media_Queen_Street,_Toronto,_Ontario_(29709430050).jpg) |
| Mary_St._at_the_Bridge,_Beaverton,_Ontario,_Canada_(1910).jpg | Beaverton, Ontario, 1910 — Wikimedia Commons, public domain | brock-township | [File page](https://commons.wikimedia.org/wiki/File:Mary_St._at_the_Bridge,_Beaverton,_Ontario,_Canada_(1910).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | broken-social-scene | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Spencer_Smith_Park_in_Burlington,_Ontario.jpg | Spencer Smith Park, Burlington — Wikimedia Commons, Creative Commons licensed | burlington | [File page](https://commons.wikimedia.org/wiki/File:Spencer_Smith_Park_in_Burlington,_Ontario.jpg) |
| Toronto_Cabbage_Town_1_(8437347293).jpg | Cabbagetown, Toronto — Alain Rouiller, CC BY-SA 2.0 | cabbagetown | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Cabbage_Town_1_(8437347293).jpg) |
| Cheltenham_Badlands,_Caledon_Hills,_Ontario,_Canada._(7097453311).jpg | Cheltenham Badlands, Caledon — kaybee07, Wikimedia Commons, CC BY 2.0 | caledon | [File page](https://commons.wikimedia.org/wiki/File:Cheltenham_Badlands,_Caledon_Hills,_Ontario,_Canada._(7097453311).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | camh-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Campbell_House.JPG | Campbell House, Toronto — Wikimedia Commons, Creative Commons licensed | campbell-house | [File page](https://commons.wikimedia.org/wiki/File:Campbell_House.JPG) |
| Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg | Maple Leaf Gardens, Toronto — Wikimedia Commons, Creative Commons licensed | canada-cup-1976 | [File page](https://commons.wikimedia.org/wiki/File:Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | canada-goose | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Four-Seasons-Centre.JPG | Four Seasons Centre, Toronto — Wikimedia Commons, CC BY-SA 1.0 | canadian-music-week | [File page](https://commons.wikimedia.org/wiki/File:Four-Seasons-Centre.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | canadian-opera-company | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Canadian_Broadcasting_Centre,_Corner_of_John_and_Front_Street,_Toronto,_Ontario_(29920113811).jpg | Canadian Broadcasting Centre, Toronto — Wikimedia Commons, Creative Commons licensed | canadian-screen-awards | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Broadcasting_Centre,_Corner_of_John_and_Front_Street,_Toronto,_Ontario_(29920113811).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | canadian-stage-theatre | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Canadian_Tire_store_Belleville_1994.jpg | Canadian Tire store, 1994 — Wikimedia Commons, Creative Commons licensed | canadian-tire | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Tire_store_Belleville_1994.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | caribana-caribbean-carnival | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Casa_Loma,_Toronto,_Ontario_(29709454210).jpg | Casa Loma — Wikimedia Commons, CC BY-SA 2.0 | casa-loma | [File page](https://commons.wikimedia.org/wiki/File:Casa_Loma,_Toronto,_Ontario_(29709454210).jpg) |
| CATHERINE_OHARA.jpg | Catherine O'Hara, 2005 — Jerry Avenaim, Wikimedia Commons, Creative Commons licensed | catherine-ohara | [File page](https://commons.wikimedia.org/wiki/File:CATHERINE_OHARA.jpg) |
| Toronto_Nathan_Phillips_Square_Christmas_tree_(16103747613).jpg | Nathan Phillips Square Christmas tree — Wikimedia Commons, Creative Commons licensed | cavalcade-of-lights | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_Christmas_tree_(16103747613).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | cbc-broadcasting-centre-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Canadian_Broadcasting_Centre,_Toronto,_Ontario_(29968452336).jpg | Canadian Broadcasting Centre, Toronto — Wikimedia Commons, Creative Commons licensed | cbc-toronto | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Broadcasting_Centre,_Toronto,_Ontario_(29968452336).jpg) |
| Graves_of_Frederick_Grant_Banting_(1891–1941)_and_Henrietta_Elizabeth_Ball_Banting_(1912–1976)_at_Mount_Pleasant_Cemetery,_Toronto.jpg | Frederick Banting's grave, Mount Pleasant Cemetery — Wikimedia Commons, CC BY 4.0 | cemeteries | [File page](https://commons.wikimedia.org/wiki/File:Graves_of_Frederick_Grant_Banting_(1891–1941)_and_Henrietta_Elizabeth_Ball_Banting_(1912–1976)_at_Mount_Pleasant_Cemetery,_Toronto.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | cfrb-radio-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | cherry-beach | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | chinatown-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Chinatown_toronto_spadina_avenue.JPG | Chinatown, Spadina Avenue, Toronto — Wikimedia Commons, CC BY-SA | chinese-food-dim-sum | [File page](https://commons.wikimedia.org/wiki/File:Chinatown_toronto_spadina_avenue.JPG) |
| Chinatown_toronto_spadina_avenue.JPG | Chinatown, Spadina Avenue — Wikimedia Commons, CC BY-SA | chinese-head-tax | [File page](https://commons.wikimedia.org/wiki/File:Chinatown_toronto_spadina_avenue.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | christie-pits-riot-1933 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | chum-radio-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | cineplex | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | cityplace | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Downtown_Bowmanville_-_King_St.jpg | Downtown Bowmanville, Ontario — Wikimedia Commons, Creative Commons licensed | clarington | [File page](https://commons.wikimedia.org/wiki/File:Downtown_Bowmanville_-_King_St.jpg) |
| CN_Tower,_Toronto,_Ontario_(29969151776).jpg | The CN Tower — Wikimedia Commons, CC BY-SA 2.0 | cn-tower | [File page](https://commons.wikimedia.org/wiki/File:CN_Tower,_Toronto,_Ontario_(29969151776).jpg) |
| Canadian_National_Exhibition_(CNE)_fireworks_(17419476860).jpg | CNE fireworks — Wikimedia Commons, CC BY-SA 2.0 | cne | [File page](https://commons.wikimedia.org/wiki/File:Canadian_National_Exhibition_(CNE)_fireworks_(17419476860).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | coca-cola-coliseum | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| The_Boiler_House,_Distillery_district._Toronto._(5617418107).jpg | The Boiler House, Distillery District — Wikimedia Commons, Creative Commons licensed | cocktail-scene | [File page](https://commons.wikimedia.org/wiki/File:The_Boiler_House,_Distillery_district._Toronto._(5617418107).jpg) |
| The_Only_Cafe,_Danforth_Avenue,_Toronto,_Canada,_May_2014.jpg | The Only Cafe, Danforth Avenue — Wikimedia Commons, Creative Commons licensed | coffee-culture | [File page](https://commons.wikimedia.org/wiki/File:The_Only_Cafe,_Danforth_Avenue,_Toronto,_Canada,_May_2014.jpg) |
| Colborne_Lodge_Toronto_2009.jpg | Colborne Lodge, High Park — Wikimedia Commons, Creative Commons licensed | colborne-lodge | [File page](https://commons.wikimedia.org/wiki/File:Colborne_Lodge_Toronto_2009.jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | comedy | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Commerce_Court_North.JPG | Commerce Court, Toronto — Wikimedia Commons, Creative Commons licensed | commerce-court | [File page](https://commons.wikimedia.org/wiki/File:Commerce_Court_North.JPG) |
| Conn_Smythe_Trophy_2010-04-03.JPG | Conn Smythe Trophy — Wikimedia Commons, Creative Commons licensed | conn-smythe | [File page](https://commons.wikimedia.org/wiki/File:Conn_Smythe_Trophy_2010-04-03.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | connaught-labs | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | convocation-hall | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | corktown | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | corso-italia | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | covid-19-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Railway_Museum_and_Steam_Whistle_Brewery_are_located_in_the_Roundhouse_Park_(27622030420).jpg | Steam Whistle Brewery, Roundhouse Park — Wikimedia Commons, Creative Commons licensed | craft-beer | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Railway_Museum_and_Steam_Whistle_Brewery_are_located_in_the_Roundhouse_Park_(27622030420).jpg) |
| Toronto_Protected_Bike_Lanes.jpg | Protected bike lane, Toronto — Wikimedia Commons, Creative Commons licensed | cycling | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Protected_Bike_Lanes.jpg) |
| Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg | Toronto teaching hospital — Wikimedia Commons, Creative Commons licensed | cystic-fibrosis-gene | [File page](https://commons.wikimedia.org/wiki/File:Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | daniels-spectrum | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Toronto City Hall — Wikimedia Commons, CC BY 2.0 | david-crombie | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | david-cronenberg | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Dunlap_Observatory.jpg | David Dunlap Observatory — Wikimedia Commons, Creative Commons licensed | david-dunlap-observatory | [File page](https://commons.wikimedia.org/wiki/File:Dunlap_Observatory.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | david-miller | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| DavisvilleToronto.JPG | Davisville, Toronto — Wikimedia Commons, Creative Commons licensed | davisville | [File page](https://commons.wikimedia.org/wiki/File:DavisvilleToronto.JPG) |
| De_Havilland_Canada_DHC-2_Beaver._(8107669296).jpg | De Havilland Canada DHC-2 Beaver — Wikimedia Commons, public domain | de-havilland-canada | [File page](https://commons.wikimedia.org/wiki/File:De_Havilland_Canada_DHC-2_Beaver._(8107669296).jpg) |
| New_Toronto_Stock_Exchange_trading_floor.jpg | Toronto Stock Exchange trading floor — Wikimedia Commons, Creative Commons licensed | design-exchange | [File page](https://commons.wikimedia.org/wiki/File:New_Toronto_Stock_Exchange_trading_floor.jpg) |
| East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg | East Don Parkland, Toronto — Wikimedia Commons, CC BY-SA 4.0 | don-river-flooding | [File page](https://commons.wikimedia.org/wiki/File:East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | downsview-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | dragon-boat-race-festival | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | drake-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | dufferin-grove-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| GM_Canada_Oshawa_-_Flickr_-_Stradablog.jpg | GM Canada, Oshawa — Wikimedia Commons, CC BY 2.0 | durham-region | [File page](https://commons.wikimedia.org/wiki/File:GM_Canada_Oshawa_-_Flickr_-_Stradablog.jpg) |
| Holland_Landing_ON.JPG | Holland Landing, Ontario — Wikimedia Commons, CC BY-SA 3.0 | east-gwillimbury | [File page](https://commons.wikimedia.org/wiki/File:Holland_Landing_ON.JPG) |
| Leaside_Bridge,_construction_(29661028238).jpg | Leaside Bridge under construction — Wikimedia Commons, CC BY 2.0 | east-york | [File page](https://commons.wikimedia.org/wiki/File:Leaside_Bridge,_construction_(29661028238).jpg) |
| Flight_stop.jpg | Flight Stop, Toronto Eaton Centre — Wikimedia Commons, Creative Commons licensed (present-day photo; no free-license photo of the 1977 Annex fire itself could be verified) | eatons-annex-fire | [File page](https://commons.wikimedia.org/wiki/File:Flight_stop.jpg) |
| 1918eatonssantaclausparade.jpg | Eaton's Santa Claus Parade, 1918 — Archives of Ontario, public domain | eatons-simpsons | [File page](https://commons.wikimedia.org/wiki/File:1918eatonssantaclausparade.jpg) |
| Bay_Street,_Financial_District,_Toronto,_Ontario_(29708936890).jpg | Bay Street, Financial District — Wikimedia Commons, Creative Commons licensed | economy | [File page](https://commons.wikimedia.org/wiki/File:Bay_Street,_Financial_District,_Toronto,_Ontario_(29708936890).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | ed-mirvish-theatres | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | education | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Edwards_Gardens2.JPG | Edwards Gardens, Toronto — Wikimedia Commons, Creative Commons licensed | edwards-gardens | [File page](https://commons.wikimedia.org/wiki/File:Edwards_Gardens2.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | eglinton-crosstown | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| E.J._Pratt_Library,_Victoria_University,_University_of_Toronto,_Canada.jpg | E.J. Pratt Library, Victoria University — Wikimedia Commons, Creative Commons licensed | ej-pratt | [File page](https://commons.wikimedia.org/wiki/File:E.J._Pratt_Library,_Victoria_University,_University_of_Toronto,_Canada.jpg) |
| Elgin_Theatre_interior.jpg | Elgin Theatre interior, Toronto — Wikimedia Commons, Creative Commons licensed | elgin-winter-garden-theatre | [File page](https://commons.wikimedia.org/wiki/File:Elgin_Theatre_interior.jpg) |
| Chinatown_toronto_spadina_avenue.JPG | Chinatown, Spadina Avenue — Wikimedia Commons, CC BY-SA | ethnic-enclaves | [File page](https://commons.wikimedia.org/wiki/File:Chinatown_toronto_spadina_avenue.JPG) |
| Humber_Bay_Arch_Bridge_at_Night_1.jpg | Humber Bay Arch Bridge, Etobicoke — Wikimedia Commons, CC BY-SA 2.0 | etobicoke | [File page](https://commons.wikimedia.org/wiki/File:Humber_Bay_Arch_Bridge_at_Night_1.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | evergreen-brick-works | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Coca-Cola_Coliseum,_Exhibition_Place,_Toronto,_Ontario_(29901775271).jpg | Coca-Cola Coliseum, Exhibition Place — Wikimedia Commons, CC BY-SA 2.0 | exhibition-place | [File page](https://commons.wikimedia.org/wiki/File:Coca-Cola_Coliseum,_Exhibition_Place,_Toronto,_Ontario_(29901775271).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | exhibition-stadium | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Tree_falls_on_vehicle_-_Toronto_Ice_Storm_2013.jpg | Toronto Ice Storm, 2013 — Wikimedia Commons, Creative Commons licensed | extreme-weather | [File page](https://commons.wikimedia.org/wiki/File:Tree_falls_on_vehicle_-_Toronto_Ice_Storm_2013.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | fairmont-royal-york | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Nathan Phillips Square, Toronto City Hall — Wikimedia Commons, CC BY 2.0 | famous-torontonians | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Caribana_Toronto_2011_(2).jpg | Caribana Toronto — Ruth Choi, CC BY-SA 2.0 | festivals | [File page](https://commons.wikimedia.org/wiki/File:Caribana_Toronto_2011_(2).jpg) |
| First_Canadian_Place,_Toronto,_Ontario_(29889104772).jpg | First Canadian Place, Toronto — Wikimedia Commons, CC BY-SA 2.0 | first-canadian-place | [File page](https://commons.wikimedia.org/wiki/File:First_Canadian_Place,_Toronto,_Ontario_(29889104772).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | flatiron-gooderham-building | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | flemingdon-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| St_Lawrence_Market,_Toronto,_West_partial_view_20170417_1.jpg | St. Lawrence Market — Wikimedia Commons, Creative Commons licensed | food | [File page](https://commons.wikimedia.org/wiki/File:St_Lawrence_Market,_Toronto,_West_partial_view_20170417_1.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | forest-hill | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | fort-rouille | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Fort_York_east_blockhouse_2.jpg | Fort York, Toronto — Wikimedia Commons, Creative Commons licensed | fort-york | [File page](https://commons.wikimedia.org/wiki/File:Fort_York_east_blockhouse_2.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | fort-york-armoury | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| F._G._Banting_1923.jpg | Frederick Banting, 1923 — Wikimedia Commons, public domain | frederick-banting | [File page](https://commons.wikimedia.org/wiki/File:F._G._Banting_1923.jpg) |
| Le_Collège_français,_Toronto,_Ontario_(30002887135).jpg | Le Collège français, Toronto — Wikimedia Commons, Creative Commons licensed | french-language-education-toronto | [File page](https://commons.wikimedia.org/wiki/File:Le_Collège_français,_Toronto,_Ontario_(30002887135).jpg) |
| G8_G20_Toronto_2010_Riot_Police_on_Yonge_St._(4736355911).jpg | Riot police, G20 Toronto 2010 — Chris Huggins, Wikimedia Commons, Creative Commons licensed | g20-toronto-2010 | [File page](https://commons.wikimedia.org/wiki/File:G8_G20_Toronto_2010_Riot_Police_on_Yonge_St._(4736355911).jpg) |
| Gardiner_Expressway,_Toronto,_Ontario_(29968916176).jpg | Gardiner Expressway — Wikimedia Commons, CC BY-SA 2.0 | gardiner-dvp | [File page](https://commons.wikimedia.org/wiki/File:Gardiner_Expressway,_Toronto,_Ontario_(29968916176).jpg) |
| Covered_Jar_with_Garden_Design,_c._1660-1690,_Arita,_hard-paste_porcelain_with_overglaze_enamels_-_Gardiner_Museum,_Toronto_-_DSC00442.JPG | Gardiner Museum, Toronto — Wikimedia Commons, Creative Commons licensed | gardiner-museum | [File page](https://commons.wikimedia.org/wiki/File:Covered_Jar_with_Garden_Design,_c._1660-1690,_Arita,_hard-paste_porcelain_with_overglaze_enamels_-_Gardiner_Museum,_Toronto_-_DSC00442.JPG) |
| GBC_Casa_Loma_02.jpg | George Brown College, Casa Loma Campus — PvOberstein, Wikimedia Commons, CC0 | george-brown-college | [File page](https://commons.wikimedia.org/wiki/File:GBC_Casa_Loma_02.jpg) |
| Gibon_House_view_from_front.jpg | Gibson House, North York — Wikimedia Commons, Creative Commons licensed | gibson-house | [File page](https://commons.wikimedia.org/wiki/File:Gibon_House_view_from_front.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | glad-day-bookshop | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | glenn-gould-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | globe-and-mail-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| GO_Transit_MP40-3C_602_Oshawa_Turnaround_Rushhour.JPG | GO Transit train, Oshawa — Wikimedia Commons, CC BY 3.0 | go-transit | [File page](https://commons.wikimedia.org/wiki/File:GO_Transit_MP40-3C_602_Oshawa_Turnaround_Rushhour.JPG) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Toronto City Hall, Nathan Phillips Square — Wikimedia Commons, CC BY 2.0 | government | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | graffiti-alley | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Where_the_Fire_Started_Toronto,_19th_April_1904_(HS85-10-14985).jpg | Where the Fire Started, Toronto, 1904 — Library and Archives Canada, public domain | great-fire-1904 | [File page](https://commons.wikimedia.org/wiki/File:Where_the_Fire_Started_Toronto,_19th_April_1904_(HS85-10-14985).jpg) |
| Greektown,_Toronto_(6221866833).jpg | Greektown, Toronto — Wikimedia Commons, Creative Commons licensed | greektown-danforth | [File page](https://commons.wikimedia.org/wiki/File:Greektown,_Toronto_(6221866833).jpg) |
| Entrance_to_McMichael_Gallery_in_Kleinburg,_Ontario,_Canada_(8203976920).jpg | McMichael Canadian Art Collection, Kleinburg — Wikimedia Commons, Creative Commons licensed | group-of-seven | [File page](https://commons.wikimedia.org/wiki/File:Entrance_to_McMichael_Gallery_in_Kleinburg,_Ontario,_Canada_(8203976920).jpg) |
| Guild_Park_and_Gardens_(26712913409).jpg | Guild Park and Gardens, Toronto — Wikimedia Commons, Creative Commons licensed | guild-park-gardens | [File page](https://commons.wikimedia.org/wiki/File:Guild_Park_and_Gardens_(26712913409).jpg) |
| Georgetown_Mill_(4018302734)_(cropped).jpg | Barber mill, Georgetown — Wikimedia Commons, CC BY 2.0 | halton-hills | [File page](https://commons.wikimedia.org/wiki/File:Georgetown_Mill_(4018302734)_(cropped).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | harbord-village | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Harbourfront,_Toronto,_Ontario_from_CN_Tower_(21652107550).jpg | Harbourfront, Toronto — Wikimedia Commons, Creative Commons licensed | harbourfront-centre | [File page](https://commons.wikimedia.org/wiki/File:Harbourfront,_Toronto,_Ontario_from_CN_Tower_(21652107550).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | harold-ballard | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | hart-house | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Cherry_Blossom_in_High_Park_69.jpg | Cherry blossoms, High Park — Wikimedia Commons, CC BY-SA 4.0 | high-park | [File page](https://commons.wikimedia.org/wiki/File:Cherry_Blossom_in_High_Park_69.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | hockey-hall-of-fame | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | holy-blossom-temple | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Toronto City Hall — Wikimedia Commons, CC BY 2.0 | homelessness | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | honest-eds | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg | Toronto General Hospital — Wikimedia Commons, Creative Commons licensed | hospitals | [File page](https://commons.wikimedia.org/wiki/File:Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg) |
| Hot_Docs_Ted_Rogers_Cinema.jpg | Hot Docs Ted Rogers Cinema, Toronto — Wikimedia Commons, Creative Commons licensed | hot-docs-festival | [File page](https://commons.wikimedia.org/wiki/File:Hot_Docs_Ted_Rogers_Cinema.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | housing | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | hto-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | hudsons-bay-company | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | humber-bay-arch-bridge | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Cinesphere,_at_Ontario_Place,_in_2012,_when_it_was_closed_for_several_years_(7157561345).jpg | Cinesphere, Ontario Place — Wikimedia Commons, Creative Commons licensed | imax-toronto | [File page](https://commons.wikimedia.org/wiki/File:Cinesphere,_at_Ontario_Place,_in_2012,_when_it_was_closed_for_several_years_(7157561345).jpg) |
| Toronto_skyline_toronto_islands_b.JPG | Toronto skyline from the Toronto Islands — Wikimedia Commons, Creative Commons licensed | indigenous-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_toronto_islands_b.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | indigo-books | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Jamaican_patties_and_redstripe.jpg | Jamaican patties — Wikimedia Commons, CC BY-SA 2.0 | jamaican-patty-toronto | [File page](https://commons.wikimedia.org/wiki/File:Jamaican_patties_and_redstripe.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | jami-mosque-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | jane-and-finch | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Jim_Carrey_2008.jpg | Jim Carrey, 2008 — Wikimedia Commons, CC BY-SA 2.0 | jim-carrey | [File page](https://commons.wikimedia.org/wiki/File:Jim_Carrey_2008.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | john-candy | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Mayor_John_Tory_in_Toronto_at_the_Good_Friday_Procession_-_2018_(27264606888)_(cropped).jpg | John Tory, 2018 — Wikimedia Commons, CC BY 2.0 | john-tory | [File page](https://commons.wikimedia.org/wiki/File:Mayor_John_Tory_in_Toronto_at_the_Good_Friday_Procession_-_2018_(27264606888)_(cropped).jpg) |
| Keanu_Reeves_2014.jpg | Keanu Reeves, 2014 — Wikimedia Commons, Creative Commons licensed | keanu-reeves | [File page](https://commons.wikimedia.org/wiki/File:Keanu_Reeves_2014.jpg) |
| Kensington_Market_Toronto_August_2017_03.jpg | Kensington Market, Toronto — Arild Vågen, CC BY-SA 4.0 | kensington-jewish-history | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Kensington_Market_Toronto_August_2017_03.jpg | Kensington Market — Arild Vågen, CC BY-SA 4.0 | kensington-market | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | kensington-pedestrian-sundays | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | kew-beach | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | king-edward-hotel | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Eaton_Hall_King_City.jpg | Eaton Hall, King City — AndroidCat, Wikimedia Commons, CC BY 3.0 | king-township | [File page](https://commons.wikimedia.org/wiki/File:Eaton_Hall_King_City.jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | CN Tower and Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | landmarks | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | laneway-housing-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| LCBO_at_Parkway_Mall.jpg | LCBO, Parkway Mall — Wikimedia Commons, CC BY-SA 4.0 | lcbo-history | [File page](https://commons.wikimedia.org/wiki/File:LCBO_at_Parkway_Mall.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | leaside-bridge | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Leslieville.jpg | Leslieville, Toronto — Simon Pulsifer, CC BY-SA | leslieville | [File page](https://commons.wikimedia.org/wiki/File:Leslieville.jpg) |
| Pride_parade_Toronto_2011.jpg | Toronto Pride parade, 2011 — Kitty Rainbow, CC BY 2.0 | lgbtq-village | [File page](https://commons.wikimedia.org/wiki/File:Pride_parade_Toronto_2011.jpg) |
| Liberty_Village_in_Toronto,_June_24_2025.jpg | Liberty Village, Toronto — PascalHD, CC BY-SA 4.0 | liberty-village | [File page](https://commons.wikimedia.org/wiki/File:Liberty_Village_in_Toronto,_June_24_2025.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | line-1-yonge-university | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| TTC_PCC_4659,_a_SUBWAY_DANFORTH_car_at_the_Luttrell_Loop,_Toronto,_ON_on_July_3,_1966_(34182476270).jpg | TTC streetcar, July 1966 — Wikimedia Commons, Creative Commons licensed | line-2-bloor-danforth | [File page](https://commons.wikimedia.org/wiki/File:TTC_PCC_4659,_a_SUBWAY_DANFORTH_car_at_the_Luttrell_Loop,_Toronto,_ON_on_July_3,_1966_(34182476270).jpg) |
| Worlds_Biggest_Bookstore.jpg | World's Biggest Bookstore, Toronto — Ian Muttoo, CC BY-SA 2.0 | literary-scene | [File page](https://commons.wikimedia.org/wiki/File:Worlds_Biggest_Bookstore.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | little-india-gerrard | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | little-italy-college-street | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | little-jamaica | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | little-portugal-bakeries | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | little-trinity-church | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Loblaw_Groceterias_Limited_Store_No_1_Toronto_ca_1919.jpg | Loblaw Groceterias store No. 1, circa 1919 — Wikimedia Commons, public domain | loblaws-history | [File page](https://commons.wikimedia.org/wiki/File:Loblaw_Groceterias_Limited_Store_No_1_Toronto_ca_1919.jpg) |
| Longbranch_TPL.jpg | Long Branch branch, Toronto Public Library — Wikimedia Commons, CC BY-SA 3.0 | long-branch | [File page](https://commons.wikimedia.org/wiki/File:Longbranch_TPL.jpg) |
| Melanie_Fiona_at_Luminato_2010_(4).jpg | Luminato Festival, Toronto — Wikimedia Commons, Creative Commons licensed | luminato-festival | [File page](https://commons.wikimedia.org/wiki/File:Melanie_Fiona_at_Luminato_2010_(4).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | luminous-veil-bloor-viaduct | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| 201708_Mackenzie_House_01.jpg | Mackenzie House, Toronto — Wikimedia Commons, Creative Commons licensed | mackenzie-house | [File page](https://commons.wikimedia.org/wiki/File:201708_Mackenzie_House_01.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | maestro-fresh-wes | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Magna_International_Headquarters_Aurora_Ontario_Night.jpg | Magna International headquarters, Aurora — Wikimedia Commons, Creative Commons licensed | magna-international | [File page](https://commons.wikimedia.org/wiki/File:Magna_International_Headquarters_Aurora_Ontario_Night.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | malvern-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg | Maple Leaf Gardens, Toronto — Wikimedia Commons, Creative Commons licensed | maple-leaf-gardens | [File page](https://commons.wikimedia.org/wiki/File:Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg) |
| AirCanadaCentre.jpg | Scotiabank Arena (formerly Air Canada Centre) — Wikimedia Commons, CC BY 2.0 | maple-leafs-1967 | [File page](https://commons.wikimedia.org/wiki/File:AirCanadaCentre.jpg) |
| Margaret_Atwood_2015.jpg | Margaret Atwood, 2015 — Larry D. Moore, CC BY 4.0 | margaret-atwood | [File page](https://commons.wikimedia.org/wiki/File:Margaret_Atwood_2015.jpg) |
| Downtown_Markham_(Rougeside_Promenade)_Centre-ville_de_Markham_(Rougeside_Promenade)_(38469952964).jpg | Downtown Markham — Wikimedia Commons, CC BY 2.0 | markham | [File page](https://commons.wikimedia.org/wiki/File:Downtown_Markham_(Rougeside_Promenade)_Centre-ville_de_Markham_(Rougeside_Promenade)_(38469952964).jpg) |
| Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg | Toronto General Hospital — Wikimedia Commons, Creative Commons licensed | mars-discovery-district | [File page](https://commons.wikimedia.org/wiki/File:Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg) |
| Marshall_McLuhan_1967.jpg | Marshall McLuhan, 1967 — Wikimedia Commons, Creative Commons licensed | marshall-mcluhan | [File page](https://commons.wikimedia.org/wiki/File:Marshall_McLuhan_1967.jpg) |
| Massey_Hall_August_2017_02.jpg | Massey Hall — Wikimedia Commons, CC BY-SA 4.0 | massey-hall | [File page](https://commons.wikimedia.org/wiki/File:Massey_Hall_August_2017_02.jpg) |
| Massey_Hall,_Toronto_Panorama.jpg | Massey Hall, Toronto — Ian Muttoo, CC BY-SA 2.0 | massey-hall-performances | [File page](https://commons.wikimedia.org/wiki/File:Massey_Hall,_Toronto_Panorama.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | massey-manufacturing | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | media | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Banting_and_Best.jpg | Banting and Best — Star Weekly Magazine, 1963, public domain | medical-history | [File page](https://commons.wikimedia.org/wiki/File:Banting_and_Best.jpg) |
| MelLastmanSquare_-_2015June03.jpg | Mel Lastman Square, North York — Wikimedia Commons, CC BY-SA 4.0 | mel-lastman | [File page](https://commons.wikimedia.org/wiki/File:MelLastmanSquare_-_2015June03.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | metro-toronto-federation-1954 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | metropolitan-united-church | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Michael_Ondaatje_at_Tulane_2010.jpg | Michael Ondaatje, 2010 — Wikimedia Commons, Creative Commons licensed | michael-ondaatje | [File page](https://commons.wikimedia.org/wiki/File:Michael_Ondaatje_at_Tulane_2010.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | michael-ondaatje-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Mike_Myers_2017.jpg | Mike Myers, 2017 — Wikimedia Commons, CC BY 2.0 | mike-myers | [File page](https://commons.wikimedia.org/wiki/File:Mike_Myers_2017.jpg) |
| Niagara_Escarpment_from_above_Rattlesnake_Point,_Milton,_Ontario.jpg | Niagara Escarpment, Rattlesnake Point, Milton — Wikimedia Commons, CC BY-SA 4.0 | milton | [File page](https://commons.wikimedia.org/wiki/File:Niagara_Escarpment_from_above_Rattlesnake_Point,_Milton,_Ontario.jpg) |
| View_of_Mimico_Waterfront_Park_and_buildings,_Toronto_2026.jpg | Mimico Waterfront Park — Wikimedia Commons, CC BY-SA 4.0 | mimico | [File page](https://commons.wikimedia.org/wiki/File:View_of_Mimico_Waterfront_Park_and_buildings,_Toronto_2026.jpg) |
| Absolute_Towers_Mississauga._South-west_view.jpg | Absolute World towers, Mississauga — Wikimedia Commons, CC BY-SA 4.0 | mississauga | [File page](https://commons.wikimedia.org/wiki/File:Absolute_Towers_Mississauga._South-west_view.jpg) |
| Absolute_Towers_Mississauga._South-west_view.jpg | Downtown Mississauga — Wikimedia Commons, CC BY-SA 4.0 (present-day photo; no free-license image of the 1979 derailment itself could be verified) | mississauga-train-derailment | [File page](https://commons.wikimedia.org/wiki/File:Absolute_Towers_Mississauga._South-west_view.jpg) |
| Rosedale-Moore_Park_2025.jpg | Rosedale–Moore Park, 2025 — Wikimedia Commons, CC BY 4.0 | moore-park | [File page](https://commons.wikimedia.org/wiki/File:Rosedale-Moore_Park_2025.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | moss-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | mount-pleasant-cemetery | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Mount_Sinai_Hospital_(50601558238).jpg | Mount Sinai Hospital, Toronto — Wikimedia Commons, Creative Commons licensed | mount-sinai-hospital | [File page](https://commons.wikimedia.org/wiki/File:Mount_Sinai_Hospital_(50601558238).jpg) |
| Bell_Media_Queen_Street,_Toronto,_Ontario_(29709430050).jpg | 299 Queen Street West, Toronto — Wikimedia Commons, Creative Commons licensed | much-music-awards | [File page](https://commons.wikimedia.org/wiki/File:Bell_Media_Queen_Street,_Toronto,_Ontario_(29709430050).jpg) |
| Kensington_Market_Toronto_August_2017_03.jpg | Kensington Market — Arild Vågen, CC BY-SA 4.0 | multiculturalism | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Nathan Phillips Square, Toronto City Hall — Wikimedia Commons, CC BY 2.0 | nathan-phillips-square | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | national-ballet-of-canada | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | necropolis-cemetery | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Kensington_Market_Toronto_August_2017_03.jpg | Kensington Market — Arild Vågen, CC BY-SA 4.0 | neighbourhoods | [File page](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| Lake_Shore_Road,_New_Toronto_1928-10-12.jpg | Lake Shore Road, New Toronto, 1928 — Wikimedia Commons, believed public domain | new-toronto | [File page](https://commons.wikimedia.org/wiki/File:Lake_Shore_Road,_New_Toronto_1928-10-12.jpg) |
| Old_Town_Hall-460_Botsford_Street-Newmarket-Ontario-HPC6381-20200905.jpg | Old Town Hall, Newmarket — Wikimedia Commons, CC BY-SA 4.0 | newmarket | [File page](https://commons.wikimedia.org/wiki/File:Old_Town_Hall-460_Botsford_Street-Newmarket-Ontario-HPC6381-20200905.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | newspapers | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | nicknames | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Michael_Jewison_and_Norman_Jewison_at_the_2009_CFC_in_L.A._event._(48198981497).jpg | Norman Jewison, Canadian Film Centre event — Wikimedia Commons, Creative Commons licensed | norman-jewison | [File page](https://commons.wikimedia.org/wiki/File:Michael_Jewison_and_Norman_Jewison_at_the_2009_CFC_in_L.A._event._(48198981497).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | noronic-fire-1949 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| MelLastmanSquare_-_2015June03.jpg | Mel Lastman Square, North York — Wikimedia Commons, CC BY-SA 4.0 | north-york | [File page](https://commons.wikimedia.org/wiki/File:MelLastmanSquare_-_2015June03.jpg) |
| Northrop_Frye_sitting_on_a_bench_at_the_University_of_Toronto.jpg | Northrop Frye, University of Toronto — Wikimedia Commons, Creative Commons licensed | northrop-frye | [File page](https://commons.wikimedia.org/wiki/File:Northrop_Frye_sitting_on_a_bench_at_the_University_of_Toronto.jpg) |
| Lite_brite_Toronto_Nuit_Blanche.jpg | Nuit Blanche Toronto — Wikimedia Commons, CC BY 2.0 | nuit-blanche-toronto | [File page](https://commons.wikimedia.org/wiki/File:Lite_brite_Toronto_Nuit_Blanche.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | oak-ridges-moraine | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Oakville_Harbour_Pier_(1).JPG | Oakville Harbour — Wikimedia Commons, public domain (CC0) | oakville | [File page](https://commons.wikimedia.org/wiki/File:Oakville_Harbour_Pier_(1).JPG) |
| Sharp_Centre_for_Design.jpg | Sharp Centre for Design, OCAD University — Wikimedia Commons, Creative Commons licensed | ocad-university | [File page](https://commons.wikimedia.org/wiki/File:Sharp_Centre_for_Design.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | old-city-hall | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Olivia_Chow_2014.jpg | Olivia Chow — Wikimedia Commons, Creative Commons licensed | olivia-chow | [File page](https://commons.wikimedia.org/wiki/File:Olivia_Chow_2014.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | ontario-food-terminal | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | ontario-line | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Ontario_Place,_Toronto,_Canada_(21653132619).jpg | Ontario Place — Wikimedia Commons, CC BY-SA 2.0 | ontario-place | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Place,_Toronto,_Canada_(21653132619).jpg) |
| Ontario_Science_Centre_Bridge_2023.jpg | Ontario Science Centre, Toronto — Wikimedia Commons, Creative Commons licensed | ontario-science-centre | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Science_Centre_Bridge_2023.jpg) |
| Downtown_Orangeville_(Broadway)_Centre-ville_de_Orangeville_(Broadway)_(24320442797).jpg | Downtown Orangeville, Broadway — Wikimedia Commons, Creative Commons licensed | orangeville | [File page](https://commons.wikimedia.org/wiki/File:Downtown_Orangeville_(Broadway)_Centre-ville_de_Orangeville_(Broadway)_(24320442797).jpg) |
| Law_Society_of_Upper_Canada,_Osgoode_Hall,_Toronto,_Ontario_(21814316256).jpg | Osgoode Hall — Wikimedia Commons, Creative Commons licensed | osgoode-hall | [File page](https://commons.wikimedia.org/wiki/File:Law_Society_of_Upper_Canada,_Osgoode_Hall,_Toronto,_Ontario_(21814316256).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | palais-royale | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | parkdale | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| High_Park_Toronto_October_2012.jpg | High Park — Benson Kua, CC BY-SA 2.0 | parks | [File page](https://commons.wikimedia.org/wiki/File:High_Park_Toronto_October_2012.jpg) |
| Path..._(1889799985).jpg | Toronto PATH tunnel — Wikimedia Commons, CC BY 2.0 | path | [File page](https://commons.wikimedia.org/wiki/File:Path..._(1889799985).jpg) |
| Peameal_bacon_sandwich.jpg | Peameal bacon sandwich — Wikimedia Commons, CC BY-SA 4.0 | peameal-bacon-sandwich | [File page](https://commons.wikimedia.org/wiki/File:Peameal_bacon_sandwich.jpg) |
| Four-Seasons-Centre.JPG | Four Seasons Centre — Wikimedia Commons, CC BY-SA 1.0 | performing-arts | [File page](https://commons.wikimedia.org/wiki/File:Four-Seasons-Centre.JPG) |
| Pickering_Nuclear_Generating_Station_at_Beachfront_Park,_June_6_2026_(03)_(5-3_cropped).jpg | Pickering Nuclear Generating Station — Wikimedia Commons, CC BY-SA 4.0 | pickering | [File page](https://commons.wikimedia.org/wiki/File:Pickering_Nuclear_Generating_Station_at_Beachfront_Park,_June_6_2026_(03)_(5-3_cropped).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | pinewood-toronto-studios | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | pizza-pizza-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | port-lands-flood-protection | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| YRT_PRESTO_tap_device_at_Finch_station.png | PRESTO tap device, Finch station — Wikimedia Commons, CC BY-SA 4.0 | presto-card | [File page](https://commons.wikimedia.org/wiki/File:YRT_PRESTO_tap_device_at_Finch_station.png) |
| Toronto_Pride_Parade_2007.jpg | Toronto Pride Parade — Wikimedia Commons, Creative Commons licensed | pride-toronto-festival | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Pride_Parade_2007.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | princes-gates | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Princess_Margaret_Hospital_Toronto_South_Building.JPG | Princess Margaret Cancer Centre, Toronto — Wikimedia Commons, Creative Commons licensed | princess-margaret-cancer-centre | [File page](https://commons.wikimedia.org/wiki/File:Princess_Margaret_Hospital_Toronto_South_Building.JPG) |
| Toronto_Public_Library_Runnymede_Branch_(4994916241).jpg | Toronto Public Library, Runnymede Branch — Wikimedia Commons, CC BY 2.0 | public-library | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Public_Library_Runnymede_Branch_(4994916241).jpg) |
| Ontario_Government_Buildings.JPG | Ontario Legislative Building, Queen's Park — Wikimedia Commons, Creative Commons licensed | queens-park | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Government_Buildings.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | raccoon-capital-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Canadian_Pacific_Railway_Building_plaque_69_Yonge_Street_Toronto_ON_M5E_1J1_Canada.jpg | Canadian Pacific Railway Building plaque, Toronto — Wikimedia Commons, CC BY-SA 4.0 | railways | [File page](https://commons.wikimedia.org/wiki/File:Canadian_Pacific_Railway_Building_plaque_69_Yonge_Street_Toronto_ON_M5E_1J1_Canada.jpg) |
| Toronto_Raptors_2019_parade_photo_by_Djuradj_Vujcic.jpg | Toronto Raptors championship parade, 2019 — Djuradj Vujcic, CC BY 2.0 | raptors-2019 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Raptors_2019_parade_photo_by_Djuradj_Vujcic.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | raptors-founding-1995 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg | East Don Parkland — Wikimedia Commons, CC BY-SA 4.0 | ravines | [File page](https://commons.wikimedia.org/wiki/File:East_Don_Parkland_-_Pedestrian_bridge_over_the_Don_River_-_20200529.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | rc-harris-water-treatment-plant | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toward_Regent_Park_from_Merchandise_Roof.jpg | Regent Park, Toronto — Wikimedia Commons, public domain | regent-park | [File page](https://commons.wikimedia.org/wiki/File:Toward_Regent_Park_from_Merchandise_Roof.jpg) |
| Ismaili_Centre,_Toronto_-_Prayer_hall.jpg | Ismaili Centre, Toronto, prayer hall — Wikimedia Commons, CC BY-SA 4.0 | religion | [File page](https://commons.wikimedia.org/wiki/File:Ismaili_Centre,_Toronto_-_Prayer_hall.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | rexdale | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Town_of_Richmond_Hill.JPG | Richmond Hill, Ontario — Wikimedia Commons, Creative Commons licensed | richmond-hill | [File page](https://commons.wikimedia.org/wiki/File:Town_of_Richmond_Hill.JPG) |
| RiverdaleFarm.jpg | Riverdale Farm, Toronto — Wikimedia Commons, Creative Commons licensed | riverdale-farm | [File page](https://commons.wikimedia.org/wiki/File:RiverdaleFarm.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | riverdale-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | rl-hearn-generating-station | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg | Toronto City Hall — Wikimedia Commons, CC BY 2.0 | rob-ford | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_and_Toronto_City_Hall_(29944923803).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | robarts-library | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | robertson-davies-massey-college | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg | Rogers Centre — Wikimedia Commons, Creative Commons licensed | rogers-centre | [File page](https://commons.wikimedia.org/wiki/File:Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | rogers-communications | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Michael_Lee-Chin_Crystal,_Daniel_Libeskind,_2007_-_Royal_Ontario_Museum,_Toronto_(1277497687).jpg | Michael Lee-Chin Crystal, ROM — Wikimedia Commons, CC BY-SA 2.0 | rom | [File page](https://commons.wikimedia.org/wiki/File:Michael_Lee-Chin_Crystal,_Daniel_Libeskind,_2007_-_Royal_Ontario_Museum,_Toronto_(1277497687).jpg) |
| Toronto_Roncesvalles_Village_Village_Roncesvalles_de_Toronto_(24317099177).jpg | Roncesvalles Avenue, Toronto — Wikimedia Commons, Creative Commons licensed | roncesvalles | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Roncesvalles_Village_Village_Roncesvalles_de_Toronto_(24317099177).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | roots-canada | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | rosedale | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Rouge_National_Urban_Park-_Orchard_and_Vista_Trails-Toronto-Ontario_(1).jpg | Rouge National Urban Park, Toronto — Wikimedia Commons, Creative Commons licensed | rouge-national-urban-park | [File page](https://commons.wikimedia.org/wiki/File:Rouge_National_Urban_Park-_Orchard_and_Vista_Trails-Toronto-Ontario_(1).jpg) |
| Toronto_-_ON_-_Roy_Thomson_Hall.jpg | Roy Thomson Hall, Toronto — Wikimedia Commons, Creative Commons licensed | roy-thomson-hall | [File page](https://commons.wikimedia.org/wiki/File:Toronto_-_ON_-_Roy_Thomson_Hall.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | royal-alexandra-theatre | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | rush-band-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | ryerson-tmu-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| City_Hall,_Toronto,_Ontario.jpg | Toronto City Hall — Wikimedia Commons, CC BY 2.0 | safety | [File page](https://commons.wikimedia.org/wiki/File:City_Hall,_Toronto,_Ontario.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | salsa-on-st-clair | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | sars-outbreak | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | scadding-cabin | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Scarborough_Bluffs,_May_4_2026_(07).jpg | Scarborough Bluffs — Wikimedia Commons, CC BY-SA 4.0 | scarborough | [File page](https://commons.wikimedia.org/wiki/File:Scarborough_Bluffs,_May_4_2026_(07).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | scarborough-bluffs-erosion | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | scarborough-rt | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | scarborough-town-centre | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Scotia_Plaza,_Toronto,_Ontario_(21814386916).jpg | Scotia Plaza, Toronto — Wikimedia Commons, Creative Commons licensed | scotia-plaza | [File page](https://commons.wikimedia.org/wiki/File:Scotia_Plaza,_Toronto,_Ontario_(21814386916).jpg) |
| Scotiabank_Arena.jpg | Scotiabank Arena, Toronto — Wikimedia Commons, CC BY-SA 4.0 | scotiabank-arena | [File page](https://commons.wikimedia.org/wiki/File:Scotiabank_Arena.jpg) |
| Former_Port_Perry_Town_Hall.JPG | Former Port Perry Town Hall — Wikimedia Commons, Creative Commons licensed | scugog-port-perry | [File page](https://commons.wikimedia.org/wiki/File:Former_Port_Perry_Town_Hall.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | second-cup | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Humber_College_North_Campus_Aerial_view_2023.jpg | Humber College North Campus — Canmenwalker, Wikimedia Commons, CC BY 4.0 | seneca-centennial-humber | [File page](https://commons.wikimedia.org/wiki/File:Humber_College_North_Campus_Aerial_view_2023.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | shopify-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Shoppers_Drug_Mart_headquarters_building.jpg | Shoppers Drug Mart head office — Jonathan Schilling, CC BY-SA 4.0 | shoppers-drug-mart | [File page](https://commons.wikimedia.org/wiki/File:Shoppers_Drug_Mart_headquarters_building.jpg) |
| Flight_stop.jpg | Flight Stop, Toronto Eaton Centre — Wikimedia Commons, Creative Commons licensed | shopping-malls | [File page](https://commons.wikimedia.org/wiki/File:Flight_stop.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | sickkids-hospital | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Ontario_Government_Buildings.JPG | Ontario Legislative Building, Queen's Park — Wikimedia Commons, Creative Commons licensed | siu-ontario | [File page](https://commons.wikimedia.org/wiki/File:Ontario_Government_Buildings.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | snow-army-1999 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | soulpepper-theatre | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | south-asian-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | spadina-garment-district | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Spadina_House.JPG | Spadina House, Toronto — Wikimedia Commons, Creative Commons licensed | spadina-museum | [File page](https://commons.wikimedia.org/wiki/File:Spadina_House.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | spanish-flu-toronto-1918 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| 299_Queen_Street_West,_Toronto,_Ontario,_Canada.jpg | 299 Queen Street West, Toronto — Wikimedia Commons, CC BY 2.0 | speakers-corner | [File page](https://commons.wikimedia.org/wiki/File:299_Queen_Street_West,_Toronto,_Ontario,_Canada.jpg) |
| Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg | Rogers Centre — Wikimedia Commons, Creative Commons licensed | sports | [File page](https://commons.wikimedia.org/wiki/File:Rogers_Centre,_Toronto,_Ontario_(21652480228).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | st-james-cathedral | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | st-james-town | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_-_ON_-_St_Lawrence_Market.jpg | St. Lawrence Market — Wikimedia Commons, Creative Commons licensed | st-lawrence-market | [File page](https://commons.wikimedia.org/wiki/File:Toronto_-_ON_-_St_Lawrence_Market.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | st-michaels-cathedral-basilica | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg | Toronto General Hospital — Wikimedia Commons, Creative Commons licensed | stem-cell-discovery | [File page](https://commons.wikimedia.org/wiki/File:Toronto_General_Hospital,_Toronto,_Ontario_(30003270175).jpg) |
| A_PCC_streetcar_in_Toronto,_in_1980_-a.jpg | TTC PCC streetcar, 1980 — Wikimedia Commons, Creative Commons licensed | streetcar-network | [File page](https://commons.wikimedia.org/wiki/File:A_PCC_streetcar_in_Toronto,_in_1980_-a.jpg) |
| Pillar_at_Museum_Station,_TTC,_Toronto_-e.jpg | Pillar at Museum Station, TTC — Wikimedia Commons, Creative Commons licensed | subway-art | [File page](https://commons.wikimedia.org/wiki/File:Pillar_at_Museum_Station,_TTC,_Toronto_-e.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | sugar-beach | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| North_Toronto_Station_(3375761997).jpg | North Toronto Station — Wikimedia Commons, Creative Commons licensed | summerhill | [File page](https://commons.wikimedia.org/wiki/File:North_Toronto_Station_(3375761997).jpg) |
| Sunnybrook_Park_2023.jpg | Sunnybrook Park, Toronto — Wikimedia Commons, Creative Commons licensed | sunnybrook-park | [File page](https://commons.wikimedia.org/wiki/File:Sunnybrook_Park_2023.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | sunnyside-amusement-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | swansea | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | tarragon-theatre | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto-Dominion_Centre_in_Toronto_1973.jpg | Toronto-Dominion Centre, 1973 — Wikimedia Commons, Creative Commons licensed | td-centre | [File page](https://commons.wikimedia.org/wiki/File:Toronto-Dominion_Centre_in_Toronto_1973.jpg) |
| Jarvis_CI.JPG | Jarvis Collegiate Institute — Simon Pulsifer, Wikimedia Commons, CC BY-SA 3.0 | tdsb-history | [File page](https://commons.wikimedia.org/wiki/File:Jarvis_CI.JPG) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | tech-scene | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | the-519 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | the-annex | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| The_Beaches_aerial_view_2023.jpg | The Beaches, Toronto — Canmenwalker, CC BY 4.0 | the-beaches | [File page](https://commons.wikimedia.org/wiki/File:The_Beaches_aerial_view_2023.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | the-bentway | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | the-grange-ago | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | the-junction | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | the-weeknd-scarborough | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | thorncliffe-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| 2013_Toronto_Film_Festival_August_29_(9737565818).jpg | Toronto International Film Festival, 2013 — Wikimedia Commons, Creative Commons licensed | tiff-festival-history | [File page](https://commons.wikimedia.org/wiki/File:2013_Toronto_Film_Festival_August_29_(9737565818).jpg) |
| TIFF_Bell_Lightbox_Founder_Lounge_2023.jpg | TIFF Bell Lightbox — Wikimedia Commons, CC BY 4.0 | tiff-lightbox | [File page](https://commons.wikimedia.org/wiki/File:TIFF_Bell_Lightbox_Founder_Lounge_2023.jpg) |
| Tim_Hortons_on_Yonge_between_Dundas_and_Shuter,_Toronto_-a.jpg | Tim Hortons, Yonge Street, Toronto — Wikimedia Commons, Creative Commons licensed | tim-hortons-toronto | [File page](https://commons.wikimedia.org/wiki/File:Tim_Hortons_on_Yonge_between_Dundas_and_Shuter,_Toronto_-a.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | timothy-eaton | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Todmorden_Mills_Toronto.JPG | Todmorden Mills, Toronto — Wikimedia Commons, Creative Commons licensed | todmorden-mills | [File page](https://commons.wikimedia.org/wiki/File:Todmorden_Mills_Toronto.JPG) |
| Toronto_skyline_from_the_Leslie_Street_Spit.jpg | Leslie Street Spit, Toronto — Wikimedia Commons, Creative Commons licensed | tommy-thompson-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_from_the_Leslie_Street_Spit.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | toronto-arenas-1917 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Etobicoke_School_of_the_Arts.jpg | Etobicoke School of the Arts — Wikimedia Commons, CC BY-SA 3.0 | toronto-arts-high-schools | [File page](https://commons.wikimedia.org/wiki/File:Etobicoke_School_of_the_Arts.jpg) |
| Bay_Street,_Financial_District,_Toronto,_Ontario_(29708936890).jpg | Bay Street, Financial District, Toronto — Ken Lund, CC BY 2.0 | toronto-big-five-banks | [File page](https://commons.wikimedia.org/wiki/File:Bay_Street,_Financial_District,_Toronto,_Ontario_(29708936890).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-catholic-district-school-board | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Christmas_Market_2018_clock.jpg | Toronto Christmas Market, 2018 — Jason Zhang, CC BY-SA 3.0 | toronto-christmas-market | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Christmas_Market_2018_clock.jpg) |
| Glenn_Gould_and_Alberto_Guerrero.jpg | Glenn Gould and Alberto Guerrero — Library and Archives Canada, public domain | toronto-classical-music | [File page](https://commons.wikimedia.org/wiki/File:Glenn_Gould_and_Alberto_Guerrero.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-craft-distilleries | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-fc-2017-treble | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| BMO_Field,_Toronto,_Ontario_(29969149766).jpg | BMO Field, Toronto — Wikimedia Commons, Creative Commons licensed | toronto-fc-founding | [File page](https://commons.wikimedia.org/wiki/File:BMO_Field,_Toronto,_Ontario_(29969149766).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-food-trucks | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-general-hospital | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Harbour_from_Harbour_Square_Park.jpg | Toronto Harbour — Wikimedia Commons, CC BY-SA 4.0 | toronto-harbour | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Harbour_from_Harbour_Square_Park.jpg) |
| Maestro_Fresh_Wes_live_in_2023.jpg | Maestro Fresh Wes, 2023 — Wikimedia Commons, Creative Commons licensed | toronto-hip-hop-before-drake | [File page](https://commons.wikimedia.org/wiki/File:Maestro_Fresh_Wes_live_in_2023.jpg) |
| Manhole_cover_reading_Toronto_Hydro_Electric_System,_Toronto,_Ontario,_2025-08-25.jpg | Toronto Hydro Electric System manhole cover — Wikimedia Commons, CC BY-SA 4.0 | toronto-hydro | [File page](https://commons.wikimedia.org/wiki/File:Manhole_cover_reading_Toronto_Hydro_Electric_System,_Toronto,_Ontario,_2025-08-25.jpg) |
| Jack-Layton-Ferry-Terminal-2025-04-09.jpg | Jack Layton Ferry Terminal, Toronto — Wikimedia Commons, CC BY-SA 4.0 | toronto-islands-ferry | [File page](https://commons.wikimedia.org/wiki/File:Jack-Layton-Ferry-Terminal-2025-04-09.jpg) |
| Oscar_Peterson_-_1950.JPG | Oscar Peterson, 1950 — Wikimedia Commons, public domain | toronto-jazz-history | [File page](https://commons.wikimedia.org/wiki/File:Oscar_Peterson_-_1950.JPG) |
| Toronto_Marlies_faceoff.jpg | Toronto Marlies — Wikimedia Commons, Creative Commons licensed | toronto-marlies | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Marlies_faceoff.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | toronto-pizza-scene | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| BADGE_-_Canada_-_ON_-_Metropolitan_Toronto_Police_(gilt)_(7906373948).jpg | Metropolitan Toronto Police badge — Wikimedia Commons, Creative Commons licensed | toronto-police-founding | [File page](https://commons.wikimedia.org/wiki/File:BADGE_-_Canada_-_ON_-_Metropolitan_Toronto_Police_(gilt)_(7906373948).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-purchase | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-railway-company | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg | Maple Leaf Gardens, Toronto — Wikimedia Commons, Creative Commons licensed | toronto-rock-lacrosse | [File page](https://commons.wikimedia.org/wiki/File:Maple_Leaf_Gardens_-_50_Carlton_Street,_Toronto,_ON_M5B_1J2,_Canada.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-sceptres-pwhl | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-sign-nathan-phillips | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Star_Building_1929.JPG | Old Toronto Star Building, 1929 — Wikimedia Commons, public domain | toronto-star-legacy | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Star_Building_1929.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-stock-exchange | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-sun-history | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-symphony-orchestra | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-telegram | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_City_Hall_Council_Chamber_(30461915762).jpg | Toronto City Hall council chamber — Wikimedia Commons, CC BY 2.0 | toronto-ward-structure | [File page](https://commons.wikimedia.org/wiki/File:Toronto_City_Hall_Council_Chamber_(30461915762).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-western-hospital | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | toronto-wolfpack | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_zoo_monorail.jpg | Toronto Zoo — Wikimedia Commons, CC BY 2.0 | toronto-zoo | [File page](https://commons.wikimedia.org/wiki/File:Toronto_zoo_monorail.jpg) |
| CLRV_TTC_Streetcar_No_4004_(8063115473).jpg | TTC streetcar — Peter Broster, CC BY 2.0 | transit | [File page](https://commons.wikimedia.org/wiki/File:CLRV_TTC_Streetcar_No_4004_(8063115473).jpg) |
| Trinity_Bellwoods_Gates.jpg | Trinity Bellwoods gates, Toronto — Wikimedia Commons, Creative Commons licensed | trinity-bellwoods-park | [File page](https://commons.wikimedia.org/wiki/File:Trinity_Bellwoods_Gates.jpg) |
| Pillar_at_Museum_Station,_TTC,_Toronto_-e.jpg | TTC subway station, Toronto — Wikimedia Commons, Creative Commons licensed | ttc-subway-safety | [File page](https://commons.wikimedia.org/wiki/File:Pillar_at_Museum_Station,_TTC,_Toronto_-e.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | tvo | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | ubisoft-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Union_Station_grand_hall.jpg | Union Station Great Hall — Wikimedia Commons, CC BY 2.0 | union-station | [File page](https://commons.wikimedia.org/wiki/File:Union_Station_grand_hall.jpg) |
| UP_Express_at_Weston_P6143108.jpg | UP Express at Weston Station, Toronto — Wikimedia Commons, Creative Commons licensed | up-express | [File page](https://commons.wikimedia.org/wiki/File:UP_Express_at_Weston_P6143108.jpg) |
| Uxbridge_downtown.jpg | Downtown Uxbridge, Ontario — Wikimedia Commons, CC BY 2.0 | uxbridge | [File page](https://commons.wikimedia.org/wiki/File:Uxbridge_downtown.jpg) |
| Ravine_footbridge_David_A_Balfour_Park.jpg | David A. Balfour Park ravine, Toronto — Wikimedia Commons, Creative Commons licensed | vale-of-avoca | [File page](https://commons.wikimedia.org/wiki/File:Ravine_footbridge_David_A_Balfour_Park.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | varsity-stadium | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| WindSeeker_at_Canada's_Wonderland,_August_2018_(3).jpg | Canada's Wonderland, Vaughan — Wikimedia Commons, CC BY-SA 3.0 | vaughan | [File page](https://commons.wikimedia.org/wiki/File:WindSeeker_at_Canada's_Wonderland,_August_2018_(3).jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | vector-institute | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Toronto-CN-tower-and-Canadian-flag-skyline.jpg | Toronto skyline — Wikimedia Commons, CC BY-SA 4.0 | video-games | [File page](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | vietnamese-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | vince-carter-raptors | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | warden-woods-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | wards-island-community | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| RC_Harris_Water_Treatment_Plant_2009.jpg | R.C. Harris Water Treatment Plant — Wikimedia Commons, CC BY 2.0 | water-treatment | [File page](https://commons.wikimedia.org/wiki/File:RC_Harris_Water_Treatment_Plant_2009.jpg) |
| Harbourfront,_Toronto,_Ontario_from_CN_Tower_(21652107550).jpg | Toronto Harbourfront — Wikimedia Commons, Creative Commons licensed | waterfront | [File page](https://commons.wikimedia.org/wiki/File:Harbourfront,_Toronto,_Ontario_from_CN_Tower_(21652107550).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | wattpad-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | wealthsimple-toronto | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline — Wikimedia Commons, CC BY 2.0 | weather | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | west-don-lands | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | weston-village | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Remembrance_Day_2014_in_Whitby,_Ontario.jpg | Downtown Whitby — Wikimedia Commons, CC BY 2.0 | whitby | [File page](https://commons.wikimedia.org/wiki/File:Remembrance_Day_2014_in_Whitby,_Ontario.jpg) |
| Stouffville_Civic_Square_-_Stouffville,_ON.jpg | Stouffville Civic Square — Wikimedia Commons, CC BY-SA 4.0 | whitchurch-stouffville | [File page](https://commons.wikimedia.org/wiki/File:Stouffville_Civic_Square_-_Stouffville,_ON.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | william-james-photographs | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_Nathan_Phillips_Square_Christmas_tree_(16103747613).jpg | Nathan Phillips Square Christmas tree — Wikimedia Commons, Creative Commons licensed | winter-festivals | [File page](https://commons.wikimedia.org/wiki/File:Toronto_Nathan_Phillips_Square_Christmas_tree_(16103747613).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | winter-stations | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Tom_Jones_Restaurant,_next_to_the_King_Edward_Hotel,_downtown_Toronto_-d.jpg | Downtown Toronto restaurant — Wikimedia Commons, public domain | winterlicious-summerlicious | [File page](https://commons.wikimedia.org/wiki/File:Tom_Jones_Restaurant,_next_to_the_King_Edward_Hotel,_downtown_Toronto_-d.jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | withrow-park | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | womens-college-hospital | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Woodbine_Racetrack.jpg | Woodbine Racetrack — Wikimedia Commons, CC BY-SA 4.0 | woodbine-racetrack | [File page](https://commons.wikimedia.org/wiki/File:Woodbine_Racetrack.jpg) |
| Harbourfront_Centre.JPG | Harbourfront Centre, Toronto — Wikimedia Commons, CC BY-SA 3.0 | word-on-the-street | [File page](https://commons.wikimedia.org/wiki/File:Harbourfront_Centre.JPG) |
| Osgoode_Hall.JPG | Osgoode Hall — Wikimedia Commons, CC BY-SA 3.0 | wrongful-convictions-ontario | [File page](https://commons.wikimedia.org/wiki/File:Osgoode_Hall.JPG) |
| Wychwood_Barns.JPG | Artscape Wychwood Barns — Wikimedia Commons, CC BY-SA 3.0 | wychwood | [File page](https://commons.wikimedia.org/wiki/File:Wychwood_Barns.JPG) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | yonge-street-longest-street-myth | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | yonge-street-riot-1992 | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Toronto_skyline_(2012).jpg | Toronto skyline, 2012 — Wikimedia Commons, CC BY 2.0 | yonge-street-van-attack | [File page](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Weston_Park_2018_07.jpg | Weston Park, Toronto — Wikimedia Commons, CC BY-SA 4.0 | york | [File page](https://commons.wikimedia.org/wiki/File:Weston_Park_2018_07.jpg) |
| Village_of_Yorkville_Park_2022.jpg | Village of Yorkville Park — Wikimedia Commons, Creative Commons licensed | yorkville | [File page](https://commons.wikimedia.org/wiki/File:Village_of_Yorkville_Park_2022.jpg) |
| Bruce_Cockburn_2007.jpg | Bruce Cockburn, 2007 — Wikimedia Commons, CC BY 2.0 | yorkville-folk-scene | [File page](https://commons.wikimedia.org/wiki/File:Bruce_Cockburn_2007.jpg) |
| Kesho_Park_at_the_Toronto_Zoo_(3354803789).jpg | Kesho Park, Toronto Zoo — Wikimedia Commons, CC BY 2.0 | zoo-science-centre | [File page](https://commons.wikimedia.org/wiki/File:Kesho_Park_at_the_Toronto_Zoo_(3354803789).jpg) |

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
