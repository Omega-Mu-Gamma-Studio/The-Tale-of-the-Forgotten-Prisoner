# Chapter Template — The Tale of the Forgotten Prisoner

This is the reusable skeleton for every chapter, in every kingdom, from
Chapter 2 onward. Chapter 1 (already written per kingdom) covers Arrival +
Incident and doesn't need to follow this shape. Chapters 2–12 should.

This file is NOT a .rpy file on purpose — it lives at the repo root, next
to PREMISES.md, so Ren'Py never tries to compile it. It's a planning
document, not game content.

---

## The 12-chapter arc, in three acts (per kingdom)

**Act 1 — Arrival (Ch 1–4)**
Ch1: Arrival + inciting incident (done for all four kingdoms)
Ch2–3: Settling in. Establish daily life, the kingdom's rules, the LI's
       personality beyond the first impression. Low stakes, high texture.
Ch4: Act 1 turning point — something raises the stakes for the first time
     (a secret glimpsed, a debt called in, a rule broken).

**Act 2 — Entanglement (Ch 5–8)**
Ch5–6: The bond with the LI deepens. Kingdom-specific plot (the frame-up,
       the debt, the collar, the curse) starts generating real
       consequences instead of just atmosphere.
Ch7: A memory-fragment chapter — the player's own crime surfaces more
     concretely here than anywhere before. Confess/hide/embrace choices
     should feel heavier in this chapter than earlier ones.
Ch8: Midpoint crisis — the kingdom's central threat becomes undeniable.

**Act 3 — Reckoning (Ch 9–12)**
Ch9–10: Escalation. The player's choices so far (RP + reckoning) start
        visibly shaping what NPCs will and won't do for them.
Ch11: Climax setup — everything converges on one confrontation.
Ch12: Kingdom climax + resolution. Chapter should end on a hook toward
      the shared convergence/ending content (see endings.rpy, not yet
      written) rather than a fully closed-off ending.

---

## Per-chapter beat template

Every chapter (2–12) should hit roughly this shape. Not a rigid formula —
skip or merge beats where the story wants to — but use it as a checklist
so no kingdom's chapter 6 ends up half the length of another's.

1. **Cold open** (1 beat) — where are we, what's the emotional temperature
   left over from last chapter. Short — a paragraph or two.
2. **Development scene A** (1–2 beats) — kingdom plot moves forward.
3. **Choice point 1 — relationship-flavored** — usually tied to `rp_adjust()`
   for the kingdom's LI or a second NPC. Doesn't have to be dramatic; small
   trust-building or trust-costing moments count.
4. **Development scene B** (1–2 beats) — bonding/dialogue with the LI, or a
   scene with a secondary NPC (Valerius, the merchant, etc).
5. **Choice point 2 — reckoning-flavored** — tied to `reckoning_adjust()`.
   This is where the player's own guilt/denial/defiance gets tested.
6. **Turn / cliffhanger** (1 beat) — the beat that makes the player want
   to open the next chapter.

Target: **5–7 narrative beats, 2 choice points** per chapter, as a
baseline. Tentpole chapters (4, 8, 12 — the act turning points) can run
3–4 choice points instead of 2, since more should be resolving at once.

Rough length: chapter 1 for each kingdom ran ~90–125 lines of .rpy. Aim
for similar in chapters 2–3, and let length grow naturally in the back
half of the story as more threads are active at once.

---

## Choice-point conventions (keep consistent across all 48 files)

- Every choice should call **one** of `rp_adjust(npc, amount)` or
  `reckoning_adjust(kind)` (or both) — see `game/scripts/characters.rpy`.
  If a choice doesn't move either tracker, ask whether it's a real choice
  or just flavor text that could be a `menu` with no mechanical effect
  (also fine, occasionally — not everything needs a stat).
- `amount` for `rp_adjust` should usually be `+1` or `-1`. Reserve `+2`/`-2`
  for chapter-defining moments (roughly one per kingdom's Act 2 or Act 3).
- New NPC introduced mid-story? Just call `rp_adjust("new_name", 1)` —
  it self-initializes. No need to touch `characters.rpy` unless you also
  want to `define` a Character() for their dialogue color/namebox.
- Keep the emerging pattern: `confess` = costly honesty, `hide` = costly
  self-protection, `embrace` = leaning into darker/self-interested
  instincts. Not every chapter needs all three — most chapters will only
  produce 1–2 of the tags, which is expected and fine.

---

## File map (what to touch, and only that)

```
game/scripts/
    characters.rpy              <- touch ONLY to define a new NPC's Character()
    prologue.rpy                <- shouldn't need touching again
    khionia/
        ch01_khionia.rpy        <- done
        ch02_khionia.rpy        <- next to write
        ch03_khionia.rpy ... ch12_khionia.rpy
    rhizoma/
        ch01_rhizoma.rpy        <- done
        ch02_rhizoma.rpy ... ch12_rhizoma.rpy
    arenia/
        ch01_arenia.rpy         <- done
        ch02_arenia.rpy ... ch12_arenia.rpy
    helos/
        ch01_helos.rpy          <- done
        ch02_helos.rpy ... ch12_helos.rpy
    endings.rpy                 <- not yet created; convergence/epilogue,
                                    write once all four Ch12s exist
```

When writing chapter N of a kingdom: **touch only that one chapter file.**
You never need to open another kingdom's folder, and you almost never
need to touch `characters.rpy` (only for brand-new named NPCs).

Each new chapter file needs, at minimum:

```renpy
# chNN_khionia.rpy — Khionia — Chapter N
#
# One-line summary of what this chapter covers.

label khionia_chNN:

    scene black
    with dissolve

    "..."

    return
```

Then, in the **previous** chapter file, change its ending `return` to
`jump khionia_chNN` once the new chapter's label actually exists.
Never leave a `jump` pointing at a label that isn't written yet — Ren'Py
will crash the moment a player reaches that line.
