---
tag: FAQ9CH2Z76
kind: statement
role: theorem
name: Hamilton's principle
msc: [70H25, 49S05, 70H03]
uses: [Q104C67P26, 5B8NFYB2XQ, PS0VV149ET]
about: [Q104C67P26]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton%27s_principle
same_as:
  wikidata: Q1145653
  wikipedia: Hamilton's principle
---

## Statement

Consider $N$ particles in $\R^3$ with masses $m_1, \dots, m_N > 0$ and positions $r = (r_1, \dots, r_N) \in \R^{3N}$.
Let $V \colon \R \times \R^{3N} \to \R$ be a potential of class $C^2$.
Let $T(\dot r) = \sum_{i=1}^N \frac12 m_i \abs{\dot r_i}^2$ be the kinetic energy and $L = T - V$ the Lagrangian.
Let $t_0 < t_1$ and let $r \colon [t_0, t_1] \to \R^{3N}$ be a $C^2$ path.
Consider Newton's equations
$$m_i \ddot r_i(t) = -\nabla_{r_i} V\big(t, r(t)\big), \qquad i = 1, \dots, N, \ t \in [t_0, t_1].$$
Let $S[r] = \int_{t_0}^{t_1} \big( T(\dot r) - V(t, r) \big) \, dt$ be the action.
Then $r$ satisfies Newton's equations if and only if $r$ is a stationary point of $S$ among $C^2$ paths with the same endpoints.

## Remarks

This is the case of mechanics of the [[stationary-action principle|Q104C67P26]].
For the proof, the [[first variation|5B8NFYB2XQ]] of $S$ in a direction $h$ with $h(t_0) = h(t_1) = 0$ is $\int_{t_0}^{t_1} \sum_i \left( m_i \dot r_i \cdot \dot h_i - \nabla_{r_i} V \cdot h_i \right) dt$.
An integration by parts turns it into $-\int_{t_0}^{t_1} \sum_i \left( m_i \ddot r_i + \nabla_{r_i} V \right) \cdot h_i \, dt$, which vanishes for all such $h$ exactly when Newton's equations hold, by the fundamental lemma of the calculus of variations.
So Newton's equations are the [[Euler–Lagrange equations|PS0VV149ET]] of $L = T - V$.
Example: a body falling near the Earth's surface, with $V(r) = m g z$, gives $\ddot z = -g$ and $\ddot x = \ddot y = 0$.
The endpoint times are fixed; Maupertuis's principle instead fixes the energy and lets the time vary.
For a system with ideal holonomic constraints, the same equivalence holds in generalized coordinates on the constraint manifold, and the constraint forces drop out.
William Rowan Hamilton formulated the principle in 1834 and 1835.

## Explanations

### L1 human

Hamilton's principle restates Newton's laws as an optimization rule.
Take the kinetic energy minus the potential energy, and add it up over the time of the motion.
The true motion is the path for which this total does not change, to first order, when the path is slightly bent with the endpoints held fixed.

### L2 human

The principle makes mechanics independent of coordinates: $T - V$ can be written in polar, spherical or any other coordinates, and the Euler–Lagrange equations in those coordinates are the equations of motion.
It is the starting point of Lagrangian and Hamiltonian mechanics, and through the Legendre transform it leads to Hamilton's canonical equations.
It also connects mechanics with the calculus of variations, so that tools such as the Jacobi condition decide when the action is in fact a minimum.
