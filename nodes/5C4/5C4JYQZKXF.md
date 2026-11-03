---
tag: 5C4JYQZKXF
kind: definition
name: Mechanical equilibrium
msc: [70C20]
defines: KHT3FBB7NZ
uses: [EZ9P9ERKNE, 9636MFFSGC, 4KSPEPZWP2, BCF1EX9W2M]
sources:
  - url: https://en.wikipedia.org/wiki/Mechanical_equilibrium
---

## Definition

Let a [[rigid body|EZ9P9ERKNE]], or a particle, be acted on by forces $F_1, \dots, F_k \in \R^3$ at points $p_1, \dots, p_k \in \R^3$.
The body is in *mechanical equilibrium* if both conditions hold:

1. the net force vanishes, $\sum_{i=1}^{k} F_i = 0$;
2. the net [[torque|9636MFFSGC]] about a reference point $O$ vanishes, $\sum_{i=1}^{k} (p_i - O) \times F_i = 0$.

For a particle all $p_i$ are equal, and condition 2 follows from condition 1.

## Remarks

When condition 1 holds, the net torque is the same about every point, so condition 2 does not depend on the choice of $O$.

Example: a weightless beam along the $x$-axis carries the downward force $(0, 0, -300)$ at $x = -2$ and $(0, 0, -200)$ at $x = 3$, and rests on a support at $x = 0$ that pushes up with $(0, 0, 500)$.
The net force is $0$, and the net torque about $0$ is $(0, -600, 0)$ from the first load plus $(0, 600, 0)$ from the second, which is $0$.

Non-example: take the [[couple|4KSPEPZWP2]] formed by $(0, 5, 0)$ at $(0.2, 0, 0)$ and $(0, -5, 0)$ at $(-0.2, 0, 0)$.
It satisfies condition 1 but has net torque $(0, 0, 2)$, so a body subject only to it is not in equilibrium.

For a system with [[generalized coordinates|BCF1EX9W2M]] $q$ and potential energy $V(q)$, a configuration $q_0$ is an equilibrium configuration when $\nabla V(q_0) = 0$, that is, all generalized forces vanish there.
