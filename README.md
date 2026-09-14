MTG Karten-Editor für GitHub Pages.

Settings → Pages → Deploy from a branch → main → /(root).


## Neue Frame-Stile hinzufügen

Lege unter `frames/` einfach einen neuen Unterordner an, zum Beispiel:

```text
frames/
├── new/
├── vintage/
└── neon/
    ├── frame_white.png
    ├── frame_blue.png
    ├── frame_black.png
    └── ...
```

Nach dem Push aktualisiert die GitHub Action automatisch `frames/manifest.json`.
Der neue Ordner erscheint danach im Dropdown **Schnellauswahl Stil**.

Die Frame-Dateinamen sollten weiterhin dem bisherigen Schema entsprechen, z. B.
`frame_white.png`, `frame_blue.png`, `frame_rg.png`, `frame_land_wu.png`, `frame_multicolor.png`.
