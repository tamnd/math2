---
tag: ZGSK8N6NKY
kind: definition
name: Trilateration
msc: [86A30, 51N20]
defines: 7WSH8Z6F7T
uses: [0NPPGHQNXQ, P9CM4GQ2T0]
sources:
  - url: https://en.wikipedia.org/wiki/True-range_multilateration
---

## Definition

Let $p_1, \dots, p_n$ be known points of $\R^3$ and let $r_1, \dots, r_n > 0$ be measured distances.
*Trilateration* is the determination of the points $x \in \R^3$ such that
$$\norm{x - p_i} = r_i \quad \text{for } i = 1, \dots, n,$$
where $\norm{\cdot}$ is the [[Euclidean distance|0NPPGHQNXQ]].
Each equation says that $x$ lies on the [[sphere|P9CM4GQ2T0]] of centre $p_i$ and radius $r_i$.

## Remarks

Example: $p_1 = (0,0,0)$, $p_2 = (2,0,0)$, $p_3 = (0,2,0)$ and $r_1 = r_2 = r_3 = \sqrt{3}$ give $x = (1, 1, \pm 1)$; indeed $\norm{(1,1,1) - (2,0,0)}^2 = 1 + 1 + 1 = 3$.
Non-example: with only $p_1$ and $p_2$, the solutions form a circle, so two distances do not determine $x$.
Subtracting the first equation from the others gives linear equations $2\ip{x}{p_1 - p_i} = r_i^2 - r_1^2 - \norm{p_i}^2 + \norm{p_1}^2$.
If $p_1, p_2, p_3$ are not collinear, there are at most two solutions, mirror images in the plane through $p_1, p_2, p_3$.
If $n \ge 4$ and the $p_i$ are not coplanar, the solution is unique when it exists.
With measurement errors, $x$ is found by least squares.
