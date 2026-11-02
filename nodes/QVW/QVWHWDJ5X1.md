---
tag: QVWHWDJ5X1
kind: definition
name: MV-algebra
msc: ["06D35", "03G20", "03B50"]
defines: 8T4M7RN9AC
uses: [0N6R902FG1, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
---

## Definition

An *MV-algebra* is a structure $(A, \oplus, \neg, 0)$, where $\oplus$ is a binary operation, $\neg$ is a unary operation and $0 \in A$, such that for all $x, y \in A$:

1. $(A, \oplus, 0)$ is a commutative [[monoid|0N6R902FG1]].
2. $\neg \neg x = x$.
3. $x \oplus \neg 0 = \neg 0$.
4. $\neg (\neg x \oplus y) \oplus y = \neg (\neg y \oplus x) \oplus x$.

## Remarks

Example: the unit interval $[0, 1]$ with $x \oplus y = \min(1, x + y)$, $\neg x = 1 - x$ and $0$ is an MV-algebra.
Clauses 1 to 3 are direct, since $\neg 0 = 1$.
For clause 4, if $y \ge x$ the left side is $\neg 1 \oplus y = y$, and if $y < x$ it is $(x - y) \oplus y = x$; so both sides equal $\max(x, y)$.

Non-example: the integers $(\Z, +, -, 0)$ satisfy clauses 1 and 2, but fail clause 3, since $1 + (-0) = 1 \ne 0$.

Every [[Boolean algebra|0XADJKM699]] is an MV-algebra with $\oplus = \vee$ and $\neg$ the complement.
The constant $\neg 0$ is written $1$, and $x \odot y = \neg(\neg x \oplus \neg y)$ is the dual operation.
