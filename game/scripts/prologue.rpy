# prologue.rpy
#
# The Prologue: The Ship, The Kraken, The Escape.
#
# Structure:
#   prologue_start           - chains, the guard, the player's name, the attack
#   prologue_choice_priority - "what matters to you as the ship dies" (self/other)
#   prologue_choice_response - "how do you meet the sea" (fight/trust)
#   prologue_resolve         - combines both choices into a kingdom, organically,
#                              and jumps to that kingdom's arrival scene
#
# No art assets exist yet. Every scene here uses "scene black" on purpose —
# nothing below depends on an image file existing. Swap these for silhouette
# art later without touching any of the logic.

label prologue_start:

    scene black
    with dissolve

    "The chains have worn smooth against your wrists."

    "You stopped counting the days somewhere past the fortieth knot scratched into the ceiling beam above your head."

    "You don't remember your crime. Not exactly. You remember the weight of it — the way a room goes quiet when you enter it, the way a length of rope feels different when it's meant for you — but not the shape of it. Not the truth."

    "The guards know. The guards don't talk."

    "What you do know is this: you are cargo now. Bound for a coastline you will never see, to answer for a crime you can no longer name."

    guard "On your feet. The manifest needs a name before the Warden feeds you to the ledger with the rest of the dead men."

    $ pname = renpy.input("What name is left to you?", default="").strip()

    if pname == "":
        $ pname = "Nameless"

    $ fullname = pname + " " + protagonist_surname

    "[pname]. It isn't really yours anymore — not after what you did to lose it. But it's the only thing left that they haven't taken."

    guard "[pname] [protagonist_surname]. Convicted of—"

    guard "...doesn't matter what you're convicted of. You'll be dead by the new moon regardless."

    "He doesn't finish the sentence. He never does. Even the guards flinch away from saying it out loud."

    "The ship groans around you. Somewhere below deck, chains rattle against wood in a rhythm that isn't the sea's."

    "Then the ship stops groaning, and starts screaming."

    scene black
    with vpunch

    "The first hit throws you against the hull hard enough to see white. The second hit isn't a wave."

    "Something vast moves beneath the ship — too large, too deliberate, too many eyes catching the storm-light beneath the black water."

    "The Kraken has found you. It does not care that you were already condemned."

    "Wood splits. Water floods in cold and immediate, and around you chained men scream the names of gods they stopped believing in three ports ago."

    "For half a second, in the spray and the dark, something glints gold in your palm that has no business being there — gone before you can close your fist around it."

    "A memory, maybe. Or a habit that never really left you."

    "The ship is going down, and you have seconds left to decide what kind of person drowns, and what kind of person doesn't."

label prologue_choice_priority:

    menu:
        "Your own survival. Nothing else matters right now.":
            $ priority = "self"
            "You stop thinking about anyone else on this ship. There isn't room for anyone else in your head right now — not if you want to still have a head in five minutes."

        "The prisoner chained beside you — you won't let him drown alone.":
            $ priority = "other"
            "You don't know his name. You never asked. But his hands are shaking too hard to work his own lock, and you can't make yourself let go of him."

    jump prologue_choice_response

label prologue_choice_response:

    "The current has you now, and it doesn't care what you just decided."

    menu:
        "Fight it. Force it to bend to you.":
            $ response = "fight"
            "You claw against the water with everything you have left, refusing to let the sea choose for you."

        "Trust it. Let it decide where you end up.":
            $ response = "trust"
            "You stop fighting. Whatever's waiting on the other side of this, exhausting yourself first won't change it."

    jump prologue_resolve

label prologue_resolve:

    python:
        # A clean 2x2 funnel. The player never sees this table — it's just
        # the sum of two panic-decisions made in the dark.
        if priority == "self" and response == "fight":
            kingdom = "arenia"
        elif priority == "self" and response == "trust":
            kingdom = "rhizoma"
        elif priority == "other" and response == "fight":
            kingdom = "khionia"
        else:
            # other + trust
            kingdom = "helos"

    "The sea does not release you gently. It never does."

    "Somewhere in the dark, the ship finishes dying without you. And somewhere else — a shore you can't see yet, in a kingdom that doesn't know your name — the water is already deciding where to put you down."

    if kingdom == "khionia":
        jump khionia_ch01
    elif kingdom == "rhizoma":
        jump rhizoma_ch01
    elif kingdom == "arenia":
        jump arenia_ch01
    elif kingdom == "helos":
        jump helos_ch01
