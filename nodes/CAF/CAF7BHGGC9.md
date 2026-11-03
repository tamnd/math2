---
tag: CAF7BHGGC9
kind: definition
name: Inelastic collision
msc: [70F35, 70F10]
defines: 1BFJYGPGB3
uses: [HFDS8NCJ1A, 4NMMPYCK2C, S08QCTRKFJ, X5G1A3A4VR]
sources:
  - url: https://en.wikipedia.org/wiki/Inelastic_collision
---

## Definition

Let two particles of masses $m_1, m_2 > 0$ have velocities $u_1, u_2 \in \R^3$ before a collision and $v_1, v_2 \in \R^3$ after it.
The collision is *inelastic* if both of the following hold:

1. the total [[momentum|HFDS8NCJ1A]] is conserved, $m_1 v_1 + m_2 v_2 = m_1 u_1 + m_2 u_2$;
2. the total [[kinetic energy|4NMMPYCK2C]] decreases strictly, $\frac12 m_1 \abs{v_1}^2 + \frac12 m_2 \abs{v_2}^2 < \frac12 m_1 \abs{u_1}^2 + \frac12 m_2 \abs{u_2}^2$.

The collision is *perfectly inelastic* if moreover $v_1 = v_2$.

## Remarks

In a perfectly inelastic collision, $v_1 = v_2 = (m_1 u_1 + m_2 u_2)/(m_1 + m_2)$.
The kinetic energy lost is $\frac12 \mu \abs{u_1 - u_2}^2$, where $\mu = m_1 m_2/(m_1 + m_2)$ is the [[reduced mass|X5G1A3A4VR]]; this is the largest loss compatible with clause 1.
Example: $m_1 = m_2 = 1$, $u_1 = 2$, $u_2 = 0$ and $v_1 = v_2 = 1$ on a line; momentum stays $2$ and kinetic energy drops from $2$ to $1$.
Non-example: with the same data, $v_1 = 0$ and $v_2 = 2$ keep the kinetic energy at $2$, so clause 2 fails; this collision is [[elastic|S08QCTRKFJ]].

## Explanations

### L1 human

A collision is inelastic when the bodies keep their total momentum but lose some energy of motion.
The most inelastic case is when they stick together.
