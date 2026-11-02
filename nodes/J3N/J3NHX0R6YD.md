---
tag: J3NHX0R6YD
kind: definition
name: Involute
msc: [53A04]
defines: E1PC4TZK5C
uses: [00R1JDDV5X, 0D98771SM0, 06JMR2XWXW, Y3ZNV24V2C]
sources:
  - url: https://en.wikipedia.org/wiki/Involute
---

## Definition

Let $\gamma \colon I \to \R^n$ be a [[regular|06JMR2XWXW]] curve of class $C^2$, parametrised by [[arc length|00R1JDDV5X]] $s$ on an interval $I$, and let $c \in \R$.
The *involute* of $\gamma$ with parameter $c$ is the curve
$$J(s) = \gamma(s) + (c - s) \, \gamma'(s), \qquad s \in I.$$
Here $\gamma'(s)$ is the unit [[tangent vector|0D98771SM0]], so $J(s)$ lies on the tangent line at $\gamma(s)$, at distance $\abs{c - s}$ from $\gamma(s)$.

## Remarks

Example: for the unit circle $\gamma(s) = (\cos s, \sin s)$ and $c = 0$, one gets $J(s) = (\cos s + s \sin s, \sin s - s \cos s)$.
Check: $J'(s) = (s \cos s, s \sin s)$, which is orthogonal to $\gamma'(s) = (-\sin s, \cos s)$.
In general $J'(s) = (c - s) \gamma''(s)$, so $J$ meets each tangent line of $\gamma$ at a right angle, and $J$ is singular at $s = c$.
Non-example: the circle of radius $2$ about the origin is not an involute of the unit circle.
Indeed, it meets each tangent line of the unit circle at an angle that is not a right angle.
For a plane curve with nonzero curvature, the [[evolute|Y3ZNV24V2C]] of each involute is the original curve, on the part where $s \ne c$.
