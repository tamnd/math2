---
tag: K1V1KVEAHN
kind: definition
name: Exclusive or
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: PTMR3P9J6C
uses: [0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Definition

Exclusive or joins two propositions into the proposition that exactly one of them holds.
Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The exclusive or of $p$ and $q$ is the proposition $p \oplus q$, read "$p$ xor $q$" or "either $p$ or $q$, but not both".
It is true when exactly one of $p$ and $q$ is true, and false when both are true or both are false:

| $p$ | $q$ | $p \oplus q$ |
|---|---|---|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

For formulas, a valuation $v$ gives $v(\varphi \oplus \psi) = \mathrm{T}$ exactly when $v(\varphi) \neq v(\psi)$.

## Notation

We write $p \oplus q$.
Other notations are $p \mathbin{\underline{\vee}} q$, $p \not\leftrightarrow q$, $p \not\equiv q$, XOR and EOR.
With truth values $1$ and $0$, the value of $p \oplus q$ is $p + q$ modulo $2$.
In Lean's Mathlib, `Xor' a b` is defined as $(a \land \neg b) \lor (b \land \neg a)$.

## Remarks

The table agrees with the table of the inclusive [[disjunction|0F72FK8EKB]] in the rows TF, FT and FF, and differs in the row TT.
So "$7$ is odd xor $7$ is prime" is F, while "$7$ is odd or $7$ is prime" is T.

The connective can be written with the other connectives in three common ways:
$$p \oplus q \equiv (p \lor q) \land \neg(p \land q) \equiv (p \land \neg q) \lor (\neg p \land q) \equiv \neg(p \leftrightarrow q).$$
The first form says "at least one, and not both".
The second form lists the two rows where the value is T.
The third form says that the truth values differ, using the [[biconditional|0S6GMNJ62Y]].
The concept page [[exclusive or|PTMR3P9J6C]] gives the arithmetic modulo $2$, associativity, parity and the examples.

## Explanations

### L1 human

"Exclusive or" means "one or the other, but not both".
"$9$ is odd xor $9$ is prime" is true, because only the first part is true.
"$7$ is odd xor $7$ is prime" is false, because both parts are true.
"$4$ is odd xor $4$ is prime" is false, because neither part is true.

### L2 human

Compute $p \oplus q$ from the second form, $(p \land \neg q) \lor (\neg p \land q)$, in the row TF.

1. $p$ is T and $q$ is F, so $\neg q$ is T and $p \land \neg q$ is T.
2. $\neg p$ is F, so $\neg p \land q$ is F.
3. The disjunction of T and F is T, so $p \oplus q$ is T, as the table says.

In this way the definition reduces $\oplus$ to $\neg$, $\land$ and $\lor$ in a truth table or a normal form.
Watch out: the first form needs both of its parts.
The part $p \lor q$ alone is the inclusive "or", which is T in the row TT.
