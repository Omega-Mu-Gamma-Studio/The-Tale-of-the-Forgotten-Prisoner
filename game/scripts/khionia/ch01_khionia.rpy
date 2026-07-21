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

label khionia_ch01:

    scene black
    with dissolve

    "Cold reaches you before land does."

    "You wash up on a beach the color of bone, snow packed hard enough to bruise. Your hands don't work properly anymore. Neither do your legs, not really — you crawl more than you walk toward the treeline, toward anything that isn't open sky and open sea."

    "Somewhere ahead, past the frost-blind trees, torchlight flickers against stone walls. A castle. Warmth. A place that might let a half-dead stranger live long enough to become a problem later."

    "You don't remember deciding to go toward it. You just do. Some animal part of you that survived the kraken and the sea has already decided that warmth is worth the risk of whoever's holding the torches."

    scene silhouette_khionia_beach
    with fade

    "The sky is grey, the snow is falling, and in the distance — maybe a mile away — you see the lights of a city built into a mountain. A castle crowns the peak."

    menu:
        "Which way do you go?"
        "Toward the city":
            jump khionia_scene1_city
        "Toward the caves":
            jump khionia_scene1_caves

label khionia_scene1_city:

    "You stumble through knee-deep snow. Every step is agony. The wind cuts through your rags like broken glass."

    "After what feels like an hour — or a lifetime — you see a small hut, half-buried in snow. Smoke rises from the chimney, but barely. It's nearly dead."

    menu:
        "Do you stop at the fisherman's hut?"
        "Stop":
            jump khionia_scene1_hut
        "Press on":
            jump khionia_scene1_continue

label khionia_scene1_hut:

    "You push the door open. It groans on frozen hinges."

    "Inside, a cold hearth. A torn cloak hangs on a hook — you take it, wrapping it around your shoulders. Warmth, finally, however thin."

    "Half a dried fish lies on the table. You eat it without hesitation. It's salty, tough, and the best thing you've ever tasted."

    "On the floor, a child's wooden toy. Carved into the shape of a bird. It's been loved — the edges worn smooth by small hands."

    "Next to it, a note. Badly written, childish scrawl:"

    "Papa went to the lake. He said he'd be back."

    "Your stomach turns. The lake is the shorter route to the castle. The dangerous route."

    "On the wall, near the door, a symbol is carved into the wood. A circle with a line through it — like a sun eclipsed. You don't recognize it."

    menu:
        "Do you take the toy?"
        "Take it":
            $ khionia_toy = True
            "You slip it into your pocket. It feels wrong to leave it here alone."
        "Leave it":
            $ khionia_toy = False
            "You can't carry more weight. You need to survive. But you remember it, even as you turn away."

    "You leave the hut. Warmer. Stronger. But haunted."

    jump khionia_scene1_path

label khionia_scene1_continue:

    "You push through the snow. The cold takes more of you with every step."

    "By the time you reach the castle gates, frostbite has begun on your fingers and toes. It will scar. You'll carry this reminder of Khionia forever."

    jump khionia_scene1_path

label khionia_scene1_caves:

    "You see cliffs to your left. Dark openings in the rock. Shelter."

    "You crawl into one of the caves. It's shallow but dry. Someone has been here recently — a fire, barely alive, still warm."

    "On the wall, near the fire, a sigil is carved into the stone. A circle with a line through it. The same symbol. Someone else is investigating Khionia's secrets — and they were here recently."

    "You find a torn cloak (you take it), half a dried fish (you eat it), and a child's wooden toy."

    "Next to the toy, a note: 'Papa went to the lake. He said he'd be back.'"

    menu:
        "Do you take the toy?"
        "Take it":
            $ khionia_toy = True
            "You slip it into your pocket. It feels wrong to leave it here alone."
        "Leave it":
            $ khionia_toy = False
            "You can't carry more weight. You need to survive. But you remember it, even as you turn away."

    "The fire dies. You leave the cave, warmer, but disturbed."

    jump khionia_scene1_path

label khionia_scene1_path:

    "The castle looms ahead. But two paths stretch before you: the frozen lake, fast and dangerous — or the road, safe but long."

    menu:
        "Which path do you take?"
        "The frozen lake":
            jump khionia_scene1_lake
        "The road":
            jump khionia_scene1_road

label khionia_scene1_lake:

    "The ice groans beneath your feet. In some places, it's thick — in others, you can see the dark water moving beneath."

    "You remember the note: 'Papa went to the lake.'"

    "You see something beneath the ice. A shape. You look closer."

    "A hand. Pressed against the ice from below. Small. A child's hand."

    "You don't stop. You can't. You keep walking, one foot in front of the other."

    "You make it across. But you're shaking. You can't feel your feet."

    "You don't look back."

    jump khionia_scene2

label khionia_scene1_road:

    "You walk along the edge of the frozen lake, following the road."

    "You pass a frozen village. Houses with smoke rising from chimneys. People live here. They watch you from behind frost-covered windows."

    "You collapse twice. You get up twice."

    "By the time you reach the castle gates, your legs are trembling. But they still work."

    jump khionia_scene2

label khionia_scene2:

    scene silhouette_khionia_gates
    with fade

    "Massive iron gates. Carved with images of wolves and snow. Guards in heavy furs, spears in hand."

    "They stop you."

    guard "Halt. Who goes there?"

    "You're barely coherent. You speak in fragments — a prisoner, a shipwreck, the kraken, please."

    "The guards look at each other. One laughs. Another says: 'We don't get many visitors. And none who look like this.'"

    menu:
        "How do you present yourself?"
        "Beg":
            $ khionia_first_impression = "beg"
            "'Please. I have nowhere else to go. I'll die out here.' The guards are moved but suspicious. 'We'll see what the King says.' They escort you inside."
        "Demand":
            $ khionia_first_impression = "demand"
            "'I was on a prison ship. The kraken attacked. I have information about what happened. Take me to your ruler.' They laugh — but they escort you inside. Curiosity wins."
        "Collapse":
            $ khionia_first_impression = "collapse"
            "You fall at their feet. You're too weak to speak. They carry you in. This is the most vulnerable path — you're completely at their mercy. You see a glimpse of their faces as they carry you. They're not cruel. Just weary."

    "A servant girl appears. Young, maybe sixteen. She brings you water."

    servant "Drink. Slowly."

    "She looks over her shoulder before she whispers:"

    servant "Be careful. The Princess is in a mood today. She's been... volatile since the prince died. They say it was an accident."

    "You try to ask about the prince. She shushes you."

    servant "Don't speak of it. Not here."

    "She disappears. The Prince died. Someone in this castle is grieving."

    jump khionia_scene3

label khionia_scene3:

    scene silhouette_khionia_hall
    with fade

    "You're brought before the royal family."

    "The Grand Hall is massive, carved from ice and stone. Tapestries hang on the walls, depicting scenes of war and winter. A fire roars in a hearth large enough to stand in."

    "The King sits on a throne of ice and bone. He is pale, thin, his eyes sunken. He looks like a man who is already dead."

    "Next to him stands Princess Asteria. She is beautiful, sharp, and cold as the winter outside. Her eyes assess you in a way that feels almost predatory."

    "In the shadows, near a pillar, stands Lord Valerius. He's older than the King, but healthier. Smiling. He watches you like a cat watches a mouse."

    leontios "Who are you?"

    menu:
        "What name do you give?"
        "Your real name":
            $ khionia_name = "real"
            "You tell him your real name. It's a risk. He might recognize it. But you're too exhausted to lie."
        "A fake name":
            $ khionia_name = "fake"
            "You choose a name on the spot. It feels wrong, but it's safer. The King's eyes narrow slightly — he knows you're hiding."
        "No name":
            $ khionia_name = "none"
            "'I don't remember.' You claim the sea took your memory. This is the most vulnerable path. The King seems to soften — just slightly."

    "You explain the shipwreck. The kraken. The prison ship. You don't say what your crime was."

    asteria "A convenient story."

    leontios "And what is your crime? The prison ships don't carry petty thieves. They carry the condemned. What did you do to be worth that kind of transport?"

    menu:
        "How do you describe your crime?"
        "Vague":
            $ reckoning_adjust("hide")
            "'I was sentenced. I don't remember the details.' You're hiding. The King watches you carefully."
        "Honest":
            $ reckoning_adjust("confess")
            "'I killed someone. It was... I didn't mean to. It was an accident.' The confession hangs in the air. Asteria's eyes narrow. She's not satisfied."
        "Defiant":
            $ reckoning_adjust("embrace")
            "'What I did doesn't matter. I'm here now. I survived.' The King holds your gaze. He respects your defiance — or he's trying to read you."

    "Princess Asteria presses you further. She's testing you. She asks about the weather, about the sea, about the kraken — all designed to see if you're lying."

    "You answer. You hold your ground."

    leontios "Enough, Asteria. Let the man breathe."

    "The King coughs. He covers his mouth with a handkerchief. A faint smear of blood. He hides it quickly. Nobody else sees it."

    leontios "You look half-dead. Eat first. Talk later."

    jump khionia_scene4

label khionia_scene4:

    scene silhouette_khionia_stairs
    with fade

    "A servant guides you to a side chamber where you can change your clothes and eat."

    "You're led up a narrow, winding staircase. The walls are damp, the torchlight dim, and every step hurts."

    menu:
        "How do you walk?"
        "Cling to the wall":
            "You move slowly, hand against the cold stone. You notice a loose stone with carvings on it. Ancient symbols. One catches your eye — a circle with a line through it. The same symbol you saw in the hut. You press the stone. It shifts slightly. You could pull it out, but the servant is waiting. You remember the marks. Someone else is investigating too."
        "Take the center":
            "You move faster. You're too exhausted to be careful. You slip on a wet patch of stone — your feet go out from under you."

    "You crash into the royal chef, coming down the stairs with a tureen of soup. He falls hard. His head strikes the stone step. He's unconscious instantly."

    "The soup goes flying. It spills directly onto Princess Asteria's gown, as she emerges from a side door."

    "She is furious."

    "But as the chef lies unconscious, his hand twitches. He's trying to reach for something. A pocket. A note. He was carrying the soup for a reason. He was going to warn someone. But you don't know that yet."

    "Guards grab you. Asteria draws a dagger."

    asteria "This time, I won't miss."

    "The King arrives, limping, leaning on a cane."

    leontios "Enough. Put down the blade, Asteria. He didn't mean it."

    "She argues. There are tears in her eyes. It's not just about the dress — it's grief, raw and uncontained."

    "She lowers the dagger. But she doesn't sheathe it."

    asteria "You're lucky, stranger. But luck runs out."

    jump khionia_scene5

label khionia_scene5:

    "The Grand Hall is in chaos. Guards shouting. Servants running. The chef is being carried away, still unconscious."

    "Lord Valerius steps forward. He holds a small vial of amber liquid."

    valerius "I found this in the chef's quarters. Hidden beneath a loose floorboard. Poison."

    "He looks at the vial with too much fondness. Like he's proud of his work. It's subtle, but you see it. He planted it."

    valerius "The chef was planning to poison the royal family. And you — you arrived by divine intervention. You stopped the plot. You are a saviour."

    menu:
        "How do you respond?"
        "Stay silent":
            $ reckoning_adjust("hide")
            $ rp_adjust("valerius", 1)
            "You accept the story. It's safer. You're alive. But you know the truth — and it weighs on you."
        "Speak up":
            $ reckoning_adjust("confess")
            $ rp_adjust("leontios", 1)
            "'I didn't know about any poison. I just fell. He's innocent.' The King looks at you, considering. Valerius's smile doesn't waver."
        "Accept the role":
            $ reckoning_adjust("embrace")
            "'If I saved the royal family, then I did what needed to be done.' The words taste like ash. But you survive."

    leontios "You'll stay in the castle. Earn your keep properly. Accident or not, it seems the gods sent you here for a reason."

    "That's it. How you go from drowning prisoner to indebted stranger in the space of one spilled tureen and one convenient vial."

    valerius "Welcome to Khionia. You're a hero now. Enjoy it while it lasts."

    "He leans in. His voice drops to a whisper."

    valerius "The snow remembers, stranger. And so do I."

    "Princess Asteria is silent. Her eyes are not just cold — they're calculating. She knows you're hiding something. She's going to find out what."

    jump khionia_scene6

label khionia_scene6:

    scene silhouette_khionia_courtyard
    with fade

    "A servant leads you to the edge of the courtyard. Below, the dungeon entrance."

    "The chef is conscious now. He's being dragged into the darkness."

    "He looks up at the castle. His eyes find you. He's not angry — he's terrified. He knows he's been framed. He knows who did it."

    chef "The vial — it wasn't mine — I was bringing the soup to warn —"

    "A guard hits him. He goes silent."

    menu:
        "What do you do?"
        "Call out":
            "You shout: 'Wait! I need to speak with him!' The guards stop. They look at you. The chef is dragged back inside. He whispers something to you before they take him away."
            $ rp_adjust("chef", 1)
            $ reckoning_adjust("confess")
        "Stay quiet":
            "You watch him disappear. Your stomach churns. You could have saved him. You didn't. You'll carry this."
            $ reckoning_adjust("hide")
        "Follow":
            "You follow the guards. You pretend to be lost. You reach the dungeon. You hear the chef screaming. You learn more about the dungeon's layout — crucial for later."
            $ khionia_dungeon_knowledge = True

    jump khionia_scene7

label khionia_scene7:

    scene silhouette_khionia_room
    with fade

    "You're given a small chamber. Barely larger than a closet. A narrow bed, a chair, a window. A candle flickers."

    "You look out at the frozen city. The lake shimmers in the distance. The caves are dark shapes in the mountain."

    menu:
        "What do you do before sleep?"
        "Examine the room":
            "You search. Behind the candle, under the mattress, in the floorboards. You find a hidden note under the mattress, written on a scrap of parchment: 'The snow remembers. Trust no one.' You don't know who left it. But it wasn't here before."
        "Look out the window":
            "You watch the snow. You think about the chef. The fisherman. The child's toy. The sigil. You remember the note in the hut: 'Papa went to the lake.' You wonder if he came back. You wonder if the child is still waiting."
        "Sleep":
            "You collapse onto the bed. You're too exhausted to stay awake. Your dreams are filled with fog, a ship, and a face you can't remember."

    "You dream."

    menu:
        "What do you focus on in your dreams?"
        "A voice":
            $ khionia_dream = "voice"
            "A voice: 'Please... please don't do this...' You feel something in your hand. Cold. Metal. A blade. You can't see the face. Only hear the voice."
        "A face":
            $ khionia_dream = "face"
            "A face: A woman crying. You know her. You loved her. You feel her hand in yours. It's trembling. What happened to her?"
        "A symbol":
            $ khionia_dream = "symbol"
            "The sigil. The circle with the line through it. It's everywhere — in the hut, in the cave, in the staircase. It burns in your mind. The memory is trying to break through."

    "You wake with a gasp. Your heart is pounding. The candle has burned low."

    "There's a knock at the door. Three sharp raps. It's not a servant's knock."

    "Princess Asteria enters without waiting. She holds your prisoner rags — the frozen, tattered things you wore when you arrived."

    "She throws them at you. They land on your chest."

    asteria "You're a terrible liar. I've had spies watching you since you arrived."

    "She steps closer. Her face is inches from yours."

    asteria "Who are you really?"

    scene black
    with dissolve

    "— End of Chapter 1: Khionia —"

    "The snow remembers, stranger. And so does Khionia."

    # Once ch02_khionia.rpy exists with a "label khionia_ch02:" at the top,
    # replace this "return" with "jump khionia_ch02".
    return