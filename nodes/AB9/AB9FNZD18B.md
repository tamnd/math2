---
tag: AB9FNZD18B
kind: statement
role: theorem
name: Theorem of the three geodesics
msc: [53C22, "58E10"]
uses: [Q61VFHCH2J, P9CM4GQ2T0, 4MCCP8GG4J]
about: [4MCCP8GG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_of_the_three_geodesics
same_as:
  wikidata: Q25143636
  wikipedia: Theorem of the three geodesics
---

## Statement

Let $g$ be a smooth [[Riemannian metric|Q61VFHCH2J]] on the two-dimensional [[sphere|P9CM4GQ2T0]] $S^2$.
Then $(S^2, g)$ has at least three geometrically distinct simple [[closed geodesics|4MCCP8GG4J]], where simple means without self-intersections.

## Remarks

The idea goes back to Lyusternik and Schnirelmann.
Consider the space of unoriented simple closed curves on $S^2$, together with the point curves.
Its topology is rich enough to force three minimax levels, in the spirit of [[Lusternik–Schnirelmann theory|QARH15D2PN]].
The difficulty is to deform curves by a length-decreasing process that keeps them simple; this caused gaps in the early arguments.
One complete proof uses the [[curve-shortening flow|DVGFRRYK10]], which preserves simplicity and, by a theorem of Grayson, either shrinks a curve to a point or converges to a closed geodesic.

Example: on a round sphere every great circle is a simple closed geodesic, so there are infinitely many.
On an ellipsoid in $\R^3$ with three distinct axes, the three principal sections in the coordinate planes are simple closed geodesics.
The bound three cannot be improved in general.

## Explanations

### L1 human

However one deforms a sphere smoothly, it still carries at least three different closed loops that go straight ahead and never cross themselves.
On a round sphere there are infinitely many such loops, the great circles.
On an egg-shaped surface with three different axes there are typically exactly three, the waists around the three axes.

### L2 human

The theorem is a sharp lower bound for simple closed geodesics.
When self-intersections are allowed, the theorem of [[Bangert and Franks|X93AEE88PX]] gives infinitely many closed geodesics on any Riemannian $S^2$.
Its proof is a model of Lusternik–Schnirelmann theory on a space of curves: three independent families of curves sweep out the sphere, and each family yields a critical level.
The first step, a single closed geodesic on $S^2$, is the [[Birkhoff min-max method|1R5X9HW6D3]].
