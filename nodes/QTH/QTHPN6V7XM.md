---
tag: QTHPN6V7XM
kind: definition
name: Birkhoff min-max method
msc: ["58E10", 53C22, 49J35]
defines: 1R5X9HW6D3
uses: [Q61VFHCH2J, P9CM4GQ2T0, 0TH78S7GBZ, 4MCCP8GG4J, TMFG2P912R]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_geodesic
---

## Definition

Let $g$ be a smooth [[Riemannian metric|Q61VFHCH2J]] on the [[sphere|P9CM4GQ2T0]] $S^2$.
A *sweepout* of $S^2$ is a continuous map $c \colon [0, 1] \times S^1 \to S^2$ such that:

1. each curve $c_t = c(t, \cdot)$ is piecewise smooth, and $t \mapsto c_t$ is continuous for the $C^0$ topology and for the [[length|0TH78S7GBZ]];
2. the curves $c_0$ and $c_1$ are constant;
3. the map $S^2 \to S^2$ induced by $c$ on the quotient of $[0, 1] \times S^1$ that collapses $\set{0} \times S^1$ and $\set{1} \times S^1$ to points has nonzero [[degree|TMFG2P912R]].

The *width* of $(S^2, g)$ is
$$W(g) = \inf_{c} \ \max_{t \in [0, 1]} L(c_t),$$
the infimum over all sweepouts $c$ of the length of the longest curve.
The *Birkhoff min-max method* shows that $W(g) > 0$ and that $W(g)$ is the length of a [[closed geodesic|4MCCP8GG4J]].
The geodesic is a limit of longest curves of a minimizing sequence of sweepouts.
Before taking the limit, a curve-shortening process is applied to all curves of each sweepout at once.

## Remarks

The width is positive because curves of small length lie in small discs, so a sweepout by short curves would induce a map of degree $0$.
Birkhoff's curve-shortening process replaces each curve by a broken geodesic through finitely many of its points, and repeats.
It acts continuously on all curves of a sweepout and does not increase lengths.

Example: on the round unit sphere, the circles of latitude $c_t(s) = (\sin \pi t \cos s, \sin \pi t \sin s, -\cos \pi t)$ form a sweepout of degree $1$, whose longest curve is the equator, of length $2\pi$.
Here $W = 2\pi$, the length of a great circle.

Non-example: a family that starts and ends at constant curves but stays in the southern hemisphere, such as $c_t(s) = (\tfrac12 \sin \pi t \cos s, \tfrac12 \sin \pi t \sin s, -\sqrt{1 - \tfrac14 \sin^2 \pi t})$, is not a sweepout.
The induced map misses the north pole, so its degree is $0$, and clause 3 fails.
