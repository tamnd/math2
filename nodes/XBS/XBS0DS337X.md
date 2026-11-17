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
We compare the meaning of the menu with the [[disjunction|0F72FK8EKB]] $p \lor q$, row by row.

1. Row TT: the meal comes with both. The restaurant's claim is false, because it promised one of the two. The disjunction $p \lor q$ is T.
2. Row TF: soup only. The claim is true, and $p \lor q$ is T.
3. Row FT: salad only. The claim is true, and $p \lor q$ is T.
4. Row FF: neither. The claim is false, and $p \lor q$ is F.
5. The claim and $p \lor q$ differ in row TT. So the "or" of the menu is not a disjunction.
6. The table of the claim is T exactly when one of $p$, $q$ is true: it is the [[exclusive or|PTMR3P9J6C]] $p \oplus q$.

## Remarks

The example shows the trap of the everyday "or": in speech it is often exclusive, while in mathematics it is inclusive.
The two readings differ only in the row where both parts are true, so the difference matters only when both parts can be true.

The context decides the everyday reading.
"Students with a passport or an identity card may enter" is inclusive: a student with both may enter.
A mathematical text that wants the exclusive reading must say so, with "but not both" or "exactly one of".

If we change the menu to "the meal comes with soup or salad, or both", then the claim becomes the inclusive disjunction $p \lor q$.

## Explanations

### L1 human

On a menu, "soup or salad" usually means one of them, not both.
If the waiter brings both and charges nothing extra, the menu did not describe the meal correctly.
In mathematics, "or" is used differently: "$4$ is even or $4$ is a square" is true, although both parts hold.
So the "or" of the menu and the "or" of mathematics are two different connectives.

### L2 human

We decide the reading of "or" in two sentences.

1. "A real number $x$ with $x^2 = 1$ is $1$ or $-1$." The parts "$x = 1$" and "$x = -1$" cannot both be true, so both readings give the same truth value, and the mathematical convention takes it as inclusive.
2. "The integer $n$ is prime or composite, for $n \geq 2$." Again the parts cannot both be true, so the readings agree.
3. "The function $f$ is bounded or continuous." Both parts can be true, for example for $f(x) = \sin x$, so the readings differ. In mathematics it is inclusive, and the sentence is true for $\sin$.

The typical use of this check is to see whether the choice of reading matters: it matters only when both parts can hold.

A trap: some puzzle books and some school texts use the exclusive "or" in examples from daily life.
Before solving such a problem, we must check which convention the text uses.
