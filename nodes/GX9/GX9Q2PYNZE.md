---
tag: GX9Q2PYNZE
kind: example
name: Sinai billiard
msc: ["37C83", "37A25"]
instance_of: [XWMKYE038F]
uses: [XWMKYE038F, S3RJQ9CX2P, 03NM7DZXXC, NJ1FJSNK6A]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamical_billiards
---

## Example

Let $\mathbb{T}^2 = \R^2 / \Z^2$ be the flat [[torus|03NM7DZXXC]], and let $D \subset \mathbb{T}^2$ be the image of a closed disc of radius $r$ with $0 < r < 1/2$.
The *Sinai billiard* is the [[billiard|XWMKYE038F]] on the table $Q = \mathbb{T}^2 \setminus \operatorname{int} D$.
Equivalently, it is the billiard in the unit square with a disc of radius $r$ removed from its centre.
A particle leaving through one side of the square comes back through the opposite side.
The table fits the definition: away from $\partial D$ the particle moves in straight lines, and on the circle $\partial D$ it reflects.
The boundary $\partial D$ is convex when seen from the disc, so it curves away from the table: the billiard is *dispersing*.

## Remarks

Sinai proved in 1970 that this billiard flow is ergodic and [[mixing|S3RJQ9CX2P]] with respect to the Liouville measure.
The mechanism is dispersion: a narrow beam of parallel trajectories hitting a convex obstacle spreads out after the reflection, which gives a positive [[Lyapunov exponent|NJ1FJSNK6A]].
Unfolding the torus gives the periodic Lorentz gas: a particle moving among discs placed at the points of $\Z^2$.

## Explanations

### L1 human

Put a round post in the middle of a square billiard table whose sides wrap around, as in a video game.
Each time the ball hits the post, nearby paths are pushed apart, like light reflected by a convex mirror.
After many bounces the ball forgets where it started, and in the long run it spends equal time in regions of equal area.
It was one of the first billiards proved to be chaotic in this strong sense.
