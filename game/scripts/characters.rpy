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


# --- The Reckoning (confess / hide / embrace) ---
# Per PREMISES.md: when the player eventually learns the truth of their
# crime, they have to decide whether to confess it, hide from it, or
# embrace it. That's not one choice at the end — it's the sum of how the
# player has been handling truth and blame all game, across every kingdom.
# Nudge this at any morally-loaded choice point, in any route, well before
# the player consciously knows what it's building toward.
default reckoning = {
    "confess": 0,
    "hide": 0,
    "embrace": 0,
}

# --- Relationship Points (RP) ---
# One entry per NPC/LI currently written into the story. This is a starting
# roster, not a ceiling — use rp_adjust() below for anyone new so a writer
# can reference a brand-new NPC without having to edit this dict first.
default relationship = {
    # Khionia
    "asteria": 0,
    "valerius": 0,
    "leontios": 0,
    "chef": 0,
    # Rhizoma
    "thalloa": 0,
    "merchant": 0,
    # Arenia
    "aurea": 0,
    # Helos
    "sidea": 0,
}

init python:

    def rp_adjust(npc, amount):
        """Nudge relationship points for any NPC, current or future.
        Auto-creates the entry at 0 if it isn't in the dict yet, so new
        NPCs don't require touching this file first.
        Usage: $ rp_adjust("asteria", 1)
        """
        relationship[npc] = relationship.get(npc, 0) + amount

    def reckoning_adjust(kind, amount=1):
        """Nudge the confess/hide/embrace tracker.
        kind must be one of "confess", "hide", "embrace".
        Usage: $ reckoning_adjust("hide")
        """
        if kind not in reckoning:
            raise Exception("reckoning_adjust: unknown kind '%s' — must be confess, hide, or embrace" % kind)
        reckoning[kind] += amount

    def reckoning_leaning():
        """Returns the currently-dominant tendency as a string. Used at the
        convergence/ending stage to help shape which ending the player is
        heading toward. Ties favor 'hide', then 'embrace', then 'confess' —
        on the theory that silence is the easiest default to fall into."""
        top = max(reckoning.values())
        for key in ("hide", "embrace", "confess"):
            if reckoning[key] == top:
                return key
        return "hide"
