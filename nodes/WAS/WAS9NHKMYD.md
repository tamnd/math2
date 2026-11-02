---
tag: WAS9NHKMYD
kind: definition
name: Eilenberg–MacLane space
msc: [55P20]
defines: AJHEYJE5XY
uses: [G5S1M9, 082GHNPJ53, 0WB6DH499T, P976WYEFMB]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg–MacLane_space
---

## Definition

Let $n \ge 1$ and let $G$ be a [[group|G5S1M9]], [[abelian|082GHNPJ53]] if $n \ge 2$.
An *Eilenberg–MacLane space of type $K(G, n)$* is a [[path-connected space|0WB6DH499T]] $X$ with base point $x_0$ such that
$$\pi_n(X, x_0) \cong G \quad \text{and} \quad \pi_k(X, x_0) = 0 \text{ for all } k \ne n, \ k \ge 1,$$
where $\pi_k$ is the $k$-th [[homotopy group|P976WYEFMB]].

## Remarks

The condition that $G$ be abelian for $n \ge 2$ is needed, since $\pi_n$ is abelian for $n \ge 2$.
For every such $G$ and $n$ there is a CW complex of type $K(G, n)$, and any two CW complexes of type $K(G, n)$ are homotopy equivalent.
One often writes $K(G, n)$ for any such CW complex.

Example: the circle $S^1$ is a $K(\Z, 1)$.
It is path-connected, $\pi_1(S^1) \cong \Z$, and $\pi_k(S^1) = 0$ for $k \ge 2$ because its universal cover $\R$ is contractible.

Non-example: the sphere $S^2$ is path-connected with $\pi_2(S^2) \cong \Z$ and $\pi_1(S^2) = 0$, but $\pi_3(S^2) \cong \Z$, so it is not a $K(\Z, 2)$.
