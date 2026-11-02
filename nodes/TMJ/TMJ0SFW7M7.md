---
tag: TMJ0SFW7M7
kind: definition
name: Semilocally simply connected space
msc: [57M10, 55Q05]
defines: R3SHZX0NZR
uses: [0CQHFPGJ45, S1XK3HXHFX]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-locally_simply_connected
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *semilocally simply connected* if every point $x \in X$ has an open neighbourhood $U$ with the following property.
The homomorphism $\pi_1(U, x) \to \pi_1(X, x)$ of [[fundamental groups|S1XK3HXHFX]] induced by the inclusion $U \hookrightarrow X$ is trivial.
Equivalently, every loop in $U$ based at $x$ is null-homotopic in $X$.

## Remarks

Example: a manifold is semilocally simply connected.
Each point has a neighbourhood $U$ homeomorphic to an open ball, so $\pi_1(U, x)$ is already trivial.

Non-example: the [[Hawaiian earring|73EBKQPP8Q]] $H = \bigcup_{n \ge 1} C_n$, where $C_n \subset \R^2$ is the circle of radius $1/n$ centred at $(1/n, 0)$, is not.
Every neighbourhood $U$ of the origin contains some $C_n$, and a loop around $C_n$ is not null-homotopic in $H$, because $H$ retracts onto $C_n$.

The cone on the Hawaiian earring is contractible, so it is semilocally simply connected, but it is not locally simply connected.
The spelling "semi-locally simply connected" is also common.
