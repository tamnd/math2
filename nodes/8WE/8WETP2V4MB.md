---
tag: 8WETP2V4MB
kind: definition
name: Descriptive geometry
msc: [51N05]
defines: 4YDJDTV6B7
uses: [0XPR1E85W0, 0V3XAMF3C1, 0RWKYX8339, YHKSDF59HK]
sources:
  - url: https://en.wikipedia.org/wiki/Descriptive_geometry
---

## Definition

Let $E$ be Euclidean 3-space with [[Cartesian coordinates|0RWKYX8339]] $(x, y, z)$.
Let $\pi_1$ be the horizontal [[plane|0V3XAMF3C1]] $z = 0$ and $\pi_2$ the vertical plane $y = 0$; they meet in the ground line $x_{12}$, the $x$-axis.
The *Monge projection* of a point $P = (x, y, z)$ is the pair of its orthogonal projections, the top view $P' = (x, y, 0) \in \pi_1$ and the front view $P'' = (x, 0, z) \in \pi_2$.
Rotate $\pi_2$ about $x_{12}$ onto $\pi_1$, so that both views lie in one drawing plane.
Then $P'$ and $P''$ lie on a common line perpendicular to $x_{12}$.
*Descriptive geometry* is the study of figures of $E$ through such pairs of views, or through more views on further image planes.
Its aim is to solve spatial problems by plane constructions on the views.

## Remarks

The map $P \mapsto (P', P'')$ is injective, since the two views give $x$, $y$ and $z$.
So a pair of views on a common perpendicular to $x_{12}$ determines a unique point.
Example: for a segment $PQ$ the true length follows from the views, since $\abs{PQ}^2 = \abs{P'Q'}^2 + (z_P - z_Q)^2$, where $\abs{P'Q'}$ is measured in the top view and $z_P - z_Q$ in the front view.
For $P = (0, 0, 0)$ and $Q = (3, 4, 12)$, one gets $\abs{P'Q'} = 5$ and $\abs{PQ} = \sqrt{25 + 144} = 13$.
Non-example: a single view does not determine the point: the points $(1, 2, 0)$ and $(1, 2, 5)$ have the same top view.
The [[Euclidean space|0XPR1E85W0]] can also be shown by central projections, as in a [[perspective projection|YHKSDF59HK]].
