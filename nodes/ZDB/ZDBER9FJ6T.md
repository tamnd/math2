---
tag: ZDBER9FJ6T
kind: statement
role: theorem
name: Ehrhart–Macdonald reciprocity
msc: [52B20, 11P21, 05A15]
uses: [F39N9NBFPZ, 9DEG0WRDHR]
about: [9DEG0WRDHR]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrhart_polynomial
---

## Statement

Let $P \subseteq \R^n$ be a [[lattice polytope|F39N9NBFPZ]] of dimension $d$, and let $E_P$ be its [[Ehrhart polynomial|9DEG0WRDHR]].
Let $P^\circ$ be the relative interior of $P$, that is, its interior inside its affine hull.
Then for every integer $t \ge 1$,
$$E_P(-t) = (-1)^d \, \#\left(t P^\circ \cap \Z^n\right).$$

## Remarks

One proof triangulates $P$ into lattice simplices and writes $P$ and $P^\circ$ as disjoint unions of half-open simplices.
For a single simplex, the integer points of all dilates are counted with a rational generating function over the cone above the simplex.
The generating functions of a cone and of its interior are related by $z \mapsto 1/z$, and this symmetry gives the sign $(-1)^d$ and the change from $P$ to $P^\circ$.

Example: for $P = [0,1]^2$, $E_P(t) = (t+1)^2$, so $E_P(-t) = (t-1)^2$.
The open square $(0,t)^2$ contains exactly the integer points $(a,b)$ with $1 \le a, b \le t-1$, and there are $(t-1)^2$ of them.
For the triangle with vertices $(0,0)$, $(1,0)$, $(0,1)$, $E_P(-t) = (t-1)(t-2)/2$, which counts the integer points with $a, b \ge 1$ and $a + b \le t - 1$.

Taking $t = 1$ gives the number of interior lattice points of $P$ as $(-1)^d E_P(-1)$.
The statement extends to rational polytopes, where $E_P$ is replaced by the Ehrhart quasi-polynomial.

## Explanations

### L1 human

The Ehrhart polynomial counts grid points in a blown-up polytope, boundary included.
Plugging negative numbers into the same polynomial counts the grid points strictly inside, up to a sign.
So one formula knows both the closed count and the open count.

### L2 human

Reciprocity says that the Ehrhart polynomials of $P$ and of $P^\circ$ are tied by $t \mapsto -t$.
It is one instance of a family of combinatorial reciprocity laws, which also includes reciprocity for order polynomials and for chromatic polynomials.
Together with $E_P(0) = 1$ and the leading coefficient being the volume, it constrains the coefficients of $E_P$.
For example, a lattice polygon $P$ with area $A$ and $b$ lattice points on its boundary has $E_P(t) = A t^2 + \frac{b}{2} t + 1$.
Reciprocity at $t = 1$ then gives $A - \frac{b}{2} + 1$ interior lattice points, which is Pick's theorem.
