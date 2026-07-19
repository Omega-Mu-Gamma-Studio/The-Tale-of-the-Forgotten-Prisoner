# The Tale of the Forgotten Prisoner

*A Dark Fantasy Visual Novel / RPG*

> **Theme Direction:** Whimsical fairytale / storybook aesthetic with warm parchment tones, dusty rose accents, and ornate carved-wood frame styling.

---

## 📖 About the Game

You are a prisoner on a cargo ship. Your crime is sealed. Your name is forgotten. Your execution awaits.

Then the kraken attacks.

In the chaos, you escape—but the sea does not release you gently. You wash ashore in one of four kingdoms, each with its own dangers, secrets, and temptations. The world doesn't know who you are. The world doesn't know what you've done.

**What will you become?**

- A **redeemer**, seeking to confess and atone?
- A **survivor**, burying your past beneath a new identity?
- A **monster**, embracing the darkness that put you on death row?

The choice is yours. But the past has a way of surfacing...

---

## 🎮 Features

- **4 Distinct Kingdoms** – Each with a unique story, cast, and atmosphere:
  - ❄️ The Frozen Kingdom of the North – Survival, sacrifice, and buried relics
  - 🌳 The Tree Kingdom – Class struggle, rot, and ancient secrets
  - 🏖️ The Sandy Shores – Corruption, pleasure, and gilded cages
  - 🏚️ The Swamp Kingdom – Exiles, ghosts, and the truth you've hidden

- **A Hidden Past** – Your crime is fixed but unknown. Discover it—or bury it forever.

- **Silhouette Aesthetic** – Most scenes use haunting silhouettes, letting your imagination fill the gaps.

- **Major Moments** – Fully rendered AI-generated images mark pivotal choices and emotional climaxes.

- **Branching Narrative** – Your choices close doors. Every decision has weight.

- **Replayability** – Four separate stories. Four distinct experiences. Each playthrough is a new journey.

---

## 🎨 Visual Design Philosophy

The game employs a **"theater of the mind"** approach:

- **Silhouettes (90%)** – Dark, atmospheric backgrounds and character shapes. The player's imagination fills the details.
- **Major Moments (10%)** – Stunning, fully rendered AI images that appear at pivotal choices, serving as emotional punctuation.

This contrast creates a powerful effect: when an image appears, it *matters*.

---

## 🎭 Theme & GUI Direction

This project uses a **whimsical fairytale / storybook GUI theme**:

- **Palette:** Warm parchment cream base, dusty rose (`#C97B84`) as the primary accent, soft sage as a secondary/muted accent
- **Frame Style:** Ornate carved wood + metal trim (dialogue box, buttons, windows)
- **Fonts:** Blackletter (UnifrakturMaguntia) for character names, warm readable serif (PT Serif) for dialogue and interface text

> **Note:** The colors and spacing are in place; the actual carved-frame art assets are still being sourced. See [Status](#-status) below.

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
│   │   ├── silhouettes/           # Silhouette backgrounds (90% of scenes)
│   │   ├── major_moments/         # Full AI-generated images (10% of scenes)
│   │   └── gui/                   # Custom UI assets (future)
│   └── scripts/
│       ├── prologue.rpy           # The shipwreck and escape sequence
│       ├── frozen.rpy             # Frozen Kingdom storyline
│       ├── tree.rpy               # Tree Kingdom storyline
│       ├── sandy.rpy              # Sandy Shores storyline
│       ├── swamp.rpy              # Swamp Kingdom storyline
│       └── endings.rpy            # All possible endings
├── make_backgrounds.py            # Script used to generate placeholder art
├── .gitignore
└── README.md
```

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

| Kingdom | Status | Progress |
|---------|--------|----------|
| Prologue | 🚧 In Development | 50% |
| Frozen Kingdom | 📝 Outlined | 0% |
| Tree Kingdom | 📝 Outlined | 0% |
| Sandy Shores | 📝 Outlined | 0% |
| Swamp Kingdom | 📝 Outlined | 0% |

*Currently working on: Prologue, UI customization, and sourcing carved-frame art assets.*

---

## 📌 Roadmap

- [x] Repository setup and initial commit
- [x] GUI theme foundation (colors, fonts, spacing)
- [x] Placeholder menu backgrounds
- [ ] Source/create carved-wood-and-metal frame art (`frame.png`, button backgrounds, namebox)
- [ ] Final illustrated main menu / game menu backgrounds
- [ ] Complete prologue (escape sequence + kingdom selection)
- [ ] Write full Frozen Kingdom storyline
- [ ] Generate silhouettes and major moments for Frozen Kingdom
- [ ] Release Chapter 1 demo
- [ ] Write remaining 3 kingdoms
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
