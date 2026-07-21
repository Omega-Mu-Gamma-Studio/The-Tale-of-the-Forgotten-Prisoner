# prologue.rpy
#
# The Prologue: The Ship, The Kraken, The Escape.
#
# Structure:
#   prologue_start          - chains, the guard, the player's name, the attack
#   prologue_choice_action  - "what kind of person are you when the ship dies"
#   prologue_choice_current - "which way does the sea take you" (skipped if
#                              the player chose the instinct/dive option)
#   prologue_resolve        - combines both choices into a kingdom, organically,
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

    "For half a second, in the spray and the dark, you see a face that isn't yours reflected in the water. You don't know if it's memory or nightmare."

    "You never do."

    "The ship is going down, and you have seconds left to decide what kind of person drowns, and what kind of person doesn't."

label prologue_choice_action:

    menu:
        "Fight your way toward a lifeboat — haul yourself over anyone in your path.":
            $ escape_action = "bold"
            "You don't ask permission. Elbows, knees, the flat of a broken oar — whatever gets you to the boat gets used."
            "Somewhere behind you, someone screams a name. You don't look back to find out whose voice it was."

        "Let go of everything and dive straight down into the black water.":
            $ escape_action = "instinct"
            "You stop thinking. Your body decides for you, folding down and under, away from the splintering wood and the thing with too many eyes."
            "The cold swallows the sound of the ship dying above you."

        "Grab the nearest wreckage and hold on — let the sea decide what happens next.":
            $ escape_action = "fatalist"
            "You've made peace with worse odds than this. You wrap both arms around a shattered spar and stop fighting the water."
            "If you were meant to answer for what you did, the sea can decide that too."

        "Reach for the prisoner chained beside you — you can't leave him to drown.":
            $ escape_action = "compassion"
            "You don't know his name. You never asked. But his hands are shaking too hard to work the lock, and you can't make yourself let go of him."
            "Whatever you did to end up here, it wasn't this. It was never this."

    if escape_action == "instinct":
        jump prologue_resolve

    jump prologue_choice_current

label prologue_choice_current:

    "The current has you now, and it's stronger than anything you can fight for long."

    menu:
        "Fight it — aim for the cold, dark line of a horizon to the north.":
            $ escape_current = "north"
            "The water turns colder with every stroke, biting at your fingers until you can't feel them anymore. Something in you insists this is right anyway."

        "Stop fighting — let the warm current carry you south, wherever it leads.":
            $ escape_current = "south"
            "The water is warmer here. It's easier to let it take you than to keep pretending you have any control left."

    jump prologue_resolve

label prologue_resolve:

    python:
        # The kingdom is never chosen directly by the player — it falls out
        # of the two choices above, the way real panic-decisions actually
        # narrow your options for you.
        if escape_action == "instinct":
            kingdom = "rhizoma"
        elif escape_current == "north":
            kingdom = "khionia"
        elif escape_action == "bold":
            kingdom = "arenia"
        else:
            # fatalist or compassion, heading south
            kingdom = "helos"

    "The sea does not release you gently. It never does."

    "Somewhere in the dark, the ship finishes dying without you. And somewhere else — a shore you can't see yet, in a kingdom that doesn't know your name — the water is already deciding where to put you down."

    if kingdom == "khionia":
        jump khionia_arrival
    elif kingdom == "rhizoma":
        jump rhizoma_arrival
    elif kingdom == "arenia":
        jump arenia_arrival
    elif kingdom == "helos":
        jump helos_arrival
