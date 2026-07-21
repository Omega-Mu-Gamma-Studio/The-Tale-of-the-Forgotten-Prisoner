# sandy.rpy — Arenia, Land of Gold
#
# Kingdom 3. Full storyline: enslavement to Aurea the mercenary, the slow
# rise toward trust and freedom. Only the Arrival beat is written here —
# see PREMISES.md for everything past this point.

define aurea = Character("Aurea", color="#d1a24a")

label arenia_arrival:

    scene black
    with dissolve

    "Sand, first. Fine as powdered sunlight, hot even through your ruined clothes, grinding into every cut the sea left on you."

    "You're face-down before you register you've stopped moving. Breathing is a decision you have to make on purpose now."

    "A shadow falls over you — leather, sand-caked boots, a sword already half-drawn. Whoever she is, she didn't come to help. She came to see what the sea dragged in worth looting."

    aurea "Huh. Still breathing. That's new."

    "You talk. You don't remember deciding to, and you definitely don't remember what you said — something desperate, something that makes her laugh, sharp and hollow, like she hasn't done it in a while."

    "She doesn't sheath the sword. But she doesn't use it either."

    jump arenia_incident

label arenia_incident:

    scene black
    with dissolve

    "She doesn't kill you. That's the whole negotiation, really — she doesn't kill you, and in exchange you don't ask what she'd have done if your excuses had been worse."

    "What she does instead is worse in a different way. There's a click at your throat before you fully understand what's happening, and then the weight of it — cold iron, heavier than it has any right to be, locked with a key she doesn't show you."

    aurea "There. Now you're mine. Try to run and I'll assume you'd rather I'd left you for the sand."

    menu:
        "Test the collar the moment her back is turned.":
            $ reckoning_adjust("embrace")
            $ rp_adjust("aurea", -1)

            "You test it anyway, once, quietly, when she isn't looking. It doesn't budge. Neither does she, when she catches you at it."

            aurea "Don't. I've killed men for less insulting attempts than that."

            "You believe her completely. It doesn't stop you from testing it — some part of you has already decided that surviving means never fully trusting the hand that spared you."

        "Stay still. Don't give her a reason.":
            $ reckoning_adjust("hide")
            $ rp_adjust("aurea", 1)

            "You don't test it. Not once. Whatever's coming, you decide, it isn't worth finding out the hard way what she meant by 'insulting attempts.'"

            aurea "Smart. Most people try it in the first hour. You'd be surprised how few make it to the second."

    "Everyone believes her — it's the whole reason the Falcon of the West walks this desert without an escort, and nobody's ever stupid enough to test it, not twice."

    "So you carry her supplies. You hold her horse. You learn, fast, which questions get answered and which ones earn a look that ends the conversation permanently."

    "It should feel like the worst thing that's happened to you since the ship went down. Instead, three days in, you catch yourself almost grateful — for the water she shares without being asked, for the fact that she hasn't once mentioned turning you in for whatever bounty a nameless escaped prisoner might be worth."

    "You don't say that out loud. You're fairly sure saying it out loud gets you killed faster than the running would."

    "It's on the fourth night, over a fire she clearly didn't want to build for company, that you say something — you don't even remember what, something stupid and half-delirious from exhaustion — and she laughs."

    "Not the sharp, hollow sound from the beach. A real one. Surprised out of her, like she'd forgotten she still had it in her."

    aurea "Gods. Don't do that again."

    "She doesn't explain why. You don't ask. But you notice, after that, that she stops checking whether you're still following quite so often — like some part of her has already decided you're not going anywhere."

    "You're still wearing the collar. She's still, technically, your owner. But something about the way she says it now sounds less like a threat, and more like she's daring herself to believe it."

    scene black
    with dissolve

    "— End of Demo: Arenia route —"

    "What happens next is written in PREMISES.md, but not yet in code: a slave trader who knows more about your past than he should, a cursed vein of gold buried beneath the Salt Flats, and a woman who hasn't kept anyone alive in years finding out exactly why that's starting to terrify her."

    "That's the next thing we build."

    return
