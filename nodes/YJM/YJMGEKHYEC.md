---
tag: YJMGEKHYEC
kind: definition
name: Ruled surface
msc: [14J26]
defines: 5NK10NGY13
uses: [KFTECAATKG, XJM2MT4S3Y, CDS1VWB7A3, ZT9A6JK8QF]
sources:
  - url: https://en.wikipedia.org/wiki/Ruled_surface
---

## Definition

Let $k$ be an algebraically closed field, and let $\mathbb{P}^1$ be the [[projective line|ZT9A6JK8QF]] over $k$.
A *ruled surface* over $k$ is a smooth projective [[algebraic surface|KFTECAATKG]] $X$ together with a surjective [[morphism|CDS1VWB7A3]] $\pi \colon X \to C$, with the following properties.
The target $C$ is a smooth projective [[curve|XJM2MT4S3Y]], and every fibre $\pi^{-1}(c)$, $c \in C$, is isomorphic to $\mathbb{P}^1$.

## Remarks

Some books also ask for a section of $\pi$; over an algebraically closed field a section always exists, by Tsen's theorem.
Every ruled surface is isomorphic over $C$ to the projectivization $\mathbb{P}(\mathcal{E})$ of a vector bundle $\mathcal{E}$ of rank $2$ on $C$.
Another usage calls a surface *ruled* when it is only birational to $C \times \mathbb{P}^1$; the surfaces of the definition are then called geometrically ruled.
Example: for any smooth projective curve $C$, the projection $C \times \mathbb{P}^1 \to C$ has every fibre $\set{c} \times \mathbb{P}^1 \cong \mathbb{P}^1$, so $C \times \mathbb{P}^1$ is ruled.
Non-example: the projective plane $\mathbb{P}^2$ is not ruled, because every morphism from $\mathbb{P}^2$ to a curve is constant.
Indeed, two fibres of a nonconstant one would be disjoint curves in $\mathbb{P}^2$, but any two curves in $\mathbb{P}^2$ meet.
