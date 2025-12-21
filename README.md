# MICRORACK Documentation Site

This repository contains the documentation site for MICRORACK modular synthesizer system, built with MkDocs Material theme.

## Repository Structure

```
docs-test/
├── docs/                          # Documentation source files
│   ├── index.md                   # About page
│   ├── assets/                    # CSS, JS, fonts, images
│   │   ├── extra.css             # Custom styling (header, tabs, sawtooth, mobile drawer)
│   │   ├── extra.js              # Custom JS (header click behavior, mobile nav reset)
│   │   ├── logo.png              # Full logo for desktop header
│   │   ├── logo_compact.png      # Compact logo for mobile header
│   │   └── martian-mono.woff2    # Custom font
│   ├── getting-started/           # Getting started guides
│   │   ├── index.md
│   │   ├── first-steps/index.md
│   │   └── setup/index.md
│   ├── modules/                   # Module documentation (auto-generated from modules-test repo)
│   │   ├── index.md              # Manual overview page
│   │   └── mod-*/README.md       # Auto-copied from modules-test (gitignored)
│   ├── specification/             # Technical specifications (auto-generated from specs-test repo)
│   │   ├── index.md              # Manual overview page
│   │   ├── mechanical.md         # Auto-copied (gitignored)
│   │   └── electrical.md       # Auto-copied (gitignored)
│   ├── ecosystem/                 # Ecosystem guides (power, I/O, chassis, etc.)
│   └── user-guide/                # User guides (patching, sound design)
├── scripts/                       # Build scripts
│   ├── clone-content.sh          # Clone external repos and update navigation
│   ├── update_nav.py             # Auto-generate modules navigation in mkdocs.yml
│   └── update_index.py           # Auto-generate index.md links
├── .github/workflows/
│   └── deploy.yml                # GitHub Actions deployment workflow
├── mkdocs.yml                    # MkDocs configuration
└── .gitignore                    # Git ignore rules
```

## External Dependencies

The site pulls content from two external repositories at build time:

1. **microrack/modules-test** - Module documentation
   - Cloned to: `modules/` (root, gitignored)
   - Copied to: `docs/modules/mod-*/` (gitignored)
   
2. **microrack/specs-test** - Technical specifications
   - Cloned to: `specification/` (root, gitignored)
   - Copied to: `docs/specification/{mechanical,electrical}.md` (gitignored)

## Build Process

### Local Development

1. Clone the repository
2. Create Python virtual environment: `python -m venv .venv`
3. Activate venv: `source .venv/bin/activate`
4. Install dependencies: `pip install mkdocs-material mkdocs-minify-plugin`
5. Run clone script: `./scripts/clone-content.sh`
   - Clones modules-test and specs-test repos
   - Copies content to docs/
   - Auto-generates module navigation in mkdocs.yml
6. Start server: `mkdocs serve`
7. View at: http://127.0.0.1:8000/

### GitHub Actions Deployment

The `.github/workflows/deploy.yml` workflow:

1. Checks out docs-test repository
2. Checks out modules-test to `modules/`
3. Checks out specs-test to `specification/`
4. Copies specs content to `docs/specification/`
5. Copies module directories to `docs/modules/`
6. Installs Python 3.12 and dependencies
7. Runs `scripts/update_nav.py` to generate module navigation
8. Builds site with `mkdocs build`
9. Deploys to GitHub Pages

## Custom Styling

### Theme Customization (`docs/assets/extra.css`)

**Font**: Martian Mono (monospace, woff2)
- Applied globally to all text and code
- Font weight: 400 for body, 500 for headings

**Color Scheme**:
- Light theme: White (#ffffff) backgrounds, black (#000000) text
- Dark theme: #1e1e1e backgrounds, white (#ffffff) text
- Auto-detection via `prefers-color-scheme` media queries
- Manual toggle available in header

**Header**:
- Sticky at top (z-index: 4)
- White in light mode, #1e1e1e in dark mode
- Shows 2px shadow (#eee / #333) when tabs hidden (scrolled)
- Clickable branding:
  - Site name "Docs": navigates to root `/`
  - Page title (on scroll): scrolls to top of current page
- Logo sizing: 1rem height, 0.2rem gap to title

**Mobile Header** (max-width: 76.1875em):
- Compact logo (`logo_compact.png`) displayed via CSS `::before` pseudo-element
- Logo size: 1.4rem × 1.4rem
- Logo color: black in light mode (via `filter: brightness(0)`), white in dark mode

**Navigation Tabs**:
- Same colors as header
- Custom sawtooth waveform separator at bottom
- 20px padding-bottom for separator space
- Sawtooth pattern: 25px period, 20px height, 2px stroke

**Sawtooth Separator Pattern**:
```
Light theme:
- Top triangle fill: #ffffff
- Stroke line: #000000

Dark theme:
- Top triangle fill: #1e1e1e
- Stroke line: #ffffff
```

**Mobile Drawer**:
- Always opens to root level navigation (via JS)
- Section title text hidden (font-size: 0), back icons visible
- Logo header: 10px bottom margin, compact height
- Back button section: compact height (min-height: 2.4rem)
- Theme-aware colors matching header

**Search Input**:
- Light: #f5f5f5 background, #ddd border
- Hover: #eeeeee background
- Focus: white background, purple (#673ab7) border
- Dark: #2d2d2d background, #444 border

**Footer**:
- 2px top border (#eee in light, #333 in dark)
- Same color scheme as header
- Social icons: 1.2rem size, 70% opacity on hover

**Sidebar Navigation**:
- Section titles hidden on desktop (redundant with tabs)
- Nested items indented 1rem (except first item which is index)
- Martian Mono font, 400 weight

**Headings**:
- h2-h6: reduce to 70% opacity on hover, full-width clickable permalink overlay
- h1: permalink hidden, not clickable
- Font weight: 500

### Custom JavaScript (`docs/assets/extra.js`)

**Header Click Behavior**:
- First topic (site name "Docs"): navigates to root `/`
- Second topic (page title on scroll): smooth scrolls to top, removes URL hash

**Mobile Drawer Reset**:
- When drawer opens, all section toggles are collapsed
- User always sees root level navigation first
- Implemented via `change` event on drawer toggle

## Navigation Structure

The navigation is defined in `mkdocs.yml` with a "Home" section for quick access and separate sections for each topic:

```yaml
nav:
  - About:                            # "Home" tab with quick links
    - About: index.md
    - Getting Started: getting-started/index.md
    - Modules: modules/index.md
    - Specification: specification/index.md
    - Ecosystem: ecosystem/index.md
    - User Guide: user-guide/index.md
  - Getting Started:                  # Detailed getting started section
    - Introduction: getting-started/index.md
    - First Steps: getting-started/first-steps/index.md
    - Setup: getting-started/setup/index.md
  - Modules:                          # Auto-generated by scripts/update_nav.py
    - Modules: modules/index.md
    - mod-clk: modules/mod-clk/README.md
    - mod-vco: modules/mod-vco/README.md
    # ... (generated from docs/modules/mod-* directories)
  - Specification:
    - Specification: specification/index.md
    - Mechanical: specification/mechanical.md
    - Electrical: specification/electrical.md
  - Ecosystem:
    - Overview: ecosystem/index.md
    - Power: ecosystem/power/index.md
    - I/O: ecosystem/io/index.md
    - Chassis: ecosystem/chassis/index.md
    - Chaining: ecosystem/chaining/index.md
    - Compatibility: ecosystem/compatibility/index.md
    - Use Cases: ecosystem/use-cases/index.md
  - User Guide:
    - Overview: user-guide/index.md
    - Patching Techniques: user-guide/patching-techniques/index.md
    - Sound Design: user-guide/sound-design/index.md
```

### Auto-Generated Module Navigation

The `scripts/update_nav.py` script:
- Scans `docs/modules/` for `mod-*` directories
- Sorts them alphabetically
- Updates the Modules section in `mkdocs.yml`
- Preserves all other navigation sections

This runs automatically:
- Locally: when running `scripts/clone-content.sh`
- CI/CD: in GitHub Actions before build

## Configuration Files

### mkdocs.yml

Key settings:
- **Site**: `site_name: Docs`, `site_url: https://docs.microrack.org`
- **Theme**: Material with deep purple primary, green accent
- **Features**: instant loading, navigation tracking, tabs, sections, top button, search suggest/highlight, code copy
- **Plugins**: search (minify removed for build speed)
- **Extensions**: code highlighting, tabs, details, admonitions, tables, TOC with permalinks
- **Custom CSS**: `docs/assets/extra.css`
- **Custom JS**: `docs/assets/extra.js`
- **Social Icons**: Instagram, Facebook, GitHub, X/Twitter, YouTube

### .gitignore

Ignores:
- Build artifacts: `site/`, `__pycache__/`
- Virtual environment: `.venv/`, `venv/`, `env/`
- Cloned repos: `/modules/`, `/specification/`
- Copied content: `docs/modules/*`, `docs/specification/*`
- Exceptions: `!docs/modules/index.md`, `!docs/specification/index.md`

## Development Notes

### Adding New Modules

1. Add module to microrack/modules-test repository
2. Run `./scripts/clone-content.sh` locally to test
3. Navigation updates automatically
4. Commit and push - GitHub Actions will deploy

### Modifying Styles

1. Edit `docs/assets/extra.css`
2. Refresh browser (Ctrl+Shift+R for hard refresh)
3. Test in both light and dark themes
4. Commit changes

### Troubleshooting

**Modules not showing:**
- Ensure `scripts/update_nav.py` runs successfully
- Check that module directories exist in `docs/modules/`
- Verify `mod-*` naming convention

**Styles not updating:**
- Hard refresh browser (Ctrl+Shift+R)
- Clear browser cache
- Check browser console for CSS errors
- Verify CSS syntax in extra.css

**Mobile drawer issues:**
- Drawer should always open to root level (via extra.js)
- Section titles should be hidden, only back icons visible
- If not working, check that extra.js is loaded

**Horizontal scroll appearing:**
- Check `overflow-x: hidden` on html/body
- Verify header `max-width: 100vw`
- Inspect sawtooth separator dimensions

## Deployment

Site deploys to: https://docs.microrack.org (CNAME configured)

Deployment happens automatically when:
- Pushing to main or master branch
- Manual workflow dispatch
- Repository dispatch event "specs-updated"

## Dependencies

**Python packages** (installed via pip):
- mkdocs-material (v9.7.1+)
- mkdocs-minify-plugin (optional)
- pyyaml (required for update_nav.py)

**External repositories**:
- microrack/modules-test
- microrack/specs-test

## Assets

| File | Purpose |
|------|---------|
| `logo.png` | Full logo for desktop header |
| `logo_compact.png` | Compact logo for mobile header (displayed via CSS) |
| `martian-mono.woff2` | Martian Mono font (variable weight 100-900) |
| `extra.css` | All custom styling (~580 lines) |
| `extra.js` | Header click behavior + mobile drawer reset |

## License & Contact

- Repository: https://github.com/microrack/docs-test
- Main site: https://microrack.org
- Support: support@microrack.org
