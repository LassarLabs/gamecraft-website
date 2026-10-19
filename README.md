# GameCraft website

Source for [lassarlabs.github.io/gamecraft-website](https://lassarlabs.github.io/gamecraft-website/), the website of the [GameCraft](https://github.com/LassarLabs/gamecraft) game engine.

The site is static HTML with one stylesheet (`assets/css/site.css`) and a small script for the mobile menu (`assets/js/site.js`). Page content lives in `build.py`, which writes every `.html` file with a shared header and footer.

```bash
python3 build.py              # regenerate the pages
python3 -m http.server 8000   # preview at http://localhost:8000
```

GitHub Pages serves the `main` branch, so changes are live shortly after they are pushed.

| Page | Contents |
| --- | --- |
| `index.html` | Overview, editor, Unity import, platforms, news |
| `features.html` | Rendering, scripting, tools, platform support |
| `showcase.html` | Scenes made with GameCraft |
| `unity.html` | Migrating from Unity |
| `docs.html` | Getting started, building from source, manuals |
| `download.html` | Downloads and system requirements |
| `roadmap.html` | Planned work |
| `changelog.html` | News and release notes |
| `faq.html` | Frequently asked questions |
| `about.html` | About the project, contributing, license |

Released under the MIT License.
