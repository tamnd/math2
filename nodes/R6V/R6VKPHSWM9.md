---
tag: R6VKPHSWM9
kind: definition
name: N-body simulation
msc: [85-10, 70F10, 65Z05]
defines: DRCDVJS6PT
uses: [62SNWC5E45, 29WRN5J730, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/N-body_simulation
---

## Definition

Let $N \ge 2$ and let $G > 0$ be the gravitational constant.
Consider point particles with masses $m_1, \dots, m_N > 0$, positions $x_i(t) \in \R^3$ and a softening length $\varepsilon \ge 0$.
The gravitational N-body equations are the system of [[ordinary differential equations|0NT64JV96A]]
$$\ddot x_i = -G \sum_{j \ne i} m_j \frac{x_i - x_j}{\left(\norm{x_i - x_j}^2 + \varepsilon^2\right)^{3/2}}, \qquad i = 1, \dots, N.$$
An *N-body simulation* is a numerical computation that starts from given positions and velocities at time $t_0$.
By a time-stepping scheme applied to this system, it produces approximations of $x_i(t_k)$ and $\dot x_i(t_k)$ at times $t_0 < t_1 < t_2 < \cdots$.

## Remarks

For $\varepsilon = 0$ the equations are those of the [[n-body problem|62SNWC5E45]] with [[Newton's law of gravitation|29WRN5J730]].
A positive $\varepsilon$ removes the divergence of the force at close encounters; it is used when each particle stands for a cloud of matter rather than a star.

Example: the leapfrog (kick-drift-kick) scheme with step $h$, which updates $v_i \leftarrow v_i + \tfrac{h}{2} a_i$, then $x_i \leftarrow x_i + h v_i$, then recomputes $a_i$ and sets $v_i \leftarrow v_i + \tfrac{h}{2} a_i$, defines an N-body simulation.
Each step only uses the right-hand side of the equations, so it is a time-stepping scheme for them.

Non-example: the closed-form Kepler orbit of two bodies is an exact solution, not a step-by-step numerical computation, so it is not an N-body simulation.

Direct summation of all pairs costs of order $N^2$ operations per step.
Tree codes and the fast multipole method lower this cost by approximating the forces of distant groups of particles.
