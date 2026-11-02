---
tag: TM5SYH4XHY
kind: statement
role: theorem
name: Löwner–John theorem
msc: [52A27, 52A40, 52A20]
uses: [437FSG3419, 0VD9ZSWWJG, 2Z2QVWZ262]
about: [WNHXE7FCG4]
sources:
  - url: https://en.wikipedia.org/wiki/John_ellipsoid
---

## Statement

Let $n \ge 1$ and let $K \subseteq \R^n$ be a compact [[convex body|437FSG3419]] with nonempty interior.
An ellipsoid is a set $c + AB$, with $B$ the closed unit ball, $c \in \R^n$ and $A$ an invertible real $n \times n$ [[matrix|0VD9ZSWWJG]]; volume means [[Lebesgue measure|2Z2QVWZ262]].

1. Among the ellipsoids contained in $K$ there is exactly one, $E = c + AB$, of maximal volume.
2. For this $E$, one has $K \subseteq c + nAB$.
3. If moreover $K = -K$, then $c = 0$ and $K \subseteq \sqrt{n}\, E$.
4. Among the ellipsoids containing $K$ there is exactly one of minimal volume.

## Remarks

One may take $A$ symmetric positive definite, by the polar decomposition.
Existence follows from compactness: the pairs $(c, A)$ with $A$ positive semidefinite and $c + AB \subseteq K$ form a compact set, and volume is continuous.
For uniqueness, let $c_1 + A_1 B$ and $c_2 + A_2 B$, with $A_i$ positive definite, both have maximal volume.
Then $\frac{c_1 + c_2}{2} + \frac{A_1 + A_2}{2} B$ also lies in $K$.
Its volume is strictly larger unless $A_1 = A_2$, by the strict log-concavity of the determinant on positive definite matrices.
If $A_1 = A_2$ but $c_1 \neq c_2$, the convex hull of the two ellipsoids contains a larger ellipsoid, stretched in the direction $c_2 - c_1$.
John characterized the case $E = B$ by contact points.
For $K \supseteq B$, the ball $B$ is the maximal ellipsoid if and only if there are $u_1, \dots, u_m \in \partial K$ with $\abs{u_i} = 1$ and weights $c_i > 0$ such that $\sum_i c_i u_i = 0$ and $\sum_i c_i u_i u_i^T = I_n$.
The bounds in 2 and 3 follow from this.
The factor $n$ in 2 is attained by a regular simplex.
The factor $\sqrt{n}$ in 3 is attained by the cube $[-1, 1]^n$, whose maximal ellipsoid is $B$ and which contains the point $(1, \dots, 1)$ of norm $\sqrt{n}$.

## Explanations

### L1 human

Every convex shape with some thickness contains a largest ellipsoid, and it is unique.
The shape is then caught between this ellipsoid and the same ellipsoid enlarged by a factor equal to the dimension.
For shapes that are symmetric about a center, the factor improves to the square root of the dimension.
So, after a linear change of coordinates, every convex body looks like a ball up to a bounded distortion.

### L2 human

Part 3 says that every $n$-dimensional normed space is at [[Banach–Mazur distance|ZJKSYYASPT]] at most $\sqrt{n}$ from Euclidean space, a basic fact of the local theory of Banach spaces.
The contact point condition in John's characterization is a decomposition of the identity.
Ball combined it with the Brascamp–Lieb inequality to prove his reverse isoperimetric inequality.
In optimization, rounding algorithms for convex bodies compute approximate John ellipsoids.
