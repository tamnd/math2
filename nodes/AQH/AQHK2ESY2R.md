---
tag: AQHK2ESY2R
kind: definition
name: No-slip condition
msc: [76D05, 35Q30, 76A02]
defines: DF0M8YNQ3D
uses: [EETVA6QYX4, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/No-slip_condition
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set whose boundary $\partial \Omega$ is a solid wall, and let $T > 0$.
Let $V \colon \partial \Omega \times (0, T) \to \R^3$ be the velocity of the wall, with $V = 0$ for a wall at rest.
A velocity field $u \colon \overline{\Omega} \times (0, T) \to \R^3$ of a fluid in $\Omega$, continuous up to the boundary, satisfies the *no-slip condition* if
$$u(x, t) = V(x, t) \quad \text{for all } x \in \partial \Omega \text{ and } t \in (0, T).$$
For a wall at rest it reads $u = 0$ on $\partial \Omega$, a homogeneous [[Dirichlet boundary condition|EETVA6QYX4]] for the [[vector field|0299VCW1TH]] $u$.
For weak solutions the equality is meant in the sense of traces.

## Remarks

Example: take the channel $0 < y < 1$ with the lower wall at rest and the upper wall moving with velocity $(U, 0, 0)$.
The field $u = (U y, 0, 0)$ satisfies the condition, since $u = 0$ at $y = 0$ and $u = (U, 0, 0)$ at $y = 1$.

Non-example: the potential flow past a cylinder at rest is tangent to the cylinder but has nonzero speed on it, so it satisfies only $u \cdot n = 0$ and fails the condition.

The condition splits into two parts: the normal part $u \cdot n = V \cdot n$ says that no fluid crosses the wall, and the tangential part says that the fluid does not slide along it.
Ideal fluids, governed by the Euler equations, only keep the normal part.
The Navier slip condition, which makes the tangential slip proportional to the tangential stress, is a common alternative.
