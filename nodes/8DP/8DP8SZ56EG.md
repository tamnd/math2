---
tag: 8DP8SZ56EG
kind: definition
name: Equivariant K-theory
msc: [19L47, 55N91]
defines: 4R0ZJ95BKQ
uses: [9TFC6ADC1C, 0WCY42EV9V, P4DZM975BV, 5FDMY7PDYY, A4393CW9G4, RKTX9MN7Q3, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
---

## Definition

Let $G$ be a [[compact Lie group|9TFC6ADC1C]] and let $X$ be a [[compact|0TVJZYB6SH]] Hausdorff space with a continuous [[action|0WCY42EV9V]] of $G$.
A *$G$-vector bundle* over $X$ is a complex [[vector bundle|P4DZM975BV]] $p \colon E \to X$ with a continuous action of $G$ on $E$ such that:

1. $p(g \cdot v) = g \cdot p(v)$ for all $g \in G$ and $v \in E$;
2. for each $g \in G$ and $x \in X$, the map $E_x \to E_{g x}$, $v \mapsto g \cdot v$, is complex linear.

An isomorphism of $G$-vector bundles is a bundle isomorphism that commutes with the action of $G$.
The *equivariant K-theory* $K_G(X)$ is the [[Grothendieck group|5FDMY7PDYY]] of the monoid of isomorphism classes of $G$-vector bundles over $X$ under direct sum.

## Remarks

The tensor product makes $K_G(X)$ a commutative ring, and an algebra over $K_G(\text{point})$.
For trivial $G$ it is the [[Grothendieck group of vector bundles|A4393CW9G4]] $K(X)$.

Example: for $X$ a point, a $G$-vector bundle is a finite-dimensional complex representation of $G$, so $K_G(\text{point}) = R(G)$, the [[representation ring|RKTX9MN7Q3]] of $G$.

Example: if $G$ acts freely on $X$, pulling back along $X \to X/G$ gives an isomorphism $K(X/G) \cong K_G(X)$.

Non-example: let $G = \Z/2$ act on a vector bundle by a map that is antilinear on fibres, such as complex conjugation on $X \times \C$, with $G$ fixing every point of $X$.
Clause 2 fails, so this is not a $G$-vector bundle; such objects give KR-theory instead.

Groups $K^{-n}_G(X)$ are defined from suspensions with trivial action, as in the non-equivariant case, and they satisfy Bott periodicity of period $2$.
