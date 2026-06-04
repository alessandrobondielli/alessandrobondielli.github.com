#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and write to _data/publications.json.

Usage:
    pip install scholarly
    python _scripts/fetch_scholar.py

Strategy: fill the author profile once (gets titles, years, venues, citation
counts, URLs) — do NOT fill individual publications, which makes one extra
HTTP request per paper and is what causes the long hangs.
Author lists are not available via this faster path; they can be added
manually to the JSON if needed.
"""

import json
import signal
import sys
from pathlib import Path

SCHOLAR_ID = "zcXQk6YAAAAJ"
OUTPUT = Path(__file__).parent.parent / "_data" / "publications.json"
TIMEOUT_SECONDS = 60


def _timeout_handler(signum, frame):
    raise TimeoutError("Google Scholar fetch exceeded time limit")


def fetch():
    from scholarly import scholarly

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(TIMEOUT_SECONDS)

    try:
        print(f"Fetching profile for Scholar ID: {SCHOLAR_ID} …")
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author, sections=["publications"])

        pubs = []
        for pub in author.get("publications", []):
            bib = pub.get("bib", {})
            venue = (
                bib.get("venue")
                or bib.get("journal")
                or bib.get("booktitle")
                or ""
            )
            entry = {
                "title":     bib.get("title", ""),
                "authors":   [],   # not available without per-paper fill
                "venue":     venue,
                "year":      int(bib["pub_year"]) if bib.get("pub_year") else None,
                "citations": pub.get("num_citations", 0),
                "url":       pub.get("pub_url", ""),
            }
            pubs.append(entry)
            print(f"  {entry['year']}  {entry['title'][:70]}")

        signal.alarm(0)

    except TimeoutError:
        signal.alarm(0)
        print(f"WARNING: timed out after {TIMEOUT_SECONDS}s — saving partial results.")

    pubs.sort(key=lambda x: (x["year"] or 0, x["citations"]), reverse=True)
    return pubs


def main():
    OUTPUT.parent.mkdir(exist_ok=True)

    try:
        from scholarly import scholarly  # noqa: F401
    except ImportError:
        print("ERROR: run  pip install scholarly  first.", file=sys.stderr)
        sys.exit(1)

    pubs = fetch()

    if not pubs:
        print("No publications fetched — leaving existing file unchanged.")
        sys.exit(0)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(pubs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(pubs)} publications → {OUTPUT}")


if __name__ == "__main__":
    main()
