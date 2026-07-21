# swamp.rpy — Helos, Land of Darkness
#
# Kingdom 4. Full storyline: bound to Sidea the young witch, chaotic magic,
# something old whispering in the swamp. Only the Arrival beat is written
# here — see PREMISES.md for everything past this point.

define sidea = Character("Sidea", color="#a480c9")

label helos_arrival:

    scene black
    with dissolve

    "Mist first, then mud, then the sound of something large sliding into black water very close to where you're lying."

    "Alligators. Three, maybe four, drawn by the smell of blood and salt on your skin. You're too weak to do anything but watch them circle."

    "Then — light. A bolt of violet fire cracks across the water and the alligators scatter, hissing, back into the dark."

    "A girl steps out of the mist. She can't be older than twenty, staff still smoking faintly at the tip, and she's looking at you less like someone she just saved and more like something she just found."

    sidea "Oh, good, you're alive. Hold still — this might feel strange."

    "She waves the staff before you can ask what 'this' means. Something cold and glowing wraps around your wrist like a bracelet made of frost and static."

    sidea "There. Now you can't leave. Don't worry — it's not permanent. Probably. I haven't figured out how to undo it yet."

    jump helos_incident

label helos_incident:

    scene black
    with dissolve

    "The curse — she insists on calling it a 'binding,' like that's less alarming — settles into your skin within the hour. Cold, faint, and always exactly where your pulse is loudest."

    sidea "Okay. So. Small chance it kills you if I don't figure out the counter-spell in time. But a much bigger chance it doesn't! Statistically speaking."

    "You ask what the statistics actually are. She changes the subject."

    "She sets up camp on a dry hummock somewhere in the middle of the mist, and it becomes clear within the first day that Sidea knows an enormous number of spells and approximately none of their consequences."

    "She tries to heal the gash on your arm from the wreckage. Your arm spends the next three hours as a tentacle. It works remarkably well as a tentacle, which somehow makes it worse."

    sidea "In my defense, that's *technically* still an arm."

    "She tries to burn off your fever. You start glowing faintly in the dark instead — a soft, sourceless purple-white that doesn't fade by morning, or the morning after that."

    sidea "Okay, that one might be permanent. But you make excellent company on night watch now, so really, we've gained something."

    "You point out that you didn't ask to glow. She points out that you didn't ask to nearly die in a swamp either, and life is full of surprises."

    "It's hard to stay angry at her. You try, a little, out of principle. It doesn't take."

    "She talks constantly — about spell theory, about the Deep, about the causeway merchants who won't sell to her anymore after the last 'incident' — and it takes you longer than it should to notice that she's not just filling silence. She's starving for it."

    sidea "...Sorry. You probably don't want the full history of everyone who's ever refused to teach me anything. I just — don't really get to talk. Out here."

    "It's the first honest thing she's said since the alligators. Something about it loosens your own tongue, just slightly."

    menu:
        "Tell her something true — the ship, the chains, the crime you can't quite remember.":
            $ reckoning_adjust("confess")
            $ rp_adjust("sidea", 1)

            "You tell her. Not all of it — you don't have all of it to give — but the ship, the chains, the shape of a crime you can't quite name. It's the first time you've said any of it out loud since it happened."

            sidea "...Huh. Okay. That's a lot heavier than 'don't really get to talk out here,' but I asked for honesty, so. Thank you. For trusting me with it."

            "She doesn't push for more. That, somehow, makes it easier to have said anything at all."

        "Say nothing. Let the moment pass.":
            $ reckoning_adjust("hide")

            "You almost tell her. The words get as far as your throat before you swallow them back down, and the moment passes the way moments do — quietly, without either of you acknowledging it happened."

            "The binding spell chooses that exact moment to hum warm against your wrist, like it noticed too."

    "That night, you wake to her sitting bolt upright at the edge of the hummock, staff gripped white-knuckled, staring out into mist that has gone very, very quiet."

    sidea "...Did you hear that?"

    "You didn't. You're not sure you want to."

    "She doesn't explain. She doesn't sleep again that night, either — and for the first time since you woke up in this swamp, the curse on your wrist feels less like the most dangerous thing out here."

    scene black
    with dissolve

    "— End of Demo: Helos route —"

    "What happens next is written in PREMISES.md, but not yet in code: a witch who's more afraid of her own power than she'll admit, a heart-shaped relic pulsing somewhere in the deepest water, and something old that's been talking to the swamp long before Sidea ever arrived."

    "That's the next thing we build."

    return
