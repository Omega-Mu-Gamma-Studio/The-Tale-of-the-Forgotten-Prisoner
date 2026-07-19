# Fantasy GUI Theme (Ren'Py)

A whimsical fairytale / storybook GUI theme for a Ren'Py visual novel, currently
in development.

## Theme direction

- **Palette:** warm parchment cream base, dusty rose (`#C97B84`) as the
  primary accent, soft sage as a secondary/muted accent.
- **Frame style:** ornate carved wood + metal trim (dialogue box, buttons,
  windows). The colors/spacing are in place; the actual carved-frame art
  assets are still being sourced -- see "Status" below.
- **Fonts:** blackletter (UnifrakturMaguntia) for character names, warm
  readable serif (PT Serif) for dialogue and interface text.

## Project structure

This repo root **is** the Ren'Py project folder -- i.e. everything lives
alongside the `game/` directory the same way it would inside a normal Ren'Py
project folder (the one the Ren'Py launcher opens). To use it:

1. Create a new project in the Ren'Py launcher (or use an existing one).
2. Copy the contents of this repo's `game/` folder into your project's
   `game/` folder, overwriting `gui.rpy` if prompted.
3. Launch from the Ren'Py launcher as usual.

```
.
├── game/
│   ├── gui.rpy              <- theme colors, fonts, sizes, spacing
│   ├── gui/
│   │   ├── main_menu.png    <- placeholder background art
│   │   └── game_menu.png    <- placeholder background art
│   └── fonts/
│       ├── UnifrakturMaguntia-Book.ttf
│       ├── PTSerif-Regular.ttf
│       ├── PTSerif-Bold.ttf
│       ├── PTSerif-Italic.ttf
│       ├── OFL-UnifrakturMaguntia.txt   <- font license (SIL OFL 1.1)
│       └── OFL-PTSerif.txt              <- font license (SIL OFL 1.1)
├── make_backgrounds.py      <- script used to generate the placeholder art
├── .gitignore
└── README.md
```

## Status

- [x] Color palette defined in `gui.rpy`
- [x] Fonts selected, embedded, and license files included
- [x] Spacing/sizing reworked for a roomier, storybook feel
- [x] Placeholder pastel menu backgrounds (not final art)
- [ ] Real carved-wood-and-metal frame/button art (`gui/frame.png`,
      `gui/button/*_background.png`, `gui/namebox.png`, etc.)
- [ ] Final illustrated main menu / game menu backgrounds

## Fonts & licensing

Both fonts are from Google Fonts and licensed under the SIL Open Font
License 1.1 (free for personal and commercial use, redistribution allowed).
The `OFL-*.txt` files in `game/fonts/` must stay alongside the font files
per the license terms.
