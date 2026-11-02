---
tag: N35SYWJMA9
kind: definition
name: Whitney sum
msc: [55R25, 57R22]
defines: BE9NJRVDR3
uses: [CX4M8K61AB, 0GBG8B49AA, 0WS9P12FQR, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_bundle
---

## Definition

Let $B$ be a topological space and let $p \colon E \to B$ and $p' \colon E' \to B$ be real (or complex) vector bundles over $B$, of ranks $n$ and $n'$.
The *Whitney sum* of $E$ and $E'$ is the space
$$E \oplus E' = \set{(v, v') \in E \times E' : p(v) = p'(v')},$$
with the [[subspace topology|0WS9P12FQR]] of the [[product|0GBG8B49AA]] $E \times E'$, together with the map $q \colon E \oplus E' \to B$, $q(v, v') = p(v)$.
The fiber $q^{-1}(b) = E_b \times E'_b$ is given the [[vector space|000AYPA9AJ]] structure of the direct sum $E_b \oplus E'_b$.

## Remarks

The map $q$ is a vector bundle of rank $n + n'$: local trivializations $p^{-1}(U) \cong U \times \R^n$ and $p'^{-1}(U) \cong U \times \R^{n'}$ combine into $q^{-1}(U) \cong U \times \R^{n + n'}$.
Equivalently, $E \oplus E'$ is the pullback of the product bundle $E \times E' \to B \times B$ along the diagonal $B \to B \times B$.
The Whitney sum is associative and commutative up to isomorphism, and the trivial bundle of rank $0$ is a unit.

Example: let $TS^2$ be the tangent bundle of $S^2 \subset \R^3$ and $\nu = \set{(x, t x) : x \in S^2, t \in \R}$ the normal line bundle.
At each $x \in S^2$, $T_x S^2 \oplus \R x = \R^3$, and so $TS^2 \oplus \nu$ is isomorphic to the trivial bundle $S^2 \times \R^3$, although $TS^2$ itself is not trivial.

Non-example: for bundles $E \to B$ and $E' \to B'$ over different bases, the product $E \times E' \to B \times B'$ is a vector bundle of rank $n + n'$.
It is not a Whitney sum, which needs a common base; it is the external direct sum.
