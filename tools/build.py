"""Builds index.html: inlines card-bg.svg (template without placeholders) into src/index.template.html."""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
bg = base64.b64encode((root / "card-bg.svg").read_bytes()).decode()
html = (root / "src" / "index.template.html").read_text(encoding="utf-8")
(root / "index.html").write_text(html.replace("__CARD_BG__", "data:image/svg+xml;base64," + bg), encoding="utf-8")
