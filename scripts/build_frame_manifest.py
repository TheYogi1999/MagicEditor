#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
FRAMES = ROOT / "frames"
LAYOUTS = ROOT / "layouts"
FRAME_OUT = FRAMES / "manifest.json"
LAYOUT_OUT = LAYOUTS / "manifest.json"
EXTS = {".png", ".jpg", ".jpeg", ".webp"}

def label_for(folder: str) -> str:
    low = folder.lower()
    if low == "new":
        return "Neu"
    if low in {"old", "vintage"}:
        return "Alt / Vintage"
    return folder.replace("_", " ").replace("-", " ").title()

styles = []
for folder in sorted(p for p in FRAMES.iterdir() if p.is_dir() and not p.name.startswith(".")):
    frames = []
    for f in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
        if not f.is_file() or f.suffix.lower() not in EXTS:
            continue
        frames.append({"name": f.name, "path": f"frames/{folder.name}/{f.name}"})
    if frames:
        styles.append({"id": folder.name, "label": label_for(folder.name), "frames": frames})

FRAME_OUT.write_text(
    json.dumps({"version": 1, "styles": styles}, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

layouts = []
if LAYOUTS.exists():
    for f in sorted(LAYOUTS.glob("*.json"), key=lambda p: p.name.lower()):
        if f.name == "manifest.json":
            continue
        label = f.stem.replace("_", " ").replace("-", " ").title()
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            if isinstance(data, dict) and data.get("name"):
                label = str(data["name"])
        except Exception as exc:
            print(f"Warnung: {f} ist kein gültiges JSON und wird übersprungen: {exc}")
            continue
        layouts.append({"id": f.stem, "label": label, "path": f"layouts/{f.name}"})

LAYOUT_OUT.write_text(
    json.dumps({"version": 1, "layouts": layouts}, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print(f"{FRAME_OUT}: {len(styles)} Stile, {sum(len(s['frames']) for s in styles)} Frames")
print(f"{LAYOUT_OUT}: {len(layouts)} Layouts")
