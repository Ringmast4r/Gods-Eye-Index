<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:166534&height=220&section=header&text=GODS%20EYE%20INDEX&fontSize=64&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=3%20projects%20%7C%20114%2C660%20combined%20stars%20%7C%2026%20shared%20feeds%20%7C%20tracked%2C%20not%20starred&descSize=18&descAlignY=58"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=22C55E&center=true&vCenter=true&multiline=true&repeat=true&width=950&height=80&lines=Every+God%27s+Eye+style+world+map+in+one+list.;World+Monitor+%C2%B7+God%27s+Eye+View+%C2%B7+OSIRIS+%C2%B7+and+the+rest;Tracked+here+so+I+don%27t+have+to+star+them+all.)](https://git.io/typing-svg)

<br>

[![Projects](https://img.shields.io/badge/Projects-3-166534?style=for-the-badge&logo=github&logoColor=white)](#-ls---core)
[![Combined stars](https://img.shields.io/badge/Combined_stars-114%2C660-22C55E?style=for-the-badge&logo=github&logoColor=white)](#-stats---live)
[![Keyless feeds](https://img.shields.io/badge/Keyless_feeds-17_of_26-000000?style=for-the-badge&logo=rss&logoColor=white)](#-cat-feedstxt)
[![Refreshed](https://img.shields.io/badge/Refreshed-2026-09-09-166534?style=for-the-badge&logo=githubactions&logoColor=white)](#-refresh)

[![Stars](https://img.shields.io/github/stars/Ringmast4r/Gods-Eye-Index?style=flat-square&color=166534&label=%E2%98%85%20Stars)](https://github.com/Ringmast4r/Gods-Eye-Index/stargazers)
[![Forks](https://img.shields.io/github/forks/Ringmast4r/Gods-Eye-Index?style=flat-square&color=22C55E&label=%E2%9A%A1%20Forks)](https://github.com/Ringmast4r/Gods-Eye-Index/network/members)
[![Repo Size](https://img.shields.io/github/repo-size/Ringmast4r/Gods-Eye-Index?style=flat-square&color=000000)](#)
[![Last Commit](https://img.shields.io/github/last-commit/Ringmast4r/Gods-Eye-Index?style=flat-square&color=166534)](https://github.com/Ringmast4r/Gods-Eye-Index/commits/main)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Ringmast4r.Gods-Eye-Index)](#)

<img src="assets/logo.svg" alt="Gods Eye Index" width="220">

</div>

---

## `> what_is_this`

```bash
you@github:~$ cat gods-eye-index.txt

  PURPOSE:        One list of every "God's Eye" style live world-map / intel dashboard on GitHub
  TRACKED:        3 projects, all active, all in the thousands of stars
  COMBINED:       114,660 stars across the tracked set
  FEEDS:          26 shared upstream data sources, 17 of them keyless
  SOURCE:         data/projects.db is the truth; README is generated from it
  REFRESHED:      2026-09-09 06:06 UTC
  STATUS:         [ ACTIVE ]
```

> In August 2026 "spy satellite simulator in your browser" repos took over GitHub Trending. This index tracks the ones that matter, with live stars, what each one actually does, what it is built on, and which upstream feeds they share. Small clones, forks and rebrands are left out on purpose.

---

## `> stats --live`

<div align="center">

| # | PROJECT | STARS | FORKS | ISSUES | LICENSE | LANG | PUSHED | STATUS |
|:-:|:--------|------:|------:|-------:|:-------:|:----:|:------:|:------:|
| 1 | [World Monitor](https://github.com/koala73/worldmonitor) | `85,870` | `12,978` | `285` | AGPL-3.0 | TypeScript | 2026-09-09 | `active` |
| 2 | [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) | `19,826` | `4,057` | `144` | MIT (code) | JavaScript | 2026-09-05 | `active` |
| 3 | [OSIRIS](https://github.com/simplifaisoul/osiris) | `8,964` | `1,835` | `9` | MIT | TypeScript | 2026-09-09 | `active` |

</div>

`active` = pushed in the last 30 days, `quiet` = 120, `stale` = older. 3 of 3 are active as of 2026-09-09.

---

## `> ls --core`

Active and massive. Forks, rebrands, dead clones and same-name projects are deliberately not listed; if it is not pushing commits and pulling thousands of stars it does not belong here.

### [World Monitor](https://github.com/koala73/worldmonitor)

`85,870 stars` · `AGPL-3.0` · `TypeScript` · `pushed 2026-09-09` · `active` · [worldmonitor.app](https://worldmonitor.app)

**The reference project: 500+ news feeds, 56 layer types, AI briefs, dual globe/flat engine, Tauri desktop, MCP server + REST + SDKs.**

Started January 2026 as one developer's personal dashboard and became the biggest project in the category. Vanilla TypeScript + Vite; globe.gl/Three.js for the 3D globe and deck.gl/MapLibre for the flat map, sharing one layer catalog. Ingests 500+ curated RSS feeds across 15 categories and synthesizes them into AI briefs (Ollama locally, or Groq/OpenRouter; Transformers.js in the browser for classification). Adds a Country Instability Index for 31 Tier-1 countries, a 7-signal finance radar, cross-stream correlation (military + market + disaster signals converging), six site variants (world, tech, finance, commodity, happy, energy) from one codebase, a Tauri 2 desktop app, and a programmatic surface: MCP server, REST API, npm CLI, Python/Ruby/Go SDKs. Flights come from Wingbits. Deploys to Vercel Edge with Upstash Redis and a 3-tier cache. Paid Pro tier gates API keys, longer history and premium layers.

| | |
|:--|:--|
| **Engine** | globe.gl + Three.js (3D), deck.gl + MapLibre GL (flat) |
| **Basemap** | vector tiles |
| **Backend** | Vercel Edge Functions, Railway relay, Upstash Redis |
| **Stores history** | no (Pro tier sells longer history) |
| **Keyless start** | yes, runs with no env vars |
| **Layers** | news (500+ feeds), conflicts, military + civil aviation, maritime AIS, undersea cables, infrastructure, markets / crypto / commodities, climate hazards, cyber signals, CII risk scores |
| **Keys** | none required; ACLED, Groq/OpenRouter and other feature keys optional; Pro key for MCP tools/call |
| **Weak spots** | keys reset on exit (desktop); Node sidecar missing on some machines breaks panels; Linux black screen; layout shift on load; browser T5 summaries unreliable; ACLED token rejections; Pro paywall creep |

### [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view)

`19,826 stars` · `MIT (code)` · `JavaScript` · `pushed 2026-09-05` · `active` · [maptheworld.ai](https://maptheworld.ai/)

**The cinematic one: CesiumJS + Google Photorealistic 3D Tiles, cockpit ride-alongs, FLIR/NVG sensor modes, voice agent. Keyless start on Esri imagery.**

Bilawal Sidhu's "spy satellite simulator in your browser, except the data is real." Vanilla JavaScript + Vite on CesiumJS: Google Photorealistic 3D Tiles when you bring a key, Esri World Imagery + Re:Earth terrain when you don't. Hit #1 on GitHub Trending in August 2026 after the MIT release. Live layers: flights (OpenSky with an adsb.lol fallback), military tracks (adsb.lol), vessels (AISStream key), satellites (CelesTrak + SGP4), earthquakes (USGS), traffic simulated along real OSM roads (TomTom optional), public CCTV (Austin, Caltrans, TfL), internet radio, bikeshare (GBFS), active fires (FIRMS key), launches (Launch Library 2). Bundled static data: ~4.3k datacenters, 704 dams, TeleGeography submarine cables (CC BY-NC-SA, carved out of the MIT license). Signature features: ride inside any tracked flight with the terrain held under you, a 250 km contacts roster, sensor styles, and voice control via the OpenAI Realtime API. Private keys route through a hardened server-side proxy with SSRF protection and per-provider budgets. No persistence at all; the README says it outright: "the present is the cheap part. The moment you try to go back in time the data gets expensive." Requires Node 24.14+ or 26.

| | |
|:--|:--|
| **Engine** | CesiumJS |
| **Basemap** | Google Photorealistic 3D Tiles (key) or Esri World Imagery (keyless) |
| **Backend** | Vite dev server + Node proxy for keyed providers |
| **Stores history** | no |
| **Keyless start** | yes (Esri imagery; flights, mil, sats, quakes, cams, radio, launches all keyless) |
| **Layers** | flights, military flights, vessels, satellites, earthquakes, traffic, CCTV, radio, bikeshare, fires, launches, datacenters, dams, submarine cables |
| **Keys** | none to start; optional Cesium ion, Google Maps, AISStream, FIRMS, TomTom, OpenAI, LL2 token |
| **Weak spots** | Google 3D unavailable in some regions (EEA); key setup confusion; npm install failures from the Node 24 floor; "AI slop" complaints about the volume of generated docs and QA scripts; no place search without a Google key; no weather layer |

### [OSIRIS](https://github.com/simplifaisoul/osiris)

`8,964 stars` · `MIT` · `TypeScript` · `pushed 2026-09-09` · `active` · [osirisai.live](https://osirisai.live)

**Next.js 16 + MapLibre "Palantir alternative": 16 layers plus a RECON toolkit (port scan, WHOIS, CVE, crypto wallet + OFAC checks) and Telegram geoparsing.**

Open Source Intelligence & Reconnaissance Integrated System. Next.js 16 + TypeScript with MapLibre GL rendering every entity through WebGL. Layers: OpenSky aviation split into commercial / private / military, 17,000+ CCTV cameras (TfL, WSDOT, Caltrans, ODOT, MDOT, Hong Kong, Taiwan, NZTA), USGS quakes, FIRMS fires, NASA EONET severe events, NOAA SWPC + N2YO space, NVD CVEs, 25+ live 24/7 broadcaster streams pinned to the map, 39 ports and 10 chokepoints as static maritime intel, 13 hand-curated conflict zones, and a Telegram layer that scrapes public t.me/s/ previews and geoparses posts in English, Cyrillic and Arabic. The RECON toolkit is the differentiator: TCP port scanner, DNS, WHOIS, SSL inspector, IP intel, CVE lookup, BTC/ETH wallet tracing with OFAC SDN cross-checks via OpenSanctions. Polling was relaxed to 15-30 minute intervals to cut Vercel edge requests by 75%. The repo description embeds a pump.fun token address, so there is a memecoin attached.

| | |
|:--|:--|
| **Engine** | MapLibre GL (WebGL) |
| **Basemap** | vector tiles |
| **Backend** | Next.js API routes as proxies, in-memory caches |
| **Stores history** | no |
| **Keyless start** | mostly; OpenSky anonymous, FIRMS and N2YO need keys |
| **Layers** | aviation, CCTV, earthquakes, fires, news streams, weather events, space weather + satellites, CVEs, conflict zones (static), ports + chokepoints (static), crypto/sanctions, Telegram posts |
| **Keys** | FIRMS, N2YO; OpenSky optional; everything else keyless |
| **Weak spots** | conflict zones and maritime are hand-typed lists, not feeds; memecoin attached to the project; edge-request costs drove slow polling |

---

## `> diff --core`

| | **World Monitor** | **God's Eye View** | **OSIRIS** |
|:--|:--|:--|:--|
| Engine | globe.gl + Three.js (3D), deck.gl + MapLibre GL (flat) | CesiumJS | MapLibre GL (WebGL) |
| Basemap | vector tiles | Google Photorealistic 3D Tiles (key) or Esri World Imagery (keyless) | vector tiles |
| Backend | Vercel Edge Functions, Railway relay, Upstash Redis | Vite dev server + Node proxy for keyed providers | Next.js API routes as proxies, in-memory caches |
| Stores history | no (Pro tier sells longer history) | no | no |
| Keyless start | yes, runs with no env vars | yes (Esri imagery; flights, mil, sats, quakes, cams, radio, launches all keyless) | mostly; OpenSky anonymous, FIRMS and N2YO need keys |
| License | AGPL-3.0 | MIT (code) | MIT |
| Stars | `85,870` | `19,826` | `8,964` |
| Signature | AI briefs + CII + MCP/SDKs | cockpit view + 3D tiles + voice | RECON toolkit + Telegram + OFAC |

**What none of them do:** keep history you own (every one is a live snapshot; God's Eye View's README says going back in time is "the expensive part"), show per-layer provenance and freshness on the map, or run fully self-hosted without a cloud edge / Redis / third-party key chain. City Monitor is the only one that writes to a database. Those gaps are the spec for the next one.

---

## `> cat feeds.txt`

The upstream sources the whole category is built on. Same feeds, different chrome.

| FEED | DOMAIN | KEY | USED BY |
|:-----|:-------|:----|:--------|
| [Google Photorealistic 3D Tiles](https://developers.google.com/maps/documentation/tile) | 3D basemap | metered key | GEV |
| [NVD](https://nvd.nist.gov/developers) | CVEs | none (rate-limited) | OSR |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/) | active fires | free MAP_KEY | GEV, OSR |
| [GBFS](https://gbfs.org) | bikeshare | none | GEV |
| [ACLED](https://acleddata.com) | conflict events | registration key | WM |
| [GDACS](https://www.gdacs.org/gdacsapi/api/events/geteventlist/MAP) | disaster alerts | none | OSR |
| [USGS](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson) | earthquakes | none | WM, GEV, OSR |
| [OpenSky Network](https://opensky-network.org/api/states/all) | flights | none (anon, rate-limited; non-commercial license) | WM, GEV, OSR |
| [Wingbits](https://wingbits.com) | flights | partner | WM |
| [adsb.lol](https://api.adsb.lol/v2/mil) | flights + military | none (ODbL) | GEV |
| [GDELT](https://api.gdeltproject.org/api/v2/geo/geo) | geo-tagged news | none | GEV (fallback), OSR |
| [Radio Browser](https://api.radio-browser.info) | internet radio | none | GEV |
| [Launch Library 2](https://ll.thespacedevs.com/2.3.0/launches/upcoming/) | launches | none (15/hr anon) or token | GEV |
| [NASA EONET](https://eonet.gsfc.nasa.gov/api/v3/events?status=open) | natural events | none | OSR |
| [City CCTV (Austin, Caltrans, TfL, WSDOT...)](https://api.tfl.gov.uk) | public cameras | none | GEV, OSR |
| [OpenStreetMap Overpass](https://overpass-api.de) | roads, military sites | none (ODbL) | GEV |
| [OpenSanctions](https://www.opensanctions.org) | sanctions (OFAC SDN) | none (CC-BY) | OSR |
| [Esri World Imagery](https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer) | satellite basemap | none | GEV |
| [N2YO](https://www.n2yo.com/api/) | satellites | free key | OSR |
| [CelesTrak](https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json) | satellites (TLE) | none | GEV |
| [NOAA SWPC](https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json) | space weather | none | OSR |
| [TeleGeography](https://www.submarinecablemap.com) | submarine cables | bundled (CC BY-NC-SA) | GEV, WM |
| [Cesium ion](https://ion.cesium.com) | terrain / 3D | free token | GEV |
| [TomTom Traffic](https://developer.tomtom.com) | traffic flow | free key (200k tiles/mo) | GEV |
| [AISStream.io](https://aisstream.io) | vessels (AIS) | free key | GEV |
| [Open-Meteo](https://open-meteo.com) | weather | none | GEV |

WM = World Monitor, GEV = God's Eye View, OSR = OSIRIS

---

## `> refresh`

```bash
python scripts/seed.py           # rebuild tables from the curated lists in seed.py
python scripts/refresh.py        # live stars / forks / license / pushed_at via gh api
python scripts/build_readme.py   # regenerate this README from data/projects.db
```

Add a project: append a dict to `PROJECTS` in `scripts/seed.py`, run the three commands, commit. Never hand-edit the `.db` or this README.

---

## `> tree`

```
Gods-Eye-Index/
├── README.md              generated, do not edit
├── assets/logo.svg
├── data/projects.db       source of truth (projects, feeds, meta)
└── scripts/
    ├── seed.py            curated lists -> db
    ├── refresh.py         gh api -> live stats
    └── build_readme.py    db -> README.md
```

---

<div align="center">

**Maintained by** [@Ringmast4r](https://github.com/Ringmast4r) · stats via `gh api`, refreshed 2026-09-09 06:06 UTC

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:166534,100:000000&height=120&section=footer&text=WATCH%20THE%20WATCHERS&fontSize=18&fontColor=ffffff&fontAlignY=65"/>

</div>
