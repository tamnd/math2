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

Let $V$ be an inner product space over $\R$ or $\C$, with [[norm|0KG4D8AP6G]] $\norm{x} = \sqrt{\ip{x}{x}}$.
Let $U$ be a finite-dimensional subspace of $V$, let $P_U$ be the [[orthogonal projection|0Q8HZTJC7G]] onto $U$, and let $v \in V$.
Then:

1. Existence: $\norm{v - P_U v} \le \norm{v - u}$ for every $u \in U$.
2. Uniqueness: equality in part 1 holds only for $u = P_U v$. So $P_U v$ is the unique point of $U$ closest to $v$.
3. Characterization: a vector $u_0 \in U$ is the closest point to $v$ if and only if $v - u_0$ lies in the [[orthogonal complement|079D68S3AW]] $U^\perp$.
4. Distance: the distance $d(v, U) = \min_{u \in U} \norm{v - u}$ is $\norm{v - P_U v}$, and $d(v, U)^2 = \norm{v}^2 - \norm{P_U v}^2$. For an orthonormal basis $e_1, \dots, e_k$ of $U$, $d(v, U)^2 = \norm{v}^2 - \sum_{i=1}^{k} \abs{\ip{v}{e_i}}^2$.

The [[proof|6RSYZNC0V8]] uses the Pythagorean theorem.

## Remarks

### Why each hypothesis is needed

- Subspace: for a set that is not convex, a closest point need not be unique. On the unit circle in $\R^2$, every point is at distance $1$ from the origin.
- Finite dimension of $U$: in $\ell^2$, take the subspace $c_{00}$ of finitely supported sequences and $y = (1, 1/2, 1/3, \dots)$. The distance $d(y, c_{00})$ is $0$, by the truncation in [[the counterexample in l2|~52588f49]], but $y \notin c_{00}$, so no point of $c_{00}$ attains it.
- Inner product norm: for the norm $\norm{(x_1, x_2)}_\infty = \max(\abs{x_1}, \abs{x_2})$ on $\R^2$, the points $(t, 0)$ with $0 \le t \le 2$ are all at distance $1$ from $(1, 1)$. So the closest point of the $x$-axis is not unique.

### Consequences

- The method of [[least squares|0BYTQ4X1HC]] is part 1 for the column space of a matrix.
- [[Bessel's inequality|0RBT5PB74K]] follows from part 4, since $d(v, U)^2 \ge 0$.
- In a space of functions, part 4 computes the mean-square error of the best polynomial or trigonometric approximation; see [[the polynomial and Fourier example|~5c06ec2d]].

### Converse

Part 3 is a converse of the definition: the orthogonality condition alone determines the closest point.
In computations one uses part 3, because it gives linear equations, while part 1 is a minimization.

### Generalizations

The [[Hilbert projection theorem|J5YNTHQMFX]] proves existence and uniqueness of a closest point in every nonempty closed convex subset of a Hilbert space.
The broader study of closest points is [[best approximation|7N4988HN3P]] in approximation theory.

## Explanations

### L1 human

The nearest point of a subspace to a given vector is the foot of the perpendicular.
Every other point of the subspace is farther away, by the Pythagorean theorem.
This turns problems of best approximation into problems of projection.

### L2 human

We find the distance from $v = (1, 2, 3)$ to the plane $U$ spanned by $(1, 1, 0)$ and $(0, 1, 1)$.

1. By [[the projection onto a plane|~33fbc74c]], $P_U v = (1/3, 8/3, 7/3)$.
2. So $v - P_U v = (2/3, -2/3, 2/3)$, and $d(v, U) = \sqrt{3 \cdot 4/9} = 2/\sqrt{3}$.
3. Check with part 4: $\norm{v}^2 = 14$ and $\norm{P_U v}^2 = (1 + 64 + 49)/9 = 114/9$. Then $14 - 114/9 = 12/9 = 4/3$, and $\sqrt{4/3} = 2/\sqrt{3}$.
4. Check with another point of $U$, say $u = (1, 2, 1)$: $\norm{v - u}^2 = 0 + 0 + 4 = 4 > 4/3$.

The typical use is to find the best approximation of data or of a function from a fixed family.
The trap is to apply part 4 with a basis that is not orthonormal.

### L3 human

Part 3 is the first-order condition for minimizing the convex function $u \mapsto \norm{v - u}^2$ on $U$: its derivative in the direction $h \in U$ is $-2 \operatorname{Re} \ip{v - u}{h}$.
For the norm of $L^2$, part 1 is the principle of least mean-square error, the basis of Fourier analysis and of linear estimation in statistics.
In a Banach space without an inner product, closest points can fail to exist or to be unique; the inner product makes the problem linear.
