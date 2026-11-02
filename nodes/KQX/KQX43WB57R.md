---
tag: KQX43WB57R
kind: definition
name: Structural stability
msc: [34D30, 37C20]
defines: D4MGFAHVMT
uses: [0299VCW1TH, 0QT00PB5G2, 0BVT6VSB3S, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_stability
---

## Definition

Let $M$ be a compact smooth manifold without boundary, such as a circle, a sphere or a torus.
Let $\mathfrak{X}^1(M)$ be the space of [[continuously differentiable|0VW90BBSJ4]] [[vector fields|0299VCW1TH]] on $M$, with the $C^1$ topology.
Two vector fields $X$ and $Y$ on $M$ are *topologically equivalent* if there is a [[homeomorphism|0QT00PB5G2]] $h \colon M \to M$ with two properties.
It maps each [[trajectory|0BVT6VSB3S]] of $X$ onto a trajectory of $Y$.
It preserves the direction of time along trajectories.
A vector field $X \in \mathfrak{X}^1(M)$ is *structurally stable* if it has a neighbourhood $\mathcal{N}$ in $\mathfrak{X}^1(M)$ such that every $Y \in \mathcal{N}$ is topologically equivalent to $X$.

## Remarks

Example: on the circle $M = \R / 2\pi\Z$, the field $X(\theta) = \sin \theta$ has the two zeros $0$ and $\pi$, with $X'(0) = 1$ and $X'(\pi) = -1$.
A field $Y$ that is $C^1$-close to $X$ still has exactly two zeros, near $0$ and $\pi$, with derivatives of the same signs.
So $Y$ has one repelling and one attracting rest point joined by two arcs, and a homeomorphism of the circle carries the trajectories of $X$ to those of $Y$.
Hence $X$ is structurally stable.

Non-example: $X(\theta) = 1 - \cos \theta$ has the single zero $0$.
For $\varepsilon > 0$, the field $1 - \cos \theta + \varepsilon$ has no zero, and it is $C^1$-close to $X$ for small $\varepsilon$.
A homeomorphism maps rest points to rest points, so these fields are not equivalent to $X$, and $X$ is not structurally stable.

For flows on a compact surface, structural stability is closely tied to hyperbolicity of the rest points and periodic orbits and to the absence of trajectories joining saddles.
For a region in the plane, the definition is adapted by asking the vector field to point inward on the boundary.
