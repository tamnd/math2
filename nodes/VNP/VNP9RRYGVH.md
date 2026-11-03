---
tag: VNP9RRYGVH
kind: definition
name: Four-velocity
msc: [83A05, 70B05]
defines: Y59V040THG
uses: [S8RKKKMSTG, Z788G6MJ9E, YG74WHC3S9, 2E9AJVZS6E]
sources:
  - url: https://en.wikipedia.org/wiki/Four-velocity
---

## Definition

Let $\sigma$ be a timelike [[world line|Z788G6MJ9E]] in Minkowski space, parametrised by its [[proper time|YG74WHC3S9]] $\tau$, so that $\tau \mapsto x(\tau)$ with $x(\tau)$ in inertial coordinates $(x^0, x^1, x^2, x^3)$.
The *four-velocity* at proper time $\tau$ is the [[four-vector|S8RKKKMSTG]]
$$U(\tau) = \frac{dx}{d\tau}(\tau).$$
If the world line is written as $t \mapsto (ct, \mathbf{x}(t))$ with velocity $\mathbf{u} = d\mathbf{x}/dt$, then
$$U = \gamma(u) \, (c, \mathbf{u}),$$
where $\gamma(u)$ is the [[Lorentz factor|2E9AJVZS6E]] of $u = \abs{\mathbf{u}}$.

## Remarks

Example: for $\mathbf{u} = (0.6 c, 0, 0)$, $\gamma = 1.25$ and $U = (1.25 c, 0.75 c, 0, 0)$.
Check: $\eta(U, U) = -(1.25)^2 c^2 + (0.75)^2 c^2 = -c^2$.
In general $\eta(U, U) = -c^2$, because $d\tau = dt / \gamma$ and $\gamma^2 (u^2 - c^2) = -c^2$.
Non-example: the derivative $dx/dt = (c, \mathbf{u})$ with respect to coordinate time is not the four-velocity: it is not a four-vector, and its squared length $-c^2 + u^2$ depends on the frame.
The four-momentum of a particle of mass $m$ is $P = m U$.
