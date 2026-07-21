# The script of the game goes in this file.
#
# The actual story lives in game/scripts/ — this file just kicks things off.
# See:
#   scripts/characters.rpy       - shared character defs + persistent story vars
#   scripts/prologue.rpy         - the ship, the kraken, the escape
#   scripts/khionia/ch01_khionia.rpy   - Khionia (the Frozen Kingdom), chapter 1
#   scripts/rhizoma/ch01_rhizoma.rpy   - Rhizoma (the Root Kingdom), chapter 1
#   scripts/arenia/ch01_arenia.rpy     - Arenia (the Golden Kingdom), chapter 1
#   scripts/helos/ch01_helos.rpy       - Helos (the Swamp Kingdom), chapter 1
#
# Each kingdom gets its own subfolder. Chapter 2 of Khionia goes in
# scripts/khionia/ch02_khionia.rpy, chapter 3 in ch03_khionia.rpy, and so on —
# see CHAPTER_TEMPLATE.md at the repo root for the beat/choice structure to
# follow in every new chapter file.

label start:

    jump prologue_start
