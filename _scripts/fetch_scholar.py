#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and write to _data/publications.json.

Usage:
    pip install scholarly
    python _scripts/fetch_scholar.py

The output file is committed to the repo so the site builds correctly even
when Scholar is temporarily unreachable (e.g. rate-limited in CI).
"""

import json
import sys
from pathlib import Path

SCHOLAR_ID = "zcXQk6YAAAAJ"
OUTPUT = Path(__file__).parent.parent / "_data" / "publications.json"


def fetch():
    try:
        from scholarly import scholarly
    except ImportError:
        print("ERROR: run  pip install scholarly  first.", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching author profile for {SCHOLAR_ID} …")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    total = len(author.get("publications", []))
    for i, pub in enumerate(author["publications"], 1):
        filled = scholarly.fill(pub)
        bib = filled.get("bib", {})

        # Normalise author string: scholarly uses " and " as separator
        raw_authors = bib.get("author", "")
        authors = [a.strip() for a in raw_authors.split(" and ")] if raw_authors else []

        venue = (
            bib.get("venue")
            or bib.get("journal")
            or bib.get("booktitle")
            or ""
        )

        entry = {
            "title":     bib.get("title", ""),
            "authors":   authors,
            "venue":     venue,
            "year":      int(bib["pub_year"]) if bib.get("pub_year") else None,
            "citations": filled.get("num_citations", 0),
            "url":       filled.get("pub_url", ""),
        }
        pubs.append(entry)
        print(f"  [{i}/{total}] {entry['title'][:70]}")

    # Sort: newest first, then by citation count
    pubs.sort(key=lambda x: (x["year"] or 0, x["citations"]), reverse=True)
    return pubs


def main():
    OUTPUT.parent.mkdir(exist_ok=True)
    pubs = fetch()
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(pubs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(pubs)} publications → {OUTPUT}")


if __name__ == "__main__":
    main()
