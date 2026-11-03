---
tag: 5EDAFMGCMW
kind: definition
name: Bending moment
msc: [74K10, 70C20]
defines: Q6XAPXMGH0
uses: [HXGCGHS070]
sources:
  - url: https://en.wikipedia.org/wiki/Bending_moment
---

## Definition

Let a straight beam lie along the $x$-axis, with cross-section $A$ in the $(y, z)$-plane and centroid of $A$ on the axis.
Let the beam bend in the $(x, y)$-plane, and let $\sigma_{xx}(x, y, z)$ be the normal [[stress|HXGCGHS070]] on the cross-section at $x$.
The *bending moment* at $x$ is
$$M(x) = \int_A y \, \sigma_{xx}(x, y, z) \, dy \, dz.$$
Let the beam be in equilibrium.
Then $M(x)$ equals the moment about $x$ of the external forces and couples on the part of the beam to one side of $x$.

## Remarks

Here $y$ points in the direction of the load, so that a moment that makes the beam sag, with tension on the side $y > 0$, is positive.
Example: a simply supported beam of length $L$ with a point load $P$ at mid-span has support reactions $P/2$.
For $0 \le x \le L/2$ the forces to the left of $x$ are only the reaction $P/2$ at $0$, with lever arm $x$, so $M(x) = Px/2$.
The largest value is $M(L/2) = PL/4$.

Non-example: the integral $\int_A \sigma_{xx} \, dy \, dz$ is the axial force, not the bending moment; it is $0$ in pure bending, while $M$ is not.

In the [[Euler–Bernoulli|13FGKM7NQ0]] theory the stress is $\sigma_{xx} = -E y w''$, where $w$ is the deflection in the direction of $y$, so $M = -E I w''$, where $I$ is the [[second moment of area|1QCSARFXQ0]].
Texts differ in the sign conventions for $M$.
