---
tag: ABE41ZYD78
kind: definition
name: Lie sphere geometry
msc: [51B25, 51B10]
defines: TFQSF9RA1G
uses: [0SQZMXB6GP, ZT9A6JK8QF, Q3Q4FF23VG, P9CM4GQ2T0]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_sphere_geometry
---

## Definition

Let $n \ge 1$ and give $\R^{n+3}$, with coordinates $(x_1, \ldots, x_{n+3})$, the symmetric [[bilinear form|0SQZMXB6GP]] of signature $(n+1, 2)$
$$\ip{x, y} = -x_1 y_1 + x_2 y_2 + \cdots + x_{n+2} y_{n+2} - x_{n+3} y_{n+3}.$$
The *Lie quadric* is the [[quadric|Q3Q4FF23VG]] $Q = \set{[x] \in \mathbb{RP}^{n+2} : \ip{x, x} = 0}$ in the [[projective space|ZT9A6JK8QF]] $\mathbb{RP}^{n+2}$.
The points of $Q$ correspond bijectively to the following objects of $\R^n$:

1. the oriented [[sphere|P9CM4GQ2T0]] with centre $p \in \R^n$ and signed radius $r \ne 0$, and the point $p$ for $r = 0$, to $\bigl[ \tfrac{1 + \abs{p}^2 - r^2}{2}, \tfrac{1 - \abs{p}^2 + r^2}{2}, p, r \bigr]$;
2. the oriented hyperplane $\set{x : x \cdot N = h}$ with unit normal $N$ and $h \in \R$, to $[h, -h, N, 1]$;
3. the point at infinity, to $[1, -1, 0, 0]$.

Two such objects are in *oriented contact* when their points $[x], [y] \in Q$ satisfy $\ip{x, y} = 0$.
A *Lie sphere transformation* is a projective transformation of $\mathbb{RP}^{n+2}$ that maps $Q$ onto itself.
*Lie sphere geometry* is the study of the properties of these objects that are invariant under Lie sphere transformations.

## Remarks

For two oriented spheres with centres $p_1, p_2$ and signed radii $r_1, r_2$, let $k_1, k_2$ be their vectors as in clause 1; a computation gives
$$\ip{k_1, k_2} = -\tfrac{1}{2} \bigl( \abs{p_1 - p_2}^2 - (r_1 - r_2)^2 \bigr).$$
So they are in oriented contact exactly when $\abs{p_1 - p_2} = \abs{r_1 - r_2}$, that is when they are tangent with matching orientations at the point of contact.
Example: in $\R^2$, take the circle with centre $(0, 0)$ and radius $2$ and the circle with centre $(1, 0)$ and radius $1$.
They have $\abs{p_1 - p_2} = 1 = \abs{2 - 1}$, so they are in oriented contact; indeed they touch at $(2, 0)$.
Non-example: the circles of radius $1$ with centres $(0, 0)$ and $(1, 0)$ have $\abs{p_1 - p_2} = 1 \ne 0 = \abs{r_1 - r_2}$; they cross at two points and are not in oriented contact.
A point ($r = 0$) is in oriented contact with a sphere exactly when it lies on it, and every hyperplane is in oriented contact with the point at infinity.
The group of Lie sphere transformations is $O(n+1, 2) / \set{\pm 1}$.
The Möbius transformations of $\R^n \cup \set{\infty}$ are the Lie sphere transformations that map points to points.
