---
tag: CSMB49BDPT
kind: example
name: Projective geometry over a finite field
msc: ["51E20", "51E15", "05B25"]
instance_of: [ZT9A6JK8QF]
uses: [0ZXZ82FTX2, MCDZP31ZF3, 2HWB7P1DZN]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_space
---

## Example

Let $q$ be a prime power, let $\F_q$ be the [[finite field|0ZXZ82FTX2]] with $q$ elements, and let $n \ge 1$.
The projective space $PG(n, q)$ is the [[projective space|ZT9A6JK8QF]] of $V = \F_q^{n+1}$.
Its points are the $1$-dimensional subspaces of $V$, and its lines are the $2$-dimensional subspaces.
In general its $k$-dimensional subspaces are the $(k+1)$-dimensional subspaces of $V$, with incidence given by inclusion.

Count of points: $V$ has $q^{n+1} - 1$ nonzero vectors, and each $1$-dimensional subspace contains $q - 1$ of them, so $PG(n, q)$ has
$$\frac{q^{n+1} - 1}{q - 1} = q^n + q^{n-1} + \cdots + q + 1$$
points.
Each line has $(q^2 - 1)/(q - 1) = q + 1$ points.

Check for $PG(3, 2)$: it has $15$ points and each line has $3$ points.
Two distinct points span a unique line, so the number of lines is $\binom{15}{2} / \binom{3}{2} = 105 / 3 = 35$.
Its planes are the $3$-dimensional subspaces of $\F_2^4$, and there are $15$ of them, one for each nonzero linear form up to scaling.

For $n = 2$, the plane $PG(2, q)$ is a [[finite projective plane|2HWB7P1DZN]] of order $q$, and $PG(2, 2)$ is the Fano plane.

## Explanations

### L1 human

Take the usual recipe for projective space, lines through the origin of a vector space, and use a finite field in place of the real numbers.
The result is a projective space with finitely many points, one of the basic objects of [[finite geometry|MCDZP31ZF3]].
Every axiom of projective geometry still holds, and all counts become explicit formulas in $q$.
For $q = 2$ and $n = 2$ one gets the seven points and seven lines of the Fano plane.
