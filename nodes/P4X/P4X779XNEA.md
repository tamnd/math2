---
tag: P4X779XNEA
kind: definition
name: Hilbert manifold
msc: [58B99, 46T05, 57N20]
defines: R8DMMW0E9M
uses: [VB95VVVDM8, PYYXEXMARY, 0BDTTM24DP, 06EH97V2A7]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_manifold
---

## Definition

Let $k \ge 1$ be an integer or $\infty$.
A *Hilbert manifold of class $C^k$* is a [[Banach manifold|VB95VVVDM8]] of class $C^k$ with an atlas of charts with values in real [[Hilbert spaces|PYYXEXMARY]].
It is *modelled on* the Hilbert space $H$ if all charts can be taken with values in $H$.
Many authors also require the underlying space to be Hausdorff and second countable, or the model $H$ to be separable.

## Remarks

Example: let $H$ be a real Hilbert space and $S = \set{x \in H : \norm{x} = 1}$ its unit sphere.
For $p \in S$, the map $x \mapsto x - \ip{x}{p} p$ restricted to $\set{x \in S : \ip{x}{p} > 0}$ is a chart onto the open unit ball of the closed hyperplane $p^\perp$, with inverse $y \mapsto y + \sqrt{1 - \norm{y}^2}\, p$.
Both maps are smooth, $p^\perp$ is a Hilbert space, and these charts cover $S$, so $S$ is a smooth Hilbert manifold.

Non-example: the [[Banach space|0BDTTM24DP]] $\ell^1$ with its identity chart is a Banach manifold, but no compatible chart takes values in a Hilbert space.
A compatible chart $\varphi$ into a Hilbert space $H$ would have a [[derivative|06EH97V2A7]] at a point that is a linear isomorphism of Banach spaces from $\ell^1$ onto $H$.
But $\ell^1$ is not isomorphic to a Hilbert space.


Every finite-dimensional smooth manifold is a Hilbert manifold modelled on $\R^n$.
