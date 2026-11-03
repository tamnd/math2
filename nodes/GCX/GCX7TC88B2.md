---
tag: GCX7TC88B2
kind: statement
role: theorem
name: Conservation of angular momentum
msc: [70A05, 70F10]
uses: [KNBP19FG6K, F5W4PMJF8V, THX3FXH5C1]
about: [7147M98XNR]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_momentum
---

## Statement

Let $N$ point particles have masses $m_i > 0$ and positions $x_i(t) \in \R^3$, and let their motion obey [[Newton's second law|KNBP19FG6K]].
Let $F_{ij}(t)$ be the force of particle $j$ on particle $i$.
Suppose that no external force acts, so that the net force on particle $i$ is $\sum_{j \ne i} F_{ij}(t)$.
Suppose that $F_{ji} = -F_{ij}$ and that $F_{ij}(t)$ is parallel to $x_i(t) - x_j(t)$ for all $i \ne j$ and all $t$.
Then the total [[angular momentum|F5W4PMJF8V]] $L(t) = \sum_{i=1}^{N} x_i(t) \times m_i \dot x_i(t)$ about the origin is constant in $t$.

## Remarks

The proof: $\dot L = \sum_i \dot x_i \times m_i \dot x_i + \sum_i x_i \times m_i \ddot x_i = \sum_{i \ne j} x_i \times F_{ij}$.
Grouping the terms for $(i, j)$ and $(j, i)$ gives $(x_i - x_j) \times F_{ij} = 0$, since the vectors are parallel.
The same argument shows that a particle moving under a [[central force|THX3FXH5C1]] has constant angular momentum about the centre.
So it moves in a plane and sweeps equal areas in equal times.
Example: a planet around a fixed Sun has $\abs{x \times \dot x}$ constant, which is Kepler's second law.
The parallel hypothesis is needed: if $F_{12} = -F_{21}$ but these forces are not along $x_1 - x_2$, they form a couple and $\dot L = (x_1 - x_2) \times F_{12} \ne 0$.

## Explanations

### L1 human

If nothing outside twists a system, its total amount of spin stays the same.
That is why a spinning skater speeds up when she pulls in her arms, and why planets move faster when they are closer to the Sun.

### L2 human

Angular momentum is a vector first integral; its constancy confines central-force motion to a plane and reduces it to one radial equation.
More generally $\dot L$ equals the total external torque, so $L$ is conserved whenever that torque vanishes.
In Lagrangian mechanics the result follows from invariance under rotations, an instance of Noether's theorem.
