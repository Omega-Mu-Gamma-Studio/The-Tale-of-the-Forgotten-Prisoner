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

    scene black
    with dissolve

    "— End of Prologue Demo: Helos route —"

    "What happens next is written in PREMISES.md, but not yet in code: spells that go hilariously, dangerously wrong, a witch who's more lonely than chaotic, and a voice in the swamp that isn't hers."

    "That's the next thing we build."

    return
