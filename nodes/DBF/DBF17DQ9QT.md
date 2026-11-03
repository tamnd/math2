---
tag: DBF17DQ9QT
kind: definition
name: Lagrangian and Eulerian specification of the flow field
msc: [76A02]
defines: 5E6K4ATM9W
uses: [H27M44BV4M, 0299VCW1TH, 0NT64JV96A, 06738GGWWK]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_and_Eulerian_specification_of_the_flow_field
---

## Definition

Let a fluid move in a region $\Omega \subseteq \R^3$ over a time interval $I$ containing $0$.
Let $\Omega_0 \subseteq \Omega$ be the region that the fluid occupies at time $0$.

1. A *Lagrangian specification* is a map $X \colon \Omega_0 \times I \to \R^3$. Here $X(a, t)$ is the position at time $t$ of the parcel that is at $a$ at time $0$. Each map $a \mapsto X(a, t)$ is a bijection onto the region occupied at time $t$.
2. An *Eulerian specification* is a time-dependent [[vector field|0299VCW1TH]] $\mathbf{u} \colon \Omega \times I \to \R^3$. Here $\mathbf{u}(x, t)$ is the velocity of the parcel at the point $x$ at time $t$.

The two are related by the [[ordinary differential equation|0NT64JV96A]]
$$\frac{\partial X}{\partial t}(a, t) = \mathbf{u}(X(a, t), t), \qquad X(a, 0) = a.$$
The label $a$ is the *Lagrangian coordinate* and the point $x$ is the *Eulerian coordinate*.

## Remarks

Example: the rigid rotation $\mathbf{u}(x, y, t) = (-y, x)$ in the plane has Lagrangian description $X(a, t) = (a_1 \cos t - a_2 \sin t,\ a_1 \sin t + a_2 \cos t)$.
Check: $\partial X / \partial t = (-a_1 \sin t - a_2 \cos t,\ a_1 \cos t - a_2 \sin t) = \mathbf{u}(X(a, t))$, and $X(a, 0) = a$.
Non-example: the map $X(a, t) = (a_1 + t, a_2)$ paired with the field $\mathbf{u} = (0, 1)$ is not a pair of matching specifications, because $\partial X / \partial t = (1, 0) \ne \mathbf{u}$.
When $\mathbf{u}$ is smooth, the Lagrangian map at each time is given by the [[flow|06738GGWWK]] of the velocity field.
