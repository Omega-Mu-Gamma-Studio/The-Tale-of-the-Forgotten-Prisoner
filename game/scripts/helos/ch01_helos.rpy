# ch01_helos.rpy — Helos, Land of Darkness — Chapter 1
# "From Darkness, Light"
#
# Full storyline: swamp survival, Sidea the young witch,
# the binding spell, chaotic magic, and the voice in the swamp.
# Chapter 2 goes in ../helos/ch02_helos.rpy

define sidea = Character("Sidea", color="#a480c9")
define voice = Character("???", color="#6a5a7a")

label helos_ch01:

    scene black
    with dissolve

    "Warmth reaches you before land does."

    "The water is warm, thick, and smells of decay. Your clothes are soaked. Your limbs are heavy. You wake face-down in murky water, your mouth filled with silt. You can barely lift your head."

    "You hear a gurgle—a bubble rising from the mud. It smells like rot."

    scene silhouette_helos_marsh
    with fade

    "You're in a swamp. Black water stretches in every direction. Twisted trees rise from the water, their roots exposed like grasping fingers. Hanging moss drips from the branches. The air is thick with mist."

    "You hear movement. A ripple in the water. Then another. You turn your head."

    "There are four of them. Their eyes break the surface, cold and unblinking. They're circling you. They're waiting."

    menu:
        "How do you react?"
        "Freeze":
            $ helos_first_reaction = "freeze"
            "You hold perfectly still. They might lose interest. They might not. You feel the water shift around you."
        "Swim":
            $ helos_first_reaction = "swim"
            "You make a break for the nearest tree. Your muscles burn. The water is thick. But you're fast."
        "Splash":
            $ helos_first_reaction = "splash"
            "You thrash, trying to scare them off. It's loud, chaotic, desperate. Mud splatters your face."

    "One of the alligators lunges. You see its jaws open. You can smell its breath—warm, wet, and hungry. Its teeth are inches from your face."

    "A bolt of purple light shoots past your head. It strikes the water between you and the alligator. The creature recoils, hissing. The others scatter."

    "You feel the shockwave—a pulse of heat and energy that ripples through the water."

    "A figure emerges from the mist."

    jump helos_scene2

label helos_scene2:

    "She's young. Barely out of her teens. Her clothes are mismatched—a tattered cloak, a patched dress, boots that are too big for her feet. She's holding a staff that's taller than she is, and it's still crackling with purple energy."

    "She looks at you. She tilts her head."

    sidea "Oh. You're alive. That's inconvenient."

    "She studies you. Her eyes are wide and curious."

    sidea "I was hoping for a corpse. I need fingers for a spell."

    "She pauses. She seems almost sorry."

    sidea "Don't take it personally. I just really need those fingers."

    menu:
        "How do you respond?"
        "Grateful":
            $ helos_approach = "grateful"
            "'You saved my life. Thank you.' You're polite. Grateful."
        "Demanding":
            $ helos_approach = "demanding"
            "'Who are you? What is this place?' You're trying to get your bearings."
        "Exhausted":
            $ helos_approach = "exhausted"
            "You just stare at her. You're too weak to speak. You're at her mercy."

    sidea "Don't thank me yet. I need something from you."

    "She raises her staff. She speaks words that sound ancient—wrong, somehow. A purple light swirls around her. It wraps around your wrist."

    jump helos_scene3

label helos_scene3:

    "The spell wraps around your wrist like a cold hand. You feel it settle into your bones. It's heavy. It's cold. It whispers in your ear at night. You can feel it in your soul."

    "The purple light fades. You look at your wrist. There's a mark there—a spiral, pulsing faintly. It doesn't hurt. But it's there. And you can feel it."

    sidea "There. Now you can't leave."

    menu:
        "How do you react to the binding spell?"
        "Panic":
            $ helos_binding_reaction = "panic"
            "'What did you do to me? Take it off!' You're afraid. Angry."
        "Curiosity":
            $ helos_binding_reaction = "curious"
            "'What does it do?' You're trying to understand."
        "Resignation":
            $ helos_binding_reaction = "resigned"
            "You just look at it. You've been collared, chained, cursed. This is just another cage. You're exhausted. You don't have the energy to fight."

    sidea "It's not permanent. Probably. I haven't figured out how to undo it yet."

    "She's not lying. You can see it in her eyes—she's terrified. She doesn't know what she's doing. She's learning. And you're her test subject."

    "You feel it pulse. It's almost like a heartbeat."

    sidea "You can't leave my side. You can't hurt me. And if I die, you die."

    "She pauses."

    sidea "I think. I'm still working on the details."

    jump helos_scene4

label helos_scene4:

    scene silhouette_helos_hut
    with fade

    "She leads you to her home—a small hut built on stilts in the middle of the swamp. It's cluttered with books, jars, dried herbs, and strange artifacts. She has a workbench covered in half-finished spells."

    sidea "I need to test something. Hold still."

    menu:
        "Do you trust her?"
        "Yes":
            $ helos_trust = True
            "You hold still. You want to see what she can do. You're curious. You're building trust."
        "No":
            $ helos_trust = False
            "You step back. You don't trust her magic. You're cautious. She's annoyed."
        "Bargain":
            $ helos_trust = False
            "'If it goes wrong, you'll fix it. Right?' She shrugs. You're not fully trusting her, but you're cooperating."

    "She waves her staff. She says a word. Purple light swirls around you."

    "You feel a tingle. Then a warmth. Then a wrongness."

    "Your arm begins to change. It stretches. It twists. You watch in horror as your hand turns into a tentacle—long, sinuous, covered in suckers."

    "She stares. Her face goes pale."

    sidea "Oh. That's new."

    "She starts flipping through her book frantically, muttering:"

    sidea "That's not what it was supposed to do. That's not—"

    menu:
        "How do you react to the mutation?"
        "Panic":
            $ helos_mutation = "panic"
            "'Turn it back! Turn it back now!' You're terrified."
        "Fascination":
            $ helos_mutation = "fascinated"
            "'What... what did you do?' You're curious. Horrified, but curious."
        "Laughter":
            $ helos_mutation = "laughter"
            "You start laughing. It's absurd. You're a prisoner, a test subject, and now you have a tentacle for an arm. You're coping with the absurdity."

    sidea "It should wear off in three hours. Probably."

    jump helos_scene5

label helos_scene5:

    "You're sitting in her hut. The tentacle is slowly turning back into an arm. She's watching you, studying you. She hasn't had anyone to talk to in a long time."

    menu:
        "What do you talk about?"
        "Her":
            $ helos_talk = "her"
            "'How long have you been alone?' You're trying to understand her."
        "Yourself":
            $ helos_talk = "you"
            "'I was on a ship. A prisoner. A kraken attacked.' You're sharing your story."
        "The swamp":
            $ helos_talk = "swamp"
            "'What is this place? What's out there?' You're trying to understand the world."

    sidea "I've been alone for years. I tried to find other witches. They were all dead. Or worse."

    "She looks away. Her voice is smaller now."

    sidea "The binding spell wasn't just to keep you close. It was to keep you with me."

    "She's not just a chaotic witch. She's desperately lonely."

    sidea "I don't even know your name."

    menu:
        "What name do you give her?"
        "Real name":
            $ helos_name = "real"
            "You tell her. You're trusting her."
        "Fake name":
            $ helos_name = "fake"
            "You give her a false name. You're protecting yourself."
        "No name":
            $ helos_name = "none"
            "'I don't remember.' You're hiding. Or you're telling the truth."

    sidea "That's okay. I'll call you something."

    "She pauses. A grin spreads across her face."

    sidea "Tentacle. I'll call you Tentacle."

    "You groan. She smiles. It's the first time you've seen her genuinely happy."

    jump helos_scene6

label helos_scene6:

    "She's trying to fix your arm. She's reading from a book."

    sidea "This should work. I think."

    menu:
        "How do you prepare?"
        "Distract her":
            $ helos_prep = "distract"
            "'Tell me more about the swamp.' You're trying to help her relax."
        "Watch closely":
            $ helos_prep = "watch"
            "You want to see what she does. You're learning."
        "Close your eyes":
            $ helos_prep = "close"
            "You don't want to see it if it goes wrong. You're scared."

    "She casts the spell. It works—your arm is normal again. But something else happens."

    "You start to glow. A soft, ethereal light emanates from your skin."

    sidea "Oh. You're glowing. That's... new."

    "There's a look in her eyes—she's studying you. She's trying to understand how it happened."

    sidea "It might be permanent. I'm not sure."

    "But her eyes are calculating. She's already thinking about how this could be useful—or dangerous."

    menu:
        "How do you react?"
        "Amused":
            $ helos_glow = "amused"
            "'I'm a lamp now.' You're leaning into the absurdity."
        "Annoyed":
            $ helos_glow = "annoyed"
            "'Fix it. Now.' You're losing patience."
        "Curious":
            $ helos_glow = "curious"
            "'Can I control it?' You're experimenting."

    sidea "I don't know. Let's find out."

    jump helos_scene7

label helos_scene7:

    scene silhouette_helos_night
    with fade

    "Night falls. The swamp is dark and alive with sounds—insects, frogs, something larger moving in the water. Sidea is asleep. You're awake, watching the mist."

    "You hear something. A whisper. It's faint, almost inaudible."

    voice "...you shouldn't be here..."

    menu:
        "What do you do?"
        "Wake Sidea":
            $ helos_voice = "wake"
            "You shake her awake. 'I heard something.' You're afraid. You need her."
        "Investigate":
            $ helos_voice = "investigate"
            "You step outside. You follow the voice. You're curious. You might be making a mistake."
        "Ignore it":
            $ helos_voice = "ignore"
            "You stay in the hut. You try to sleep. You're trying to avoid the inevitable."

    "The voice is still there. It's old. It's patient."

    voice "...she doesn't know what she's doing. She'll hurt you. She'll hurt herself. You need to leave."

    "You look at Sidea. She's sleeping soundly, her staff beside her. She looks young. Vulnerable."

    "The voice pauses. Then, softer:"

    voice "She's so lonely."

    voice "But you can't leave. She bound you. She did it to keep you."

    "The voice isn't angry. It's sad."

    voice "She doesn't even know your name."

    jump helos_scene8

label helos_scene8:

    scene silhouette_helos_morning
    with fade

    "You wake up. The glow has faded, but your skin still has a faint shimmer. Sidea is already awake, making tea."

    sidea "I think I figured out how to undo the binding."

    menu:
        "How do you respond?"
        "Relieved":
            $ helos_morning = "relieved"
            "'Good. Let's do it.' You want your freedom back."
        "Suspicious":
            $ helos_morning = "suspicious"
            "'Why now?' You don't trust her change of heart."
        "Nervous":
            $ helos_morning = "nervous"
            "'What happens if you undo it?' You're afraid of the consequences."

    "She pauses."

    sidea "I don't want to. But I will. It's not fair to keep you here."

    "She reaches for your wrist. Her fingers are cold. She looks up at you."

    sidea "I don't want to. But I will."

    "This is an intimate moment. She's touching you voluntarily—and it's not about magic. It's about letting go."

    sidea "I'll be alone again."

    "You realize: she's not just testing spells. She's testing connection. She's trying to figure out how to be with someone without breaking them."

    menu:
        "What do you tell her?"
        "Stay":
            $ helos_choice = "stay"
            "'I'll stay. For now. You need help.' You're choosing to stay."
            $ rp_adjust("sidea", 2)
        "Leave":
            $ helos_choice = "leave"
            "'I need to go. I have things to figure out.' You're choosing to leave."
        "Uncertain":
            $ helos_choice = "uncertain"
            "'I don't know yet. Let's take it one day at a time.' You're keeping your options open."

    sidea "It's okay. You can leave. But I'll be here. If you ever want to come back."

    scene black
    with dissolve

    "The swamp remembers everything. And it's patient."

    "— End of Chapter 1: Helos —"

    # Once ch02_helos.rpy exists with a "label helos_ch02:" at the top,
    # replace this "return" with "jump helos_ch02".
    return