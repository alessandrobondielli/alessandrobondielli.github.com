# alessandrobondielli.github.com

Personal academic website for [Alessandro Bondielli](https://alessandrobondielli.github.com), PhD, Assistant Professor at the University of Pisa (NLP).

Built with Jekyll 4, deployed to GitHub Pages via GitHub Actions. No external theme — fully custom CSS.

## Local development

```bash
bundle install          # first time only
bundle exec jekyll serve --livereload
```

## Structure

| File/Dir | Purpose |
|---|---|
| `_config.yml` | Site-wide settings and author links |
| `assets/css/main.css` | All styles (single file, CSS variables at the top) |
| `_layouts/` | `default.html`, `page.html`, `post.html` |
| `_includes/` | `head.html`, `nav.html`, `footer.html` |
| `index.html` | Home page |
| `about.md` | Bio |
| `research.md` | Research areas |
| `publications.md` | Publication list |
| `teaching.md` | Course listings |
| `_posts/` | Blog / news posts |
| `_data/publications.json` | Scholar data fetched locally via `_scripts/fetch_scholar.py` |

See [CLAUDE.md](CLAUDE.md) for full content and theming guidance.
