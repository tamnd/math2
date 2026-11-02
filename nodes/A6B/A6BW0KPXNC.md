---
tag: A6BW0KPXNC
kind: definition
name: Directional statistics
msc: [62H11]
defines: 8GZJQBPBY0
uses: [T62369RFH6, 0Q5CG2NEQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Directional_statistics
---

## Definition

Let $p \ge 2$ and let $S^{p-1} = \set{x \in \R^p : \abs{x} = 1}$ be the unit [[sphere|T62369RFH6]].
*Directional statistics* is the statistics of data $x_1, \ldots, x_n$ with values in $S^{p-1}$.
More generally the data may lie in a compact manifold such as a rotation group.
For $p = 2$ it is called circular statistics.
Its basic [[statistics|0Q5CG2NEQ8]] come from the resultant vector $R = x_1 + \cdots + x_n$.

1. The *mean resultant length* is $\bar R = \abs{R}/n$, a number in $[0, 1]$.
2. If $R \ne 0$, the *mean direction* is $R / \abs{R} \in S^{p-1}$.
3. For $p = 2$, the *circular variance* is $1 - \bar R$.

## Remarks

Example: the angles $350°$ and $10°$ give the unit vectors $(\cos 10°, -\sin 10°)$ and $(\cos 10°, \sin 10°)$.
Their sum is $R = (2 \cos 10°, 0)$, so the mean direction is $0°$ and $\bar R = \cos 10° \approx 0.985$.
Non-example: for the angles $0°$ and $180°$, $R = 0$, so the mean direction is not defined; then $\bar R = 0$ and the circular variance is $1$.
The value $\bar R$ is close to $1$ when the directions are concentrated, and close to $0$ when they are spread out or balanced.
The mean direction is the point $m \in S^{p-1}$ that maximises $\sum_i m^T x_i$, so it does not depend on the choice of a zero angle.
