---
tag: ZV2QXSKFRG
kind: example
name: '"Exactly one of p, q, r" is not p ⊕ q ⊕ r'
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: PTMR3P9J6C
    note: the exclusive or of three inputs is true when all three are true, while "exactly one of three" is false in that row
uses: [PTMR3P9J6C, 025YZN3VJW, 0F72FK8EKB, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Example

A puzzle says "exactly one of the three suspects tells the truth".
Let $p$, $q$, $r$ be the three statements, and let $E(p, q, r)$ be "exactly one of $p$, $q$, $r$ is true".
Many readers translate $E$ as the [[exclusive or|PTMR3P9J6C]] of three inputs, $p \oplus q \oplus r$.
We check that the two differ.

1. Take the row in which $p$, $q$, $r$ are all T.
2. Three inputs are T, not exactly one, so $E(p, q, r)$ is F.
3. For $p \oplus q \oplus r$, first $p \oplus q$ is F, because both parts are T.
   Then $\mathrm{F} \oplus \mathrm{T}$ is T, so $p \oplus q \oplus r$ is T.
4. The two connectives differ in this row, so $E(p, q, r)$ is not $p \oplus q \oplus r$.
5. In the other seven rows they agree, because a count of true inputs from $0$ to $2$ is odd exactly when it is $1$.

## Remarks

### Parity is not uniqueness

The exclusive or of many inputs counts parity, not uniqueness.
For two inputs the two ideas coincide, because "odd" and "exactly one" mean the same thing for a count of $0$, $1$ or $2$.
From three inputs on, they separate.
With four inputs, the two connectives differ in the rows with $3$ true inputs, since $3$ is odd.
With four true inputs, both are F.

### A correct formula

A correct formula for $E$ says "at least one, and no two together", using [[disjunction|0F72FK8EKB]], [[conjunction|025YZN3VJW]] and [[negation|029JBBF693]]:
$$E(p, q, r) \equiv (p \lor q \lor r) \land \neg(p \land q) \land \neg(p \land r) \land \neg(q \land r).$$
In the row TTT, the part $\neg(p \land q)$ is F, so the formula is F, as it should be.
Another correct form lists the three rows where $E$ is T: $(p \land \neg q \land \neg r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land \neg q \land r)$.

## Explanations

### L1 human

"Exactly one of the three doors is open" is false when all three doors are open.
But a lamp wired to three switches is on when all three switches are flipped, because three is odd.
So the exclusive or of three things is not the same as "exactly one of three".

### L2 human

Check the correct formula for $E$ in the row $p$ T, $q$ F, $r$ F.

1. $p \lor q \lor r$ is T, because $p$ is T.
2. Each of $p \land q$, $p \land r$ and $q \land r$ contains a false input, so each is F.
   Their negations are T.
3. The conjunction of four true parts is T, so the formula gives T, and indeed exactly one input is T.

The correct formula is the one to use in puzzles and counting conditions of the form "exactly one of three".
Watch out: never translate "exactly one of the three speakers tells the truth" as an exclusive or of the three statements.
