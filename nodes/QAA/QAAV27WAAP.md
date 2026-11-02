---
tag: QAAV27WAAP
kind: definition
name: Alexandrov space
msc: [53C23, 53C20]
defines: 71AWVBG6KH
uses: [0VKD1TP7F3, 0BY52JW6NK, 0FE2SB8WVJ, 1FAF2VNA4G]
sources:
  - url: https://en.wikipedia.org/wiki/Alexandrov_space
---

## Definition

Let $k$ be a real number.
Let $M_k$ and $D_k$ be the model surface of constant curvature $k$ and its diameter bound, as for [[CAT(k) spaces|1FAF2VNA4G]].
Let $(X, d)$ be a [[metric space|0VKD1TP7F3]].
The space $X$ is a *length space* if each distance $d(x, y)$ is the infimum of the lengths of continuous curves from $x$ to $y$.
Geodesic triangles and comparison triangles in $M_k$ are as for CAT($k$) spaces.

The space $X$ is an *Alexandrov space of curvature $\ge k$* if:

1. $X$ is a [[complete|0BY52JW6NK]], [[locally compact|0FE2SB8WVJ]] length space, and
2. each point of $X$ has a neighbourhood $U$ with the following property.
   Take any geodesic triangle in $U$ of perimeter less than $2 D_k$, any vertex $x$ and any point $p$ on the opposite side.
   Let $\bar x, \bar p$ be the comparison points in a comparison triangle in $M_k$.
   Then $d(x, p) \ge d_{M_k}(\bar x, \bar p)$.

Many authors also require $X$ to have finite Hausdorff dimension; that dimension is then an integer.

## Remarks

Example: a complete Riemannian manifold with [[sectional curvature|1X42JAA349]] $\ge k$ is an Alexandrov space of curvature $\ge k$, by [[Toponogov's theorem|KX0B3AWD5H]].
In particular $\R^n$ has curvature $\ge 0$; its triangles equal their comparison triangles.

Non-example: the hyperbolic plane of curvature $-1$ does not have curvature $\ge 0$.
Take a geodesic triangle in it and the midpoint of one side.
The distance from the opposite vertex to this midpoint is strictly less than in the flat comparison triangle, so clause 2 fails for $k = 0$.

For an integer $m \ge 2$, let $C_m$ be the quotient of $\R^2$ by the group of rotations about $0$ through multiples of $2\pi/m$.
This cone is an Alexandrov space of curvature $\ge 0$, and it is not a smooth Riemannian manifold at its tip.
