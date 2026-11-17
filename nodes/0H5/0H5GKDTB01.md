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

Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The disjunction of $p$ and $q$ is the proposition $p \lor q$, read "$p$ or $q$".
The proposition $p \lor q$ is false when $p$ is false and $q$ is false.
In the three other cases, $p \lor q$ is true.

| $p$ | $q$ | $p \lor q$ |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

For formulas, a valuation $v$ gives $v(\varphi \lor \psi) = $ F exactly when $v(\varphi) = $ F and $v(\psi) = $ F.
The propositions $p$ and $q$ are the disjuncts of $p \lor q$.

## Notation

This sub-area writes $p \lor q$.
Some books on Boolean algebra write $p + q$.
With truth values $1$ and $0$, the value of $p \lor q$ is the maximum $\max(p, q)$, and also $p + q - pq$.
In Lean's Mathlib, the disjunction of `a` and `b` is `Or a b`, written `a ∨ b`.

## Remarks

This "or" is inclusive: the first row of the table makes $p \lor q$ true when both $p$ and $q$ are true.
The [[exclusive or|~777e424f]] has the same table except in the first row, where it is false.
In daily speech "or" is often exclusive, but in mathematics it is inclusive unless the text says "but not both".
The proof rules that match the definition are disjunction introduction (from $p$, or from $q$, conclude $p \lor q$) and disjunction elimination (proof by cases); in Mathlib they are `Or.inl`, `Or.inr` and `Or.elim`.
The [[union|0X1GSWNBN1]] of two sets is defined by disjunction: $x \in A \cup B$ means $x \in A \lor x \in B$.
The concept page [[disjunction|0F72FK8EKB]] gives the laws, the rules in detail, the examples and the non-examples.

## Explanations

### L1 human

The sentence "$4$ is even or $4$ is odd" is a disjunction.
It is true, because one part is true.
In mathematics, "or" also allows both parts to be true: "$4$ is even or $4$ is a square" is true.
A disjunction is false only when both parts are false, as in "$5$ is even or $5$ is a square".

### L2 human

We compute the truth value of $\neg p \lor (q \land r)$ for $p$ T, $q$ T, $r$ F.

1. $\neg p$ is F, because $p$ is T.
2. $q \land r$ is F, because $r$ is F.
3. $\neg p \lor (q \land r)$ is F, by the last row of the table: both disjuncts are F.

The definition is used in this way inside every truth table: one row of the table of $\lor$ at each occurrence of $\lor$.

A trap: a disjunction of many parts is true as soon as one part is true, so a single T decides it, and only the row with every part F gives F.
