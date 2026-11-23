---
tag: 5KXKTWPV3P
kind: example
name: No inhabitant of the island can say "I am a knave"
msc: ["03B05", "00A08"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: MVADXMFV59
    note: the translation a <-> not a is false in both rows, so no knight or knave can make this statement
uses: [MVADXMFV59, 0S6GMNJ62Y, 05RSK4Q657, KBYY281V8T]
sources:
  - url: https://en.wikipedia.org/wiki/Knights_and_Knaves
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

Suppose an inhabitant $A$ of the [[island of knights and knaves|MVADXMFV59]] says "I am a knave".
We show that this situation cannot occur on the island, so it is not a knights and knaves puzzle.

1. Let $a$ be "$A$ is a knight", so the statement "I am a knave" is $\neg a$.
2. By the rule of the island, the statement gives the [[biconditional|0S6GMNJ62Y]] $a \leftrightarrow \neg a$.
3. The [[truth table|05RSK4Q657]] has two rows.

| $a$ | $\neg a$ | $a \leftrightarrow \neg a$ |
|---|---|---|
| T | F | F |
| F | T | F |

4. The biconditional is false in both rows, so no type of $A$ is consistent with the statement.
5. In words, a knight cannot say it, because it would be false, and a knave cannot say it, because it would be true.

## Remarks

The sentence "I am a knave" is the island's version of the [[liar sentence|KBYY281V8T]].
The liar sentence produces a paradox, while on the island the sentence only contradicts the assumption that $A$ said it.
So a puzzle that reports this statement has no solution, and the conclusion is that the report is false.
The same argument shows that no inhabitant can say "I am a knave and $2 + 2 = 4$".
An inhabitant can say "I am a knave and $2 + 2 = 5$", because $a \leftrightarrow (\neg a \land \bot)$ is true when $a$ is false, so the speaker is a knave.
In variants of the island with normals, a speaker who says "I am a knave" must be a normal, since a normal may say a true or a false sentence.

## Explanations

### L1 human

A truth-teller who says "I am a liar" would be telling a lie, which a truth-teller never does.
A liar who says "I am a liar" would be telling the truth, which a liar never does.
So nobody on the island can say this sentence.
If a story claims that someone on the island said it, the story is wrong.

### L2 human

A statement whose biconditional is false in every row cannot be made on the island.
For one speaker the test is short: $a \leftrightarrow S$ must be true for $a$ true or for $a$ false.
For "I am a knave or $2 + 2 = 5$", the formula $a \leftrightarrow (\neg a \lor \bot)$ is again $a \leftrightarrow \neg a$, so this statement is impossible too.
For "I am a knave or $2 + 2 = 4$", the formula $a \leftrightarrow \top$ holds for $a$ true, so a knight can say it.
Watch out: the habit from earlier puzzles suggests "so $A$ is a knave", but both rows fail, so no type is consistent and the statement itself is impossible.
