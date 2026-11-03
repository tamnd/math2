---
tag: T1SHG5MD9R
kind: statement
role: theorem
name: Conservation of momentum
msc: [70A05, 70F10]
uses: [KNBP19FG6K, HFDS8NCJ1A]
about: [37Q4BTJMXW]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum
---

## Statement

Let $N$ point particles have masses $m_i > 0$ and positions $x_i(t) \in \R^3$, and let their motion obey [[Newton's second law|KNBP19FG6K]].
Let $F_{ij}(t)$ be the force of particle $j$ on particle $i$.
Suppose that no external force acts, so that the net force on particle $i$ is $\sum_{j \ne i} F_{ij}(t)$.
Suppose that these forces obey Newton's third law, $F_{ji} = -F_{ij}$ for all $i \ne j$.
Then the total [[momentum|HFDS8NCJ1A]] $P(t) = \sum_{i=1}^{N} m_i \dot x_i(t)$ is constant in $t$.

## Remarks

The proof: $\dot P = \sum_i \sum_{j \ne i} F_{ij}$, and the terms cancel in pairs, since $F_{ij} + F_{ji} = 0$.
As a consequence, the centre of mass $X = \frac{1}{M}\sum_i m_i x_i$, with $M = \sum_i m_i$, moves with constant velocity $P/M$.
Example: a gun of mass $M$ at rest fires a bullet of mass $m$ at velocity $v$; the gun recoils at velocity $-m v / M$.
If external forces act, the same computation gives $\dot P = \sum_i F_i^{\text{ext}}$, so $P$ changes; for instance a falling system gains downward momentum.
Without the third law the conclusion fails: two particles with $F_{12} = F_{21} = (1, 0, 0)$ give $\dot P = (2, 0, 0)$.

## Explanations

### L1 human

In an isolated system, the total momentum never changes.
When two skaters push each other apart, they move off in opposite directions, and the heavier one moves more slowly.

### L2 human

Momentum conservation is the main tool for collisions, where the forces are unknown and brief but act in equal and opposite pairs.
In Lagrangian mechanics it follows from invariance of the Lagrangian under translations, an instance of Noether's theorem.
It also lets one pass to the centre-of-mass frame, which separates the motion of the system as a whole from its internal motion.
