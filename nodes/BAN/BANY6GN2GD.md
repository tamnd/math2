---
tag: BANY6GN2GD
kind: definition
name: Hyperbolic triangle
msc: [51M10, 51M09]
defines: GCZ8EEDCHS
uses: [GN4N94GQ0Z, NSYMQMHPDN, 0CTNFGYMM2, 85MM2EA0TK]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_triangle
---

## Definition

Let $\mathbb{H}^2$ be the [[hyperbolic plane|GN4N94GQ0Z]] of constant curvature $-1$.
Let $A$, $B$, $C$ be three points of $\mathbb{H}^2$ that do not lie on one [[geodesic|NSYMQMHPDN]] line.
The *hyperbolic triangle* $ABC$ is the union of the three geodesic segments $AB$, $BC$ and $CA$, together with the region they bound.
Its sides are the hyperbolic lengths $a = d(B, C)$, $b = d(C, A)$, $c = d(A, B)$.
Its angles $\alpha$, $\beta$, $\gamma$ at $A$, $B$, $C$ are the angles between the tangent vectors of the two sides at each vertex.

## Remarks

Example: in the [[Poincaré disk model|85MM2EA0TK]], take $A = 0$, $B = 1/2$ and $C = i/2$.
The only geodesic through $0$ and $1/2$ is the real diameter, which does not contain $i/2$, so $A, B, C$ span a hyperbolic triangle.
Its angle at $A$ is $\pi/2$, since the model is conformal and the sides at $A$ are perpendicular diameters.
Non-example: the points $0$, $1/4$, $1/2$ lie on the real diameter, which is one geodesic line, so they do not form a hyperbolic triangle.
In curvature $-1$, the angles satisfy $\alpha + \beta + \gamma < \pi$, and the area is $\pi - (\alpha + \beta + \gamma)$.
One also allows vertices at infinity, on the ideal boundary; a triangle with all three vertices ideal is an *ideal triangle*, with all angles $0$ and area $\pi$.
The notion is the hyperbolic counterpart of the Euclidean [[triangle|0CTNFGYMM2]].
