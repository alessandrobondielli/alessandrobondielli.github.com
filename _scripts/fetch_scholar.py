#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and write to _data/publications.json.

Usage:
    pip install scholarly
    python _scripts/fetch_scholar.py

Run locally — Google blocks cloud/CI IP ranges so this is never run in CI.
"""

import json
import signal
import sys
from pathlib import Path

SCHOLAR_ID = "zcXQk6YAAAAJ"
OUTPUT = Path(__file__).parent.parent / "_data" / "publications.json"
TIMEOUT_SECONDS = 120


def _timeout_handler(signum, frame):
    raise TimeoutError(f"Timed out after {TIMEOUT_SECONDS}s")


def fetch():
    from scholarly import scholarly

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(TIMEOUT_SECONDS)

    try:
        print(f"Fetching profile for {SCHOLAR_ID} …")
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author, sections=["publications"])

        pubs = []
        total = len(author.get("publications", []))

        for i, pub in enumerate(author["publications"], 1):
            filled = scholarly.fill(pub)
            bib = filled.get("bib", {})

            raw_authors = bib.get("author", "")
            authors = [a.strip() for a in raw_authors.split(" and ")] if raw_authors else []

            venue = (
                bib.get("citation")
                or bib.get("journal")
                or bib.get("booktitle")
                or ""
            )

            try:
                bibtex = scholarly.bibtex(filled)
            except Exception:
                bibtex = ""

            entry = {
                "title":     bib.get("title", ""),
                "authors":   authors,
                "venue":     venue,
                "year":      int(bib["pub_year"]) if bib.get("pub_year") else None,
                "citations": filled.get("num_citations", 0),
                "url":       filled.get("pub_url", ""),
                "bibtex":    bibtex,
            }
            pubs.append(entry)
            print(f"  [{i}/{total}] {entry['title'][:70]}")

        signal.alarm(0)

    except TimeoutError as e:
        signal.alarm(0)
        print(f"WARNING: {e} — saving {len(pubs)} partial results.")

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
