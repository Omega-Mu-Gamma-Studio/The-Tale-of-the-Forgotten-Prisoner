# ch01_rhizoma.rpy — Rhizoma, Root of Life — Chapter 1
# "From Roots, All Things"
#
# Full storyline: underground survival, Thalloa the root-gatherer,
# the merchant's workshop, the poison mushroom, and the Heartwood Seed.
# Chapter 2 goes in ../rhizoma/ch02_rhizoma.rpy
# ============================================================
# Rhizoma Chapter 1 - Image Definitions
# Based on PROMPTS.md file naming convention
# ============================================================

# --- Silhouette BGs ---
image silhouette_rhizoma_roots = "images/silhouettes/rhizoma/silhouette_rhizoma_roots.png"
image silhouette_rhizoma_path = "images/silhouettes/rhizoma/silhouette_rhizoma_path.png"
image silhouette_rhizoma_workshop = "images/silhouettes/rhizoma/silhouette_rhizoma_workshop.png"
image silhouette_rhizoma_aftermath = "images/silhouettes/rhizoma/silhouette_rhizoma_aftermath.png"
image silhouette_rhizoma_secret = "images/silhouettes/rhizoma/silhouette_rhizoma_secret.png"

# --- Major Moments ---
image major_rhizoma_roots = "images/major_moments/rhizoma/major_rhizoma_roots.png"
image major_rhizoma_trade = "images/major_moments/rhizoma/major_rhizoma_trade.png"
image major_rhizoma_poison = "images/major_moments/rhizoma/major_rhizoma_poison.png"
image major_rhizoma_thalloa_secret = "images/major_moments/rhizoma/major_rhizoma_thalloa_secret.png"

# --- Character Silhouettes ---
image thalloa = "images/characters/rhizoma/thalloa_default.png"
image thalloa_hopeful = "images/characters/rhizoma/thalloa_hopeful.png"
image thalloa_determined = "images/characters/rhizoma/thalloa_determined.png"

image merchant = "images/characters/rhizoma/merchant_default.png"
image merchant_calculating = "images/characters/rhizoma/merchant_calculating.png"

image canopy_noble = "images/characters/rhizoma/canopy_noble.png"
image guard = "images/characters/rhizoma/guard.png"
image root_dweller = "images/characters/rhizoma/root_dweller.png"


# ============================================================
# Rhizoma Chapter 1: "From Roots, All Things"
# ============================================================

define thalloa = Character("Thalloa", color="#8fbf7f")
define merchant = Character("Merchant", color="#c9b98a")
define noble = Character("Canopy Noble", color="#d1a24a")
define guard = Character("Guard", color="#d9d9d9")

label rhizoma_ch01:

    # ============================================================
    # Scene 1: The Root-Tangle
    # ============================================================

    scene black with fade

    "Darkness reaches you before land does."

    scene silhouette_rhizoma_roots with fade

    "You wake tangled in roots. They're massive—as thick as your torso, stretching up into darkness."
    "You're hanging upside down, water dripping from your clothes. Your head is pounding. Your ribs ache."
    "The current spat you out here."

    "You can't move. The roots are wrapped around your legs, your arms, your chest. You can barely breathe."

    # MAJOR MOMENT: The Root-Tangle
    show major_rhizoma_roots at truecenter with dissolve
    pause 1.5
    hide major_rhizoma_roots with dissolve

    menu:
        "How do you free yourself?"
        "Pull":
            $ rhizoma_escape = "pull"
            "The roots are rough, scraping your skin raw. Your muscles scream. But one by one, they break."
        "Twist":
            $ rhizoma_escape = "twist"
            "You work yourself loose, moving with the roots rather than against them. It's slower—you're exhausted—but you're not bleeding."
        "Call out":
            $ rhizoma_escape = "call"
            "Your voice echoes in the darkness. You wait. The silence stretches. And then—footsteps."

    "You fall to the ground. You're in a cavern, but it's not like any cavern you've seen."
    "The ceiling is a tangle of roots, and they glow with a soft, pulsing light—bioluminescent fungi."
    "The air is warm and humid, smelling of earth, moss, and something sweet."

    "You see water dripping from the roots. It's amber-colored. You touch it. It's sticky—sap."

    "You realize: you're not in a cave. You're inside a tree. A massive, ancient tree. And the roots are its veins."

    jump rhizoma_scene2


    # ============================================================
    # Scene 2: The First Encounter
    # ============================================================

    label rhizoma_scene2:

    scene silhouette_rhizoma_roots with fade

    "You hear movement. A figure emerges from the darkness—a girl, young, perhaps eighteen."
    "She's holding a basket, and she's picking glowing mushrooms from the roots."
    "Her clothes are simple, patched, and stained with soil. Her hair is dark and tangled."
    "Her eyes are wide, curious, and utterly unafraid."

    "She stops when she sees you. She tilts her head. She doesn't scream. She doesn't run."

    show thalloa at left with dissolve

    menu:
        "How do you greet her?"
        "Desperate":
            $ rhizoma_greeting = "desperate"
            mc "\"Please. I need help. I was on a ship. I don't know where I am.\""
        "Cautious":
            $ rhizoma_greeting = "cautious"
            mc "\"Who are you? Where is this place?\""
        "Silent":
            $ rhizoma_greeting = "silent"
            "You just stare at her. You're too exhausted to speak. Let her make the first move."

    "She approaches. She touches your arm. Her fingers are cool."

    thalloa "You're not from here. I can tell."

    "She looks up at the roots. She presses her ear against one. She listens."
    "She listens longer than necessary. When she pulls away, her eyes are wider—like she heard something she didn't expect."

    thalloa "The tree says you're lost. But you're not dangerous."

    "She hesitates."

    thalloa "It also said... you're afraid."

    mc "Afraid of what?"

    thalloa "I don't know. It didn't say."

    "But you can tell she's holding something back."

    hide thalloa with dissolve

    jump rhizoma_scene3


    # ============================================================
    # Scene 3: The Journey to Zōopolis
    # ============================================================

    label rhizoma_scene3:

    scene silhouette_rhizoma_path with fade

    "She leads you through the roots. The path is winding, narrow in places, opening into vast caverns in others."
    "You pass villages carved into the roots—homes built into the wood, glowing with mushroom-light."

    show thalloa at left with dissolve

    "You see people. Root-people. They're small, pale, their eyes wide and adapted to darkness."
    "They dress in simple clothes. They don't speak much. They watch you as you pass—suspicious, wary."

    hide thalloa with dissolve

    menu:
        "How do you react to their stares?"
        "Look down":
            $ rhizoma_stares = "down"
            "You keep your eyes on the ground. You don't want to offend. They relax slightly."
        "Look back":
            $ rhizoma_stares = "back"
            "You meet their eyes. You don't look away. You're a survivor, not a threat. They shift, uncertain."
        "Ask Thalloa":
            $ rhizoma_stares = "ask"
            mc "\"Why are they looking at me like that?\""

            show thalloa at left with dissolve
            thalloa "They don't see outsiders. They're afraid. But they'll get used to you."
            hide thalloa with dissolve

    show root_dweller at right with dissolve

    "A root-dweller, an older man with a scarred face, spits at Thalloa's feet. She doesn't react. She keeps walking."

    hide root_dweller with dissolve
    show thalloa at left with dissolve

    mc "Why didn't you say anything?"

    thalloa "He's afraid. That's all. The rot has been spreading for years. People are scared. They take it out on anyone they can."

    hide thalloa with dissolve

    "You look back. The man is still watching you. He's not angry—he's terrified."

    show thalloa at left with dissolve

    "Thalloa tells you about Rhizoma: the caverns, the roots, the Heart-Root at the center."
    "She tells you about the caste system—root-gatherers like her at the bottom, merchants in the middle, and the Canopy Lord and his nobles at the top, living in the branches above the roots."

    thalloa "The merchant's a good man. He'll give you work. And he won't ask too many questions."

    "There's something in her voice—a warning. Don't tell him everything."

    hide thalloa with dissolve

    jump rhizoma_scene4


    # ============================================================
    # Scene 4: The Merchant's Workshop
    # ============================================================

    label rhizoma_scene4:

    scene silhouette_rhizoma_workshop with fade

    "You arrive at the merchant's workshop. It's carved into a massive root, a series of chambers filled with goods—fungi drying on racks, amber chunks glowing on shelves, jars of root-essence bubbling over low fires."
    "It smells of earth, honey, and something sharp."

    show merchant at center with dissolve
    show thalloa at left with dissolve

    "The merchant is there. He's older, round, with a kind face and sharp eyes. He looks you over."

    merchant "Who's this?"

    thalloa "A survivor. The tree told me to bring him here."

    "He raises an eyebrow. He knows what the tree means."

    merchant "Well, if the tree speaks, who am I to argue?"

    hide thalloa with dissolve

    menu:
        "How do you present yourself?"
        "Humble":
            $ rhizoma_presentation = "humble"
            mc "\"I'll work hard. I don't need much. Just a place to stay.\""
        "Curious":
            $ rhizoma_presentation = "curious"
            mc "\"What is this place? What do you do here?\""
        "Guarded":
            $ rhizoma_presentation = "guarded"
            mc "\"I don't trust you. I don't trust anyone.\""

    "He gives you a job: sorting mushrooms. Simple, repetitive work."
    "You learn the types—which are safe, which are medicinal, which are poisonous. He teaches you the names."
    "You learn quickly. Faster than he expects."

    "You notice him watching you too closely. His eyes follow your hands as you sort."

    merchant "Where are you from?"

    mc "I don't remember."

    merchant "Good. Don't try."

    "It's unsettling. He knows something about you. He's not just kind—he's calculating."

    "As you work, you notice a corner of the workshop. A locked chest."
    "A strange symbol carved into the wood—a circle with a line through it."
    "The same symbol from Khionia. But you don't recognize it. Not yet."

    hide merchant with dissolve

    jump rhizoma_scene5


    # ============================================================
    # Scene 5: The First Trade
    # ============================================================

    label rhizoma_scene5:

    scene silhouette_rhizoma_workshop with fade

    "A noble arrives. A Canopy-dweller. He's tall, thin, dressed in fine clothes made of woven root-fiber."
    "He's accompanied by guards. He looks at you with disdain."

    show canopy_noble at center with dissolve
    show guard at right with dissolve

    noble "This is the outsider? He looks like a drowned rat."

    "He wants to buy rare mushrooms. The merchant says: 'We have a new batch. He'll take care of it.'"

    hide canopy_noble
    hide guard
    show merchant at center with dissolve

    menu:
        "How do you handle the trade?"
        "Standard":
            $ rhizoma_trade = "standard"
            "You give him the mushrooms he requests. Safe, common varieties. You're playing it safe."
        "Bold":
            $ rhizoma_trade = "bold"
            "You suggest a variety he didn't ask for. A rare, valuable one. It's risky—if it goes wrong, you're blamed."
        "Innovative":
            $ rhizoma_trade = "innovative"
            "You negotiate. You bundle the mushrooms with a package of dried herbs, offering a better price. The merchant is impressed—you have skills he didn't expect."

    hide merchant with dissolve
    show canopy_noble at center with dissolve
    show guard at right with dissolve

    if rhizoma_trade in ["bold", "innovative"]:
        "The noble's eyes narrow. He studies you."

        noble "You're not from here. Where did you learn to trade like this?"

        menu:
            "How do you answer?"
            "Truthful":
                $ rhizoma_answer = "truthful"
                mc "\"I was a merchant. In my old life.\""
                "You're revealing a piece of your past."
            "Vague":
                $ rhizoma_answer = "vague"
                mc "\"I learned from experience.\""
                "You're hiding."
            "Deflect":
                $ rhizoma_answer = "deflect"
                mc "\"Does it matter? You're getting a good deal.\""
                "You're deflecting, shifting the focus."

    # MAJOR MOMENT: The Trade
    show major_rhizoma_trade at truecenter with dissolve
    pause 1.5
    hide major_rhizoma_trade with dissolve

    "The trade is successful. The merchant praises you."
    "Thalloa smiles, but it's careful. She's watching you, as if she's waiting for something."

    hide canopy_noble
    hide guard
    show thalloa at left with dissolve

    thalloa "You're good at that. Too good."

    mc "Is that a problem?"

    thalloa "I don't know yet."

    hide thalloa with dissolve

    jump rhizoma_scene6


    # ============================================================
    # Scene 6: The Mistake
    # ============================================================

    label rhizoma_scene6:

    scene silhouette_rhizoma_workshop with fade

    "Days pass. You work. You learn. You begin to fit in."
    "Thalloa brings you food, talks to you about the tree."

    show thalloa at left with dissolve

    thalloa "The rot is spreading. The Canopy Lord is draining the tree's essence. He doesn't care about the roots—only his gardens."

    hide thalloa with dissolve

    "You don't understand. You're too focused on survival."

    "One day, you're sorting mushrooms. You find one you don't recognize."
    "It's beautiful—bright red, covered in tiny gold spots. It looks valuable. You set it aside."

    "A nobleman arrives—not the previous one, a different one, older, tired."
    "He's looking for medicine. His wife is ill."
    "You see the mushroom on the table. You think it's medicinal. You offer it to him."

    show canopy_noble at center with dissolve

    menu:
        "Do you tell the merchant before you sell it?"
        "Yes":
            $ rhizoma_mistake = "tell"
            "You show him the mushroom. He looks at it—and his face goes pale."

            show merchant at right with dissolve

            merchant "That's not medicine. That's poison."

            "He takes it from you. He sends the noble away empty-handed."
            "You avoid disaster. The merchant is grateful. But you've seen him afraid."

            hide merchant with dissolve

        "No":
            $ rhizoma_mistake = "sell"
            "You sell it. You feel proud—you made a sale."
            "The noble leaves. The merchant discovers what you did. He's furious."

            show merchant at right with dissolve

            merchant "Do you have any idea what you've done?"

            "You've made a fatal mistake."

            hide merchant with dissolve

    hide canopy_noble with dissolve
    show thalloa at left with dissolve

    "After the noble leaves, Thalloa pulls you aside. She whispers:"

    thalloa "I should have told you. That mushroom... it's the same one that's killing the roots. The rot starts with it."

    "You feel a chill. Your mistake isn't just personal—it's connected to the kingdom's dying. You've touched the rot."

    hide thalloa with dissolve

    # MAJOR MOMENT: The Poison Mushroom
    show major_rhizoma_poison at truecenter with dissolve
    pause 1.5
    hide major_rhizoma_poison with dissolve

    "The noble's wife falls ill."

    if rhizoma_mistake == "sell":
        "She nearly dies."
    else:
        "She's still unwell, and the noble blames you for the delay."

    "Either way, blame lands on you."

    "Later, you learn: the noble's wife has been sick for months. She's survived—but she's been dying slowly."
    "The rot is systemic. The poison mushroom is a symptom, not the cause."

    jump rhizoma_scene7


    # ============================================================
    # Scene 7: The Aftermath
    # ============================================================

    label rhizoma_scene7:

    scene silhouette_rhizoma_aftermath with fade

    "The merchant's workshop is visited by the noble's guards. They demand answers. They're armed. They're angry."

    show guard at right with dissolve
    show merchant at center with dissolve

    "The merchant protects you."

    merchant "The outsider didn't know. It was my fault. I left the poison where he could reach it."

    hide merchant with dissolve
    show thalloa at left with dissolve

    "Thalloa begs him to save you. She's on her knees. She's crying."

    thalloa "He didn't mean it. He's just new. Please."

    hide thalloa
    hide guard
    show merchant at center with dissolve

    menu:
        "How do you react to being saved?"
        "Grateful":
            $ rhizoma_saved = "grateful"
            mc "\"Thank you. I won't forget this.\""
            "You accept his help. You owe him."
        "Defiant":
            $ rhizoma_saved = "defiant"
            mc "\"I didn't need you to speak for me. I can defend myself.\""
            "You stand tall. You don't want to be indebted."
        "Confused":
            $ rhizoma_saved = "confused"
            mc "\"Why are you doing this? You don't know me.\""
            merchant "No. But I know the girl. She doesn't ask for much. When she begs, I listen."
            "You realize Thalloa is more important than you thought."

    "After the guards leave, the merchant says:"

    merchant "But this isn't the first time. The noble's wife is sick, but she's not dead. She's survived. She's been sick for months."

    "He looks at you."

    merchant "The rot is spreading. People are dying slowly. And the Canopy Lord doesn't care."

    hide merchant with dissolve

    jump rhizoma_scene8


    # ============================================================
    # Scene 8: The Debt
    # ============================================================

    label rhizoma_scene8:

    scene silhouette_rhizoma_workshop with fade

    show merchant at center with dissolve

    "The merchant saves you, but at a cost."

    merchant "You're useful. You have skills no one in Rhizoma has. I'm keeping you."

    "You're not a prisoner. But you're not free."
    "He'll use your knowledge, your outside perspective, your trading skills. You owe him your life."

    menu:
        "How do you accept the debt?"
        "Acceptance":
            $ rhizoma_debt = "accept"
            mc "\"I understand. I'll work for you. I'll earn my freedom.\""
            "You'll stay until you've paid your debt."
        "Resistance":
            $ rhizoma_debt = "resist"
            mc "\"I don't owe you anything. I didn't ask for your help.\""
            "You push back. He's not your master."
        "Negotiation":
            $ rhizoma_debt = "negotiate"
            mc "\"I'll help you. But I want something in return. I want to know about the Canopy Lord. I want to understand the rot.\""
            "You're not just surviving—you're investigating."

    "He looks at you. There's something in his eyes—calculation, yes, but also hope."

    merchant "You have outside knowledge. You see things we've forgotten. That's why the tree sent you."

    "You don't understand. But he doesn't explain further."

    hide merchant with dissolve
    show thalloa at left with dissolve

    "Thalloa is silent. She looks at you with something in her eyes—not pity, not fear. It's hope."
    "She knows something. She's waiting for the right moment."

    hide thalloa with dissolve

    jump rhizoma_scene9


    # ============================================================
    # Scene 9: Thalloa's Secret
    # ============================================================

    label rhizoma_scene9:

    scene silhouette_rhizoma_secret with fade

    show thalloa at center with dissolve

    "After the merchant leaves, Thalloa takes you aside."
    "She leads you to a small chamber, deep in the roots. It's quiet here. The sounds of the workshop fade."

    "She presses her ear against the wood. She listens. Then she whispers:"

    thalloa "The tree speaks to me. It's been telling me about you since you arrived."

    menu:
        "How do you respond?"
        "Curious":
            $ rhizoma_secret = "curious"
            mc "\"What does it say?\""
        "Skeptical":
            $ rhizoma_secret = "skeptical"
            mc "\"I don't believe you.\""
        "Afraid":
            $ rhizoma_secret = "afraid"
            mc "\"Why is it talking about me?\""

    "She looks at you. Her eyes are wide, earnest, and utterly certain."

    thalloa "The tree says you're the key. The rot is spreading because the Heartwood Seed has been moved. Someone took it. And the tree says you know where it is."

    # MAJOR MOMENT: Thalloa's Secret
    show major_rhizoma_thalloa_secret at truecenter with dissolve
    pause 1.5
    hide major_rhizoma_thalloa_secret with dissolve

    "You don't remember. But her words echo something—a memory, a dream."
    "The sigil. The circle with the line through it."
    "A chamber of roots and light. A seed, pulsing with warmth."

    "She adds, her voice dropping:"

    thalloa "The tree also said... that you're afraid of what you'll find."

    "You feel exposed. She's not just seeing you—she's seeing into your hidden crime."
    "Whatever you did, wherever you came from, the tree knows. And it sent you here for a reason."

    thalloa "You're not here by accident. The tree brought you here. And when you remember what you did, everything will change."

    hide thalloa with dissolve

    scene black with fade

    "The tree remembers what you've forgotten. And it's waiting for you to remember."

    # ============================================================
    # End of Chapter 1: Rhizoma
    # ============================================================

    "— End of Chapter 1: Rhizoma —"

    # Once ch02_rhizoma.rpy exists with a "label rhizoma_ch02:" at the top,
    # replace this "return" with "jump rhizoma_ch02".
    return