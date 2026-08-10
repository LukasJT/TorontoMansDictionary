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

| Image | Photographer | License | Source |
|---|---|---|---|
| CN Tower & skyline (hero) | Wikimedia Commons contributor | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | [File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg](https://commons.wikimedia.org/wiki/File:Toronto-CN-tower-and-Canadian-flag-skyline.jpg) |
| Toronto skyline (2012) | Wikimedia Commons contributor | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | [File:Toronto skyline (2012).jpg](https://commons.wikimedia.org/wiki/File:Toronto_skyline_(2012).jpg) |
| Kensington Market, Aug 2017 | Arild Vågen | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | [File:Kensington Market Toronto August 2017 03.jpg](https://commons.wikimedia.org/wiki/File:Kensington_Market_Toronto_August_2017_03.jpg) |
| TTC CLRV Streetcar No. 4004 | Peter Broster | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | [File:CLRV TTC Streetcar No 4004 (8063115473).jpg](https://commons.wikimedia.org/wiki/File:CLRV_TTC_Streetcar_No_4004_(8063115473).jpg) |

Images are loaded directly from Wikimedia Commons via `Special:FilePath`
(a stable MediaWiki redirect to the current full-resolution file) rather than
bundled into the repo, so credit and licensing always stay attached to the
original file page.

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
