---
tag: K17GT0KGZF
kind: example
name: Knights and knaves puzzles
msc: ["03B05", "00A08"]
topics: [PM1AYWABA7]
audience: school
instance_of: [MVADXMFV59]
uses: [MVADXMFV59, 0S6GMNJ62Y, 05RSK4Q657, 0WCP0PVET6, 025YZN3VJW]
sources:
  - url: https://en.wikipedia.org/wiki/Knights_and_Knaves
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

On the [[island of knights and knaves|MVADXMFV59]], knights make only true statements and knaves make only false statements.
For an inhabitant $A$, let $a$ be the proposition "$A$ is a knight".
If $A$ says $S$, then $a \leftrightarrow S$ is true, by the definition of the [[biconditional|0S6GMNJ62Y]].
We solve one puzzle in two ways, and then we find a question that identifies a road.

Puzzle 1: $A$ says "we are both knaves", and we must find the types of $A$ and $B$.
The statement is $\neg a \land \neg b$, so the puzzle is the formula $a \leftrightarrow (\neg a \land \neg b)$.
Method 1 is a [[truth table|05RSK4Q657]].

| $a$ | $b$ | $\neg a \land \neg b$ | $a \leftrightarrow (\neg a \land \neg b)$ |
|---|---|---|---|
| T | T | F | F |
| T | F | F | F |
| F | T | F | T |
| F | F | T | F |

1. By the truth table of [[conjunction|025YZN3VJW]], the column $\neg a \land \neg b$ is true only when $a$ and $b$ are both false.
2. The last column is true when $a$ and $\neg a \land \neg b$ have the same value.
3. Only the third row has T in the last column, so $A$ is a knave and $B$ is a knight.

Method 2 is a [[proof by cases|0WCP0PVET6]].

4. If $A$ is a knight, the statement is true, so $A$ is a knave, which contradicts the case.
5. If $A$ is a knave, the statement is false, so $A$ and $B$ are not both knaves, and since $A$ is a knave, $B$ is a knight.
6. Check: "we are both knaves" is false because $B$ is a knight, and a knave makes false statements, so the solution is consistent and matches step 3.

Puzzle 2: a road splits into a left road and a right road, and exactly one of them leads to the village.
An inhabitant of unknown type stands at the fork, and we may ask one yes-or-no question.
Let $k$ be "the inhabitant is a knight" and $L$ be "the left road leads to the village".
An inhabitant answers yes to a question $q$ exactly when $k \leftrightarrow q$ is true, since a knight says yes to true questions and a knave says yes to false ones.

7. The direct question "does the left road lead to the village?" fails, because the answer is yes exactly when $k \leftrightarrow L$, which depends on the unknown $k$.
8. The question "are you a knight if and only if the left road leads to the village?" has $q = (k \leftrightarrow L)$, so the answer is yes exactly when $k \leftrightarrow (k \leftrightarrow L)$.
9. The question "if I asked you whether the left road leads to the village, would you say yes?" has the inner answer yes exactly when $k \leftrightarrow L$.
   So again $q = (k \leftrightarrow L)$, and the answer is yes exactly when $k \leftrightarrow (k \leftrightarrow L)$.
10. The table checks all four cases.

| $k$ | $L$ | $k \leftrightarrow L$ | direct question | questions 8 and 9 |
|---|---|---|---|---|
| T | T | T | yes | yes |
| T | F | F | no | no |
| F | T | F | no | yes |
| F | F | T | yes | no |

11. In every row, the answer to questions 8 and 9 is yes exactly when $L$ is true, so the traveler takes the left road after a yes and the right road after a no.

## Remarks

The rule $a \leftrightarrow S$ turns each puzzle into a formula of propositional logic, and the solutions are the rows where the formula is true.
In puzzle 1, the truth table and the case analysis are the same computation, since the case analysis tests the rows in two groups by the value of $a$.
If $A$ says instead "at least one of us is a knave", the formula is $a \leftrightarrow (\neg a \lor \neg b)$, and the only solution is that $A$ is a knight and $B$ is a knave.
In puzzle 2, the identity $k \leftrightarrow (k \leftrightarrow L) \equiv L$ explains why both questions work: the speaker's type appears twice and cancels.
Logic grid puzzles, in which a table of possibilities is filled by elimination, form another family, collected under [[logic and deduction puzzles|4QETN23YNF]].

## Explanations

### L1 human

Two people meet us, and the first one says "we are both liars".
A truth-teller could never say this, because it would make the speaker a liar.
So the first person is a liar, and the sentence is false.
The sentence would be true if both were liars, so the second person is not a liar.
For the road, ask: "if I asked you whether the left road goes to the village, would you say yes?"
A truth-teller reports a true answer.
A liar lies about a lie, and the two lies cancel, so the answer is also correct.

### L2 human

A puzzle on the island is solved in four steps.
First, give each inhabitant a letter for "is a knight".
Second, translate each statement $S$ of an inhabitant $X$ as $x \leftrightarrow S$.
Third, find the rows of the truth table in which all the biconditionals are true, or test the cases for one inhabitant at a time.
Fourth, check each solution against the original sentences.
A mistake in the second step usually gives no solution or two solutions, so the count of solutions is a check on the translation.
Watch out: the direct question of step 7 looks enough, but the table shows that a knave answers it wrongly in both rows where $k$ is false.
