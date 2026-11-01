---
tag: Q07RA7AMDE
kind: definition
name: Semiring
msc: [16Y60]
defines: D31S3GR51T
uses: [0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Semiring
---

## Definition

Let $S$ be a set with two binary operations $+$ and $\cdot$, and two elements $0$ and $1$ of $S$.
The tuple $(S, +, \cdot, 0, 1)$ is a *semiring* if the following hold.

1. $(S, +, 0)$ is a commutative [[monoid|0N6R902FG1]].
2. $(S, \cdot, 1)$ is a monoid.
3. Multiplication distributes over addition on both sides: $a \cdot (b + c) = a \cdot b + a \cdot c$ and $(a + b) \cdot c = a \cdot c + b \cdot c$ for all $a, b, c \in S$.
4. Zero is absorbing: $0 \cdot a = a \cdot 0 = 0$ for all $a \in S$.

The semiring is *commutative* if its multiplication is commutative.

## Remarks

The natural numbers $\N = \set{0, 1, 2, \dots}$ with the usual addition and multiplication form a commutative semiring.
The four clauses are the familiar rules of arithmetic on $\N$.
The tropical semiring is $\R \cup \set{\infty}$ with $\min$ as addition, ordinary $+$ as multiplication, $\infty$ as zero and $0$ as one.
For instance, $a + \min(b, c) = \min(a + b, a + c)$ gives distributivity, and $a + \infty = \infty$ gives the absorbing clause.
The positive integers $\set{1, 2, 3, \dots}$ with the usual operations are not a semiring: there is no additive identity, so clause 1 fails.
A [[ring|0B1261B5ED]] is exactly a semiring in which $(S, +)$ is a group; clause 4 then follows from the others.
Some authors omit $0$ or $1$ from the definition, and some do not require clause 4.
