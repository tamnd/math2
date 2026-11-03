---
tag: S08QCTRKFJ
kind: definition
name: Elastic collision
msc: [70F35, 70F10]
defines: NSF6MKF91K
uses: [HFDS8NCJ1A, 4NMMPYCK2C]
sources:
  - url: https://en.wikipedia.org/wiki/Elastic_collision
---

## Definition

Let two particles of masses $m_1, m_2 > 0$ have velocities $u_1, u_2 \in \R^3$ before a collision and $v_1, v_2 \in \R^3$ after it.
The collision is *elastic* if both of the following hold:

1. the total [[momentum|HFDS8NCJ1A]] is conserved, $m_1 v_1 + m_2 v_2 = m_1 u_1 + m_2 u_2$;
2. the total [[kinetic energy|4NMMPYCK2C]] is conserved, $\frac12 m_1 \abs{v_1}^2 + \frac12 m_2 \abs{v_2}^2 = \frac12 m_1 \abs{u_1}^2 + \frac12 m_2 \abs{u_2}^2$.

## Remarks

For motion on a line, the solution with $(v_1, v_2) \ne (u_1, u_2)$ is
$$v_1 = \frac{(m_1 - m_2) u_1 + 2 m_2 u_2}{m_1 + m_2}, \qquad v_2 = \frac{(m_2 - m_1) u_2 + 2 m_1 u_1}{m_1 + m_2}.$$
Example: equal masses with $u_1 = 1$, $u_2 = 0$ give $v_1 = 0$, $v_2 = 1$; momentum $1$ and kinetic energy $\frac12 m$ are unchanged.
Non-example: equal masses with $u_1 = 1$, $u_2 = 0$ that stick together give $v_1 = v_2 = \frac12$; momentum is conserved but the kinetic energy drops from $\frac12 m$ to $\frac14 m$, so clause 2 fails.
On a line, if clause 1 holds and $(v_1, v_2) \ne (u_1, u_2)$, then clause 2 is equivalent to $v_2 - v_1 = -(u_2 - u_1)$: the relative velocity is reversed.

## Explanations

### L1 human

A collision is elastic when no kinetic energy is lost.
The bodies bounce apart with the same relative speed with which they met.
