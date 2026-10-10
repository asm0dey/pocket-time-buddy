"""Build site/index.html (self-hosted, installable, offline) from app.html (the bare page body published as the claude.ai artifact)."""
from pathlib import Path

root = Path(__file__).parent
app = (root / "app.html").read_text()
cut = app.index("</style>") + len("</style>")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#142030">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Time Buddy">
<style>
:root {{ padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); box-sizing: border-box; height: 100%; }}
body {{ margin: 0; }}
img {{ max-width: 100%; }}
[hidden] {{ display: none !important; }}
</style>
{app[:cut]}
</head>
<body>{app[cut:]}
<script>
if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {{}});
</script>
</body>
</html>
"""
(root / "site" / "index.html").write_text(page)
print("built site/index.html")
