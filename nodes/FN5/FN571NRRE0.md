---
tag: FN571NRRE0
kind: definition
name: Second moment of area
msc: [74K10, 26B15]
defines: 1QCSARFXQ0
uses: [0X7EEWES5G]
sources:
  - url: https://en.wikipedia.org/wiki/Second_moment_of_area
---

## Definition

Let $A \subset \R^2$ be a bounded measurable region in the $(y, z)$-plane.
The *second moments of area* of $A$ about the $z$-axis and the $y$-axis are
$$I_z = \int_A y^2 \, dA, \qquad I_y = \int_A z^2 \, dA.$$
The *product moment of area* is $I_{yz} = \int_A y z \, dA$, and the *polar moment of area* about the origin is $J = \int_A (y^2 + z^2) \, dA = I_y + I_z$.
In beam theory the axes pass through the [[centroid|0X7EEWES5G]] of the cross-section.

## Remarks

Example: for the rectangle $\abs{y} \le h/2$, $\abs{z} \le b/2$, the moment about the centroidal $z$-axis is $I_z = \int_{-h/2}^{h/2} y^2 b \, dy = bh^3/12$.
For a disc of radius $R$ centred at the origin, $I_y = I_z = \pi R^4/4$ and $J = \pi R^4/2$.

Non-example: the integral $\int_A y \, dA$ is the first moment of area; it is $0$ about a centroidal axis, so it does not measure resistance to bending.

Let $I_c$ be the moment about a centroidal axis and $\abs{A}$ the area.
The parallel axis theorem gives $I = I_c + d^2 \abs{A}$ for a parallel axis at distance $d$.
The symbol $I$ is used both for this quantity and for the mass [[moment of inertia|08ANASGBXV]], which has the mass density in the integral.
