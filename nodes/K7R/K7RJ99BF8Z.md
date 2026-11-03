---
tag: K7RJ99BF8Z
kind: example
name: Chaplygin sleigh
msc: [70F25, "70E18"]
instance_of: [PTRV0QFSB9]
uses: [PTRV0QFSB9, EZ9P9ERKNE, C9YCMAPKMT]
sources:
  - url: https://en.wikipedia.org/wiki/Chaplygin_sleigh
same_as:
  wikidata: Q17006435
  wikipedia: Chaplygin sleigh
---

## Example

The Chaplygin sleigh is a [[rigid body|EZ9P9ERKNE]] that moves on a horizontal plane.
It rests on the plane at a knife edge and at other points that slide without friction.
The knife edge forbids motion of its contact point perpendicular to the blade.
Let $(x, y)$ be the contact point of the blade and $\theta$ the angle of the blade with the $x$-axis.
Let $m > 0$ be the mass and $I > 0$ the moment of inertia about the centre of mass.
Let $a \ne 0$ be the signed distance from the contact point to the centre of mass, measured along the blade.
The configuration space is $\R^2 \times S^1$ with coordinates $(x, y, \theta)$, and the constraint is
$$-\dot x \sin\theta + \dot y \cos\theta = 0.$$
The vector fields $(\cos\theta, \sin\theta, 0)$ and $(0, 0, 1)$ span the allowed velocities, and their Lie bracket $(-\sin\theta, \cos\theta, 0)$ is not in their span.
So the constraint is not integrable, and the sleigh is a [[nonholonomic system|PTRV0QFSB9]].

## Remarks

Write $v$ for the speed of the contact point along the blade and $\omega = \dot\theta$.
The equations of motion are
$$\dot v = a\, \omega^2, \qquad \dot\omega = -\frac{m a}{I + m a^2}\, v\, \omega.$$
They conserve the [[kinetic energy|C9YCMAPKMT]] $E = \frac12 m v^2 + \frac12 (I + m a^2)\, \omega^2$: its derivative is $m a v \omega^2 - m a v \omega^2 = 0$.
Take $a > 0$; then $v$ never decreases, and if $\omega \ne 0$ initially, $\omega \to 0$ and $v \to \sqrt{2E/m}$ as $t \to \infty$.
So the sleigh ends up moving in a straight line with its centre of mass ahead of the blade, whatever the initial spin.
This shows a feature of nonholonomic systems: the energy is conserved, but phase space volume is not, and the motion has attracting states.

## Explanations

### L1 human

Picture a flat board on ice, with a single skate blade under one point and smooth feet elsewhere.
The blade lets that point slide forward and back but never sideways.
If you spin the board and push it, the spinning dies out and the board settles into gliding straight, with its heavy part in front.
No energy is lost; the blade only turns the energy of spinning into energy of gliding.
