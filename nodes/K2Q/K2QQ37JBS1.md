---
tag: K2QQ37JBS1
kind: definition
name: Coefficient of restitution
msc: [70F35, 70F10]
defines: 46XB01VKY4
uses: [S08QCTRKFJ, CAF7BHGGC9, HFDS8NCJ1A]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_of_restitution
---

## Definition

Let two particles of masses $m_1, m_2 > 0$ move on a line and collide.
They have velocities $u_1, u_2 \in \R$ before the collision and $v_1, v_2 \in \R$ after it, where $u_1 > u_2$ so that they approach.
The *coefficient of restitution* of the collision is
$$e = \frac{v_2 - v_1}{u_1 - u_2},$$
the ratio of the speed of separation to the speed of approach.

## Remarks

If [[momentum|HFDS8NCJ1A]] is conserved, the kinetic energy lost equals $\frac12 \mu (1 - e^2)(u_1 - u_2)^2$, where $\mu = m_1 m_2/(m_1 + m_2)$.
So $e = 1$ for an [[elastic collision|S08QCTRKFJ]], $e = 0$ for a perfectly [[inelastic collision|CAF7BHGGC9]], and $0 \le e < 1$ for other collisions that lose energy without the bodies passing through each other.
Example: a ball dropped from height $h$ hits the floor at speed $\sqrt{2gh}$; if it rises to height $h'$, then $e = \sqrt{h'/h}$, so $h = 1$ and $h' = 0.64$ give $e = 0.8$.
Non-example: if $u_1 \le u_2$, the particles do not approach, the denominator is not positive, and the quantity is not a coefficient of restitution.
For oblique collisions, $e$ is defined with the components of the velocities along the line of contact.

## Explanations

### L1 human

The coefficient of restitution says how much of the closing speed comes back as separating speed.
It runs from $0$, the bodies stick, to $1$, a perfect bounce.
