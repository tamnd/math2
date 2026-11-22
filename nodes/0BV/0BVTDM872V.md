---
tag: 0BVTDM872V
kind: statement
role: theorem
name: Pythagorean theorem in an inner product space
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0Y2X7P2WB7, 0MFJJV97RJ]
uses: [0TS7VZJBWD, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: Inner product spaces
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

For orthogonal vectors, the squared length of the sum is the sum of the squared lengths; over $\mathbb{R}$ the converse holds, and over $\mathbb{C}$ it fails.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.

1. If $x, y \in V$ are [[orthogonal|0TS7VZJBWD]], then $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$.
2. If $x_1, \dots, x_k \in V$ are pairwise orthogonal, then $\norm{x_1 + \dots + x_k}^2 = \norm{x_1}^2 + \dots + \norm{x_k}^2$.
3. For all $x, y \in V$, the identity $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ holds if and only if $\operatorname{Re}\ip{x}{y} = 0$.
4. If $\mathbb{K} = \mathbb{R}$, the converse of part 1 holds: the identity $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ implies $x \perp y$.
5. If $\mathbb{K} = \mathbb{C}$, the converse of part 1 fails: in $\mathbb{C}$ with $\ip{z}{w} = z\overline{w}$, the vectors $x = 1$ and $y = i$ satisfy the identity, but $\ip{x}{y} = -i$.

The [[proof|794QRK467A]] expands $\norm{x + y}^2$.

## Remarks

### The law of cosines behind it

Every part comes from one expansion, valid for all $x$ and $y$:
$$\norm{x + y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2.$$
It is the law of cosines of an inner product space, and the theorem reads off what happens when the middle term vanishes.
Orthogonality kills $\ip{x}{y}$, and so the middle term, which gives part 1.
The identity itself kills only the real part, which gives part 3.

### Why each hypothesis is needed

Part 1 needs orthogonality.
For $x = y = (1, 0)$ in $\mathbb{R}^2$ we get $\norm{x + y}^2 = 4$, but $\norm{x}^2 + \norm{y}^2 = 2$.

Part 2 needs every pair to be orthogonal, not only the pairs of neighbors in the list.
In $\mathbb{R}^2$ the vectors $(1, 0)$, $(0, 1)$, $(1, 0)$ have orthogonal neighbors, but
$$\norm{(2, 1)}^2 = 5 \neq 3 = 1 + 1 + 1.$$

The norm must be the induced norm.
For the maximum norm on $\mathbb{R}^2$ and the dot-orthogonal vectors $(1, 1)$ and $(1, -1)$, we get $\norm{(2, 0)}_\infty^2 = 4$, but $1 + 1 = 2$.

Part 4 needs real scalars, and the [[counterexample over $\mathbb{C}$|VT90B84J5V]] gives the details of part 5.

### What it gives you

If $x \perp y$, then $\norm{x + y} \geq \norm{x}$, with equality only for $y = 0$.
This is why an orthogonal projection gives the [[closest point|0MCDDSCB9Z]] of a subspace.

Part 2 gives the length of a vector in an [[orthonormal basis|0S9GGTR0EX]] $(e_1, \dots, e_n)$:
$$\norm{a_1e_1 + \dots + a_ne_n}^2 = \abs{a_1}^2 + \dots + \abs{a_n}^2,$$
because the vectors $a_je_j$ are pairwise orthogonal with $\norm{a_je_j}^2 = \abs{a_j}^2$.
This is the finite form of [[Parseval's identity|047RFCNVSK]].
It also shows that [[orthonormal families are linearly independent|0JWM6GJNQW]]: if $\sum_j a_je_j = 0$, then $\sum_j \abs{a_j}^2 = 0$, so every $a_j$ is $0$.

### The converse

Over $\mathbb{R}$ the converse holds, by part 4.
Over $\mathbb{C}$ one test is not enough, but two tests are: $x \perp y$ if and only if both
$$\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2 \quad \text{and} \quad \norm{x + iy}^2 = \norm{x}^2 + \norm{y}^2.$$
The reason is that $\ip{x}{iy} = -i\ip{x}{y}$, so $\operatorname{Re}\ip{x}{iy} = \operatorname{Im}\ip{x}{y}$, and part 3 for $x$ and $iy$ detects the imaginary part.

For three or more vectors the converse of part 2 fails, even over $\mathbb{R}$.
In $\mathbb{R}^2$ the vectors $(1, 0)$, $(0, 1)$ and $(-1, 1)$ give
$$\norm{(0, 2)}^2 = 4 = 1 + 1 + 2,$$
but $(1, 0) \cdot (-1, 1) = -1$, so the first and third are not orthogonal.

### Generalizations

In a [[Hilbert space|HM2HHE3J51]], part 2 extends to convergent series of pairwise orthogonal vectors.
In probability, the variance of a sum of uncorrelated random variables is the sum of their variances, which is part 2 for the covariance inner product on random variables of mean zero.

## Explanations

### L1 human

This is the theorem of Pythagoras for vectors.
Two orthogonal vectors are the legs of a right triangle, and their sum is the hypotenuse.
For $(3, 0)$ and $(0, 4)$ in the plane, the sum $(3, 4)$ has squared length $25 = 9 + 16$.
The theorem holds in every inner product space, also in spaces of functions.

### L2 human

Here is the theorem for functions.
On polynomials of degree at most $2$, use the [[integral inner product|W6NJ22XGWT]] $\ip{p}{q} = \int_0^1 p(t)q(t)\,dt$, and take $p = 1$ and $q = t - \frac12$.
They are orthogonal, because
$$\ip{p}{q} = \int_0^1 \left(t - \tfrac12\right) dt = \tfrac12 - \tfrac12 = 0.$$
The squared norms are $\norm{p}^2 = 1$ and
$$\norm{q}^2 = \int_0^1 \left(t^2 - t + \tfrac14\right) dt = \tfrac13 - \tfrac12 + \tfrac14 = \tfrac{1}{12}.$$
The sum is $p + q = t + \frac12$, and
$$\norm{p + q}^2 = \int_0^1 \left(t^2 + t + \tfrac14\right) dt = \tfrac13 + \tfrac12 + \tfrac14 = \tfrac{13}{12} = 1 + \tfrac{1}{12},$$
as the theorem says.
The typical use is to compute a length after splitting a vector into orthogonal pieces, as in least squares.
Watch out over $\mathbb{C}$: the identity alone does not prove orthogonality, as part 5 shows.

### L3 human

The theorem is the reason that orthogonal decompositions make length computations additive.
In an orthonormal basis it says that the coordinate map to $\mathbb{K}^n$ with the standard inner product is an isometry.
The failure of the converse over $\mathbb{C}$ shows that a complex inner product holds more than its real part $\operatorname{Re}\ip{x}{y}$.
That real part is an inner product on $V$ viewed as a real space of twice the dimension, and in that real space $1$ and $i$ really are orthogonal.
