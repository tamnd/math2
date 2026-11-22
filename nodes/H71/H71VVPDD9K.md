---
tag: H71VVPDD9K
kind: example
name: The statement "if P, then not Q" is not the negation of "if P, then Q"
msc: ["97E40", "03B05"]
topics: [WMY13MXY3W]
audience: school
not_instance_of:
  - target: K930V33BSC
    note: both conditionals are true when P is false, so the second one is not the negation of the first
uses: [K930V33BSC, FA6YZGR2SS, 0V4QXPGJQK, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

Many students negate "if $P$, then $Q$" as "if $P$, then not $Q$".
We show that this is not a correct [[negation|K930V33BSC]].
A negation must be true exactly when the original statement is false, so one case where both are true is enough.

1. Take $P$ to be "$1 = 2$" and $Q$ to be "$3 > 0$".
2. The [[conditional|FA6YZGR2SS]] "if $1 = 2$, then $3 > 0$" is true, because its hypothesis is false.
   This is [[vacuous truth|0V4QXPGJQK]].
3. The conditional "if $1 = 2$, then $3 \leq 0$" is also true, for the same reason.
4. So the two statements are true at the same time.
   A statement and its negation cannot both be true.
5. So "if $P$, then not $Q$" is not the negation of "if $P$, then $Q$".
   The correct negation is "$P$ and not $Q$", here "$1 = 2$ and $3 \leq 0$", which is false.

## Remarks

A [[truth table|05RSK4Q657]] shows all four cases at once.

| $P$ | $Q$ | if $P$, then $Q$ | if $P$, then not $Q$ | $P$ and not $Q$ |
|---|---|---|---|---|
| T | T | T | F | F |
| T | F | F | T | T |
| F | T | T | T | F |
| F | F | T | T | F |

The column "$P$ and not $Q$" is the opposite of the column "if $P$, then $Q$" in every row, so it is the negation.
The column "if $P$, then not $Q$" is the opposite only in the two rows where $P$ is true.
In the two rows where $P$ is false, it agrees with the original.

The inverse "if not $P$, then not $Q$" is not the negation either.
When $P$ and $Q$ are both true, the conditional and its inverse are both true.

## Explanations

### L1 human

A teacher says: "if it rains, the trip is cancelled".
The teacher breaks this promise only if it rains and the trip still takes place.
The sentence "if it rains, the trip is not cancelled" is a different promise.
On a dry day, the teacher breaks neither promise.
So the second sentence does not say that the first promise was broken.

### L2 human

Test the wrong form on a statement with a hidden quantifier: "for every integer $n$, if $n^2 < 0$, then $n = 0$".

1. No integer has $n^2 < 0$.
   So the hypothesis is false for every $n$, and the statement is true.
2. The wrong form is "for every integer $n$, if $n^2 < 0$, then $n \neq 0$".
   For the same reason, it is also true.
3. Two true statements are not negations of each other, so the wrong form fails here too.
4. The correct negation is "there is an integer $n$ with $n^2 < 0$ and $n \neq 0$".
   It is false, as the negation of a true statement must be.

The correct form is the one to assume in a proof by contradiction: we assume "$P$ and not $Q$", not "if $P$, then not $Q$".

Watch out: for some statements the wrong form happens to have the opposite truth value.
"For every integer $n$, if $n > 3$, then $n^2 > 9$" is true, and the wrong form "for every integer $n$, if $n > 3$, then $n^2 \leq 9$" is false.
One such check does not show that a form is a negation.
The form must give the opposite truth value in every case, and the case of a false hypothesis breaks it.
