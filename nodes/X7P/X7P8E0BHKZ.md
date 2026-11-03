---
tag: X7P8E0BHKZ
kind: definition
name: Great-circle distance
msc: [51M09, 86A30]
defines: 5K7ZVAQM4A
uses: [P9CM4GQ2T0, SQ9RQVANMG]
sources:
  - url: https://en.wikipedia.org/wiki/Great-circle_distance
---

## Definition

Let $S$ be the [[sphere|P9CM4GQ2T0]] of radius $r > 0$ centred at the origin $O$ of $\R^3$.
Let $P$ and $Q$ be points of $S$, and let $\theta \in [0, \pi]$ be the angle between the vectors $\vec{OP}$ and $\vec{OQ}$.
The *great-circle distance* between $P$ and $Q$ is $d(P, Q) = r\theta$.
If $P$ and $Q$ have latitudes $\varphi_1, \varphi_2$ and longitudes $\lambda_1, \lambda_2$, then
$$\cos\theta = \sin\varphi_1 \sin\varphi_2 + \cos\varphi_1 \cos\varphi_2 \cos(\lambda_2 - \lambda_1).$$

## Remarks

Example: on the unit sphere, the North Pole $(0, 0, 1)$ and the point $(1, 0, 0)$ give $\cos\theta = 0$, so $d = \pi/2$; the formula agrees, with $\varphi_1 = \pi/2$ and $\varphi_2 = 0$.
Non-example: the chord length $\abs{PQ} = 2r\sin(\theta/2)$ is the straight-line distance through the sphere, not the great-circle distance; for antipodal points it is $2r$, while $d = \pi r$.
The great-circle distance is the length of the shortest curve on $S$ from $P$ to $Q$, and it is the metric of [[spherical geometry|SQ9RQVANMG]].
For small $\theta$ the arccosine formula loses accuracy, and the [[haversine formula|AQADG9N8EV]] is used instead.
