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
# player makes. Hidden from the player at all times; it surfaces only
# through nightmares, memory-fragments, and NPC reactions, per PREMISES.md.
#
# Canon: the player stole the crown jewel of a prince. They believe they
# were justified — but a crime is a crime, and it's why they were on the
# ship to begin with. Never state this outright in a scene; hint at it
# (a glint of gold, a flash of a throne room, a guard's odd reaction)
# and let the player piece it together over time.
default true_crime = "stole_the_crown_jewel"

# The Prologue's escape sequence is two simple binary choices:
#   priority: what the player cares about in the moment ("self" or "other")
#   response: how the player meets the sea ("fight" or "trust")
# The 2x2 combination funnels the player into a kingdom organically —
# they are never shown a literal "pick your kingdom" menu.
default priority = None
default response = None

# The kingdom the player ends up in: "khionia", "rhizoma", "arenia", or "helos".
default kingdom = None
