# Pocket Time Buddy

A phone-first take on World Time Buddy: hours run down the screen, cities run across, and you pick a meeting slot in 15-minute steps to see it in every city at once.

Live at **https://time.asm0dey.site**.

- 2,100+ cities (every city over 300,000 people and every capital), searchable by name, country or time zone
- Select a time range by dragging the band's handles (touch) or across rows (mouse)
- Share a link that restores the cities, date and selected range
- Works offline and installs to the home screen
- Off-grid zones such as Kathmandu (+5:45) are drawn as shifted columns, so their hours line up with real time

Everything runs in the browser: no server code, no tracking. Your cities stay in your browser's local storage.

## Files

| Path | What it is |
|------|------------|
| `app.html` | The app: markup, styles, script and city data in one file |
| `build.py` | Wraps `app.html` into `site/index.html` with the PWA head and service-worker registration |
| `site/` | What gets served: the built page, `sw.js`, `manifest.json`, icons |
| `compose.yaml` | Optional self-hosting behind a reverse proxy (nginx, non-root, read-only) |

## Build and run locally

```sh
python3 build.py
python3 -m http.server -d site 8000
```

Pushing to `main` publishes to GitHub Pages.

## Credits

City data from [GeoNames](https://www.geonames.org/), licensed under CC BY 4.0.

## Licence

GPL-3.0-or-later. See [LICENSE](LICENSE).
