---
tag: ~f7fcb79c
kind: example
name: 'Three inhabitants, two statements: "all of us are knaves" and "exactly one of us is a knight"'
msc: ["03B05", "00A08"]
topics: [PM1AYWABA7]
audience: school
instance_of: [MVADXMFV59]
uses: [MVADXMFV59, 0S6GMNJ62Y, 05RSK4Q657, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Knights_and_Knaves
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

Three inhabitants $A$, $B$, $C$ of the [[island of knights and knaves|MVADXMFV59]] meet a visitor.
$A$ says "all of us are knaves", and $B$ says "exactly one of us is a knight".
$C$ says nothing.
We find the type of each inhabitant.

1. Dictionary. Let $a$, $b$, $c$ be "$A$ is a knight", "$B$ is a knight", "$C$ is a knight". Let $E$ be "exactly one of $a, b, c$ is true".
2. Translation. The statement of $A$ gives $a \leftrightarrow (\neg a \land \neg b \land \neg c)$, and the statement of $B$ gives $b \leftrightarrow E$. Reason: the rule of the island, through the [[biconditional|0S6GMNJ62Y]].
3. [[Truth table|05RSK4Q657]] with $2^3 = 8$ rows. The column "$A$ ok" is the first biconditional, and the column "$B$ ok" is the second.

| $a$ | $b$ | $c$ | $\neg a \land \neg b \land \neg c$ | $A$ ok | $E$ | $B$ ok |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | T | F | F | F | F | F |
| T | F | T | F | F | F | T |
| T | F | F | F | F | T | F |
| F | T | T | F | T | F | F |
| F | T | F | F | T | T | T |
| F | F | T | F | T | T | F |
| F | F | F | T | F | F | T |

4. Only the sixth row has T in both "ok" columns. So $A$ is a knave, $B$ is a knight, and $C$ is a knave.
5. Check by [[cases|0WCP0PVET6]]. If $A$ were a knight, then all three would be knaves, $A$ included, which is impossible. So $A$ is a knave, and the statement of $A$ is false: at least one of the three is a knight.
6. Case $B$ is a knave. Then $E$ is false. Since $A$ and $B$ are knaves and at least one of the three is a knight, $C$ is the only knight, so $E$ is true. This contradicts the case.
7. Case $B$ is a knight. Then $E$ is true, and $B$ is that one knight, so $C$ is a knave. This agrees with step 4.

## Remarks

The silent inhabitant $C$ is still determined, because the statements of $A$ and $B$ talk about $C$.
Step 5 is the same argument as for an inhabitant who says "I am a knave and something else": such a speaker must be a knave, and the "something else" must be false.
If $B$ had said nothing, the rows with $A$ ok would be rows 5, 6 and 7, so $A$ would be a knave and the types of $B$ and $C$ would not be determined beyond "not both knaves".
So the second statement is needed for a unique solution.

## Explanations

### L1 human

The first inhabitant says "all three of us are liars".
A truth-teller cannot say that, because it would call the speaker a liar.
So the first inhabitant is a liar, and at least one of the three tells the truth.
The second inhabitant says "exactly one of us tells the truth".
If the second were a liar, the third would be the only truth-teller, and the sentence would be true, which a liar cannot say.
So the second tells the truth, and the second is the only truth-teller.

### L2 human

The typical use is to compare the two methods on one puzzle.
The truth table needs $8$ rows and no ideas, while the case analysis needs $3$ steps and the right choice of the first case.
Starting with $A$ is the right choice, because the statement of $A$ is of the form "I am a knave and $\ldots$", which settles $A$ at once.
A trap is to read "exactly one of us is a knight" as "at least one of us is a knight".
With that reading, rows 5 and 6 both satisfy the two biconditionals, and the type of $C$ is no longer determined.
