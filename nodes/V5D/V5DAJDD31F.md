---
tag: V5DAJDD31F
kind: definition
name: Rolling without slipping
msc: ["70E18", "70F25"]
defines: PPW75DGKDR
uses: [EZ9P9ERKNE, 2FTZ7D8Z0F, K160D2Z0CS]
sources:
  - url: https://en.wikipedia.org/wiki/Rolling
---

## Definition

Let a [[rigid body|EZ9P9ERKNE]] $B$ move in contact with a surface $S$ that is fixed in space.
Let $G(t)$ be a point fixed in $B$, with [[velocity|K160D2Z0CS]] $v_G(t)$, and let $\omega(t)$ be the [[angular velocity|2FTZ7D8Z0F]] of $B$.
Let $P(t)$ be the point of contact of $B$ with $S$.
The body *rolls without slipping* on $S$ if, at every time $t$, the material point of $B$ at $P(t)$ has velocity zero:
$$v_G(t) + \omega(t) \times \big(P(t) - G(t)\big) = 0.$$

## Remarks

If $S$ is itself moving, the condition asks that the material points of $B$ and $S$ at the contact point have equal velocities.
The contact point $P(t)$ moves along $S$ and along the surface of $B$; only the material point of $B$ there is momentarily at rest.

Example: a disc of radius $r$ rolling in a vertical plane along the $x$-axis, with centre $G = (x, r)$ and angle of rotation $\phi$ measured clockwise.
Here $\omega = -\dot\phi\, e_z$ and $P - G = (0, -r, 0)$, so $\omega \times (P - G) = (-r\dot\phi, 0, 0)$.
The condition becomes $\dot x = r\dot\phi$, which integrates to $x = r\phi + \text{const}$: in this case the constraint is holonomic.

Non-example: a wheel that is locked while the car brakes on ice has $\omega = 0$ and $v_G \ne 0$, so its contact point slides; this is slipping.

For a disc rolling upright on a plane, the analogous conditions on $\dot x$, $\dot y$ involve the heading angle and cannot be integrated to conditions on positions alone.

## Explanations

### L1 human

Rolling without slipping means no skidding: the part of the body touching the ground does not slide over it.
For a wheel, the distance travelled equals the length of rim that has touched the ground.
