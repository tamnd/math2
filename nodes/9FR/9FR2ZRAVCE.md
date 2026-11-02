---
tag: 9FR2ZRAVCE
kind: definition
name: Spherical trigonometry
msc: [51M09, 51M10]
defines: SXQGHWHFRF
uses: [SQ9RQVANMG, T62369RFH6, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_trigonometry
---

## Definition

Let $S^2 \subset \R^3$ be the unit [[sphere|T62369RFH6]] with the great circles as lines, as in [[spherical geometry|SQ9RQVANMG]].
Let $A$, $B$, $C \in S^2$ be linearly independent vectors of $\R^3$.
The *spherical triangle* $ABC$ is the region of $S^2$ bounded by the three shorter great-circle arcs $BC$, $CA$, $AB$.
Its sides are the arc lengths $a = \arccos(B \cdot C)$, $b = \arccos(C \cdot A)$, $c = \arccos(A \cdot B)$, each in $(0, \pi)$.
Its angle $\gamma$ at $C$ is the angle between the planes of the arcs $CA$ and $CB$, measured inside the triangle.
The angles $\alpha$ at $A$ and $\beta$ at $B$ are defined in the same way.
*Spherical trigonometry* is the study of the relations among these six quantities $a, b, c, \alpha, \beta, \gamma$.

## Remarks

Example: for $A = (1, 0, 0)$, $B = (0, 1, 0)$, $C = (0, 0, 1)$, all sides and all angles equal $\pi/2$.
The spherical law of cosines $\cos c = \cos a \cos b + \sin a \sin b \cos \gamma$ checks: both sides are $0$.
Non-example: the vectors $A = (1, 0, 0)$, $B = (-1, 0, 0)$ and $C = (0, 0, 1)$ are linearly dependent.
The points $A$ and $B$ are antipodal, there is no unique shorter arc $AB$, and $A, B, C$ do not form a spherical triangle.
The standard relations are the law of cosines for sides above, the law of cosines for angles $\cos \gamma = -\cos \alpha \cos \beta + \sin \alpha \sin \beta \cos c$, and the law of sines $\dfrac{\sin a}{\sin \alpha} = \dfrac{\sin b}{\sin \beta} = \dfrac{\sin c}{\sin \gamma}$.
On a sphere of radius $R$, the sides are the arc lengths divided by $R$.
