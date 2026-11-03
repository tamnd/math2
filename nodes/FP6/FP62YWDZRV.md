---
tag: FP62YWDZRV
kind: example
name: Luneburg lens
msc: [78A05]
instance_of: [C9TV3FZEM4]
uses: [MQ5ZJ7VADG, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Luneburg_lens
same_as:
  wikidata: Q739536
  wikipedia: Luneburg lens
---

## Example

Fix $R > 0$.
The *Luneburg lens* is the ball $\abs{x} \le R$ with [[refractive index|9VGK0SP6EQ]]
$$n(x) = \sqrt{2 - \abs{x}^2 / R^2},$$
placed in a surrounding medium of index $1$.
The index is smooth on the ball and not constant, so the ball is a [[gradient-index medium|C9TV3FZEM4]].
It equals $\sqrt 2$ at the centre and $1$ on the boundary sphere.
So it matches the outside index, and no ray is refracted at the surface.
Let a parallel beam travel in the direction of a unit vector $e$.
The ray equation for this index shows that every ray of the beam entering the ball leaves it at the same point $Re$.
By reversibility of rays, a point source on the surface produces a parallel beam on the other side.

## Explanations

### L1 human

The Luneburg lens is a ball whose index grows from $1$ at the surface to about $1.41$ at the centre.
It focuses a parallel beam coming from any direction to a point on its back surface.
Because the ball looks the same from every direction, one lens works for all directions at once, which is why the design is used for radar reflectors and antennas.
