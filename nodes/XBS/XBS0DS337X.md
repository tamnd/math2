---
tag: XBS0DS337X
kind: example
name: The "or" of "the meal comes with soup or salad" is exclusive
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0F72FK8EKB
    note: the restaurant's claim is false when the meal comes with both, while a disjunction is true when both parts are true
uses: [0F72FK8EKB, PTMR3P9J6C]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
---

## Example

A menu says "the meal comes with soup or salad", and the restaurant means that the price includes one of the two, not both.
Let $p$ be "the meal comes with soup" and $q$ be "the meal comes with salad".
We compare the claim of the menu with the [[disjunction|0F72FK8EKB]] $p \lor q$, row by row.

| $p$ | $q$ | menu claim | $p \lor q$ |
|---|---|---|---|
| T | T | F | T |
| T | F | T | T |
| F | T | T | T |
| F | F | F | F |

1. In the row TT the meal comes with both, and the claim is F, because it promised one of the two.
   The disjunction is T in this row.
2. In the rows TF and FT exactly one is served, and both the claim and $p \lor q$ are T.
3. In the row FF neither is served, and both are F.
4. The claim and $p \lor q$ differ in row TT, so the "or" of the menu is not a disjunction.
5. The claim is T exactly when one of $p$, $q$ is T, which is the table of the [[exclusive or|PTMR3P9J6C]] $p \oplus q$.

## Remarks

Everyday "or" is often exclusive, while mathematical "or" is inclusive.
The two readings differ only in the row where both parts are true, so the difference matters only when both parts can hold.

Context decides the everyday reading.
"Students with a passport or an identity card may enter" is inclusive, since a student with both may enter.
A mathematical text that wants the exclusive reading says so, with "but not both" or "exactly one of".
Change the menu to "soup or salad, or both" and its claim becomes $p \lor q$.

## Explanations

### L1 human

On a menu, "soup or salad" usually means one of them, not both.
If the waiter brings both and charges nothing extra, the menu did not describe the meal correctly.
In mathematics "or" is used differently: "$4$ is even or $4$ is a square" is true, although both parts hold.
So the "or" of the menu and the "or" of mathematics are two different connectives.

### L2 human

Decide whether the reading of "or" matters in three sentences.
In "a real $x$ with $x^2 = 1$ is $1$ or $-1$", the parts "$x = 1$" and "$x = -1$" cannot both hold, so both readings give the same truth value.
In "an integer $n \ge 2$ is prime or composite", again the parts cannot both hold, and the readings agree.
In "the function $f$ is bounded or continuous", both parts can hold, for example for $f(x) = \sin x$, so the readings differ; the mathematical reading is inclusive, and the sentence is true for $\sin$.
The reading matters only when both parts can hold.
Watch out: some puzzle books and school texts use the exclusive "or" in examples from daily life, so check the convention of the text before you solve its problems.
