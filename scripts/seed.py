#!/usr/bin/env python3
"""Seed data/projects.db from the curated lists below.

This file is the editing surface. Add or fix a project here, then run:

    python scripts/seed.py        # rebuild the tables from this file
    python scripts/refresh.py     # pull live stars / forks / pushed_at from GitHub
    python scripts/build_readme.py

Never hand-edit the .db; it is regenerated from this script. Live stats
(stars, forks, pushed_at, license, ...) are filled by refresh.py and kept
across re-seeds.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "projects.db"

# tier: core = the ones that blew up | derivative = forks, ports, rebrands,
# bridges | small = independent small builds | namesake = same name, not a map
PROJECTS = [
    # ---------------------------------------------------------------- core
    dict(
        slug="koala73/worldmonitor",
        name="World Monitor",
        tier="core",
        summary="The reference project: 500+ news feeds, 56 layer types, AI briefs, "
        "dual globe/flat engine, Tauri desktop, MCP server + REST + SDKs.",
        overview=(
            "Started January 2026 as one developer's personal dashboard and became the "
            "biggest project in the category. Vanilla TypeScript + Vite; globe.gl/Three.js "
            "for the 3D globe and deck.gl/MapLibre for the flat map, sharing one layer "
            "catalog. Ingests 500+ curated RSS feeds across 15 categories and synthesizes "
            "them into AI briefs (Ollama locally, or Groq/OpenRouter; Transformers.js in the "
            "browser for classification). Adds a Country Instability Index for 31 Tier-1 "
            "countries, a 7-signal finance radar, cross-stream correlation (military + "
            "market + disaster signals converging), six site variants (world, tech, finance, "
            "commodity, happy, energy) from one codebase, a Tauri 2 desktop app, and a "
            "programmatic surface: MCP server, REST API, npm CLI, Python/Ruby/Go SDKs. "
            "Flights come from Wingbits. Deploys to Vercel Edge with Upstash Redis and a "
            "3-tier cache. Paid Pro tier gates API keys, longer history and premium layers."
        ),
        engine="globe.gl + Three.js (3D), deck.gl + MapLibre GL (flat)",
        basemap="vector tiles",
        backend="Vercel Edge Functions, Railway relay, Upstash Redis",
        stores_history="no (Pro tier sells longer history)",
        keyless_start="yes, runs with no env vars",
        layers=(
            "news (500+ feeds), conflicts, military + civil aviation, maritime AIS, "
            "undersea cables, infrastructure, markets / crypto / commodities, climate "
            "hazards, cyber signals, CII risk scores"
        ),
        keys="none required; ACLED, Groq/OpenRouter and other feature keys optional; Pro key for MCP tools/call",
        weak=(
            "keys reset on exit (desktop); Node sidecar missing on some machines breaks "
            "panels; Linux black screen; layout shift on load; browser T5 summaries "
            "unreliable; ACLED token rejections; Pro paywall creep"
        ),
        homepage="https://worldmonitor.app",
    ),
    dict(
        slug="bilawalsidhu/gods-eye-view",
        name="God's Eye View",
        tier="core",
        summary="The cinematic one: CesiumJS + Google Photorealistic 3D Tiles, cockpit "
        "ride-alongs, FLIR/NVG sensor modes, voice agent. Keyless start on Esri imagery.",
        overview=(
            "Bilawal Sidhu's \"spy satellite simulator in your browser, except the data is "
            "real.\" Vanilla JavaScript + Vite on CesiumJS: Google Photorealistic 3D Tiles "
            "when you bring a key, Esri World Imagery + Re:Earth terrain when you don't. "
            "Hit #1 on GitHub Trending in August 2026 after the MIT release. Live layers: "
            "flights (OpenSky with an adsb.lol fallback), military tracks (adsb.lol), "
            "vessels (AISStream key), satellites (CelesTrak + SGP4), earthquakes (USGS), "
            "traffic simulated along real OSM roads (TomTom optional), public CCTV "
            "(Austin, Caltrans, TfL), internet radio, bikeshare (GBFS), active fires "
            "(FIRMS key), launches (Launch Library 2). Bundled static data: ~4.3k "
            "datacenters, 704 dams, TeleGeography submarine cables (CC BY-NC-SA, carved "
            "out of the MIT license). Signature features: ride inside any tracked flight "
            "with the terrain held under you, a 250 km contacts roster, sensor styles, "
            "and voice control via the OpenAI Realtime API. Private keys route through a "
            "hardened server-side proxy with SSRF protection and per-provider budgets. No "
            "persistence at all; the README says it outright: \"the present is the cheap "
            "part. The moment you try to go back in time the data gets expensive.\" "
            "Requires Node 24.14+ or 26."
        ),
        engine="CesiumJS",
        basemap="Google Photorealistic 3D Tiles (key) or Esri World Imagery (keyless)",
        backend="Vite dev server + Node proxy for keyed providers",
        stores_history="no",
        keyless_start="yes (Esri imagery; flights, mil, sats, quakes, cams, radio, launches all keyless)",
        layers=(
            "flights, military flights, vessels, satellites, earthquakes, traffic, CCTV, "
            "radio, bikeshare, fires, launches, datacenters, dams, submarine cables"
        ),
        keys="none to start; optional Cesium ion, Google Maps, AISStream, FIRMS, TomTom, OpenAI, LL2 token",
        weak=(
            "Google 3D unavailable in some regions (EEA); key setup confusion; npm install "
            "failures from the Node 24 floor; \"AI slop\" complaints about the volume of "
            "generated docs and QA scripts; no place search without a Google key; no "
            "weather layer"
        ),
        homepage="https://maptheworld.ai/",
    ),
    dict(
        slug="simplifaisoul/osiris",
        name="OSIRIS",
        tier="core",
        summary="Next.js 16 + MapLibre \"Palantir alternative\": 16 layers plus a RECON "
        "toolkit (port scan, WHOIS, CVE, crypto wallet + OFAC checks) and Telegram geoparsing.",
        overview=(
            "Open Source Intelligence & Reconnaissance Integrated System. Next.js 16 + "
            "TypeScript with MapLibre GL rendering every entity through WebGL. Layers: "
            "OpenSky aviation split into commercial / private / military, 17,000+ CCTV "
            "cameras (TfL, WSDOT, Caltrans, ODOT, MDOT, Hong Kong, Taiwan, NZTA), USGS "
            "quakes, FIRMS fires, NASA EONET severe events, NOAA SWPC + N2YO space, NVD "
            "CVEs, 25+ live 24/7 broadcaster streams pinned to the map, 39 ports and 10 "
            "chokepoints as static maritime intel, 13 hand-curated conflict zones, and a "
            "Telegram layer that scrapes public t.me/s/ previews and geoparses posts in "
            "English, Cyrillic and Arabic. The RECON toolkit is the differentiator: TCP "
            "port scanner, DNS, WHOIS, SSL inspector, IP intel, CVE lookup, BTC/ETH wallet "
            "tracing with OFAC SDN cross-checks via OpenSanctions. Polling was relaxed to "
            "15-30 minute intervals to cut Vercel edge requests by 75%. The repo "
            "description embeds a pump.fun token address, so there is a memecoin attached."
        ),
        engine="MapLibre GL (WebGL)",
        basemap="vector tiles",
        backend="Next.js API routes as proxies, in-memory caches",
        stores_history="no",
        keyless_start="mostly; OpenSky anonymous, FIRMS and N2YO need keys",
        layers=(
            "aviation, CCTV, earthquakes, fires, news streams, weather events, space "
            "weather + satellites, CVEs, conflict zones (static), ports + chokepoints "
            "(static), crypto/sanctions, Telegram posts"
        ),
        keys="FIRMS, N2YO; OpenSky optional; everything else keyless",
        weak=(
            "conflict zones and maritime are hand-typed lists, not feeds; memecoin "
            "attached to the project; edge-request costs drove slow polling"
        ),
        homepage="https://osirisai.live",
    ),
    # --------------------------------------------------------------- small
    dict(
        slug="VrushankPatel/godseye",
        name="Godseye 1.0",
        tier="small",
        summary="Frontend-only React + CesiumJS BYOK globe with the longest layer list of "
        "the small builds: buoys, METAR, SIGMET, aurora, Wikidata conflicts, DOE outages.",
        overview=(
            "React + Vite + CesiumJS + Tailwind + Zustand, no backend at all: every feed "
            "is fetched from the browser, so keyed sources need your own keys in a local "
            "secrets file. Inspired by Bilawal's WorldView write-up. Layers beyond the "
            "usual flights / satellites / quakes / CCTV: GDACS disaster alerts, EONET "
            "hazards, IRIS seismic stations, OurAirports, WFP ports + AISstream vessels, "
            "DOE ODIN outages + WRI power plants, NWS alert polygons, NDBC ocean buoys, "
            "Smithsonian volcanic activity, SWPC aurora and GOES flares, METAR flight "
            "categories, AIRMET/SIGMET hazard polygons, Open-Meteo weather and AQI grids, "
            "Wikidata SPARQL armed conflicts, military bases (NTAD + OSM), restricted "
            "airspace. Vision modes: NVG, FLIR, CRT, Anime, God Mode. The author notes "
            "Codex was used for scaffolding. Hosted at godseye-x.web.app."
        ),
        engine="CesiumJS",
        basemap="Google 3D Tiles (BYOK) or Cesium default",
        backend="none (browser fetch only)",
        stores_history="no",
        keyless_start="partial; keyed layers stay empty",
        layers="30+ toggles, see overview",
        keys="BYOK: Google 3D, YouTube, Guardian, AISStream, FIRMS",
        weak="browser-direct fetches hit CORS and rate limits; hosted build depends on the author's keys",
        homepage="https://godseye-x.web.app/",
    ),
    dict(
        slug="noaRoblesLevy/GodsEye",
        name="God's Eye (noaRoblesLevy)",
        tier="small",
        summary="Early CesiumJS + Google 3D Tiles clone with NVG/FLIR/CRT/Anime shaders and "
        "a God Mode; successor to osint-worldmap; dead since March 2026.",
        overview=(
            "One of the first public clones of Bilawal's original WorldView demo, built "
            "before God's Eye View itself was open-sourced. CesiumJS with Google "
            "Photorealistic 3D Tiles (falls back to NASA Blue Marble), CelesTrak "
            "satellites via SGP4, OpenSky aircraft, Austin traffic cameras, simulated "
            "traffic particles on OSM streets, and Canvas2D post-processing shaders. Seven "
            "source files, no backend, no license file. Its predecessor osint-worldmap is "
            "a TypeScript version of the same idea. Last commit 2026-03-05."
        ),
        engine="CesiumJS",
        basemap="Google 3D Tiles or NASA Blue Marble",
        backend="none",
        stores_history="no",
        keyless_start="partial",
        layers="satellites, aircraft, CCTV (Austin), simulated traffic",
        keys="Google Maps (optional), Cesium ion",
        weak="abandoned; no license",
        homepage="",
    ),
    dict(
        slug="noaRoblesLevy/osint-worldmap",
        name="osint-worldmap",
        tier="small",
        summary="The TypeScript predecessor of noaRoblesLevy/GodsEye. Satellites, ships, planes on a world map.",
        overview=(
            "Two-day project from late February 2026 that became GodsEye a week later. "
            "Kept here only so the lineage is complete."
        ),
        engine="", basemap="", backend="none", stores_history="no", keyless_start="",
        layers="satellites, ships, planes", keys="", weak="abandoned", homepage="",
    ),
    dict(
        slug="OdinMB/city-monitor",
        name="City Monitor",
        tier="small",
        summary="World Monitor scaled down to one city (Berlin): cron ingest into PostgreSQL, "
        "pre-built JSON, React + MapLibre. The only one here that actually stores data.",
        overview=(
            "A city-scale take: weather, transit disruptions, news, events, police "
            "reports, air quality, wastewater virus measures, water levels, pharmacies, "
            "traffic, construction. What makes it worth reading for anyone building their "
            "own is the architecture: Node/Express cron jobs ingest feeds on a schedule "
            "into PostgreSQL (Drizzle ORM) and serve pre-built JSON to a React 19 + "
            "MapLibre SPA. GPT-5 for news summaries. Turborepo monorepo. Live at "
            "citymonitor.app and still active."
        ),
        engine="MapLibre GL",
        basemap="vector tiles",
        backend="Express + node-cron + PostgreSQL",
        stores_history="yes (PostgreSQL)",
        keyless_start="needs a DATABASE_URL",
        layers="weather, transit, news, events, police, air quality, wastewater, water, pharmacies, traffic, construction",
        keys="PostgreSQL, OpenAI for summaries",
        weak="single city; Render.com deploy",
        homepage="https://citymonitor.app",
    ),
    dict(
        slug="AnishNehete/TheSphere",
        name="Sphere",
        tier="small",
        summary="Search-first \"why is X happening\" platform on a photorealistic globe: "
        "entity resolution, scoped evidence, causal chain, portfolio impact.",
        overview=(
            "Python full-stack that treats the globe as the front door to an "
            "investigation loop: ask a question (\"Why is TSLA down?\", \"Compare Japan vs "
            "Korea\"), resolve the entity, retrieve scoped evidence, explain the cause, "
            "show market and portfolio impact, save and share. A different goal from the "
            "map-first projects: the map is context, the answer is the product. Two days "
            "of commits in April 2026, no license."
        ),
        engine="photorealistic 3D globe (see repo)",
        basemap="",
        backend="Python",
        stores_history="investigations are saved",
        keyless_start="no",
        layers="signals, markets, news, weather, conflict as evidence sources",
        keys="LLM + market data keys",
        weak="two-day project; no license",
        homepage="https://thesphere.icu/",
    ),
    # ---------------------------------------------------------- derivative
    dict(
        slug="meet-the-1337/AtlasWatchtower",
        name="Atlas Watchtower",
        tier="derivative",
        summary="World Monitor rebrand with desktop builds and \"30+ sources\"; one push in August 2026.",
        overview=(
            "A renamed World Monitor (the README still opens with \"WorldMonitor is...\"). "
            "Same feature set: earthquakes, fires, military and commercial flights, AIS, "
            "100+ RSS feeds with AI clustering, markets / crypto / prediction markets, "
            "cyber threat indicators, internet outage mapping, country instability "
            "scoring. Ships web, PWA and Windows / macOS / Linux desktop. Created and last "
            "pushed on the same day, 2026-08-10."
        ),
        engine="World Monitor", basemap="", backend="World Monitor", stores_history="no",
        keyless_start="yes", layers="World Monitor's", keys="World Monitor's",
        weak="single-commit rebrand", homepage="https://atlas-watchtower.vercel.app",
    ),
    dict(
        slug="wilson-cheng1110/WorldPredict",
        name="Worldcast",
        tier="derivative",
        summary="Bridges World Monitor with the MiroFish multi-agent simulator: pick a live "
        "event, simulate downstream effects, get notified when reality matches.",
        overview=(
            "Pick any event on the World Monitor globe, click \"Predict this event,\" and "
            "MiroFish spawns thousands of AI agents with memory and personality to "
            "simulate what happens next across markets, geopolitics and supply chain. It "
            "then emits a checklist of verifiable watch signals and keeps scanning incoming "
            "World Monitor events; when one matches, you get a browser notification. Runs "
            "against included mocks without Docker. AGPL, last pushed 2026-05-11."
        ),
        engine="World Monitor (iframe) + own UI", basemap="", backend="bridge service on :3333",
        stores_history="prediction history", keyless_start="mocks only",
        layers="World Monitor's", keys="LLM keys for MiroFish",
        weak="depends on two upstreams", homepage="https://wilson-cheng1110.github.io/WorldPredict",
    ),
    dict(
        slug="dagnazty/WorldMonitor_CYD",
        name="WorldMonitor CYD Edition",
        tier="derivative",
        summary="World Monitor Desktop Companion ported to a $15 ESP32 Cheap Yellow Display.",
        overview=(
            "Complete port of the World Monitor companion to the 2.8-inch ESP32 CYD "
            "touchscreen: Yahoo Finance indices / VIX / yields, USGS earthquakes, NASA "
            "EONET events, plus mock risk scores and news. Touch navigation, kiosk "
            "auto-advance, WiFi config stored in flash. Arduino / PlatformIO with "
            "TFT_eSPI. MIT."
        ),
        engine="TFT_eSPI on ESP32", basemap="none", backend="none (device polls APIs)",
        stores_history="no", keyless_start="yes", layers="markets, earthquakes, natural events",
        keys="none", weak="mock news and risk scores", homepage="",
    ),
    dict(
        slug="sjkncs/worldmonitor-enhanced",
        name="World Monitor Enhanced",
        tier="derivative",
        summary="World Monitor copy with bolted-on \"quant trading AI (75-85% accuracy),\" "
        "10-second military tracking and energy alerts. Treat the accuracy claims as marketing.",
        overview=(
            "A World Monitor snapshot from March 2026 with three add-ons documented in "
            "Chinese: a FinBERT + LSTM + GARCH trading signal generator, OpenSky military "
            "tracking at 10-second refresh with 6-hour trajectory prediction, and an "
            "energy-intelligence alert layer. One day of commits."
        ),
        engine="World Monitor", basemap="", backend="World Monitor", stores_history="no",
        keyless_start="yes", layers="World Monitor's + quant, military, energy",
        keys="World Monitor's", weak="unverifiable accuracy claims; one-day snapshot", homepage="",
    ),
    dict(
        slug="worldmonitor-app/worldmonitor",
        name="World Monitor Pro",
        tier="derivative",
        summary="Marketing repo for the paid World Monitor Pro tier (equity research, AI "
        "morning briefs, 100+ connectors); little code of its own.",
        overview=(
            "Describes the Pro upsell: equity research, geopolitical frameworks, central "
            "bank tracking, AI morning briefs to Slack / Telegram / WhatsApp, satellite "
            "imagery and SAR, 50,000+ mapped infrastructure assets, 100+ enterprise "
            "connectors. Useful only as a map of where the upstream project is heading "
            "commercially."
        ),
        engine="World Monitor", basemap="", backend="", stores_history="Pro feature",
        keyless_start="", layers="", keys="", weak="marketing only", homepage="",
    ),
    dict(
        slug="tncsharetool/worldmonitor",
        name="World Monitor (tncsharetool)",
        tier="derivative",
        summary="World Monitor re-upload pitched as an \"MMO-like world map\" creators can "
        "monetize with affiliate flows and ad networks; 1,700-line README.",
        overview=(
            "A March 2026 copy of World Monitor whose README was rewritten around "
            "monetization: affiliate flows, ad networks, community hosting. Same code, "
            "different pitch. Points at breaths.me."
        ),
        engine="World Monitor", basemap="", backend="World Monitor", stores_history="no",
        keyless_start="yes", layers="World Monitor's", keys="World Monitor's",
        weak="re-upload with an ad pitch", homepage="https://breaths.me",
    ),
    dict(
        slug="shawn14/worldview",
        name="worldview (shawn14)",
        tier="derivative",
        summary="Next.js spy-satellite-sim clone from March 2026 with the untouched create-next-app README. Dead.",
        overview=(
            "CesiumJS + Google 3D Tiles + live aircraft / satellites + military-style "
            "visual filters, per the description. The README is still the Next.js "
            "boilerplate. Two days of commits."
        ),
        engine="CesiumJS", basemap="Google 3D Tiles", backend="Next.js", stores_history="no",
        keyless_start="no", layers="aircraft, satellites", keys="Google Maps", weak="abandoned", homepage="",
    ),
    # ------------------------------------------------------------ namesake
    dict(
        slug="LeonardoCides/God-s-eye",
        name="God-s-eye (LeonardoCides)",
        tier="namesake",
        summary="Username enumeration across social platforms. Same name, not a map.",
        overview="Multi-threaded digital-footprint search by handle. Listed so it is not confused with the map projects.",
        engine="", basemap="", backend="Python CLI", stores_history="", keyless_start="",
        layers="", keys="", weak="", homepage="",
    ),
    dict(
        slug="Shajal-Kumar/Gods-Eye",
        name="Gods-Eye (Shajal-Kumar)",
        tier="namesake",
        summary="Human-in-the-loop OSINT framework. Same name, not a map.",
        overview="Python OSINT framework with an analyst in the loop. Not a globe.",
        engine="", basemap="", backend="Python", stores_history="", keyless_start="",
        layers="", keys="", weak="", homepage="",
    ),
    dict(
        slug="KamalDevelopers/GodsEyeView",
        name="GodsEyeView (KamalDevelopers)",
        tier="namesake",
        summary="A hobby operating system that shows up first when you search the name.",
        overview="\"The next most holy operating system.\" Unrelated; here so the search result makes sense.",
        engine="", basemap="", backend="", stores_history="", keyless_start="",
        layers="", keys="", weak="", homepage="",
    ),
]

# The feeds everyone builds on. key: none | free | metered | partner | bundled
FEEDS = [
    ("OpenSky Network", "flights", "none (anon, rate-limited; non-commercial license)", "https://opensky-network.org/api/states/all", "WM, GEV, OSR, GSE, NGE"),
    ("adsb.lol", "flights + military", "none (ODbL)", "https://api.adsb.lol/v2/mil", "GEV"),
    ("Wingbits", "flights", "partner", "https://wingbits.com", "WM"),
    ("AISStream.io", "vessels (AIS)", "free key", "https://aisstream.io", "GEV, GSE"),
    ("CelesTrak", "satellites (TLE)", "none", "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json", "GEV, GSE, NGE"),
    ("N2YO", "satellites", "free key", "https://www.n2yo.com/api/", "OSR"),
    ("USGS", "earthquakes", "none", "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson", "all"),
    ("NASA FIRMS", "active fires", "free MAP_KEY", "https://firms.modaps.eosdis.nasa.gov/api/", "GEV, OSR, GSE"),
    ("NASA EONET", "natural events", "none", "https://eonet.gsfc.nasa.gov/api/v3/events?status=open", "OSR, GSE, CYD"),
    ("GDACS", "disaster alerts", "none", "https://www.gdacs.org/gdacsapi/api/events/geteventlist/MAP", "GSE, OSR"),
    ("NWS api.weather.gov", "US weather alerts", "none (User-Agent required)", "https://api.weather.gov/alerts/active", "GSE"),
    ("NOAA SWPC", "space weather", "none", "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json", "OSR, GSE"),
    ("NOAA NDBC", "ocean buoys", "none", "https://www.ndbc.noaa.gov/", "GSE"),
    ("Launch Library 2", "launches", "none (15/hr anon) or token", "https://ll.thespacedevs.com/2.3.0/launches/upcoming/", "GEV"),
    ("GDELT", "geo-tagged news", "none", "https://api.gdeltproject.org/api/v2/geo/geo", "GEV (fallback), OSR"),
    ("Open-Meteo", "weather / AQI", "none", "https://open-meteo.com", "GEV, GSE"),
    ("Radio Browser", "internet radio", "none", "https://api.radio-browser.info", "GEV"),
    ("GBFS", "bikeshare", "none", "https://gbfs.org", "GEV"),
    ("TomTom Traffic", "traffic flow", "free key (200k tiles/mo)", "https://developer.tomtom.com", "GEV"),
    ("OpenStreetMap Overpass", "roads, military sites", "none (ODbL)", "https://overpass-api.de", "GEV, GSE"),
    ("Google Photorealistic 3D Tiles", "3D basemap", "metered key", "https://developers.google.com/maps/documentation/tile", "GEV, GSE, NGE"),
    ("Cesium ion", "terrain / 3D", "free token", "https://ion.cesium.com", "GEV, NGE"),
    ("Esri World Imagery", "satellite basemap", "none", "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer", "GEV"),
    ("OpenFreeMap", "vector basemap", "none", "https://tiles.openfreemap.org/styles/positron", "-"),
    ("TeleGeography", "submarine cables", "bundled (CC BY-NC-SA)", "https://www.submarinecablemap.com", "GEV, WM"),
    ("OpenSanctions", "sanctions (OFAC SDN)", "none (CC-BY)", "https://www.opensanctions.org", "OSR"),
    ("NVD", "CVEs", "none (rate-limited)", "https://nvd.nist.gov/developers", "OSR"),
    ("ACLED", "conflict events", "registration key", "https://acleddata.com", "WM"),
    ("City CCTV (Austin, Caltrans, TfL, WSDOT...)", "public cameras", "none", "https://api.tfl.gov.uk", "GEV, OSR, GSE, NGE"),
]
FEED_ABBR = "WM = World Monitor, GEV = God's Eye View, OSR = OSIRIS, GSE = Godseye 1.0, NGE = noaRoblesLevy/GodsEye, CYD = WorldMonitor CYD"

SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
  slug TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  tier TEXT NOT NULL CHECK (tier IN ('core','small','derivative','namesake')),
  summary TEXT NOT NULL,
  overview TEXT NOT NULL,
  engine TEXT, basemap TEXT, backend TEXT, stores_history TEXT, keyless_start TEXT,
  layers TEXT, keys TEXT, weak TEXT, homepage TEXT,
  -- live fields, filled by refresh.py
  stars INTEGER, forks INTEGER, open_issues INTEGER, license TEXT, language TEXT,
  created_at TEXT, pushed_at TEXT, archived INTEGER, description TEXT,
  refreshed_at TEXT
);
CREATE TABLE IF NOT EXISTS feeds (
  name TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  key_required TEXT NOT NULL,
  url TEXT NOT NULL,
  used_by TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT);
"""

LIVE_COLS = ("stars", "forks", "open_issues", "license", "language", "created_at",
             "pushed_at", "archived", "description", "refreshed_at")


def main() -> None:
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)

    # keep live stats across re-seeds
    live = {r[0]: r[1:] for r in con.execute(
        f"SELECT slug, {', '.join(LIVE_COLS)} FROM projects")}

    con.execute("DELETE FROM projects")
    for p in PROJECTS:
        cols = list(p.keys())
        con.execute(
            f"INSERT INTO projects ({', '.join(cols)}) VALUES ({', '.join('?' * len(cols))})",
            [p[c] for c in cols])
        if p["slug"] in live:
            con.execute(
                f"UPDATE projects SET {', '.join(c + '=?' for c in LIVE_COLS)} WHERE slug=?",
                [*live[p["slug"]], p["slug"]])

    con.execute("DELETE FROM feeds")
    con.executemany("INSERT INTO feeds VALUES (?,?,?,?,?)", FEEDS)
    con.execute("INSERT OR REPLACE INTO meta VALUES ('feed_abbr', ?)", (FEED_ABBR,))
    con.commit()

    n = con.execute("SELECT count(*) FROM projects").fetchone()[0]
    f = con.execute("SELECT count(*) FROM feeds").fetchone()[0]
    print(f"seeded {n} projects, {f} feeds -> {DB}")


if __name__ == "__main__":
    main()
