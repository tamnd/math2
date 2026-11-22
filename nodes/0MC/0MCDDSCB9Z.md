---
tag: 0MCDDSCB9Z
kind: statement
role: theorem
name: Best approximation theorem
msc: [46C05, 41A50, 65F20]
topics: [8GQVME4SZZ]
audience: ug1
about: [0B8KZRT28M]
uses: [0Q8HZTJC7G, 0KG4D8AP6G, 079D68S3AW]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_projection_theorem
    locator: Finite dimensional case
  - book: isbn:9780321982384
    locator: Section 6.3
  - book: isbn:9783031410253
    locator: Section 6C
---

## Statement

The point of a subspace that lies closest to a given vector is the orthogonal projection of the vector, and no other point of the subspace is as close.

Let $V$ be an inner product space over $\R$ or $\C$, with [[norm|0KG4D8AP6G]] $\norm{x} = \sqrt{\ip{x}{x}}$.
Let $U$ be a finite-dimensional subspace of $V$, let $P_U$ be the [[orthogonal projection|0Q8HZTJC7G]] onto $U$, and let $v \in V$.
Then the following hold.

1. Existence: $\norm{v - P_U v} \le \norm{v - u}$ for every $u \in U$.
2. Uniqueness: equality in part 1 holds only for $u = P_U v$, so $P_U v$ is the unique point of $U$ closest to $v$.
3. Characterization: a vector $u_0 \in U$ is the closest point to $v$ if and only if $v - u_0$ lies in the [[orthogonal complement|079D68S3AW]] $U^\perp$.
4. Distance: the distance $d(v, U) = \min_{u \in U} \norm{v - u}$ equals $\norm{v - P_U v}$, and $d(v, U)^2 = \norm{v}^2 - \norm{P_U v}^2$; for an orthonormal basis $e_1, \dots, e_k$ of $U$ this is $d(v, U)^2 = \norm{v}^2 - \sum_{i=1}^{k} \abs{\ip{v}{e_i}}^2$.

The [[proof|6RSYZNC0V8]] splits $v - u$ into two orthogonal pieces and uses the Pythagorean theorem.

## Remarks

### Why each hypothesis is needed

The set $U$ must be a subspace, or at least convex, for the closest point to be unique.
On the unit circle in $\R^2$, every point is at distance $1$ from the origin, so the origin has infinitely many closest points on the circle.

The subspace must be finite-dimensional, or closed in a complete space, for a closest point to exist.
In the Hilbert space $\ell^2$ of square-summable sequences, take the subspace $c_{00}$ of finitely supported sequences and $y = (1, \frac{1}{2}, \frac{1}{3}, \dots)$.
Cutting $y$ off after $N$ terms gives points of $c_{00}$ at distance $\bigl(\sum_{n > N} \frac{1}{n^2}\bigr)^{1/2}$, which tends to $0$.
So $d(y, c_{00}) = 0$, but $y \notin c_{00}$, and no point attains the distance; [[the counterexample in l2|DNZF0R4VMZ]] studies this subspace.

The norm must come from an inner product.
For the maximum norm $\norm{(x_1, x_2)}_\infty = \max(\abs{x_1}, \abs{x_2})$ on $\R^2$, each point $(t, 0)$ with $0 \le t \le 2$ has
$$\norm{(1, 1) - (t, 0)}_\infty = \max(\abs{1 - t}, 1) = 1,$$
so the $x$-axis has a whole segment of closest points to $(1, 1)$.

### What it gives you

Part 3 turns a minimization into linear equations, and that is how the theorem is used.
For the column space of a matrix $A$, the condition $b - Ax \perp \operatorname{Col}(A)$ reads $A^{\mathsf{T}}(b - Ax) = 0$, which gives the normal equations of [[least squares|0BYTQ4X1HC]].
Part 4 gives [[Bessel's inequality|0RBT5PB74K]] at once, since $d(v, U)^2 \ge 0$ means $\sum_i \abs{\ip{v}{e_i}}^2 \le \norm{v}^2$.
In a space of functions, part 4 computes the mean-square error of the best polynomial or trigonometric approximation, as [[the polynomial and Fourier example|899D63WW04]] shows.

### Two ways to see the closest point

Part 1 describes $P_U v$ by a property that involves every point of $U$, and it cannot be checked directly.
Part 3 describes the same point by finitely many equations: $v - u_0$ must be orthogonal to each vector of a basis of $U$.
So the geometric problem "find the nearest point" and the algebraic problem "make the error perpendicular" have the same answer.

### Generalizations

The [[Hilbert projection theorem|J5YNTHQMFX]] gives a unique closest point in every nonempty closed convex subset of a Hilbert space, and for a closed subspace that point is again characterized by part 3.
The wider study of closest points from a fixed family, in norms that need not come from an inner product, is the subject of [[best approximation|7N4988HN3P]] in approximation theory.

## Explanations

### L1 human

The nearest point of a flat floor to a lamp on the ceiling is the spot straight below it.
Any other spot on the floor is farther away, because the lamp, the spot below and the other spot form a right triangle, and the slanted side is the longest side.
For example, a lamp $3$ meters above the floor is $5$ meters from a spot $4$ meters to the side of the point below it.

### L2 human

How far is $v = (1, 2, 3)$ from the plane $U$ spanned by $(1, 1, 0)$ and $(0, 1, 1)$?
[[The projection onto a plane|8YDFZV8S5W]] gives $P_U v = \frac{1}{3}(1, 8, 7)$, so the error and the distance are
$$v - P_U v = \tfrac{1}{3}(2, -2, 2), \qquad d(v, U) = \sqrt{\tfrac{4 + 4 + 4}{9}} = \frac{2}{\sqrt{3}}.$$
Part 4 gives a check that needs no subtraction of vectors, since $\norm{v}^2 = 14$ and $\norm{P_U v}^2 = \frac{1 + 64 + 49}{9} = \frac{114}{9}$:
$$14 - \frac{114}{9} = \frac{126 - 114}{9} = \frac{4}{3} = \left( \frac{2}{\sqrt{3}} \right)^2.$$
Another point of the plane, such as $u = (1, 2, 1) = (1, 1, 0) + (0, 1, 1)$, is farther away: $\norm{v - u}^2 = 0 + 0 + 4 = 4 > \frac{4}{3}$.
Watch out: the sum in part 4 needs an orthonormal basis, and the two spanning vectors above are neither orthogonal nor of length $1$.

### L3 human

Part 3 is the first-order condition for minimizing the convex function $u \mapsto \norm{v - u}^2$ on $U$.
Its derivative at $u$ in a direction $h \in U$ is $-2 \operatorname{Re} \ip{v - u}{h}$, and setting it to zero for every $h$ gives $v - u \perp U$.
In $L^2$, the theorem is the principle of least mean-square error behind Fourier analysis and linear estimation in statistics.
In a normed space without an inner product, closest points can fail to be unique, and the map to the closest point need not be linear; the inner product is what makes the problem linear.
