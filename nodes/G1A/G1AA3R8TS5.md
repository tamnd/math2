---
tag: G1AA3R8TS5
kind: definition
name: Trapped surface
msc: ["83C75", "83C57", "53C50"]
defines: 26AVAT8306
uses: [BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Trapped_surface
---

## Definition

Let $(M, g)$ be a time-oriented four-dimensional [[Lorentzian manifold|BY4QYYS788]].
Let $S \subset M$ be a compact, connected, spacelike, two-dimensional submanifold without boundary.
At each point of $S$ the normal space is a two-dimensional Lorentzian plane, so it contains exactly two future-directed null directions.
Choose smooth future-directed null normal fields $\ell_+$ and $\ell_-$ along $S$, one in each direction.
The *null expansion* of $S$ along $\ell_\pm$ is
$$\theta_\pm = \sum_{i=1}^{2} g(\nabla_{e_i} \ell_\pm, e_i),$$
where $(e_1, e_2)$ is a local orthonormal frame of the tangent spaces of $S$.
The surface $S$ is a *closed trapped surface* if $\theta_+ < 0$ and $\theta_- < 0$ at every point of $S$.

## Remarks

The expansion $\theta_\pm$ is the rate of change of the area element of $S$ when $S$ is pushed along $\ell_\pm$.
Rescaling $\ell_\pm$ by a positive function rescales $\theta_\pm$ by the same function, so the sign condition does not depend on the choice.
If $\theta_+ = 0$ for the outgoing direction, the surface is called marginally outer trapped.

Example: in the [[Schwarzschild metric|6Y50T68WKY]] of mass $m$, extended across $r = 2m$, take a round sphere of area radius $r < 2m$.
In the region $r < 2m$ the function $r$ strictly decreases along every future-directed causal curve.
The area of the sphere is $4\pi r^2$, so it decreases in both null directions, and $\theta_+ < 0$ and $\theta_- < 0$.

Non-example: in Minkowski space, the round sphere $t = 0$, $\abs{x} = R$ has $\theta_+ = 2/R > 0$ for the outgoing null normal $\partial_t + \partial_r$.
It has $\theta_- = -2/R < 0$ for the ingoing one, so it fails the condition $\theta_+ < 0$.
