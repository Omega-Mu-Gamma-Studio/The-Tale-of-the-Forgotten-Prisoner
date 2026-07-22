# ch01_khionia.rpy — Khionia, Land of Endless Snow — Chapter 1
# "The Snow Remembers"
#
# Full storyline: castle intrigue, Princess Asteria, Lord Valerius framing
# an innocent chef. This chapter covers the Arrival + Incident beats.
# Chapter 2 goes in ../khionia/ch02_khionia.rpy

define asteria = Character("Princess Asteria", color="#a9c9e8")
define valerius = Character("Lord Valerius", color="#5c7a99")
define leontios = Character("King Leontios", color="#c9b98a")
define chef = Character("The Royal Chef", color="#d9d9d9")
define servant = Character("Servant Girl", color="#e0d5c1")

# ============================================================
# Khionia Chapter 1 - Image Definitions with Size Fixes
# ============================================================

# --- Silhouette BGs (fill the screen completely) ---
image khionia_bg_beach:
    "images/silhouettes/khionia/silhouette_khionia_beach.png"
    fit "cover"

image khionia_bg_gates:
    "images/silhouettes/khionia/silhouette_khionia_gates.png"
    fit "cover"

image khionia_bg_hall:
    "images/silhouettes/khionia/silhouette_khionia_hall.png"
    fit "cover"

image khionia_bg_stairs:
    "images/silhouettes/khionia/silhouette_khionia_stairs.png"
    fit "cover"

image khionia_bg_courtyard:
    "images/silhouettes/khionia/silhouette_khionia_courtyard.png"
    fit "cover"

image khionia_bg_room:
    "images/silhouettes/khionia/silhouette_khionia_room.png"
    fit "cover"

# --- Major Moments (show the whole image, centered) ---
image khionia_mm_hut:
    "images/major_moments/khionia/major_khionia_fisherman_hut.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_lake_hand:
    "images/major_moments/khionia/major_khionia_lake_hand.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_fall:
    "images/major_moments/khionia/major_khionia_fall.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_asteria_portrait:
    "images/major_moments/khionia/major_khionia_asteria_portrait.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_valerius_vial:
    "images/major_moments/khionia/major_khionia_valerius_vial.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_chef_look:
    "images/major_moments/khionia/major_khionia_chef_look.png"
    fit "contain"
    align (0.5, 0.5)

image khionia_mm_dream:
    "images/major_moments/khionia/major_khionia_dream.png"
    fit "contain"
    align (0.5, 0.5)
# ============================================================
# Khionia Chapter 1: "The Snow Remembers"
# ============================================================

label khionia_ch01:

    # ============================================================
    # Scene 1: The Frozen Shore
    # ============================================================
    
    scene khionia_bg_beach with fade
    
    "Your mouth is dry. Your tongue feels like leather."
    "Your lips are cracked and bleeding."
    "You're face-down on black sand. Ice crystals have formed on your eyelashes."
    "Your fingers are numb. Your prisoner rags are frozen stiff."
    "You don't remember how you got here—only the ship, the kraken, the water."
    
    "You push yourself up. The sky is grey, the snow is falling."
    "In the distance—maybe a mile away—you see the lights of a city built into a mountain."
    "A castle crowns the peak."
    
    # ============================================================
    # Choice 1: Which way do you go?
    # ============================================================
    
    menu:
        "The City":
            jump khionia_ch1_path_city
        "The Caves":
            jump khionia_ch1_path_caves

    # ============================================================
    # Path A: The City
    # ============================================================
    
    label khionia_ch1_path_city:
        scene khionia_bg_beach with dissolve
        
        "You stumble through knee-deep snow. Every step is agony."
        "The wind cuts through your rags like a knife."
        "You pass a frozen fisherman's hut. It's small, half-buried in snow."
        
        menu:
            "Stop at the hut":
                jump khionia_ch1_hut
            "Keep walking":
                jump khionia_ch1_keep_walking

    label khionia_ch1_hut:
        # MAJOR MOMENT: Fisherman's Hut
        scene black with fade
        show khionia_mm_hut at truecenter with dissolve
        pause 2.0
        
        "You push the door open."
        "Inside, a cold hearth. A torn cloak hangs on a hook."
        "You take it—warmth."
        "Half a dried fish on the table. You eat it—strength."
        "A child's wooden toy lies on the floor. Carved into the shape of a bird."
        "Next to the toy, a note. Badly written, childish scrawl:"
        "\"Papa went to the lake. He said he'd be back.\""
        "Your stomach turns. The lake is the shorter route. The dangerous one."
        "On the wall, near the door, a symbol is carved into the wood."
        "A circle with a line through it—like a sun eclipsed."
        "You don't recognize it. But you'll see it again."
        "You take the toy. You slip it into your pocket."
        "It feels wrong to leave it here."
        
        hide khionia_mm_hut with dissolve
        jump khionia_ch1_path_continue

    label khionia_ch1_keep_walking:
        scene khionia_bg_beach with dissolve
        
        "You push through. The cold takes more of you."
        "You arrive at the castle gates with frostbite beginning on your fingers and toes."
        "A permanent reminder. A scar."
        
        jump khionia_ch1_path_continue

    # ============================================================
    # Path B: The Caves
    # ============================================================
    
    label khionia_ch1_path_caves:
        scene khionia_bg_beach with dissolve  # Use beach as stand-in for caves
        
        "You see cliffs to your left. Dark openings in the rock."
        "Shelter."
        "You crawl into one of the caves. It's shallow but dry."
        "Someone has been here recently—there's a dying fire, ash still warm."
        "On the wall, near the fire, a sigil is carved into the stone."
        "A circle with a line through it."
        "The same symbol. Someone else is investigating Khionia's secret."
        "You find a torn cloak—take it for warmth."
        "Half a dried fish—eat it."
        "A child's wooden toy. A bird."
        "Next to the toy, a note:"
        "\"Papa went to the lake. He said he'd be back.\""
        "The fire dies. You leave the cave, warmer, but disturbed."
        
        jump khionia_ch1_path_continue

    # ============================================================
    # Path Continuation: The Lake or The Road
    # ============================================================
    
    label khionia_ch1_path_continue:
        scene khionia_bg_beach with dissolve
        
        menu:
            "Take the lake path (faster, dangerous)":
                jump khionia_ch1_lake
            "Take the road path (safer, longer)":
                jump khionia_ch1_road

    label khionia_ch1_lake:
        scene khionia_bg_beach with dissolve
        
        # MAJOR MOMENT: Lake Hand
        show khionia_mm_lake_hand at truecenter with dissolve
        pause 1.5
        hide khionia_mm_lake_hand with dissolve
        
        "The ice is thick in places, thin in others."
        "You can hear it groaning beneath your feet."
        "You remember the note: \"Papa went to the lake.\""
        "You see dark shapes beneath the ice. Frozen bodies? Trees?"
        "You don't look too closely."
        "You make it across. But you're shaking. You can't feel your feet."
        
        jump khionia_ch1_gates

    label khionia_ch1_road:
        scene khionia_bg_beach with dissolve
        
        "You walk along the edge of the frozen lake, following the road."
        "You pass a frozen village. Houses with smoke rising from chimneys."
        "People live here. They watch you from behind frost-covered windows."
        "You collapse twice. You get up twice."
        "You reach the castle gates. Exhausted. But your feet still work."
        
        jump khionia_ch1_gates

    # ============================================================
    # Scene 2: The Castle Threshold
    # ============================================================
    
    label khionia_ch1_gates:
        scene khionia_bg_gates with fade
        
        "Massive iron doors. Carved with images of wolves and snow."
        "Guards in heavy furs, spears in hand."
        "They stop you."
        
        "You're barely coherent. You speak in fragments."
        "A prisoner. A shipwreck. The kraken. Please."
        
        "The guards look at each other. One of them laughs."
        "Another says: \"We don't get many visitors. And none who look like this.\""
        
        menu:
            "Beg for mercy":
                jump khionia_ch1_beg
            "Demand to see the King":
                jump khionia_ch1_demand
            "Collapse from exhaustion":
                jump khionia_ch1_collapse

    label khionia_ch1_beg:
        scene khionia_bg_gates with dissolve
        
        "\"I have nowhere else to go. Please. I'll die out here.\""
        "The guards are moved but suspicious."
        "One of them says: \"We'll see what the King says.\""
        "They escort you inside."
        
        jump khionia_ch1_servant

    label khionia_ch1_demand:
        scene khionia_bg_gates with dissolve
        
        "\"I was on a prison ship. The kraken attacked. I have information about what happened. Take me to your ruler.\""
        "They laugh but escort you inside."
        "They don't believe you, but curiosity wins."
        
        jump khionia_ch1_servant

    label khionia_ch1_collapse:
        scene khionia_bg_gates with dissolve
        
        "You fall at their feet. You're too weak to speak."
        "They carry you in. You're completely at their mercy."
        "You see a glimpse of their faces as they carry you—they're not cruel. Just weary."
        
        jump khionia_ch1_servant

    label khionia_ch1_servant:
        scene khionia_bg_hall with fade
        
        "A servant girl appears. Young, maybe sixteen."
        "She brings you water. She's kind but afraid."
        "She whispers: \"Be careful. The Princess is in a mood today. She's been... volatile since the prince died.\""
        "You try to ask about the prince. She shushes you."
        "\"Don't speak of it.\" She disappears."
        "The prince died. You note this."
        "Someone in this castle is grieving."

    # ============================================================
    # Scene 3: The Grand Hall
    # ============================================================
    
    label khionia_ch1_grand_hall:
        scene khionia_bg_hall with fade
        
        "You're brought before the royal family."
        "The Grand Hall is massive, carved from ice and stone."
        "Tapestries hang on the walls, depicting scenes of war and winter."
        "A fire roars in a hearth large enough to stand in."
        
        "The King sits on a throne of ice and bone."
        "He is pale, thin, his eyes sunken. He looks like a man who is already dead."
        
        "Next to him stands Princess Asteria."
        "She is beautiful, sharp, and cold as the winter outside."
        "Her eyes assess you in a way that feels almost predatory."
        
        # MAJOR MOMENT: Asteria Portrait
        show khionia_mm_asteria_portrait at truecenter with dissolve
        pause 1.5
        hide khionia_mm_asteria_portrait with dissolve
        
        "In the shadows, near a pillar, stands Lord Valerius."
        "He's older than the King, but healthier. Smiling."
        "He watches you like a cat watches a mouse."
        
        "The King speaks: \"Who are you?\""
        
        menu:
            "Tell your real name":
                jump khionia_ch1_real_name
            "Give a fake name":
                jump khionia_ch1_fake_name
            "Say you don't remember":
                jump khionia_ch1_no_name

    label khionia_ch1_real_name:
        scene khionia_bg_hall with dissolve
        
        "You tell him your name. It's a risk. He might recognize it."
        "The King nods slowly. \"A name from the old lands.\""
        "You don't know if that's good or bad."
        
        jump khionia_ch1_crime

    label khionia_ch1_fake_name:
        scene khionia_bg_hall with dissolve
        
        "You choose a name on the spot. It feels wrong, but it's safer."
        "The King raises an eyebrow. \"That's a northern name. You don't look northern.\""
        "You don't answer."
        
        jump khionia_ch1_crime

    label khionia_ch1_no_name:
        scene khionia_bg_hall with dissolve
        
        "\"I don't remember. The sea took my memory.\""
        "The King looks at you. He doesn't believe you. But he doesn't press."
        "\"A convenient story,\" the Princess mutters."
        
        jump khionia_ch1_crime

    label khionia_ch1_crime:
        scene khionia_bg_hall with dissolve
        
        "The King asks: \"And what is your crime? What did you do to end up on that ship?\""
        
        menu:
            "Be vague: 'I don't remember the details'":
                jump khionia_ch1_crime_vague
            "Be honest: 'I killed someone. It was an accident.'":
                jump khionia_ch1_crime_honest
            "Be defiant: 'What I did doesn't matter. I'm here now.'":
                jump khionia_ch1_crime_defiant

    label khionia_ch1_crime_vague:
        scene khionia_bg_hall with dissolve
        
        "\"I was sentenced. I don't remember the details.\""
        "The Princess scoffs. \"Convenient.\""
        "The King holds up a hand. He is more curious than she is."
        
        jump khionia_ch1_crime_continue

    label khionia_ch1_crime_honest:
        scene khionia_bg_hall with dissolve
        
        "\"I killed someone. It was... I didn't mean to. It was an accident.\""
        "The Princess's eyes narrow. \"What kind of accident?\""
        "You don't answer. You can't."
        
        jump khionia_ch1_crime_continue

    label khionia_ch1_crime_defiant:
        scene khionia_bg_hall with dissolve
        
        "\"What I did doesn't matter. I'm here now. I survived.\""
        "The Princess looks at you. She's studying you. She says nothing."
        
        jump khionia_ch1_crime_continue

    label khionia_ch1_crime_continue:
        scene khionia_bg_hall with dissolve
        
        "Princess Asteria presses you further. She asks about the weather, about the sea, about the kraken."
        "She's testing you. Looking for holes in your story."
        "You answer. You hold your ground."
        
        "The King intervenes: \"Enough. Let the man breathe.\""
        "He orders soup to be brought."
        "\"You look half-dead. Eat first. Talk later.\""
        
        "As the King speaks, he coughs into his handkerchief."
        "A faint smear of blood. He hides it quickly."
        "Nobody else sees it. But you do."
        "The King is dying. Faster than anyone knows."

    # ============================================================
    # Scene 4: The Staircase
    # ============================================================
    
    label khionia_ch1_stairs:
        scene khionia_bg_stairs with fade
        
        "A servant guides you to a side chamber where you can change your clothes and eat."
        "You're led up a narrow, winding staircase."
        "The walls are damp, the torchlight is dim, and every step hurts."
        
        menu:
            "Cling to the wall":
                jump khionia_ch1_stairs_wall
            "Take the center":
                jump khionia_ch1_stairs_center

    label khionia_ch1_stairs_wall:
        scene khionia_bg_stairs with dissolve
        
        "You move slowly, hand against the stone."
        "You notice a loose stone with carvings on it. Ancient symbols."
        "One of them catches your eye—a circle with a line through it."
        "The same symbol you saw in the hut and the cave."
        "You press the stone. It shifts slightly."
        "You could pull it out, but the servant is waiting."
        "You remember the marks. Someone is investigating too."
        "You leave it. For now."
        
        jump khionia_ch1_fall

    label khionia_ch1_stairs_center:
        scene khionia_bg_stairs with dissolve
        
        "You move faster. You're too exhausted to be careful."
        "You slip on a wet patch of stone—your feet go out from under you."
        
        jump khionia_ch1_fall

    label khionia_ch1_fall:
        scene khionia_bg_stairs with dissolve
        
        # MAJOR MOMENT: The Fall
        show khionia_mm_fall at truecenter with dissolve
        pause 1.5
        hide khionia_mm_fall with dissolve
        
        "You crash into the royal chef, who is coming down the stairs with a tureen of soup."
        "He falls hard, his head striking the stone step. He's unconscious instantly."
        "The soup goes flying. It spills directly onto Princess Asteria's gown, who has just emerged from a side door."
        "She is furious. Her beautiful dress is ruined, soaked in scalding broth."
        "She screams for the guards."
        
        "As the chef lies unconscious, his hand twitches."
        "He's trying to reach for something. A pocket. A note."
        "He was carrying the soup for a reason. He was going to warn someone. Or stop someone."
        "You only see the twitch."
        
        "Guards grab you. The Princess draws a dagger."
        "\"This time, I won't miss.\""
        "She advances. You're on the floor, covered in soup, helpless."
        
        "The King arrives, limping, leaning on a cane."
        "His voice is weak but firm: \"Enough. Put down the blade, Asteria. He didn't mean it.\""
        "She argues. There are tears in her eyes."
        "It's not just about the dress—it's grief, raw and uncontained."
        "She lowers the dagger. But she doesn't sheathe it."
        "\"You're lucky, stranger. But luck runs out.\""

    # ============================================================
    # Scene 5: The Accusation
    # ============================================================
    
    label khionia_ch1_accusation:
        scene khionia_bg_hall with fade
        
        "The Grand Hall is in chaos. Guards are shouting, servants are running."
        "The chef is being carried away, still unconscious."
        "The King is calm, but you saw the blood on his handkerchief."
        
        "Lord Valerius steps forward. He holds a small vial of amber liquid."
        
        # MAJOR MOMENT: Valerius with the vial
        show khionia_mm_valerius_vial at truecenter with dissolve
        pause 1.5
        hide khionia_mm_valerius_vial with dissolve
        
        "\"I found this in the chef's quarters. Hidden beneath a loose floorboard. Poison.\""
        "He looks at the vial with too much fondness. Like he's proud of his work."
        "He planted it."
        
        "Valerius spins the story: the chef was planning to poison the royal family."
        "You, the stranger, arrived by divine intervention."
        "You stopped the plot. You are a saviour."
        
        menu:
            "Stay silent":
                jump khionia_ch1_accusation_silent
            "Speak up: 'He's innocent'":
                jump khionia_ch1_accusation_speak
            "Accept the role":
                jump khionia_ch1_accusation_accept

    label khionia_ch1_accusation_silent:
        scene khionia_bg_hall with dissolve
        
        "You say nothing. It's safer. You're alive."
        "But the chef is going to die."
        
        jump khionia_ch1_accusation_aftermath

    label khionia_ch1_accusation_speak:
        scene khionia_bg_hall with dissolve
        
        "\"I didn't know about any poison. I just fell. He's innocent.\""
        "The Princess looks at you. For a moment, you see something in her eyes."
        "Doubt. Or curiosity."
        "Valerius smiles. It doesn't reach his eyes."
        "\"Of course. The outsider is confused. He doesn't know what he saw.\""
        "He dismisses you."
        
        jump khionia_ch1_accusation_aftermath

    label khionia_ch1_accusation_accept:
        scene khionia_bg_hall with dissolve
        
        "\"If I saved the royal family, then I did what needed to be done.\""
        "Valerius claps you on the shoulder. His grip is too tight."
        "The King smiles. He thanks you."
        
        jump khionia_ch1_accusation_aftermath

    label khionia_ch1_accusation_aftermath:
        scene khionia_bg_hall with dissolve
        
        "The King assigns you as a royal assistant. You'll serve the family."
        "You're not a guest. You're not a prisoner. You're indebted."
        
        "Lord Valerius claps you on the shoulder. He's too close."
        "He smells like incense and old wine."
        "\"Welcome to Khionia. You're a hero now. Enjoy it while it lasts.\""
        
        "Princess Asteria is silent. She watches you."
        "Her eyes are not just cold—they're calculating."
        "She knows you're hiding something. She's going to find out what."

    # ============================================================
    # Scene 6: The Chef's Fate
    # ============================================================
    
    label khionia_ch1_chef:
        scene khionia_bg_courtyard with fade
        
        "You're given a moment alone. A servant leads you to the edge of the courtyard."
        "Below, the dungeon entrance."
        
        # MAJOR MOMENT: Chef's Look
        show khionia_mm_chef_look at truecenter with dissolve
        pause 1.5
        hide khionia_mm_chef_look with dissolve
        
        "You see the chef, conscious now, being dragged into the darkness."
        "He looks up at the castle. His eyes find you."
        "He doesn't look angry—he looks terrified."
        "He knows he's been framed. He knows who did it."
        "He tries to shout something, but a guard hits him. He goes silent."
        
        menu:
            "Call out: 'Wait! I need to speak with him!'":
                jump khionia_ch1_chef_speak
            "Stay quiet and watch":
                jump khionia_ch1_chef_quiet
            "Follow the guards to the dungeon":
                jump khionia_ch1_chef_follow

    label khionia_ch1_chef_speak:
        scene khionia_bg_courtyard with dissolve
        
        "You call out. The guards stop. They look at you."
        "The chef is dragged back inside. You might get a few moments with him."
        "He'll whisper something to you before he's taken away."
        "Valerius will know you interfered."
        
        jump khionia_ch1_room

    label khionia_ch1_chef_quiet:
        scene khionia_bg_courtyard with dissolve
        
        "You watch him disappear. Your stomach churns."
        "You could have saved him. You didn't."
        "This haunts you."
        
        jump khionia_ch1_room

    label khionia_ch1_chef_follow:
        scene khionia_bg_courtyard with dissolve
        
        "You follow the guards. You pretend to be lost."
        "You reach the dungeon. You hear the chef screaming."
        "You learn more about the dungeon's layout—crucial for later."
        
        jump khionia_ch1_room

    # ============================================================
    # Scene 7: Your New Room
    # ============================================================
    
    label khionia_ch1_room:
        scene khionia_bg_room with fade
        
        "You're given a small chamber. Barely larger than a closet."
        "A narrow bed, a chair, a window. A candle flickers on a small table."
        "You look out the window. The frozen city stretches below you."
        "The lake shimmers in the distance. The caves are dark shapes in the mountain."
        
        menu:
            "Examine the room":
                jump khionia_ch1_room_examine
            "Look out the window":
                jump khionia_ch1_room_window
            "Sleep":
                jump khionia_ch1_room_sleep

    label khionia_ch1_room_examine:
        scene khionia_bg_room with dissolve
        
        "You search the room. Behind the candle, under the mattress, in the floorboards."
        "Under the mattress, you find a hidden note."
        "It's written on a scrap of parchment:"
        "\"The snow remembers. Trust no one.\""
        "You don't know who left it. But it wasn't there before you arrived."
        "Someone in the castle knows you're here."
        
        jump khionia_ch1_dream

    label khionia_ch1_room_window:
        scene khionia_bg_room with dissolve
        
        "You watch the snow. You think about the chef. The fisherman. The child's toy. The sigil."
        "You remember the note in the hut: \"Papa went to the lake.\""
        "You wonder if he came back. You wonder if the child is still waiting."
        
        jump khionia_ch1_dream

    label khionia_ch1_room_sleep:
        scene khionia_bg_room with dissolve
        
        "You collapse onto the bed. You're too exhausted to stay awake."
        "Your dreams are filled with fog, a ship, and a face you can't remember."
        
        jump khionia_ch1_dream

    # ============================================================
    # The Dream
    # ============================================================
    
    label khionia_ch1_dream:
        scene black with fade
        
        # MAJOR MOMENT: Dream (can be used for all three choices)
        show khionia_mm_dream at truecenter with dissolve
        pause 2.0
        
        "You dream..."
        "The fog is thick. You can barely see your own hands."
        "A voice echoes: \"You can't run forever.\""
        "A face appears in the mist. You know them. You loved them. What happened to them?"
        
        menu:
            "Focus on the voice":
                jump khionia_ch1_dream_voice
            "Focus on the face":
                jump khionia_ch1_dream_face
            "Focus on the symbol":
                jump khionia_ch1_dream_symbol

    label khionia_ch1_dream_voice:
        scene black with dissolve
        
        "\"Please... please don't do this...\""
        "You hear someone begging. You can't see their face."
        "Only hear their voice."
        
        jump khionia_ch1_wake

    label khionia_ch1_dream_face:
        scene black with dissolve
        
        "A woman crying. You know her. You loved her."
        "What happened to her?"
        
        jump khionia_ch1_wake

    label khionia_ch1_dream_symbol:
        scene black with dissolve
        
        "The sigil. The circle with the line through it."
        "It's everywhere—in the hut, in the cave, in the staircase."
        "You realize you've seen it before. In your old life."
        "What does it mean?"
        
        jump khionia_ch1_wake

    # ============================================================
    # Wake Up & Cliffhanger
    # ============================================================
    
    label khionia_ch1_wake:
        scene khionia_bg_room with fade
        hide khionia_mm_dream with dissolve
        
        "You wake with a gasp. Your heart is pounding. The candle has burned low."
        "There's a knock at the door. Three sharp raps. It's not a servant's knock."
        "The door opens. Princess Asteria enters without waiting."
        
        # MAJOR MOMENT: Asteria Portrait (reused for the confrontation)
        show khionia_mm_asteria_portrait at truecenter with dissolve
        pause 1.0
        
        "She holds your prisoner rags—the frozen, tattered things you wore when you arrived."
        "She throws them at you. They land on your chest."
        
        "\"You're a terrible liar. I've had spies watching you since you arrived.\""
        "She steps closer. Her face is inches from yours."
        "\"Who are you really?\""
        
        hide khionia_mm_asteria_portrait with dissolve
        
        # END OF CHAPTER 1
        return