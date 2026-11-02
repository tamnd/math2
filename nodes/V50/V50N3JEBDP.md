---
tag: V50N3JEBDP
kind: definition
name: Cayley–Klein metric
msc: [51F99, 51M10]
defines: J7ZE3EGRYX
uses: [ZT9A6JK8QF, Q3Q4FF23VG, 09ASMRMD67]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Klein_metric
---

## Definition

Let $n \ge 1$ and let $Q$ be a nondegenerate [[quadric|Q3Q4FF23VG]] in the real [[projective space|ZT9A6JK8QF]] $\mathbb{P}^n$, called the *absolute*.
Let $c$ be a nonzero real or imaginary constant.
Let $x$ and $y$ be two distinct points not on $Q$ such that the line $xy$ is not tangent to $Q$.
Let $a$ and $b$ be the two points where the line $xy$ meets $Q$, taken in the complexification when they are not real.
The *Cayley–Klein distance* of $x$ and $y$ is
$$d(x, y) = c \log (x, y; a, b),$$
where $(x, y; a, b)$ is the [[cross-ratio|09ASMRMD67]] of the four points on the line.
Also $d(x, x) = 0$.

## Remarks

Hyperbolic case: let $Q$ be an ellipsoid and let $x$ and $y$ lie inside it.
Then $a$ and $b$ are real.
In an affine chart with the points in the order $a, x, y, b$ on the line, take $c = \frac{1}{2}$ and the cross-ratio $\frac{\abs{xb} \, \abs{ya}}{\abs{xa} \, \abs{yb}}$.
This ratio is greater than $1$, so $d(x, y) > 0$, and $d(x, y) \to \infty$ as $y$ tends to $b$.
This is the [[Beltrami–Klein model|1WN9B18H86]] of hyperbolic space with curvature $-1$.

Elliptic case: if $Q$ has no real points, such as $x_0^2 + x_1^2 + x_2^2 = 0$, then $a$ and $b$ are complex conjugate, and an imaginary constant $c$ gives the real distance of [[elliptic geometry|H5GB19W2H3]].

Non-example: a degenerate quadric, such as a double plane, does not fit the definition, because a line meets it in one point only.
Euclidean geometry appears only as a limit of the nondegenerate cases.

Conventions for the order in the cross-ratio differ between sources; they change the sign of the logarithm, not the geometry.
