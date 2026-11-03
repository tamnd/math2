---
tag: V57V5WKGE2
kind: problem
name: Sitnikov problem
msc: [70F07, 37N05, 70K55]
uses: [JE1Z920QKT, CSVPJAA75E, MSB4ZTG422, DBKXCGDKTD, N0N7CMRCMH]
about: [JE1Z920QKT]
sources:
  - url: https://en.wikipedia.org/wiki/Sitnikov_problem
same_as:
  wikidata: Q1697929
  wikipedia: Sitnikov problem
history:
  posed_by: "Kirill Sitnikov"
  first_stated: "1960"
---

## Problem

Let $e \in [0, 1)$.
Two bodies of mass $\frac{1}{2}$ each move in the plane $z = 0$ on Kepler ellipses of eccentricity $e$.
Their motions are symmetric with respect to their centre of mass at the origin.
Units are chosen so that the gravitational constant is $1$ and the period of the primaries is $2 \pi$.
This is a solution of the [[two-body problem|CSVPJAA75E]], and the distance of each primary from the origin is $\rho(t) = \frac{1}{2} \left( 1 - e \cos E(t) \right)$, where $E(t)$ solves [[Kepler's equation|MSB4ZTG422]] $t = E - e \sin E$.
A third body of negligible mass moves on the $z$-axis, which is invariant by symmetry, and its height satisfies
$$z''(t) = - \frac{z(t)}{\left( z(t)^2 + \rho(t)^2 \right)^{3/2}}.$$
Describe the solutions of this equation for all time.

## Remarks

The Sitnikov problem is a special case of the restricted [[three-body problem|JE1Z920QKT]].
For $e = 0$ the distance $\rho$ is constant, the equation is autonomous with one degree of freedom and conserved energy, and it is an [[integrable system|N0N7CMRCMH]].
For $e > 0$ the equation depends periodically on time, and its motions can be [[chaotic|DBKXCGDKTD]].
Sitnikov proved the existence of oscillatory motions, in which $z$ is unbounded but returns infinitely often to a bounded region.
Moser later described the motions for small $e > 0$ by symbolic dynamics.
Any sequence of large enough numbers of revolutions of the primaries between successive crossings of the plane is realised by some motion.

## Explanations

### L1 human

Two equal stars orbit each other on ellipses, and a small planet moves up and down on the line through their centre of mass, perpendicular to their orbit.
If the stars move on circles, the up-and-down motion is regular and easy to describe.
If the orbits are elliptic, the pull on the planet changes with time, and the planet may bounce higher and higher, escape, or move in an unpredictable way.
This very simple model already contains chaos and motions that are neither bounded nor escaping.
