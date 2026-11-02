---
tag: YC9E5JJDDF
kind: definition
name: Evolute
msc: [53A04]
defines: Y3ZNV24V2C
uses: [NWSFMCRWHJ, 7JQS6VKFEZ, 06JMR2XWXW]
sources:
  - url: https://en.wikipedia.org/wiki/Evolute
---

## Definition

Let $\gamma \colon I \to \R^2$ be a [[regular|06JMR2XWXW]] curve of class $C^2$ on an interval $I$.
Let $N(t)$ be its unit tangent rotated by a right angle counterclockwise, and let $k(t)$ be its signed [[curvature|7JQS6VKFEZ]].
Assume that $k(t) \ne 0$ for all $t \in I$.
The *evolute* of $\gamma$ is the curve
$$E(t) = \gamma(t) + \frac{1}{k(t)} N(t), \qquad t \in I.$$
So $E(t)$ is the centre of the [[osculating circle|NWSFMCRWHJ]] of $\gamma$ at $t$.

## Remarks

Example: for $\gamma(t) = (t, t^2)$, one has $k(t) = 2 (1 + 4t^2)^{-3/2}$ and $N(t) = (-2t, 1) / \sqrt{1 + 4t^2}$.
Then $E(t) = (-4t^3, 1/2 + 3t^2)$, so the evolute is the semicubical parabola $27 x^2 = 16 (y - 1/2)^3$.
Non-example: for $\gamma(t) = (t, t^3)$ on $\R$, the curvature vanishes at $t = 0$, so the evolute is not defined on the whole interval; near $t = 0$ the centres of curvature go off to infinity.
The evolute of a circle of radius $r$ is the constant curve at its centre.
If $\gamma$ is of class $C^3$, then $E'(t)$ is parallel to $N(t)$, and $E'(t) = 0$ exactly where $k'(t) = 0$, that is, at the vertices of $\gamma$.
