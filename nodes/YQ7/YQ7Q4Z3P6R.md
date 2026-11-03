---
tag: YQ7Q4Z3P6R
kind: definition
name: Statics
msc: [70C20]
defines: 5WCSERB8S4
uses: [KHT3FBB7NZ, EZ9P9ERKNE, 9636MFFSGC, Q05G0NZDNB]
sources:
  - url: https://en.wikipedia.org/wiki/Statics
---

## Definition

Fix an [[inertial frame|Q05G0NZDNB]].
A system of [[rigid bodies|EZ9P9ERKNE]] and particles is in *static equilibrium* if all its points are at rest in this frame at all times.
*Statics* is the part of mechanics that determines the forces and [[torques|9636MFFSGC]] in systems in static equilibrium.
It also determines the configurations in which such equilibrium is possible.
Its basic equations are the conditions of [[mechanical equilibrium|KHT3FBB7NZ]] for each body of the system.
Let the forces $F_i$ act on the body at the points $p_i$, and let $O$ be any reference point.
Then
$$\sum_i F_i = 0, \qquad \sum_i (p_i - O) \times F_i = 0.$$

## Remarks

By Newton's second law, a body at rest has zero acceleration, so the forces on it balance; this is why the equilibrium conditions hold.

Example: a weightless plank on two supports at $x = 0$ and $x = 4$ carries a load of $600$ newtons at $x = 1$.
The support forces $R_0$ and $R_4$ satisfy $R_0 + R_4 = 600$ and, taking torques about $0$, $4 R_4 = 600$.
So $R_4 = 150$ and $R_0 = 450$ newtons.

Non-example: a spinning wheel whose centre is fixed satisfies both equilibrium equations, yet its points are moving, so it is not in static equilibrium and lies outside statics.
In the plane the equations give three scalar equations per body; a structure with more unknown support forces than equations is called statically indeterminate.
