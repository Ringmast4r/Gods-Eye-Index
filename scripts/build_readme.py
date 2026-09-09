#!/usr/bin/env python3
"""Render README.md from data/projects.db.

    python scripts/build_readme.py

Banner language follows the README Banner Playbook (capsule header, typing
SVG, for-the-badge row, live stats badges, terminal-style headings, footer
capsule). Palette: black to green (166534 / 22C55E).
"""
from __future__ import annotations

import sqlite3
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "projects.db"
OUT = ROOT / "README.md"

USER, REPO = "Ringmast4r", "Gods-Eye-Index"
PRIMARY, ACCENT = "166534", "22C55E"

TIER_TITLE = {"core": "ls --core"}
TIER_BLURB = {
    "core": "Active and massive. Forks, rebrands, dead clones and same-name projects are "
            "deliberately not listed; if it is not pushing commits and pulling thousands of "
            "stars it does not belong here.",
}


def status(pushed: str | None, archived: int | None) -> str:
    if archived:
        return "archived"
    if not pushed:
        return "?"
    days = (date.today() - datetime.strptime(pushed, "%Y-%m-%d").date()).days
    if days <= 30:
        return "active"
    if days <= 120:
        return "quiet"
    return "stale"


def fmt(n: int | None) -> str:
    return f"{n:,}" if isinstance(n, int) else "-"


def cell(s: str | None) -> str:
    return (s or "-").replace("|", "\\|").replace("\n", " ")


def main() -> None:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT * FROM projects ORDER BY CASE tier WHEN 'core' THEN 0 WHEN 'small' THEN 1 "
        "WHEN 'derivative' THEN 2 ELSE 3 END, stars DESC, slug").fetchall()
    feeds = con.execute("SELECT * FROM feeds ORDER BY domain, name").fetchall()
    products = con.execute("SELECT * FROM products ORDER BY name").fetchall()
    meta = dict(con.execute("SELECT k, v FROM meta"))
    refreshed = meta.get("refreshed_at", "never")

    tracked = [r for r in rows if r["tier"] != "namesake"]
    core = [r for r in rows if r["tier"] == "core"]
    total_stars = sum(r["stars"] or 0 for r in tracked)
    active = sum(1 for r in tracked if status(r["pushed_at"], r["archived"]) == "active")
    keyless_feeds = sum(1 for f in feeds if f["key_required"].startswith("none"))

    desc = f"{len(tracked)} projects | {total_stars:,} combined stars | {len(feeds)} shared feeds | tracked, not starred"
    header = (
        "https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:" + PRIMARY +
        "&height=220&section=header&text=" + quote("GODS EYE INDEX") +
        "&fontSize=64&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=" +
        quote(desc) + "&descSize=18&descAlignY=58")
    typing = (
        "https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=" + ACCENT +
        "&center=true&vCenter=true&multiline=true&repeat=true&width=950&height=80&lines=" +
        "Every+God%27s+Eye+style+world+map+in+one+list.;" +
        "World+Monitor+%C2%B7+God%27s+Eye+View+%C2%B7+OSIRIS+%C2%B7+and+the+rest;" +
        "Tracked+here+so+I+don%27t+have+to+star+them+all.")
    footer = (
        "https://capsule-render.vercel.app/api?type=waving&color=0:" + PRIMARY +
        ",100:000000&height=120&section=footer&text=" +
        quote("WATCH THE WATCHERS") + "&fontSize=18&fontColor=ffffff&fontAlignY=65")

    o: list[str] = []
    w = o.append

    # ------------------------------------------------------------ hero
    w('<div align="center">\n')
    w(f'<img width="100%" src="{header}"/>\n')
    w(f'[![Typing SVG]({typing})](https://git.io/typing-svg)\n')
    w("<br>\n")
    w(f"[![Projects](https://img.shields.io/badge/Projects-{len(tracked)}-{PRIMARY}?style=for-the-badge&logo=github&logoColor=white)](#-ls---core)")
    w(f"[![Combined stars](https://img.shields.io/badge/Combined_stars-{quote(f'{total_stars:,}')}-{ACCENT}?style=for-the-badge&logo=github&logoColor=white)](#-stats---live)")
    w(f"[![Keyless feeds](https://img.shields.io/badge/Keyless_feeds-{keyless_feeds}_of_{len(feeds)}-000000?style=for-the-badge&logo=rss&logoColor=white)](#-cat-feedstxt)")
    w(f"[![Refreshed](https://img.shields.io/badge/Refreshed-{quote(refreshed[:10])}-{PRIMARY}?style=for-the-badge&logo=githubactions&logoColor=white)](#-refresh)\n")
    w(f"[![Stars](https://img.shields.io/github/stars/{USER}/{REPO}?style=flat-square&color={PRIMARY}&label=%E2%98%85%20Stars)](https://github.com/{USER}/{REPO}/stargazers)")
    w(f"[![Forks](https://img.shields.io/github/forks/{USER}/{REPO}?style=flat-square&color={ACCENT}&label=%E2%9A%A1%20Forks)](https://github.com/{USER}/{REPO}/network/members)")
    w(f"[![Repo Size](https://img.shields.io/github/repo-size/{USER}/{REPO}?style=flat-square&color=000000)](#)")
    w(f"[![Last Commit](https://img.shields.io/github/last-commit/{USER}/{REPO}?style=flat-square&color={PRIMARY})](https://github.com/{USER}/{REPO}/commits/main)")
    w(f"[![Visitors](https://visitor-badge.laobi.icu/badge?page_id={USER}.{REPO})](#)\n")
    w('<img src="assets/logo.svg" alt="Gods Eye Index" width="220">\n')
    w("</div>\n")
    w("---\n")

    # ------------------------------------------------------------ intro
    w("## `> what_is_this`\n")
    w("```bash")
    w("you@github:~$ cat gods-eye-index.txt\n")
    w("  PURPOSE:        One list of every \"God's Eye\" style live world-map / intel dashboard on GitHub")
    w(f"  TRACKED:        {len(tracked)} projects, all active, all in the thousands of stars")
    w(f"  COMBINED:       {total_stars:,} stars across the tracked set")
    w(f"  FEEDS:          {len(feeds)} shared upstream data sources, {keyless_feeds} of them keyless")
    w("  SOURCE:         data/projects.db is the truth; README is generated from it")
    w(f"  REFRESHED:      {refreshed}")
    w("  STATUS:         [ ACTIVE ]")
    w("```\n")
    w("> In August 2026 \"spy satellite simulator in your browser\" repos took over GitHub Trending. "
      "This index tracks the ones that matter, with live stars, what each one actually does, "
      "what it is built on, and which upstream feeds they share. Small clones, forks and "
      "rebrands are left out on purpose.\n")
    w("---\n")

    # ------------------------------------------------------------ stats
    w("## `> stats --live`\n")
    w('<div align="center">\n')
    w("| # | PROJECT | STARS | FORKS | ISSUES | LICENSE | LANG | PUSHED | STATUS |")
    w("|:-:|:--------|------:|------:|-------:|:-------:|:----:|:------:|:------:|")
    for i, r in enumerate(tracked, 1):
        w(f"| {i} | [{r['name']}](https://github.com/{r['slug']}) | `{fmt(r['stars'])}` | `{fmt(r['forks'])}` | "
          f"`{fmt(r['open_issues'])}` | {cell(r['license'])} | {cell(r['language'])} | {cell(r['pushed_at'])} | "
          f"`{status(r['pushed_at'], r['archived'])}` |")
    w("\n</div>\n")
    w(f"`active` = pushed in the last 30 days, `quiet` = 120, `stale` = older. {active} of {len(tracked)} are active as of {refreshed[:10]}.\n")
    w("---\n")

    # ------------------------------------------------------------ tiers
    for tier in ("core",):
        grp = [r for r in rows if r["tier"] == tier]
        if not grp:
            continue
        w(f"## `> {TIER_TITLE[tier]}`\n")
        w(f"{TIER_BLURB[tier]}\n")
        if tier == "namesake":
            w("| REPO | WHAT IT ACTUALLY IS |")
            w("|:-----|:--------------------|")
            for r in grp:
                w(f"| [{r['slug']}](https://github.com/{r['slug']}) | {cell(r['summary'])} |")
            w("")
            continue
        for r in grp:
            st = status(r["pushed_at"], r["archived"])
            home = f" · [{r['homepage'].replace('https://', '').rstrip('/')}]({r['homepage']})" if r["homepage"] else ""
            w(f"### [{r['name']}](https://github.com/{r['slug']})\n")
            w(f"`{fmt(r['stars'])} stars` · `{cell(r['license'])}` · `{cell(r['language'])}` · `pushed {cell(r['pushed_at'])}` · `{st}`{home}\n")
            w(f"**{r['summary']}**\n")
            w(f"{r['overview']}\n")
            if tier in ("core", "small"):
                w("| | |")
                w("|:--|:--|")
                w(f"| **Engine** | {cell(r['engine'])} |")
                w(f"| **Basemap** | {cell(r['basemap'])} |")
                w(f"| **Backend** | {cell(r['backend'])} |")
                w(f"| **Stores history** | {cell(r['stores_history'])} |")
                w(f"| **Keyless start** | {cell(r['keyless_start'])} |")
                w(f"| **Layers** | {cell(r['layers'])} |")
                w(f"| **Keys** | {cell(r['keys'])} |")
                w(f"| **Weak spots** | {cell(r['weak'])} |")
                w("")
        w("---\n")

    # ------------------------------------------------------------ closed source
    if products:
        w("## `> ls --closed-source`\n")
        w("Hosted competitors with no public repo. Listed so the picture is complete, not because you can clone them.\n")
        for p in products:
            w(f"### [{p['name']}]({p['url']})\n")
            bits = [f"`{p['status']}`", f"`{cell(p['stack'])}`"]
            if p["pricing"]:
                bits.append(f"`{cell(p['pricing'])}`")
            w(" · ".join(bits) + f" · [{p['slug']}]({p['url']})\n")
            w(f"**{p['summary']}**\n")
            w(f"{p['overview']}\n")
        w("---\n")

    # ------------------------------------------------------------ diff
    w("## `> diff --core`\n")
    w("| | " + " | ".join(f"**{r['name']}**" for r in core) + " |")
    w("|:--|" + "|".join(":--" for _ in core) + "|")
    for label, col in (("Engine", "engine"), ("Basemap", "basemap"), ("Backend", "backend"),
                       ("Stores history", "stores_history"), ("Keyless start", "keyless_start"),
                       ("License", "license")):
        w(f"| {label} | " + " | ".join(cell(r[col]) for r in core) + " |")
    w("| Stars | " + " | ".join(f"`{fmt(r['stars'])}`" for r in core) + " |")
    w("| Signature | AI briefs + CII + MCP/SDKs | cockpit view + 3D tiles + voice | RECON toolkit + Telegram + OFAC |")
    w("")
    w("**What none of them do:** keep history you own (every one is a live snapshot; God's Eye View's README says going back in time is \"the expensive part\"), "
      "show per-layer provenance and freshness on the map, or run fully self-hosted without a cloud edge / Redis / third-party key chain. "
      "City Monitor is the only one that writes to a database. Those gaps are the spec for the next one.\n")
    w("---\n")

    # ------------------------------------------------------------ feeds
    w("## `> cat feeds.txt`\n")
    w("The upstream sources the whole category is built on. Same feeds, different chrome.\n")
    w("| FEED | DOMAIN | KEY | USED BY |")
    w("|:-----|:-------|:----|:--------|")
    for f in feeds:
        w(f"| [{f['name']}]({f['url']}) | {cell(f['domain'])} | {cell(f['key_required'])} | {cell(f['used_by'])} |")
    w("")
    w(f"{meta.get('feed_abbr', '')}\n")
    w("---\n")

    # ------------------------------------------------------------ refresh
    w("## `> refresh`\n")
    w("```bash")
    w("python scripts/seed.py           # rebuild tables from the curated lists in seed.py")
    w("python scripts/refresh.py        # live stars / forks / license / pushed_at via gh api")
    w("python scripts/build_readme.py   # regenerate this README from data/projects.db")
    w("```\n")
    w("Add a project: append a dict to `PROJECTS` in `scripts/seed.py`, run the three commands, commit. "
      "Never hand-edit the `.db` or this README.\n")
    w("---\n")

    # ------------------------------------------------------------ tree
    w("## `> tree`\n")
    w("```")
    w("Gods-Eye-Index/")
    w("├── README.md              generated, do not edit")
    w("├── assets/logo.svg")
    w("├── data/projects.db       source of truth (projects, feeds, meta)")
    w("└── scripts/")
    w("    ├── seed.py            curated lists -> db")
    w("    ├── refresh.py         gh api -> live stats")
    w("    └── build_readme.py    db -> README.md")
    w("```\n")
    w("---\n")

    # ------------------------------------------------------------ footer
    w('<div align="center">\n')
    w(f"**Maintained by** [@{USER}](https://github.com/{USER}) · stats via `gh api`, refreshed {refreshed}\n")
    w(f'<img width="100%" src="{footer}"/>\n')
    w("</div>")

    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(tracked)} tracked, {total_stars:,} stars)")


if __name__ == "__main__":
    main()
