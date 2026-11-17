---
tag: 0M28ASWG8T
kind: definition
name: Conjunction
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
defines: 025YZN3VJW
uses: [0ZGC7ZESYN]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Definition

Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The conjunction of $p$ and $q$ is the proposition $p \land q$, read "$p$ and $q$".
The proposition $p \land q$ is true when $p$ is true and $q$ is true.
In the three other cases, $p \land q$ is false.

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

For formulas, a valuation $v$ gives $v(\varphi \land \psi) = $ T exactly when $v(\varphi) = $ T and $v(\psi) = $ T.
The propositions $p$ and $q$ are the conjuncts of $p \land q$.

## Notation

This sub-area writes $p \land q$.
Other notations are $p \,\&\, q$, $p \cdot q$ and $pq$.
With truth values $1$ and $0$, the value of $p \land q$ is the product $pq$, and also the minimum $\min(p, q)$.
In Lean's Mathlib, the conjunction of `a` and `b` is `And a b`, written `a ∧ b`.

## Remarks

The table is symmetric in $p$ and $q$, so $p \land q$ and $q \land p$ have the same truth value; conjunction is commutative.
A check of the $8$ rows for three variables shows that $(p \land q) \land r$ and $p \land (q \land r)$ are both true only in the row TTT, so conjunction is associative.
The proof rules that match the definition are conjunction introduction (from $p$ and $q$ conclude $p \land q$) and conjunction elimination (from $p \land q$ conclude $p$, and conclude $q$); in Mathlib they are `And.intro`, `And.left` and `And.right`.
The [[intersection|0ZNMMA9TF5]] of two sets is defined by conjunction: $x \in A \cap B$ means $x \in A \land x \in B$.
The concept page [[conjunction|025YZN3VJW]] gives the English forms, the laws, the examples and the non-examples.

## Explanations

### L1 human

The sentence "$6$ is even and $6$ is divisible by $3$" is a conjunction.
It is true, because both parts are true.
If one part is false, the whole sentence is false: "$6$ is even and $6$ is divisible by $4$" is false.

### L2 human

We compute the truth value of $(p \land q) \land \neg r$ for $p$ T, $q$ T, $r$ F.

1. $p \land q$ is T, by the first row of the table.
2. $\neg r$ is T, because $r$ is F.
3. $(p \land q) \land \neg r$ is T, by the first row of the table applied to the values of steps 1 and 2.

The definition is used in this way inside every truth table: one row of the table of $\land$ at each occurrence of $\land$.

A trap: a conjunction of many parts is false as soon as one part is false, so a single F row decides it.
