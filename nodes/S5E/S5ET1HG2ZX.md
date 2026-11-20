---
tag: S5ET1HG2ZX
kind: statement
role: theorem
name: Erdős-Kaplansky theorem
aliases: [erdos-kaplansky-theorem]
msc: ["15A03", "15A04", "03E10"]
topics: [9K7FFF26QR]
audience: ug2
about: [07JBSZE0V4]
uses: [0M856Q1AMZ, 05G2G0P224, 00MS9VMQ9Z, 0QKPNZKNEA, 0WTEMGYV2C]
sources:
  - url: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kaplansky_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Infinite-dimensional case
same_as:
  wikipedia: Erdős–Kaplansky theorem
---

## Statement

Let $F$ be a field and let $V$ be an infinite-dimensional vector space over $F$.
Let $B$ be a basis of $V$, which exists by the theorem that [[every vector space has a basis|00MS9VMQ9Z]], so $\dim V = \abs{B}$.
Then the [[dual space|0M856Q1AMZ]] $V^*$ has [[dimension|05G2G0P224]]
$$\dim V^* = \abs{F^B} = \abs{F}^{\dim V},$$
where $\abs{\cdot}$ is the [[cardinal number|0QKPNZKNEA]] of a set.
In particular, $\dim V^* > \dim V$, so $V^*$ is not isomorphic to $V$.

More generally, for every infinite set $I$, the space $F^I$ of all functions $I \to F$ satisfies $\dim F^I = \abs{F^I}$.

## Remarks

### Why each hypothesis is needed

- $V$ must be infinite-dimensional. If $\dim V = n$ is finite, then $\dim V^* = n$, while $\abs{F}^n$ is infinite for infinite $F$.
- The statement uses the axiom of choice, through the existence of a basis of $V$ and of $V^*$, and through cardinal arithmetic.

### Consequences

- For $V = \Q^{(\N)}$, of countable dimension $\aleph_0$, the dual $\Q^{\N}$ has dimension $\aleph_0^{\aleph_0} = 2^{\aleph_0}$, the cardinal of the continuum.
- For $F = \F_2$ and $\dim V = \aleph_0$, the dual has dimension $2^{\aleph_0}$. So $V^*$ is not isomorphic to $V$ also over a finite field.
- The evaluation map $V \to V^{**}$ is not surjective for infinite-dimensional $V$, because $\dim V^{**} > \dim V^* > \dim V$. This gives a second proof of one part of the theorem on the [[double dual|0ZJM9D7NPS]].

### Converse

If $\dim V^* = \dim V$, then $V$ is finite-dimensional.
This is the contrapositive of the strict inequality.

### Generalizations

- The formula $\dim F^I = \abs{F^I}$ for infinite $I$ is the general form. The statement on $V^*$ is the case $I = B$, since $V^* \cong F^B$.
- For finite $I$, the formula changes to $\dim F^I = \abs{I}$, the finite case of the [[dimension of the dual space|00889YD15K]].

## History

The theorem is named after Paul Erdős and Irving Kaplansky.
Bourbaki gives the formula $\dim F^I = \abs{F^I}$ in the volume Algebra I of the Elements of Mathematics.

## Explanations

### L1 human

When a space has infinitely many basis vectors, its dual space is always strictly larger in dimension.
The space of finitely supported sequences of rational numbers has a countable basis.
Its dual is the space of all rational sequences, and that space needs uncountably many basis vectors.
So in infinite dimension, a space and its dual are never isomorphic.

### L2 human

The proof compares sizes of sets with dimensions.

1. $V^*$ is in bijection with $F^B$, because a form is any choice of values on the basis $B$.
2. An infinite-dimensional space $W$ has exactly $\max(\abs{F}, \dim W)$ elements.
3. $\dim F^B \ge \abs{F}$, because the geometric sequences $(1, a, a^2, \dots)$ for $a \in F$ are independent.
4. Steps 2 and 3 give $\dim V^* = \abs{V^*} = \abs{F}^{\abs{B}}$.
5. Cantor's theorem gives $\abs{F}^{\abs{B}} \ge 2^{\abs{B}} > \abs{B}$.

The typical use is to show that the finite-dimensional duality theory cannot hold without change in infinite dimension.
A trap: the theorem is about the algebraic dual; the continuous dual of a Hilbert space is isomorphic to the space.

### L3 human

The theorem is one reason why functional analysis replaces the algebraic dual by the continuous dual.
For a Hilbert space $H$, the continuous dual is isomorphic to $H$ by the Riesz representation theorem, but the algebraic dual is much larger.
The formula $\dim F^I = \abs{F^I}$ also computes the dimension of many function spaces, for example $\dim_\R \R^{\R} = 2^{2^{\aleph_0}}$.
