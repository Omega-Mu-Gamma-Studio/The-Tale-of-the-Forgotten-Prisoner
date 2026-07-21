# The script of the game goes in this file.
#
# The actual story lives in game/scripts/ — this file just kicks things off.
# See:
#   scripts/characters.rpy  - shared character defs + persistent story vars
#   scripts/prologue.rpy    - the ship, the kraken, the escape
#   scripts/frozen.rpy      - Khionia (the Frozen Kingdom)
#   scripts/tree.rpy        - Rhizoma (the Root Kingdom)
#   scripts/sandy.rpy       - Arenia (the Golden Kingdom)
#   scripts/swamp.rpy       - Helos (the Swamp Kingdom)

label start:

    jump prologue_start
