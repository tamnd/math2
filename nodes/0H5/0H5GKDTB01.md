---
tag: 0H5GKDTB01
kind: definition
name: Disjunction
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 0F72FK8EKB
uses: [0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Definition

Disjunction joins two propositions into the proposition that at least one of them holds.
Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The disjunction of $p$ and $q$ is the proposition $p \lor q$, read "$p$ or $q$".
It is false when $p$ is false and $q$ is false, and true in the three other cases:

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

For formulas, a valuation $v$ satisfies $v(\varphi \lor \psi) = \mathrm{F}$ exactly when $v(\varphi) = \mathrm{F}$ and $v(\psi) = \mathrm{F}$.
The propositions $p$ and $q$ are the disjuncts of $p \lor q$.

## Notation

We write $p \lor q$; some books on Boolean algebra write $p + q$.
With truth values $1$ and $0$, the value of $p \lor q$ is $\max(p, q)$, which also equals $p + q - pq$.
In Lean's Mathlib, the disjunction of `a` and `b` is `Or a b`, written `a ∨ b`.

## Remarks

The first row is the one to read with care: $p \lor q$ is T when both parts are T, so this "or" is inclusive.
For example, "$4$ is even or $4$ is a square" is T, although both parts hold.
The [[exclusive or|PTMR3P9J6C]] has the same table except in that row, where it is F, so it is not a disjunction in this sense.
In daily speech "or" is often exclusive, but in mathematics it is inclusive unless the text says "but not both".

The matching proof rules are disjunction introduction, from $p$ or from $q$ conclude $p \lor q$, and disjunction elimination, which is proof by cases; in Mathlib they are `Or.inl`, `Or.inr` and `Or.elim`.
The [[union|0X1GSWNBN1]] of sets is defined by disjunction: $x \in A \cup B$ means $x \in A \lor x \in B$.
The concept page [[disjunction|0F72FK8EKB]] gives the laws, the rules in detail and the worked examples.

## Explanations

### L1 human

The sentence "$4$ is even or $4$ is odd" is a disjunction, and it is true because one part is true.
In mathematics "or" also allows both parts to be true, so "$4$ is even or $4$ is a square" is true.
A disjunction is false only when both parts are false, as in "$5$ is even or $5$ is a square".

### L2 human

Compute $\neg p \lor (q \land r)$ when $p$ and $q$ are T and $r$ is F.
Since $p$ is T, $\neg p$ is F, and since $r$ is F, $q \land r$ is F.
Both disjuncts are F, so the last row of the table makes the whole formula F.
Every truth table uses the definition this way, one row of the table of $\lor$ at each occurrence of $\lor$.
Watch out: a disjunction of many parts is T as soon as one part is T, and only the row with every part F gives F.
