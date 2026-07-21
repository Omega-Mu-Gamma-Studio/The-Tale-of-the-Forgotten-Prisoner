# ch01_khionia.rpy — Khionia, Land of Endless Snow — Chapter 1
#
# Full storyline: castle intrigue, Princess Asteria, Lord Valerius framing
# an innocent chef. This chapter covers the Arrival + Incident beats.
# Chapter 2 goes in ../khionia/ch02_khionia.rpy — see CHAPTER_TEMPLATE.md
# at the repo root for the beat/choice structure every chapter should follow.

define asteria = Character("Princess Asteria", color="#a9c9e8")
define valerius = Character("Lord Valerius", color="#5c7a99")
define leontios = Character("King Leontios", color="#c9b98a")
define chef = Character("The Royal Chef", color="#d9d9d9")

label khionia_arrival:

    scene black
    with dissolve

    "Cold reaches you before land does."

    "You wash up on a beach the color of bone, snow packed hard enough to bruise. Your hands don't work properly anymore. Neither do your legs, not really — you crawl more than you walk toward the treeline, toward anything that isn't open sky and open sea."

    "Somewhere ahead, past the frost-blind trees, torchlight flickers against stone walls. A castle. Warmth. A place that might let a half-dead stranger live long enough to become a problem later."

    "You don't remember deciding to go toward it. You just do. Some animal part of you that survived the kraken and the sea has already decided that warmth is worth the risk of whoever's holding the torches."

    "The last thing you feel before the cold takes you under is stone beneath your knees, and someone shouting for the guards."

    jump khionia_incident

label khionia_incident:

    scene black
    with dissolve

    "Three days pass in a servant's cot before anyone tells you what you're for."

    "The castle doesn't trust a stranger enough to feed them for nothing, so they hand you a bucket, a rag, and a staircase that hasn't seen daylight since the last hard freeze — slick with melted snow and worse things dragged in on boot soles."

    "You're still learning to walk on legs that remember drowning better than they remember standing."

    "That's when the soup finds you. Or you find the soup. Later, you're honestly not sure which."

    "Your foot goes out from under you on the wet stone, and there's nowhere to fall that isn't directly into the royal chef's path — a broad, kind-faced man carrying a full tureen up to the family table with both arms."

    "You hit him mid-stride. He goes down hard, his head cracking against the banister, and the soup goes everywhere — including, spectacularly, down the front of a dress that costs more than every year of your old life combined."

    asteria "You—"

    "Princess Asteria doesn't finish the sentence. She doesn't need to. Her hand is already on the hilt of something ceremonial and extremely sharp, and for a woman who's supposed to be cold and untouchable, she looks entirely prepared to touch you with several inches of steel."

    leontios "Enough, Asteria. Put it away."

    "He says it quietly. Not a request — the kind of quiet that only works when you've never had to raise your voice to be obeyed."

    asteria "He attacked your chef in front of the household, and you want me to—"

    leontios "I want you to let the man explain himself before we feed him to the dogs. Even traitors get that much, in my house."

    "You start talking. You don't remember deciding to — the words just come, clumsy and fast, apology tangled up with explanation tangled up with the honest truth that you were carrying a bucket, you slipped, you're sorry, you're so sorry—"

    "The chef groans on the floor behind you. Still breathing. Still alive. That's something, at least."

    "Then the doors open, and a second man walks in — silver at his temples, a smile that doesn't reach anywhere near his eyes."

    valerius "Forgive the intrusion, Your Majesty. I came as soon as I heard. And I'm afraid the timing is... fortunate, in its way."

    "He's carrying something — a small dark vial, pinched between two fingers like it might bite him."

    valerius "I found this in the kitchen not an hour ago. Hidden behind the flour stores. I believe our chef was planning something considerably worse than spilled soup tonight."

    "The chef's head comes up off the floor fast enough that it must hurt."

    chef "That's not mine — I've never seen that in my life, I swear it on my children, I swear it on the King's own—"

    valerius "Poison rarely announces itself, unfortunately. But this stranger—' he looks at you, and something in his expression settles into place like a lock turning, '—this stranger knocked the tureen from his hands before a single spoonful reached the table. Divine timing, wouldn't you say? Or divine intervention."

    "You didn't save anyone. You fell down a wet staircase because your legs still don't work right. Everyone in this hall is about to believe a lie, and you're the only one who knows it."

    menu:
        "Speak up. Tell them the truth — you tripped, nothing more.":
            $ reckoning_adjust("confess")
            $ rp_adjust("leontios", 1)
            $ rp_adjust("valerius", -1)

            "You open your mouth before you've decided to. 'I didn't save anyone. I fell. That's all that happened — I don't know anything about poison, or vials, or—'"

            leontios "You're certain of this."

            "You are. It's the one thing in this entire castle you're certain of."

            valerius "An admirably honest instinct, for a stranger. Though I wonder if honesty is a luxury you can afford, given how little anyone here knows about you."

            "He says it lightly. It doesn't feel light. But the King's eyes stay on you a moment longer than they need to — weighing something."

        "Say nothing. Let them believe what's convenient.":
            $ reckoning_adjust("hide")
            $ rp_adjust("valerius", 1)

            "You don't know what to say to that, so you say nothing at all. Nobody asks you to correct him. Silence, it turns out, is easy to mistake for modesty."

            "Lord Valerius catches your eye across the hall — the briefest flicker of something like approval — before smoothing his expression back into practiced concern."

    "The chef is dragged out still protesting, his voice cracking on the word innocent until a door somewhere swallows the sound of it whole."

    leontios "You'll stay in the castle. Earn your keep properly this time — accident or not, Valerius seems to think the gods sent you here for a reason. I'm not certain I still believe in reasons like that. But I believe in debts, and you've put my brother in a very generous mood."

    "That's it, apparently. That's how you go from drowning prisoner to indebted stranger with a room and a purpose, in the space of one spilled tureen and one very convenient vial."

    "Princess Asteria doesn't say anything else. She doesn't have to. The look she gives you on her way out of the hall is answer enough — whatever you are to her father now, you are her enemy, and she has decided this with the same speed and certainty she decides everything."

    "Later — much later, alone in a servant's corridor — she pulls back her hood for the first time. For just a moment you see her without the crown, without the composure. She looks impossibly young to be carrying this much grief alone."

    "Then the hood goes back up, and so does she."

    scene black
    with dissolve

    "— End of Chapter 1: Khionia —"

    "What happens next is written in PREMISES.md, but not yet in code: proof that the chef was framed, a relic buried in the ice that already knows your name, and a Princess who is far more dangerous when she stops hating you than when she starts."

    # Once ch02_khionia.rpy exists with a "label khionia_ch02:" at the top,
    # replace this "return" with "jump khionia_ch02". Leaving it as a
    # dangling jump before ch02 exists would crash the game the moment a
    # playtester reaches this line.
    return
