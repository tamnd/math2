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

The quotient space of a vector space by a subspace is the set of parallel copies of the subspace, with addition and scaling done through representatives.
Let $F$ be a field, let $V$ be a [[vector space|05EGHEQZAW]] over $F$, and let $U$ be a [[subspace|0EPTJA5QV4]] of $V$.
For $v \in V$, the *coset* of $v$ is the set
$$v + U = \{v + u : u \in U\}.$$
The *quotient space* $V / U$ is the set of all cosets $v + U$ with $v \in V$, with the operations
$$(v + U) + (w + U) = (v + w) + U, \qquad a(v + U) = av + U$$
for $v, w \in V$ and $a \in F$.

## Notation

We write $V / U$ and read it "$V$ modulo $U$".
The coset $v + U$ is also written $[v]$ or $\bar v$, and any vector in it is a *representative*.

## Remarks

The definition has one hidden condition: the operations must not depend on the representatives.
This is where the hypothesis that $U$ is a subspace is used, and the [[proposition on cosets|YYH67TQ9GV]] checks it.
The same proposition shows that $v + U = w + U$ holds if and only if $v - w \in U$, and that the zero of $V / U$ is $0 + U = U$.

For a small example, let $U$ be the $x$-axis in $\R^2$.
The coset of $(a, b)$ is the horizontal line $y = b$, so the cosets are the horizontal lines, and the map $(a, b) + U \mapsto b$ is an isomorphism $V / U \cong \R$.

A set that fails the subspace condition gives no quotient.
For the line $y = 1$, which misses the origin, the relation "$u - v$ lies in the line" is not reflexive, as [[the line that misses the origin|E3MQ50YQNR]] shows.
The concept page on the [[quotient space|0BR3FY5Q8M]] has more examples and the main properties.

## Explanations

### L1 human

In the quotient space $V / U$ we treat two vectors as the same when they differ by a vector of $U$.
Each element of $V / U$ is a copy of $U$ shifted by some vector.
Dividing the plane by a line through the origin gives the set of all lines parallel to it, and that set behaves like a single line.

### L2 human

To add two cosets, pick a vector in each, add the vectors, and take the coset of the result.
For $U$ the $x$-axis in $\R^2$, the cosets $(5, 1) + U$ and $(-2, 3) + U$ add to
$$(5, 1) + (-2, 3) + U = (3, 4) + U,$$
which is the line $y = 4$.
Picking the representatives $(0, 1)$ and $(0, 3)$ instead gives $(0, 4) + U$, the same line.
The answer did not depend on the choice, and that is exactly what the definition needs.
