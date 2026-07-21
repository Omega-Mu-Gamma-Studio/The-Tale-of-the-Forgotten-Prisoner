# characters.rpy
#
# Shared character definitions and persistent story variables.
# Kingdom-specific NPCs (Asteria, Thalloa, Aurea, Sidea, etc.) are defined
# in their own kingdom script files, right next to the scenes that use them.

# --- The Protagonist ---
# The player enters a first name during the Prologue. The surname is fixed
# narrative canon and is never presented as a choice.
define protagonist_surname = "Alessios"

# --- Narrator / unnamed voices used in the Prologue ---
define guard = Character("A Guard", color="#8a8a8a")


# --- Persistent story state ---

# Player-chosen first name, and the combined full name once it's known.
default pname = ""
default fullname = ""

# The player's crime. FIXED — does not change based on any choice the
# player makes. Hidden from the player at all times unless a scene
# explicitly reveals a piece of it.
#
# This is a placeholder value so later scenes (nightmares, NPC reactions,
# memory-fragments) have something consistent to reference. The real,
# final answer is a worldbuilding decision we should nail down together
# before writing any scene that reveals part of it.
default true_crime = "accident"

# Which "temperament" choice and which current the player picked during
# the Prologue's escape sequence. These funnel the player into a kingdom
# organically — the player is never shown a literal "pick your kingdom" menu.
default escape_action = None
default escape_current = None

# The kingdom the player ends up in: "khionia", "rhizoma", "arenia", or "helos".
default kingdom = None
