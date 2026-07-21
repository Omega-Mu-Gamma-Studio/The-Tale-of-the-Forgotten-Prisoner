# ch01_arenia.rpy — Arenia, Land of Gold — Chapter 1
# "Gold from Sand"
#
# Full storyline: desert survival, Aurea the Falcon of the West,
# the iron collar, and the slow rise from slave to something more.
# Chapter 2 goes in ../arenia/ch02_arenia.rpy

define aurea = Character("Aurea", color="#d1a24a")
define merchant = Character("Merchant", color="#c9b98a")
define guard = Character("Guard", color="#d9d9d9")

label arenia_ch01:

    scene black
    with dissolve

    "Heat reaches you before land does."

    "Your mouth is dry. Your tongue feels like leather. Your lips are cracked and bleeding. The sun is so bright it hurts your eyes even through closed eyelids."

    "You're face-down on sand so fine it looks like powdered sunlight. Your skin is raw—salt-crusted, sunburned, bleeding in places. Your clothes are torn rags. You're too weak to stand."

    scene silhouette_arenia_beach
    with fade

    "You're not on the beach. You're on the edge of the desert. The sea is behind you, vast and grey. The dunes stretch ahead, golden and endless. You can taste salt and dust."

    "A shadow falls over you. A figure. She's wearing battered leather, sand-caked boots, a sword at her hip. Her eyes are cold."

    "She doesn't help you. She kneels down. She starts going through your pockets. Your rags. Your hands. She's looting you."

    menu:
        "How do you react?"
        "Groan":
            $ arenia_first_reaction = "groan"
            "You let out a sound. She stops. She looks at you—really looks. You're alive. She didn't expect that."
        "Grab her wrist":
            $ arenia_first_reaction = "grab"
            "You're weak, but you reach out. She freezes. Your fingers touch her skin. She's startled—no one touches her."
        "Stay still":
            $ arenia_first_reaction = "still"
            "You play dead. She continues looting. You wait for the right moment. You're patient. Cunning."

    "She holds a knife to your throat."

    aurea "You're not dead."

    "It's not a question. You breathe. She watches your chest rise and fall."

    aurea "Unlucky."

    "You try to speak. Your voice is a croak. You say something ridiculous—anything to buy time."

    mc "'I'm not worth looting. I'm poor. I'm a prisoner. I owe money to a very dangerous man.'"

    "She laughs. It's sharp and hollow."

    aurea "So do I. Welcome to the club."

    "There's a flicker of something in her eyes—not warmth, but recognition."

    jump arenia_scene2

label arenia_scene2:

    "She doesn't kill you. She doesn't help you. She sits down on the sand, a few feet away. She's watching you. She's waiting."

    "You're too weak to move. You're at her mercy."

    menu:
        "What do you say?"
        "Pleading":
            $ arenia_approach = "plead"
            "'Please. I need water. I'll die here.' You're vulnerable. Begging."
        "Defiant":
            $ arenia_approach = "defiant"
            "'If you're going to kill me, do it. Don't make me wait.' You're unafraid. Or pretending to be."
        "Curious":
            $ arenia_approach = "curious"
            "'Who are you?' You're trying to understand her."

    "She doesn't answer. Instead, she pulls out an iron collar. It's heavy, cold, and degrading."

    aurea "This is your new life. You're my property now. You carry my supplies. You hold my horse. You do what I say."

    "She approaches. She's done this before—she knows the motion, the click, the weight. But she hesitates. Just for a second. She looks at you—really looks. Something about you gives her pause. Then she shakes it off. She puts it on."

    menu:
        "How do you react to the collar?"
        "Submit":
            $ arenia_collar_reaction = "submit"
            "You lower your head. You let her put it on. You're accepting your fate. For now."
        "Fight":
            $ arenia_collar_reaction = "fight"
            "You try to push her away. You're too weak. She pins you down. She puts it on anyway. You resisted. She respects that. But it's on."
        "Negotiate":
            $ arenia_collar_reaction = "negotiate"
            "'I'll work for you. I'll earn my keep. But I won't wear that.' She laughs again. 'Oh, you'll wear it.' She puts it on. You tried. You failed."

    "The collar clicks shut. It's heavy. It's cold. It's a constant reminder: you belong to her."

    jump arenia_scene3

label arenia_scene3:

    scene silhouette_arenia_desert
    with fade

    "She's been tracking something—a caravan, a target. You don't know. She doesn't tell you. You're just following."

    "The heat is unbearable. The sand shifts beneath your feet. Your skin is cracked and bleeding. You've been walking for hours."

    "You pass a dead animal—a lizard, half-buried in the sand. It couldn't survive the heat."

    "Aurea glances at it."

    aurea "One of my ancestors. They died here."

    "She's not talking about the animal. She's talking about a person. The desert is a graveyard for her family."

    menu:
        "How do you survive the desert?"
        "Silent endurance":
            $ arenia_desert = "endure"
            "You don't complain. You just keep walking. Aurea notices. She respects that."
        "Ask for water":
            $ arenia_desert = "ask"
            "'Please. I need water. I can't keep going.' You're vulnerable. She might give you some. Or not."
        "Collapse":
            $ arenia_desert = "collapse"
            "You can't take it anymore. You fall to your knees. She stops. She looks at you."

    if arenia_desert == "ask":
        "She stops. She looks at you. For a moment, she doesn't move."
        "Then she uncorks her waterskin. She holds it to your lips."
        aurea "Drink. Slowly. I don't need you dying before you're useful."
        "You drink. It's the best thing you've ever tasted."
    elif arenia_desert == "collapse":
        "She sighs. She kneels beside you. She holds a waterskin to your lips."
        aurea "You're not even useful yet, and you're already a burden."
        "But she helps you. She didn't have to."
    else:
        "She watches you. There's a flicker of something in her eyes—surprise, maybe."
        aurea "You're stubborn. That's useful."

    jump arenia_scene4

label arenia_scene4:

    scene silhouette_arenia_caravan
    with fade

    "You reach a caravan—a trading post on the edge of the desert. Tents, camels, merchants."

    "Aurea dismounts. She ties the horse to a post. She looks at you."

    aurea "Stay here. Don't move. Don't talk to anyone. Don't touch anything."

    menu:
        "Do you obey her?"
        "Yes":
            $ arenia_obey = True
            "You stay. You wait. You watch. You're learning to obey. She'll trust you more."
        "No":
            $ arenia_obey = False
            "You wander. You look around. You talk to a merchant. You're testing boundaries. She'll be angry, but she'll also be impressed by your courage."
        "Escape attempt":
            $ arenia_obey = False
            "You see an opportunity. You could run. You could disappear into the desert. You're not ready to accept the collar."

    if not arenia_obey:
        "You see a merchant—a wealthy man with a sharp smile. He looks at you. He sees the collar."

        merchant "A new slave? The Falcon must be desperate."

        "He knows about Aurea. He knows about the Falcon of the West."

        merchant "She's killed everyone who's tried to help her. You won't last."

        "He looks at you like he's looking at a familiar painting—he knows he's seen it before, but he can't remember where."

        merchant "I know you. From somewhere. I've seen your face before. You're not from here. Did you come from the north? The frozen lands?"

        menu:
            "How do you respond to the merchant?"
            "Defend her":
                $ arenia_merchant_response = "defend"
                "'She's not that bad.' You're already protecting her. Interesting."
            "Ask for help":
                $ arenia_merchant_response = "help"
                "'Can you help me escape?' You're planning to leave."
            "Ignore him":
                $ arenia_merchant_response = "ignore"
                "You say nothing. You walk away. You're staying neutral."

        "You don't answer his question about the frozen lands. But the merchant knows something. He's connected to your past."

    jump arenia_scene5

label arenia_scene5:

    "Aurea returns. She sees you wandering. She's furious. She grabs you by the collar."

    aurea "What did I say?"

    menu:
        "How do you respond?"
        "Apologetic":
            $ arenia_confrontation = "apologetic"
            "'I'm sorry. I didn't mean to disobey.' You're submissive. You want to survive."
        "Defensive":
            $ arenia_confrontation = "defensive"
            "'I was just looking around. I didn't touch anything.' You're asserting yourself. She's angry, but she respects you."
        "Bold":
            $ arenia_confrontation = "bold"
            "'I'm not your dog. You don't own me.' You're fighting back. She might hit you. Or she might smile."

    "The merchant approaches. He offers to buy you."

    merchant "I'll give you double her price. She's wasting you."

    "Aurea's hand moves to her sword. She's not going to let you go—even if she has to kill the merchant to keep you. She doesn't want to lose you."

    "She looks at you. She's waiting. She wants to see what you'll do."

    menu:
        "How do you respond to the merchant's offer?"
        "Stay with Aurea":
            $ arenia_choice = "stay"
            "'I'm not for sale.' You choose her. She's surprised. Pleased, maybe."
            $ rp_adjust("aurea", 2)
        "Consider the offer":
            $ arenia_choice = "consider"
            "'What will you do with me?' You're curious. Aurea's eyes narrow."
        "Accept the offer":
            $ arenia_choice = "leave"
            "'I'll go with him.' You're leaving her. She'll be furious. But you're free."

    "The merchant backs down. He knows better than to fight the Falcon."

    jump arenia_scene6

label arenia_scene6:

    scene silhouette_arenia_night
    with fade

    "The merchant leaves. The sun sets. The desert cools. You're alone with Aurea. She's quiet. She's watching the stars."

    menu:
        "What do you talk about?"
        "Her past":
            $ arenia_talk = "her"
            "'Why are you alone? Why don't you have anyone?' She's defensive. But she might open up."
        "Your past":
            $ arenia_talk = "you"
            "'I was a prisoner too. I was on a ship. A kraken attacked. I escaped.' She listens. She doesn't comment."
        "The collar":
            $ arenia_talk = "collar"
            "'This thing is heavy. Does it have to be so tight?' She laughs. 'You'll get used to it.' But she loosens it slightly."

    "She looks at you. There's a flicker of something in her eyes."

    aurea "You're the first person I haven't killed in years. Do you know why?"

    "You shake your head."

    aurea "I don't know either."

    "She's as surprised as you are."

    "She adds, her voice quieter:"

    aurea "The last person I didn't kill—I married him. He died in the desert three years ago."

    "She pauses."

    aurea "I'm trying to see if you'll die like the last one."

    "The collar isn't just a tool of control. It's a test."

    jump arenia_scene7

label arenia_scene7:

    scene silhouette_arenia_camp
    with fade

    "You make camp in the desert. Aurea builds a fire. She sleeps close to it, her sword within reach. You sleep on the other side of the fire, the collar heavy on your neck."

    menu:
        "What do you think about before sleep?"
        "Escape":
            $ arenia_night = "escape"
            "You could run. The desert is vast. You might survive. You might die. But you could try."
        "Stay":
            $ arenia_night = "stay"
            "You're staying. You don't know why. But you're not leaving."
        "Dream":
            $ arenia_night = "dream"
            "You close your eyes. You dream of the ship. The kraken. The waves."

    if arenia_night == "dream":
        "You dream of your past. A figure in the shadows. A voice: 'You can't run forever.'"
        "A figure steps forward—a silhouette in the shadows."

        menu:
            "What do you do in the dream?"
            "Reach out":
                $ arenia_dream = "reach"
                "You try to touch them. Your fingers reach through the darkness. You're seeking connection. Atonement."
            "Turn away":
                $ arenia_dream = "turn"
                "You can't face them. You walk into the darkness. You're running. Even in your dreams."
            "Speak":
                $ arenia_dream = "speak"
                "'Who are you? What do you want from me?' You're confronting your past."

    "You wake up gasping. The collar is cold against your skin."

    "Aurea is awake. She's watching you."

    aurea "Bad dreams?"

    menu:
        "How do you respond?"
        "Truth":
            $ reckoning_adjust("confess")
            "'I killed someone. I'm trying to forget.' You're confessing."
        "Lie":
            $ reckoning_adjust("hide")
            "'Just the ship. The kraken.' You're hiding."
        "Silence":
            "You say nothing. She doesn't push."

    aurea "Everyone has bad dreams in the desert. It's the silence. Makes you hear things."

    jump arenia_scene8

label arenia_scene8:

    scene silhouette_arenia_morning
    with fade

    "Sunrise. The desert is golden again. Aurea is packing. She looks at you."

    aurea "We're going to the city. I have a job."

    menu:
        "How do you prepare for the journey?"
        "Eager":
            $ arenia_morning = "eager"
            "'What kind of job?' You're curious. Involved."
        "Resigned":
            $ arenia_morning = "resigned"
            "'I just need to survive.' You're going along with it."
        "Suspicious":
            $ arenia_morning = "suspicious"
            "'Is it dangerous?' You're cautious."

    "Aurea steps closer. She reaches for your neck. You flinch."

    aurea "Relax. I'm loosening it."

    "She adjusts the collar slightly. It's a small act of care—a crack in the power dynamic. You feel your skin breathe. It's not freedom. But it's something."

    aurea "We're going to the city of gold. The Salt Flats. You're going to meet the merchant who owns me. He wants to see you."

    mc "Why does he want to see me?"

    "She doesn't answer."

    aurea "You'll find out."

    "She mounts her horse. She looks down at you."

    aurea "You're not a slave. Not really. But you're not free either. Not yet. Earn it."

    scene black
    with dissolve

    "The desert remembers everything. And it never forgets."

    "— End of Chapter 1: Arenia —"

    # Once ch02_arenia.rpy exists with a "label arenia_ch02:" at the top,
    # replace this "return" with "jump arenia_ch02".
    return