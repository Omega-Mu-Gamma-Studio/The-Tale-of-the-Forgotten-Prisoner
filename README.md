# The Tale of the Forgotten Prisoner

*A Dark Fantasy Visual Novel / RPG*

> **Theme Direction:** Whimsical fairytale / storybook aesthetic with warm parchment tones, dusty rose accents, and ornate carved-wood frame styling.

---

## 📖 About the Game

You are a prisoner on a cargo ship. Your crime is sealed. Your name is forgotten. Your execution awaits.

Then the kraken attacks.

In the chaos, you escape—but the sea does not release you gently. Two panic-decisions made in the dark (what you protect, and how you meet the sea) organically funnel you into one of four kingdoms, each with its own dangers, secrets, and temptations. The world doesn't know who you are. The world doesn't know what you've done.

**What will you become?**

- A **redeemer**, seeking to confess and atone?
- A **survivor**, burying your past beneath a new identity?
- A **monster**, embracing the darkness that put you on death row?

The choice is yours. But the past has a way of surfacing...

---

## 🎮 Features

- **4 Distinct Kingdoms** – Each with a unique story, cast, and atmosphere, planned as a full 12-chapter route apiece:
  - ❄️ Khionia, the Frozen Kingdom of the North – Survival, sacrifice, and buried relics
  - 🌳 Rhizoma, the Tree Kingdom – Class struggle, rot, and ancient secrets
  - 🏖️ Arenia, the Sandy Shores – Corruption, pleasure, and gilded cages
  - 🏚️ Helos, the Swamp Kingdom – Exiles, ghosts, and the truth you've hidden

- **A Hidden Past** – Your crime is fixed but unknown. Discover it—or bury it forever. See [Mechanics](#-mechanics) for how this is tracked under the hood.

- **Silhouette Aesthetic** – Most scenes use haunting silhouettes, letting your imagination fill the gaps.

- **Major Moments** – Fully rendered AI-generated images mark pivotal choices and emotional climaxes.

- **Branching Narrative** – Your choices close doors. Every decision has weight, tracked per-NPC and across your reckoning with your own crime.

- **Replayability** – Four separate 12-chapter stories. Four distinct experiences. Each playthrough is a new journey.

---

## 🎨 Visual Design Philosophy

The game employs a **"theater of the mind"** approach:

- **Silhouettes (90%)** – Dark, atmospheric backgrounds and character shapes. The player's imagination fills the details.
- **Major Moments (10%)** – Stunning, fully rendered AI images that appear at pivotal choices, serving as emotional punctuation.

This contrast creates a powerful effect: when an image appears, it *matters*.

---

## ⚙️ Mechanics

Two persistent trackers run underneath every route, defined in `game/scripts/characters.rpy`:

- **The Reckoning** (`reckoning`) — a confess / hide / embrace tally. Nudged by morally-loaded choices in every kingdom, not chosen directly. Never shown to the player as a stat; it surfaces through nightmares, memory fragments, and NPC reactions, and eventually shapes the ending.
- **Relationship Points** (`relationship`) — one running total per NPC/LI, nudged the same way. `rp_adjust("name", amount)` auto-creates a new NPC's entry the first time it's called, so a new character can be introduced mid-chapter without editing this file first.

The player's crime itself is fixed narrative canon (not chosen or randomized) and is only ever hinted at — see `PREMISES.md` for the full breakdown of what it is and how it's meant to surface.

---

## 🎭 Theme & GUI Direction

This project uses a **whimsical fairytale / storybook GUI theme**:

- **Palette:** Warm parchment cream base, dusty rose (`#C97B84`) as the primary accent, soft sage as a secondary/muted accent
- **Frame Style:** Ornate carved wood + metal trim (dialogue box, buttons, windows)
- **Fonts:** Blackletter (UnifrakturMaguntia) for character names, warm readable serif (PT Serif) for dialogue and interface text

> **Note:** The colors and spacing are in place; the actual carved-frame art assets are still being sourced. See [Story Status](#-story-status) below.

---

## 🖼️ Art Direction

Character and background art is planned to be AI-generated, in a **semi-realistic, painterly style** — natural but slightly stylized proportions, soft cel shading blended with painterly rendering, warm rim lighting. Deliberately not photorealistic: photoreal AI output tends to be where inconsistency and uncanny-valley artifacts (faces, hands) show up worst, and it's much harder to keep a character looking like *themselves* across dozens of generations. A painterly semi-realistic style hides those inconsistencies better while still reading as more grounded than flat cel-shaded anime.

Each kingdom has an implied color identity already baked into its namebox colors, and backgrounds should follow the same palette:

| Kingdom | Namebox Color | Palette Direction |
|---------|---------------|--------------------|
| Khionia | `#a9c9e8` | Icy blue-white |
| Rhizoma | `#8fbf7f` | Bioluminescent green-gold |
| Arenia | `#d1a24a` | Warm gold-terracotta |
| Helos | `#a480c9` | Misty violet-teal |

**Background reuse plan:** rather than a unique background per scene, each kingdom gets a small set of location "slots" (an exterior establishing shot, the player's living quarters, one or two key event locations, the climax location — roughly 4–6 per kingdom) reused across chapters. A day/night or lit/unlit color-grade pass on the same painting can stand in for a new beat without commissioning new art, which matters a lot at 48-chapters-of-content scale.

---

## 🛠️ Tech Stack

- **Engine:** [Ren'Py](https://www.renpy.org/) – Visual Novel engine with robust customization
- **Art:** AI-generated images (Midjourney / DALL-E) + custom silhouette assets
- **Version Control:** Git / GitHub
- **Fonts:** Google Fonts (UnifrakturMaguntia, PT Serif) – SIL Open Font License 1.1
- **Future Plans:** Custom GUI enhancements, ambient audio, and mobile/web deployment

---

## 🚀 Getting Started

### Prerequisites

- [Ren'Py 8.0+](https://www.renpy.org/latest.html) installed on your system

### Installation

This repository root **is** the Ren'Py project folder—everything lives alongside the `game/` directory the same way it would inside a normal Ren'Py project folder.

1. Clone the repository:
   ```bash
   git clone https://github.com/Omega-Mu-Gamma-Studio/The-Tale-of-the-Forgotten-Prisoner.git
   ```

2. Open the project in Ren'Py:
   - Launch Ren'Py
   - Click "Open Project"
   - Navigate to and select the project directory

3. Launch the game:
   - Click "Launch Project"

### Alternative: Copy Theme to Existing Project

If you already have a Ren'Py project and just want the GUI theme:

1. Copy the contents of this repo's `game/` folder into your project's `game/` folder
2. Overwrite `gui.rpy` if prompted
3. Launch from the Ren'Py launcher as usual

---

## 📂 Project Structure

```
The-Tale-of-the-Forgotten-Prisoner/
├── game/
│   ├── gui.rpy                    # Theme colors, fonts, sizes, spacing
│   ├── gui/
│   │   ├── main_menu.png          # Placeholder background art
│   │   └── game_menu.png          # Placeholder background art
│   ├── fonts/
│   │   ├── UnifrakturMaguntia-Book.ttf
│   │   ├── PTSerif-Regular.ttf
│   │   ├── PTSerif-Bold.ttf
│   │   ├── PTSerif-Italic.ttf
│   │   ├── OFL-UnifrakturMaguntia.txt   # Font license (SIL OFL 1.1)
│   │   └── OFL-PTSerif.txt              # Font license (SIL OFL 1.1)
│   ├── images/
│   │   ├── silhouettes/           # Silhouette backgrounds (90% of scenes) — not yet populated
│   │   ├── major_moments/         # Full AI-generated images (10% of scenes) — not yet populated
│   │   └── gui/                   # Custom UI assets (future)
│   ├── script.rpy                 # Entry point — jumps straight into the prologue
│   └── scripts/
│       ├── characters.rpy         # Shared character defs, reckoning + RP trackers
│       ├── prologue.rpy           # The shipwreck and escape sequence (complete)
│       ├── khionia/
│       │   └── ch01_khionia.rpy   # Chapter 1 written; ch02–ch12 to come
│       ├── rhizoma/
│       │   └── ch01_rhizoma.rpy   # Chapter 1 written; ch02–ch12 to come
│       ├── arenia/
│       │   └── ch01_arenia.rpy    # Chapter 1 written; ch02–ch12 to come
│       ├── helos/
│       │   └── ch01_helos.rpy     # Chapter 1 written; ch02–ch12 to come
│       └── endings.rpy            # Convergence/epilogues — not yet created
├── CHAPTER_TEMPLATE.md             # Per-chapter beat/choice template for all 48 chapter files
├── PREMISES.md                     # Full world, kingdom, and crime lore reference
├── make_backgrounds.py            # Script used to generate placeholder art
├── .gitignore
└── README.md
```

Each kingdom is planned as a full 12-chapter route (48 chapter files total across all four). See `CHAPTER_TEMPLATE.md` for the beat structure every chapter from Chapter 2 onward should follow, and the file-naming convention (`chNN_{kingdom}.rpy`) to keep all four routes consistent.

---

## 🧩 Customization Guide

### Changing the UI (CSS-like)

All UI variables are in `game/gui.rpy`. This is your "CSS file."

**Example:**
```renpy
## Colors
define gui.text_color = "#e0e0e0"        # Text color
define gui.background_color = "#0a0a0a"  # Background color
define gui.accent_color = "#C97B84"      # Dusty rose accent
define gui.hover_color = "#7a9abf"       # Hover color
```

**Replacing UI Images:**

- Dialogue box: Replace `game/gui/textbox.png`
- Choice buttons: Replace `game/gui/button.png` and `button_hover.png`
- Main menu: Replace `game/gui/overlay/main_menu.png`

---

## 📝 Story Status

| Route | Status | Progress |
|-------|--------|----------|
| Prologue | ✅ Complete | 4/4 beats — ship, kraken, escape choices, kingdom routing |
| Khionia (Frozen) | 🚧 In Development | Chapter 1/12 written |
| Rhizoma (Tree) | 🚧 In Development | Chapter 1/12 written |
| Arenia (Sandy Shores) | 🚧 In Development | Chapter 1/12 written |
| Helos (Swamp) | 🚧 In Development | Chapter 1/12 written |
| Endings / Convergence | 📝 Not Started | 0% — waits until all four routes reach Chapter 12 |

**Total planned content:** 12 chapters × 4 kingdoms = 48 chapter files, plus the prologue and endings/convergence content.

*Currently working on: writing Chapter 2 across all four kingdoms, following the structure in `CHAPTER_TEMPLATE.md`. Background/character art sourcing hasn't started yet — see [Art Direction](#-art-direction) below for the current plan.*

---

## 📌 Roadmap

- [x] Repository setup and initial commit
- [x] GUI theme foundation (colors, fonts, spacing)
- [x] Placeholder menu backgrounds
- [x] Complete prologue (escape sequence + organic kingdom routing)
- [x] Reckoning tracker (confess/hide/embrace) + per-NPC Relationship Points system
- [x] Chapter 1 written for all four kingdoms (Khionia, Rhizoma, Arenia, Helos)
- [x] Per-kingdom chapter folder structure + reusable chapter template (`CHAPTER_TEMPLATE.md`)
- [ ] Write Chapters 2–12 for all four kingdoms (48 chapter files total)
- [ ] Write `endings.rpy` convergence/epilogue content once all four Ch.12s exist
- [ ] Source/create carved-wood-and-metal frame art (`frame.png`, button backgrounds, namebox)
- [ ] Final illustrated main menu / game menu backgrounds
- [ ] Generate silhouettes and major-moment art per kingdom, following the palette in [Art Direction](#-art-direction)
- [ ] Release Chapter 1 demo (all four kingdoms playable through Ch.1)
- [ ] Add ambient audio and sound effects
- [ ] Port to web (HTML/CSS/JS) for broader accessibility

---

## 🎨 GUI Assets Needed

The following art assets are still being sourced:

- [ ] Ornate carved wood + metal trim frame (`gui/frame.png`)
- [ ] Button backgrounds (`gui/button/*_background.png`)
- [ ] Namebox (`gui/namebox.png`)
- [ ] Final illustrated main menu background
- [ ] Final illustrated game menu background

---

## 🐛 Known Issues

- None yet! Game is in early development.

---

## 📄 License & Usage

**This project is currently in active development and is not yet a finished product.**

- The source code and assets in this repository are shared **for development, testing, and portfolio purposes only**.
- This is **not** a commercial release. No license for commercial use, redistribution, or derivative works is granted at this time.
- All rights are reserved by **Omega Mu Gamma Studio** until the project reaches a completed state and an official license is chosen.
- The included fonts (UnifrakturMaguntia and PT Serif) are licensed under the SIL Open Font License 1.1 and may be used freely in accordance with that license. The `OFL-*.txt` files in `game/fonts/` must remain with the font files per the license terms.

For inquiries about licensing, collaboration, or future commercial use, please contact the studio directly.

---

## 🙏 Acknowledgments

- [Ren'Py](https://www.renpy.org/) – The engine that makes visual novels accessible
- [Midjourney](https://www.midjourney.com/) & [DALL-E](https://openai.com/dall-e/) – AI art generation (for future major moments)
- [Google Fonts](https://fonts.google.com/) – UnifrakturMaguntia and PT Serif fonts (SIL Open Font License 1.1)
- The open-source community – For tools, inspiration, and support

---

## 📬 Contact

**Omega Mu Gamma Studio**

- **GitHub:** [Omega-Mu-Gamma-Studio](https://github.com/Omega-Mu-Gamma-Studio)
- **Project Repository:** [The-Tale-of-the-Forgotten-Prisoner](https://github.com/Omega-Mu-Gamma-Studio/The-Tale-of-the-Forgotten-Prisoner)