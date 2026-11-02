---
tag: 5DYYRZWER6
kind: example
name: Cross-polytope
msc: [52B12, 52B11, 51M20]
instance_of: [300K6CB1KH, YVJ15PGKDM]
uses: [R7V3S9V891, DPDXN2FJC4, P9PYM71GMM, 6DXF1T506B]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-polytope
same_as:
  wikidata: Q1187914
  wikipedia: Cross-polytope
---

## Example

For $d \ge 1$, let $e_1, \dots, e_d$ be the standard basis of $\R^d$.
The $d$-dimensional *cross-polytope* is
$$X_d = \operatorname{conv}\set{\pm e_1, \dots, \pm e_d} = \set{x \in \R^d : \abs{x_1} + \cdots + \abs{x_d} \le 1}.$$
It is a [[convex polytope|300K6CB1KH]] with the $2d$ [[vertices|R7V3S9V891]] $\pm e_i$.

A set of vertices spans a proper face exactly when it contains no pair $e_i, -e_i$.
Indeed, for signs $\epsilon_i \in \set{1, -1}$ the vector $c = (\epsilon_1, \dots, \epsilon_d)$ gives $c \cdot x \le 1$ on $X_d$, with equality on the hull of $\epsilon_1 e_1, \dots, \epsilon_d e_d$.
So the [[facets|DPDXN2FJC4]] are the $2^d$ simplices $\operatorname{conv}\set{\epsilon_1 e_1, \dots, \epsilon_d e_d}$, and $X_d$ is a [[simplicial polytope|YVJ15PGKDM]].
Choosing $k + 1$ of the $d$ axes and a sign for each gives the number of $k$-faces:
$$f_k(X_d) = 2^{k+1} \binom{d}{k+1}, \qquad 0 \le k \le d-1.$$

## Remarks

For $d = 2$ the cross-polytope is a square turned by $45$ degrees, and for $d = 3$ it is the regular octahedron.
It is the [[polar polytope|6DXF1T506B]] of the [[hypercube|P9PYM71GMM]] $[-1,1]^d$: a vector $y$ satisfies $x \cdot y \le 1$ for all $x \in [-1,1]^d$ exactly when $\abs{y_1} + \cdots + \abs{y_d} \le 1$.
Its unit ball description shows that it is the unit ball of the $\ell^1$ norm.

## Explanations

### L1 human

Put a point at distance one on each side of the origin along every axis, and wrap a skin around these points.
In the plane you get a diamond, in space an octahedron.
The cross-polytope is the same shape in any dimension.
Its faces are all triangles or their higher versions, simplices, which makes it the dual of the cube.
