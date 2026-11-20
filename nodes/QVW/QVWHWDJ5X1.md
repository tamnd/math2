---
tag: QVWHWDJ5X1
kind: definition
name: MV-algebra
msc: ["06D35", "03G20", "03B50"]
defines: 8T4M7RN9AC
topics: [QYA4H5Y7VR]
audience: research
uses: [0N6R902FG1, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Definitions
  - book: isbn:9780792360094
---

## Definition

An *MV-algebra* is a structure $(A, \oplus, \neg, 0)$, where $\oplus$ is a binary operation, $\neg$ is a unary operation and $0 \in A$, such that for all $x, y \in A$:

1. $(A, \oplus, 0)$ is a commutative [[monoid|0N6R902FG1]].
2. $\neg \neg x = x$.
3. $x \oplus \neg 0 = \neg 0$.
4. $\neg (\neg x \oplus y) \oplus y = \neg (\neg y \oplus x) \oplus x$.

## Notation

We write $1 := \neg 0$, $x \odot y := \neg(\neg x \oplus \neg y)$ and $x \to y := \neg x \oplus y$.
The relation $x \le y$ iff $\neg x \oplus y = 1$ is a lattice order with $x \lor y = \neg(\neg x \oplus y) \oplus y$.
So clause 4 says that this join is symmetric in $x$ and $y$.

## Remarks

Example: the unit interval $[0, 1]$ with $x \oplus y = \min(1, x + y)$, $\neg x = 1 - x$ and $0$ is an MV-algebra.
Clauses 1 to 3 are direct, since $\neg 0 = 1$.
For clause 4, if $y \ge x$ the left side is $\neg 1 \oplus y = y$, and if $y < x$ it is $(x - y) \oplus y = x$; so both sides equal $\max(x, y)$.

Non-example: the integers $(\Z, +, -, 0)$ satisfy clauses 1 and 2, but fail clause 3, since $1 + (-0) = 1 \ne 0$.

Every [[Boolean algebra|0XADJKM699]] is an MV-algebra with $\oplus = \vee$ and $\neg$ the complement.
An MV-algebra is Boolean iff $x \oplus x = x$ for all $x$.
The [[standard MV-algebra satisfies these axioms|~bd015994]], and [[MV-algebras|8T4M7RN9AC]] are the algebras of Łukasiewicz logic.

## Explanations

### L1 human

The rules describe a truth value "not" and a capped sum "or".
The capped sum never goes above the top value $1 = \neg 0$.
Rule 4 says that two ways to compute "the larger of $x$ and $y$" agree.

### L2 human

1. In $[0, 1]$, take $x = 0.3$ and $y = 0.8$.
2. Then $\neg x \oplus y = 0.7 \oplus 0.8 = 1$, so $\neg(\neg x \oplus y) \oplus y = 0 \oplus 0.8 = 0.8$.
3. Also $\neg y \oplus x = 0.2 \oplus 0.3 = 0.5$, so $\neg(\neg y \oplus x) \oplus x = 0.5 \oplus 0.3 = 0.8$.
4. Both sides give $0.8 = \max(0.3, 0.8)$.

The trap: $\oplus$ is not the lattice join; $0.5 \oplus 0.5 = 1$.
