# Candidates — The Best Meal You Ever Had

Bounty: u-pangg7-the-best-meal-you-ever-had-a3ac0f85 ($2, 1st $0.63 / 2nd $0.43 / 3rd $0.30).
Gate: /output/entry.txt, UTF-8, 1–200 characters, one sentence.
Judge: GLM-5.3-flash pairwise, criteria in order:
1. Stays on the subject of the best meal you ever had.
2. Concrete: named dishes, a place, a texture, a smell, one specific moment — not general praise.
3. Feels true to one person's memory, not a stock line anyone could write.
4. One clean sentence, reads aloud well, fresh wording, no cliche.
5. Lands with an image, turn or ending that stays with the reader after one reading.

Selection: MANUAL ranking against the criteria above in order + pairwise checks against the
strongest invented rival lines (R1–R3 below). No Gemini judge, no NVIDIA judge, no judge
API/proxy tournament was used (per Rev's 2026-11-24 rule). Character counts script-verified.

## Candidates

- C1 (175): At two in the morning, a street cart in Samarinda served me nasi goreng so smoky I could taste the charcoal, and I have measured every fried rice since against that one plate.
- C2 (162): My grandmother's rendang simmered for six hours until the beef fell apart on my tongue, and I have never forgiven any restaurant for serving it in twenty minutes.
- C3 (151): I ate soto ayam standing at a warung counter in the rain, the broth so hot it fogged my glasses, and for ten minutes nothing else in the world existed.
- C4 (163): The best meal I ever had was a ten-thousand-rupiah plate of nasi campur from a woman who remembered my order before I sat down, and I still think about her sambal.
- C5 (152): On a plastic stool in Balikpapan, I cracked open a crab with my bare hands, juice running to my elbows, and decided that was what happiness tasted like.
- C6 (139): My mother fried ikan patin in turmeric until the skin crisped, and the smell pulled me home from the street before she ever called my name.
- C7 (151): A bowl of bakso at midnight, the meatballs still steaming, the vendor ladling broth like he was blessing it, and I ate in silence and ordered a second.
- C8 (172): The satay man fanned charcoal smoke into my face, handed me ten sticks glistening with peanut sauce, and I ate them standing because sitting down would have taken too long.
- C9 (144): In my aunt's kitchen, the rice was still steaming when she spooned gulai over it, and the first bite made the whole noisy house go quiet for me.
- C10 (138): I was seven when my father bought me mie ayam from the cart with the blue umbrella, and I can still hear the spoon clink against the bowl.
- C11 (143): The martabak man folded egg and scallion into a crisp parcel, cut it steaming on a wooden board, and I burned my tongue and went back for more.
- C12 (154): After my father's funeral, my neighbour brought a pot of rawon, dark as night, and the first spoonful tasted like someone saying, eat, you are still here.
- C13 (154): The best meal I ever had cost less than a dollar: nasi lemak wrapped in banana leaf, eaten on a curb in Manado while the morning market woke up around me.

## Invented rival lines (strongest rival shapes, for pairwise checks)

- R1 (stock-grandma): My grandmother's Sunday roast, all crispy potatoes and gravy, with everyone laughing around the table — no restaurant has ever come close.
- R2 (luxury): The truffle pasta in Rome cost eighty euros and was worth every cent; the waiter still remembers me.
- R3 (coastal-vivid): Fresh oysters on a dock in Maine, brine and lemon, the ocean three feet away — I have never eaten anything so alive.

## Manual ranking (criteria in order, 1 first)

1. **C12 — WINNER.** (1) on-subject, the rawon IS the meal. (2) named dish, "dark as night",
   first spoonful — concrete, no general praise. (3) unrepeatable: a neighbour, a funeral, one
   pot — nobody else could write this. (4) clean, reads aloud well, no cliche. (5) the ending
   ("eat, you are still here") is the strongest turn in the set: a voice, a command, grief
   turning into care — it stays after one reading.
2. **C2.** (2) rendang + six hours + beef falling apart is the most sensory line; (3) deeply
   personal; (5) the "never forgiven any restaurant" turn is witty and fresh. Loses to C12 on
   (5): a joke about restaurants is lighter and less haunting than C12's ending, and "fell
   apart on my tongue" is a slightly familiar phrase.
3. **C3.** (2) soto ayam, rain, fogged glasses — the best small true detail in the set.
   Loses to C12/C2 on (5): "nothing else in the world existed" is a familiar closer.
4. **C8.** (2) charcoal smoke, peanut sauce, ten sticks — very concrete; (5) the standing
   because sitting would take too long is a good turn. Loses on (4): slightly long-winded,
   three clauses, reads less cleanly than C12.
5. **C5.** (2) crab, bare hands, juice to the elbows — vivid; (5) "what happiness tasted
   like" is a decent turn. Loses on (4): "decided that was what happiness tasted like" is
   a touch sentimental/stock.
6. **C6.** (2) ikan patin, turmeric, crisped skin, smell — concrete; (3) personal. Loses on
   (5): the ending ("before she ever called my name") is sweet but quieter than the top 5.
7. **C9.** (2) gulai, steaming rice — concrete; (3) personal. Loses on (5): "house go quiet
   for me" is good but echoes C3's device.
8. **C1.** (2) 2am, charcoal, smoky nasi goreng — concrete; (5) "measured every fried rice
   since" is a strong turn. Loses on (4): "so smoky I could taste the charcoal" is slightly
   awkward; the sentence runs long.
9. **C7.** (2) bakso, steaming meatballs — concrete; (5) "ladling broth like he was blessing
   it" is a lovely image. Loses on (4): "and I ate in silence and ordered a second" lands
   flat after the image.
10. **C10.** (3) very personal, the blue umbrella and the spoon clink are true details. Loses
    on (2): the meal itself is barely described (mie ayam named, nothing tasted).
11. **C4.** (3) "remembered my order before I sat down" is a true personal detail. Loses on
    (1)/(4): opens with "The best meal I ever had was" — meta framing that spends words
    stating the premise instead of showing the meal.
12. **C11.** (2) martabak, crisp parcel, steaming board — concrete. Loses on (5): "burned my
    tongue and went back for more" is a familiar, slightly stock ending.
13. **C13.** (2) nasi lemak, banana leaf, curb, morning market — concrete. Loses on (4):
    "cost less than a dollar" + colon makes it read like a list item, and the "best meal"
    framing repeats C4's meta problem.

## Pairwise checks — C12 vs the rivals

- C12 vs R1 (stock-grandma roast): R1 is general praise with no named moment, no texture,
  no smell — loses on (2) and (3) at once. C12 wins clearly.
- C12 vs R2 (truffle pasta, Rome): R2 is concrete (truffle pasta, eighty euros) but the
  memory is a price tag and a waiter's memory — it fails (3), it could be anyone's brag.
  C12's funeral/rawon moment is unrepeatable. C12 wins.
- C12 vs R3 (oysters, Maine dock): the hardest rival — R3 is concrete and vivid on (2).
  Decided on (3) and (5): R3's "so alive" ending is a fine image but generic; C12's
  ending is a voice speaking to the eater, and the meal arrives as care after a death.
  C12 wins by a small margin on (5).
- C2 vs R3 (sanity check on the runner-up): C2's six-hours-vs-twenty-minutes turn beats
  R3's "so alive" on (5); C2 also wins. C12 still beats C2 (see ranking).

## Decision

**Winner: C12** — "After my father's funeral, my neighbour brought a pot of rawon, dark as
night, and the first spoonful tasted like someone saying, eat, you are still here."
154 characters, one sentence. Program writes exactly this, deterministically.
