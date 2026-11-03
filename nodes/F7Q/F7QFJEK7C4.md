---
tag: F7QFJEK7C4
kind: example
name: Projectile motion
msc: [70B05, 70A05]
illustrates: [KNBP19FG6K]
uses: [KNBP19FG6K, 04S2GMHX82]
sources:
  - url: https://en.wikipedia.org/wiki/Projectile_motion
same_as:
  wikidata: Q10281355
  wikipedia: Projectile motion
---

## Example

A particle of mass $m$ moves in the vertical plane with coordinates $(x, z)$, under uniform gravity $(0, -mg)$ with $g > 0$ and without air resistance.
It starts at the origin at time $0$ with speed $v > 0$ at the angle $\theta \in (0, \pi/2)$ above the horizontal.
[[Newton's second law|KNBP19FG6K]] gives $\ddot x = 0$ and $\ddot z = -g$, so
$$x(t) = v t \cos\theta, \qquad z(t) = v t \sin\theta - \tfrac12 g t^2.$$
Check: $m(\ddot x, \ddot z) = (0, -mg)$, and $(x(0), z(0)) = (0, 0)$, $(\dot x(0), \dot z(0)) = (v\cos\theta, v\sin\theta)$.
Eliminating $t = x/(v \cos\theta)$ gives the path
$$z = x \tan\theta - \frac{g}{2 v^2 \cos^2\theta}\, x^2,$$
a [[parabola|04S2GMHX82]].
The particle returns to $z = 0$ at time $2 v \sin\theta / g$, at the distance $R = v^2 \sin(2\theta)/g$.
The range $R$ is largest for $\theta = \pi/4$, and the greatest height is $v^2 \sin^2\theta/(2g)$.

## Explanations

### L1 human

A thrown ball moves sideways at a steady speed while gravity pulls it down at a steady rate.
Together these two motions draw a parabola.
On flat ground and without air, a throw at $45$ degrees goes farthest, and throws at $30$ and $60$ degrees land at the same spot.
