# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this site is

Personal academic website for **Alessandro Bondielli**, PhD, Assistant Professor at the University of Pisa (NLP). Built with Jekyll 4, deployed to GitHub Pages via GitHub Actions. No Jekyll theme — fully custom CSS.

## Build and serve

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

**New publication** — edit `publications.md` directly. Copy an existing `.pub-item` block and update the fields. Bold your name in `pub-authors` with `<strong>`.

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

## Google Scholar integration (future)

When ready to auto-populate publications from Scholar:
1. Install `scholarly` Python package: `pip install scholarly`
2. Create a script `_scripts/fetch_publications.py` that queries your Scholar profile and writes `_data/publications.json`
3. Replace the static HTML in `publications.md` with a Liquid loop over `site.data.publications`
4. Add the script as a step in `.github/workflows/` before the Jekyll build step
