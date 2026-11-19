# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this site is

Personal academic website for **Alessandro Bondielli**, PhD, Assistant Professor at the University of Pisa (NLP). Built with Jekyll 4, deployed to GitHub Pages via GitHub Actions. No Jekyll theme — fully custom CSS.

## Build and serve

Ruby is managed by rbenv (`.ruby-version` = 3.3.6). Non-interactive shells may pick up the system Ruby 2.6 and fail with a bundler version error; activate rbenv first: `eval "$(rbenv init - zsh)"`.

```bash
bundle install          # first time only
bundle exec jekyll serve --livereload
bundle exec jekyll build
```

## Site structure

| File/Dir | Purpose |
|---|---|
| `_config.yml` | Site-wide settings and author links |
| `assets/css/main.css` | All styles (single file) |
| `_layouts/` | `default.html` (base), `page.html`, `post.html` |
| `_includes/` | `head.html`, `nav.html`, `footer.html` |
| `index.html` | Home page (profile + news pulled from posts) |
| `about.md` | Long bio |
| `research.md` | Research areas + posts tagged `research` |
| `blog.html` | All posts |
| `publications.md` | Manually curated publication list |
| `teaching.md` | Course listings |
| `contact.md` | Full contact info |
| `_posts/` | Blog posts (Jekyll standard) |

## Adding content

**New blog post** — create `_posts/YYYY-MM-DD-slug.md`:
```yaml
---
layout: post
title: "Your title"
tags: [research, NLP]   # tag 'research' makes the post appear on /research/
excerpt: "One sentence shown in listings."
---
```

**New publication** — add/edit the entry in `_data/publications.json` (title, authors, venue, year, citations, url); `publications.md` renders it via Liquid. See the Google Scholar section for fetching. Also update the cards in `research.md` when a paper belongs to a research area.

**Blog post for a paper** — pattern used for the EMNLP 2026, NL4AI 2026 and arXiv posts:
- Extract text with `pdftotext -layout`, and figures with `pdfimages -png`; embedded images come with a separate soft mask (`smask`), so composite each onto white with Pillow before saving (see `assets/img/posts/pos-sae/`).
- Save figures in `assets/img/posts/<slug>/` and embed with `<figure><img src="{{ '/assets/img/posts/<slug>/figX.png' | relative_url }}" alt="…"><figcaption>…</figcaption></figure>` (styled in `main.css` under `.post-body figure`).
- Do not state facts (talk details, locations, attendance) that are not in the paper or an official page.
- Post `date:` comes from the filename. Homepage news shows the 5 newest posts, so pick dates deliberately if one post must appear last/first (e.g. real arXiv/proceedings dates).
- Post titles are plain text in `<title>`, the blog list and the feed — do not use Markdown (`_italics_`) in `title:`; use quotes instead.
- Homepage news dates use `<br>` between "Mon D," and the year; a literal `\n` inside a Liquid `date` format does not produce a line break.

**Profile photo** — place `assets/img/photo.jpg` (square, ≥300 px), then in `index.html` replace the `<svg>` inside `.avatar-placeholder` with:
```html
<img src="{{ '/assets/img/photo.jpg' | relative_url }}" alt="Alessandro Bondielli">
```

**Author links** — update the `author:` section in `_config.yml` (scholar, orcid, acl fields).

## Visual theming guide

All visual variables live at the **top of `assets/css/main.css`** inside `:root { … }`. You never need to touch anything else to retheme the site.

```css
:root {
  /* Swap these two lines to change the accent color */
  --color-primary:        #1d4ed8;   /* main accent (blue) */
  --color-primary-light:  #dbeafe;   /* tint used for cards and tags */
  --color-primary-dark:   #1e40af;   /* hover shade */

  /* Text */
  --color-text:           #1e293b;   /* body text */
  --color-text-muted:     #64748b;   /* secondary text */

  /* Backgrounds */
  --color-bg:             #ffffff;   /* page background */
  --color-bg-subtle:      #f8fafc;   /* card/section backgrounds */
  --color-border:         #e2e8f0;   /* dividers */

  /* Fonts — swap the value to any Google Fonts family */
  --font-sans: 'Inter', system-ui, sans-serif;

  /* Max content width */
  --max-width: 860px;
}
```

### Common rethemes

| Goal | Change |
|---|---|
| Switch to green | `--color-primary: #16a34a`, `--color-primary-light: #dcfce7`, `--color-primary-dark: #15803d` |
| Wider layout | `--max-width: 1020px` |
| Darker background | `--color-bg: #0f172a`, `--color-bg-subtle: #1e293b`, `--color-border: #334155`, `--color-text: #f1f5f9`, `--color-text-muted: #94a3b8` |
| Different font | Replace `'Inter'` with any [Google Font](https://fonts.google.com) name and update the `<link>` in `_includes/head.html` |

## Google Scholar integration

Publications are fetched **locally** via `_scripts/fetch_scholar.py` and committed as `_data/publications.json`. The CI pipeline does not fetch Scholar — Google blocks cloud/CI IP ranges, so it would hang indefinitely.

**To update publications:**
```bash
pip install scholarly
python _scripts/fetch_scholar.py
git add _data/publications.json
git commit -m "update publications"
git push
```

**How it works:**
- `scholarly` queries Scholar ID `zcXQk6YAAAAJ` and writes `_data/publications.json`
- `publications.md` loops over `site.data.publications` via Liquid
- Author name "Bondielli" is automatically bolded in the author list
- `_data/publications.json` is committed to the repo; never delete it

**Known issues (as of Nov 2026):**
- `scholarly` needs `bibtexparser<2` (2.x breaks `scholarly` imports). Use a venv outside the repo, e.g. `pip install scholarly "bibtexparser<2"`.
- Scholar often blocks the per-paper detail pages (`scholarly.fill(pub)` raises `AttributeError`), which crashes `fetch_scholar.py` and returns entries without authors/links. The author-profile listing itself still works.
- Workaround used: list the profile, and only append entries whose title is not already in `_data/publications.json` (merge, don't overwrite), then fill authors/venue/url by hand from the official source (ACL Anthology `.bib`, arXiv, CEUR, SSRN). Browser (Claude in Chrome) can read pages that block plain fetches (ProQuest, SSRN) but never bypass a bot check.
- `_data/publications.json` contains hand-corrected entries (e.g. MAIA "All-in-one" → EMNLP Findings 2025 with Anthology link; AI-SSI protocol; NL4AI overview). A full re-fetch from Scholar would overwrite these; re-apply or merge instead.
- Scholar lists some papers as arXiv/preprint after they are published at a venue; check and fix venue/url by hand.

**To change the Scholar ID**, update `SCHOLAR_ID` in `_scripts/fetch_scholar.py`.
