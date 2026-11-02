---
tag: DH4P0W4V3J
kind: definition
name: Moving frame
msc: [53A55, 53C05]
defines: 3K774WEHHY
uses: [F45VQ47GPV, WY6K3P4YCG, F4HWTRNXAP]
sources:
  - url: https://en.wikipedia.org/wiki/Moving_frame
---

## Definition

Let $M$ be a smooth manifold of dimension $n$, and let $U \subset M$ be open.
A *moving frame*, or local frame, on $U$ is an ordered $n$-tuple $(E_1, \dots, E_n)$ of smooth vector fields on $U$.
The condition is that $(E_1(p), \dots, E_n(p))$ is a basis of $T_pM$ for every $p \in U$.
The *dual coframe* is the $n$-tuple of $1$-forms $(\theta^1, \dots, \theta^n)$ on $U$ with $\theta^i(E_j) = \delta^i_j$.

## Remarks

A moving frame on $U$ is the same as a smooth section over $U$ of the [[frame bundle|F4HWTRNXAP]] of $M$.
Example: on $\R^2 \setminus \set{0}$ with polar coordinates, $E_1 = \partial_r$ and $E_2 = \frac1r \partial_\theta$ form a moving frame; at each point they are orthonormal for the Euclidean metric, so they form a basis.
Non-example: on $\R^2$, the pair $(\partial_x, x \, \partial_y)$ is not a moving frame, because at the points with $x = 0$ the second field vanishes.
Given an affine connection $\nabla$, the connection forms $\omega^i_j$ of the frame are defined by $\nabla E_j = \sum_i \omega^i_j \otimes E_i$, and Cartan's structure equations express torsion and curvature through $d\theta^i$ and $d\omega^i_j$.
A moving frame on all of $M$ exists only when the [[tangent bundle|WY6K3P4YCG]] is trivial; for example $S^2$ has none.
