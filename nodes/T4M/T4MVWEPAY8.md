---
tag: T4MVWEPAY8
kind: definition
name: Variable-mass system
msc: [70F99, 70M20]
defines: Z82XBYZD1P
uses: [KNBP19FG6K, 37Q4BTJMXW, T1SHG5MD9R]
sources:
  - url: https://en.wikipedia.org/wiki/Variable-mass_system
---

## Definition

A *variable-mass system* is a body, treated as a point particle, whose mass $m(t) > 0$ changes with time because matter leaves it or joins it.
Let $v(t)$ be its velocity and let $F$ be the external force on it.
Let $u(t)$ be the velocity, relative to the body, of the matter that leaves or joins it at time $t$.
Its equation of motion is
$$m \frac{dv}{dt} = F + u \frac{dm}{dt}.$$

## Remarks

The equation follows from [[conservation of momentum|T1SHG5MD9R]] for the body together with the mass $\abs{dm}$ that it exchanges in a short time $dt$.
The total [[momentum|37Q4BTJMXW]] changes by $F\, dt$, as in [[Newton's second law|KNBP19FG6K]].
The term $u\, dm/dt$ is the thrust.

Example: a rocket ejects gas backwards at speed $v_e$ relative to itself, so $u = -v_e\, \hat{v}$ for the unit vector $\hat v$ in the direction of motion, and $dm/dt < 0$.
The thrust $-v_e\, \hat{v}\, dm/dt$ then points forwards.

Non-example: a closed system made of a rocket together with all its exhaust has constant mass, so it is not a variable-mass system; its total momentum changes only by $F$.

The naive formula $F = d(mv)/dt$ is wrong in general, since it depends on the choice of inertial frame.
It is right only when $u = -v$, that is, when the exchanged matter is at rest.
