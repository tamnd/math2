---
tag: BDFXWM8XK1
kind: definition
name: Fréchet manifold
msc: [58B99, 46T05]
defines: EBMCFQT0JN
uses: [3GAA614673, EAZF9NJW12, 0QT00PB5G2, 02BH3MCBQB, 0MXB4CKHFW, 9K15AMGBV9]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_manifold
---

## Definition

Let $F$ and $G$ be real [[Fréchet spaces|3GAA614673]], and let $U \subseteq F$ be open.
A map $f \colon U \to G$ is of class $C^1$ if it is continuous, the [[Gateaux derivative|EAZF9NJW12]] $Df(x) h = \lim_{t \to 0} (f(x + t h) - f(x)) / t$ exists for all $x \in U$ and $h \in F$, and $Df \colon U \times F \to G$ is continuous.
It is of class $C^{k+1}$ if it is $C^1$ and $Df$ is $C^k$, and *smooth* if it is $C^k$ for all $k$.

Let $M$ be a [[Hausdorff space|0MXB4CKHFW]].
A *smooth Fréchet atlas* on $M$ is a family of charts $(U_i, \varphi_i)_{i \in I}$ such that:

1. Each $U_i$ is open in $M$ and the sets $U_i$ cover $M$.
2. Each $\varphi_i$ is a [[homeomorphism|0QT00PB5G2]] from $U_i$ onto an [[open subset|02BH3MCBQB]] of a Fréchet space.
3. Each transition map $\varphi_j \circ \varphi_i^{-1} \colon \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j)$ is smooth.

A *Fréchet manifold* is a space $M$ with an equivalence class of smooth Fréchet atlases, two atlases being equivalent when their union is an atlas.

## Remarks

Every Banach space is a Fréchet space, and every smooth [[Banach manifold|9K15AMGBV9]] is a Fréchet manifold.

Example: the Fréchet space $C^\infty(S^1)$ of smooth functions on the circle, with the single chart $\id$, is a Fréchet manifold.
More generally, for a compact manifold $K$ and a manifold $N$, the space $C^\infty(K, N)$ of smooth maps is a Fréchet manifold.
The diffeomorphisms of $K$ form a Fréchet Lie group.

Non-example: take charts with values in the space of compactly supported smooth functions on $\R$ with the sup norm.
That normed space is not complete, so it is not a Fréchet space and clause 2 fails.
