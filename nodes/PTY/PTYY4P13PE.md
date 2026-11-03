---
tag: PTYY4P13PE
kind: definition
name: KR-theory
msc: [19L47, 55N15]
defines: 1C2K6BSHPK
uses: [GP56NBN9RY, P4DZM975BV, 5FDMY7PDYY, 9E4JE4902G, P7MN6MQV7P, 0TVJZYB6SH, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/KR-theory
---

## Definition

Let $X$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]] with a continuous [[involution|GP56NBN9RY]] $\tau \colon X \to X$, so $\tau \circ \tau = \id$.
A *Real vector bundle* over $(X, \tau)$ is a complex [[vector bundle|P4DZM975BV]] $p \colon E \to X$ with a continuous map $\sigma \colon E \to E$ such that:

1. $\sigma \circ \sigma = \id_E$ and $p \circ \sigma = \tau \circ p$;
2. for each $x \in X$, the restriction $\sigma \colon E_x \to E_{\tau(x)}$ is antilinear: $\sigma(\lambda v) = \bar{\lambda} \sigma(v)$ for $\lambda \in \C$.

An isomorphism of Real vector bundles is an isomorphism of complex vector bundles that commutes with the maps $\sigma$.
The group $KR(X)$ is the [[Grothendieck group|5FDMY7PDYY]] of the monoid of isomorphism classes of Real vector bundles over $(X, \tau)$ under direct sum.

## Remarks

Example: let $\tau = \id_X$.
For a Real bundle $(E, \sigma)$, each $\sigma$ is an antilinear involution of a fibre $E_x$, and its fixed points form a real vector bundle $E^\sigma$ with $E = E^\sigma \otimes_{\R} \C$.
So $KR(X) \cong KO(X)$, the [[real K-theory|P7MN6MQV7P]] of $X$.

Example: let $Y = X \times \set{1, 2}$ with $\tau$ exchanging the two copies.
A Real bundle over $Y$ is determined by its restriction $F$ to the first copy, so $KR(Y) \cong K(X)$, the [[complex K-theory|9E4JE4902G]] of $X$.

Non-example: if $\sigma$ is complex linear on fibres instead of antilinear, clause 2 fails.
Then $(E, \sigma)$ is a bundle with an action of $\Z/2$ by linear maps; such bundles give equivariant K-theory, not KR-theory.

With $\R^{p,q} = \R^q \oplus i \R^p$ and complex conjugation as involution, one defines groups $KR^{p,q}(X)$ by suspension.
Atiyah's $(1,1)$-periodicity theorem states that suspension by $\R^{1,1} = \C$ with conjugation does not change KR-theory; both complex and real Bott periodicity follow from it.
