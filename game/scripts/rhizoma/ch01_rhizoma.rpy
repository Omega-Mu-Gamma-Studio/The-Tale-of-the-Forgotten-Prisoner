# ch01_rhizoma.rpy — Rhizoma, Root of Life — Chapter 1
#
# Full storyline: merchant's apprentice, Thalloa, the Canopy Lord draining
# the Heartwood. This chapter covers the Arrival + Incident beats.
# Chapter 2 goes in ../rhizoma/ch02_rhizoma.rpy — see CHAPTER_TEMPLATE.md
# at the repo root for the beat/choice structure every chapter should follow.

define thalloa = Character("Thalloa", color="#8fbf7f")
define merchant = Character("The Merchant", color="#c9a15a")

label rhizoma_arrival:

    scene black
    with dissolve

    "The current doesn't let go of you. It drags you down and sideways, through some hidden seam in the seafloor, and the world above disappears entirely."

    "You wake tangled in roots the size of ship masts, coughing up water that shouldn't exist this far underground. Bioluminescent fungus glows dull gold along the walls — enough light to see by, and no more."

    "A girl crouches a few feet away, picking glowing mushrooms with the unhurried calm of someone who has never once been surprised by an unconscious stranger washing up in her cave."

    thalloa "You're not from the roots."

    thalloa "Come on, then. Slowly. I know someone who'll give you work, if you can still hold your hands steady."

    "You don't know where 'up' is anymore. You're not sure it matters."

    jump rhizoma_incident

label rhizoma_incident:

    scene black
    with dissolve

    "The merchant's name gets spoken with more reverence than kings get, back where you're from. Down here, it just earns you a nod and slightly better pay."

    "He puts you to work sorting fungi by grade, weighing amber by the ounce, learning which root-essence cures a fever and which one stops a heart. The work is simple. Repetitive. Safer than anything's been in longer than you can remember."

    "You're good at it. Better than good, though it takes three weeks before anyone notices why."

    merchant "You don't haggle like a Root-person."

    "You don't. You haggle like someone who's watched merchants in a dozen ports lie to sailors, farmers, and each other — every trick you never meant to learn, surfacing now because apparently some part of your old life survived the kraken even if your memory of it didn't."

    merchant "Do that again. With the guild buyer, this time. Let's see if it was luck."

    "It wasn't luck. Word travels fast in tunnels with nowhere else for it to go, and within a month the guild is watching you the way people watch a card sharp they haven't decided whether to hire or ban."

    thalloa "You've changed more in a season than this place changes in a decade."

    "She says it like it's a warning, not a compliment. You're starting to understand that from Thalloa, sometimes those are the same thing."

    "Then you make the mistake that almost gets you both killed."

    scene black
    with vpunch

    "A noble family orders a delicacy mushroom for a feast — rare, expensive, and nearly identical to a species that stops a grown man's heart inside the hour if it's harvested a single day too early."

    "You didn't know the difference mattered. Nobody told you. By the time anyone realizes what's wrong, the noble's youngest son is on the floor, and the finger is already pointing at you."

    "The guild wants blood. Yours, specifically."

    menu:
        "Take responsibility. It was your hands that served it.":
            $ reckoning_adjust("confess")
            $ rp_adjust("thalloa", 1)

            "'It was me,' you say, before anyone else can decide the story for you. 'My hands. My mistake. Nobody else's.'"

            "It doesn't make the guild elders any less furious. But Thalloa's expression shifts — something between relief and worry, like she'd braced for you to be someone smaller than that."

        "Say no one taught you the difference. Let the blame land elsewhere.":
            $ reckoning_adjust("hide")
            $ rp_adjust("merchant", 1)
            $ rp_adjust("thalloa", -1)

            "'Nobody told me,' you say. It's even true. 'How was I supposed to know?' The guild elders' attention drifts, just slightly, toward the merchant who trained you and never once mentioned the difference."

            "Thalloa doesn't say anything. She doesn't have to — the look on her face makes it clear she noticed exactly what you just did, and exactly who it cost."

    thalloa "He didn't do it on purpose! He's still learning our roots, he's still—"

    "She's shouting at her own master now, in front of guild elders, in front of everyone. You've never once seen her raise her voice."

    merchant "Enough, Thalloa."

    "He says it the way you imagine he says everything — flat, unreadable, already three moves ahead of the room."

    merchant "The boy stays alive. Under my protection. My name against the guild's suspicion — a costly thing to spend, so understand this clearly: you don't work for me anymore. You belong to my ledger now, same as any debt. And I intend to collect."

    "It isn't a rescue. Not really. It's a purchase, dressed up as mercy, and you're too tired and too frightened to argue with the difference."

    "That night, Thalloa finds you in the tunnel outside your room."

    thalloa "He'll use you. Whatever he wants you for — trade routes, secrets, things that aren't fungi and amber — he'll use every bit of you until there's nothing useful left."

    thalloa "I couldn't stop that. I'm sorry. I could only make sure you were alive to be used."

    "You don't know what to say to that. Nobody's fought that hard for you in longer than you can remember — which, these days, isn't saying much."

    scene black
    with dissolve

    "— End of Chapter 1: Rhizoma —"

    "What happens next is written in PREMISES.md, but not yet in code: a merchant with ambitions that go well past trade, a Canopy Lord slowly killing the tree everyone down here depends on, and a girl who's been able to hear that tree her whole life — telling it that you might be the reason it's still breathing at all."

    # Once ch02_rhizoma.rpy exists with a "label rhizoma_ch02:" at the top,
    # replace this "return" with "jump rhizoma_ch02".
    return
