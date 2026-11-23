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

Conjunction joins two propositions into the proposition that both hold.
Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The conjunction of $p$ and $q$ is the proposition $p \land q$, read "$p$ and $q$".
It is true when $p$ is true and $q$ is true, and false in the three other cases:

| $p$ | $q$ | $p \land q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

For formulas, a valuation $v$ satisfies $v(\varphi \land \psi) = \mathrm{T}$ exactly when $v(\varphi) = \mathrm{T}$ and $v(\psi) = \mathrm{T}$.
The propositions $p$ and $q$ are the conjuncts of $p \land q$.

## Notation

We write $p \land q$; other books write $p \,\&\, q$, $p \cdot q$ or $pq$.
With truth values $1$ and $0$, the value of $p \land q$ is the product $pq$, and also $\min(p, q)$.
In Lean's Mathlib, the conjunction of `a` and `b` is `And a b`, written `a ∧ b`.

## Remarks

The definition asks for both conjuncts, and one T is not enough.
For example, "$6$ is even and $6$ is divisible by $3$" is T, but "$6$ is even and $6$ is divisible by $4$" is F, because its second conjunct is F.

The table is symmetric in $p$ and $q$, so conjunction is commutative.
For three variables, both $(p \land q) \land r$ and $p \land (q \land r)$ are T only in the row TTT, so conjunction is associative.
The matching proof rules are conjunction introduction, from $p$ and $q$ conclude $p \land q$, and conjunction elimination, from $p \land q$ conclude $p$ and conclude $q$; in Mathlib they are `And.intro`, `And.left` and `And.right`.
The [[intersection|0ZNMMA9TF5]] of sets is defined by conjunction: $x \in A \cap B$ means $x \in A \land x \in B$.
The concept page [[conjunction|025YZN3VJW]] gives the English forms, the laws and the worked examples.

## Explanations

### L1 human

The sentence "$6$ is even and $6$ is divisible by $3$" is a conjunction.
It is true, because both parts are true.
If one part is false, the whole sentence is false, so "$6$ is even and $6$ is divisible by $4$" is false.

### L2 human

Compute $(p \land q) \land \neg r$ when $p$ and $q$ are T and $r$ is F.
The first row of the table makes $p \land q$ T, and $\neg r$ is T because $r$ is F.
The first row again, applied to these two values, makes the whole formula T.
Every truth table uses the definition this way, one row of the table of $\land$ at each occurrence of $\land$.
Watch out: a conjunction of many parts is F as soon as one part is F, so a single F decides it.
