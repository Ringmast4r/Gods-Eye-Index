#!/usr/bin/env python3
"""Pull live GitHub stats for every project into data/projects.db.

Uses the GitHub CLI (`gh api`) so it rides on whatever login you already have.
Run after seed.py and before build_readme.py:

    python scripts/refresh.py            # all projects
    python scripts/refresh.py --only koala73/worldmonitor
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "projects.db"

# GitHub reports NOASSERTION for repos whose LICENSE file carries carve-outs or
# is non-standard; these are the licenses their READMEs actually state.
LICENSE_OVERRIDES = {
    "bilawalsidhu/gods-eye-view": "MIT (code)",
    "OdinMB/city-monitor": "AGPL-3.0",
    "meet-the-1337/AtlasWatchtower": "AGPL-3.0",
    "tncsharetool/worldmonitor": "AGPL-3.0",
    "sjkncs/worldmonitor-enhanced": "AGPL-3.0",
}


def gh_repo(slug: str) -> dict | None:
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{slug}"], capture_output=True, text=True, check=True,
            encoding="utf-8").stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"  ! {slug}: {getattr(e, 'stderr', e)}".strip(), file=sys.stderr)
        return None
    return json.loads(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="refresh a single slug")
    args = ap.parse_args()

    con = sqlite3.connect(DB)
    slugs = [r[0] for r in con.execute("SELECT slug FROM projects ORDER BY slug")]
    if args.only:
        slugs = [s for s in slugs if s == args.only]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    ok = 0
    for slug in slugs:
        d = gh_repo(slug)
        if not d:
            continue
        lic = (d.get("license") or {}).get("spdx_id") or "none"
        if lic == "NOASSERTION":
            lic = LICENSE_OVERRIDES.get(slug, "custom")
        con.execute(
            """UPDATE projects SET stars=?, forks=?, open_issues=?, license=?, language=?,
               created_at=?, pushed_at=?, archived=?, description=?, refreshed_at=?
               WHERE slug=?""",
            (d["stargazers_count"], d["forks_count"], d["open_issues_count"], lic,
             d.get("language") or "-", d["created_at"][:10], d["pushed_at"][:10],
             1 if d.get("archived") else 0, d.get("description") or "", now, slug))
        print(f"  {slug:40s} {d['stargazers_count']:>7,} stars  pushed {d['pushed_at'][:10]}")
        ok += 1

    con.execute("INSERT OR REPLACE INTO meta VALUES ('refreshed_at', ?)", (now,))
    con.commit()
    print(f"refreshed {ok}/{len(slugs)} at {now}")


if __name__ == "__main__":
    main()
