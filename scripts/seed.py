#!/usr/bin/env python3
"""Seed data/projects.db from the curated lists below.

This file is the editing surface. Add or fix a project here, then run:

    python scripts/seed.py        # rebuild the tables from this file
    python scripts/refresh.py     # pull live stars / forks / pushed_at from GitHub
    python scripts/build_readme.py

Never hand-edit the .db; it is regenerated from this script. Live stats
(stars, forks, pushed_at, license, ...) are filled by refresh.py and kept
across re-seeds.

Only projects that are ACTIVE (pushing commits) and MASSIVE (thousands of
stars) belong here. Forks, rebrands, dead clones and same-name projects were
dropped on purpose; do not add them back.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "projects.db"

PROJECTS = [
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
]

# The feeds the three are built on. key: none | free | metered | partner | bundled
FEEDS = [
    ("OpenSky Network", "flights", "none (anon, rate-limited; non-commercial license)", "https://opensky-network.org/api/states/all", "WM, GEV, OSR"),
    ("adsb.lol", "flights + military", "none (ODbL)", "https://api.adsb.lol/v2/mil", "GEV"),
    ("Wingbits", "flights", "partner", "https://wingbits.com", "WM"),
    ("AISStream.io", "vessels (AIS)", "free key", "https://aisstream.io", "GEV"),
    ("CelesTrak", "satellites (TLE)", "none", "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json", "GEV"),
    ("N2YO", "satellites", "free key", "https://www.n2yo.com/api/", "OSR"),
    ("USGS", "earthquakes", "none", "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson", "WM, GEV, OSR"),
    ("NASA FIRMS", "active fires", "free MAP_KEY", "https://firms.modaps.eosdis.nasa.gov/api/", "GEV, OSR"),
    ("NASA EONET", "natural events", "none", "https://eonet.gsfc.nasa.gov/api/v3/events?status=open", "OSR"),
    ("GDACS", "disaster alerts", "none", "https://www.gdacs.org/gdacsapi/api/events/geteventlist/MAP", "OSR"),
    ("NOAA SWPC", "space weather", "none", "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json", "OSR"),
    ("Launch Library 2", "launches", "none (15/hr anon) or token", "https://ll.thespacedevs.com/2.3.0/launches/upcoming/", "GEV"),
    ("GDELT", "geo-tagged news", "none", "https://api.gdeltproject.org/api/v2/geo/geo", "GEV (fallback), OSR"),
    ("Open-Meteo", "weather", "none", "https://open-meteo.com", "GEV"),
    ("Radio Browser", "internet radio", "none", "https://api.radio-browser.info", "GEV"),
    ("GBFS", "bikeshare", "none", "https://gbfs.org", "GEV"),
    ("TomTom Traffic", "traffic flow", "free key (200k tiles/mo)", "https://developer.tomtom.com", "GEV"),
    ("OpenStreetMap Overpass", "roads, military sites", "none (ODbL)", "https://overpass-api.de", "GEV"),
    ("Google Photorealistic 3D Tiles", "3D basemap", "metered key", "https://developers.google.com/maps/documentation/tile", "GEV"),
    ("Cesium ion", "terrain / 3D", "free token", "https://ion.cesium.com", "GEV"),
    ("Esri World Imagery", "satellite basemap", "none", "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer", "GEV"),
    ("TeleGeography", "submarine cables", "bundled (CC BY-NC-SA)", "https://www.submarinecablemap.com", "GEV, WM"),
    ("OpenSanctions", "sanctions (OFAC SDN)", "none (CC-BY)", "https://www.opensanctions.org", "OSR"),
    ("NVD", "CVEs", "none (rate-limited)", "https://nvd.nist.gov/developers", "OSR"),
    ("ACLED", "conflict events", "registration key", "https://acleddata.com", "WM"),
    ("City CCTV (Austin, Caltrans, TfL, WSDOT...)", "public cameras", "none", "https://api.tfl.gov.uk", "GEV, OSR"),
]
FEED_ABBR = "WM = World Monitor, GEV = God's Eye View, OSR = OSIRIS"

SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
  slug TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  tier TEXT NOT NULL CHECK (tier IN ('core')),
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
