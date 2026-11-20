---
tag: 0SVR29SV1V
kind: definition
name: Quotient space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
defines: 0BR3FY5Q8M
uses: [0EPTJA5QV4, 05EGHEQZAW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.hasQuotient
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
---

## Definition

Let $F$ be a field, let $V$ be a [[vector space|05EGHEQZAW]] over $F$, and let $U$ be a [[subspace|0EPTJA5QV4]] of $V$.
For $v \in V$, the *coset* of $v$ is $v + U = \{v + u : u \in U\}$.
The *quotient space* $V / U$ is the set of all cosets $v + U$ with $v \in V$, with the operations
$$(v + U) + (w + U) = (v + w) + U, \qquad a(v + U) = av + U$$
for $v, w \in V$ and $a \in F$.

## Notation

We write $V / U$ and read it "$V$ modulo $U$".
The coset $v + U$ is also written $[v]$ or $\bar v$.

## Remarks

The operations are well defined, because $U$ is a subspace: the result does not depend on the choice of $v$ and $w$ in their cosets, see the [[proposition on cosets|~1aa01a37]].
Two cosets $v + U$ and $w + U$ are equal if and only if $v - w \in U$.
The zero vector of $V / U$ is the coset $0 + U = U$.
In $\R^2$ with $U$ the $x$-axis, the cosets are the horizontal lines, and $V / U$ is isomorphic to $\R$.

## Explanations

### L1 human

In the quotient space $V / U$, we treat two vectors as the same when they differ by a vector of $U$.
Each element of $V / U$ is a copy of $U$ shifted by some vector.
Dividing the plane by a line gives the set of all lines parallel to it, which behaves like a single line.

### L2 human

To add two cosets, pick a vector in each, add the vectors, and take the coset of the result.
For $U$ the $x$-axis in $\R^2$, the cosets $(5, 1) + U$ and $(-2, 3) + U$ add to $(3, 4) + U$, the line $y = 4$.
Picking $(0, 1)$ and $(0, 3)$ instead gives $(0, 4) + U$, the same line.
