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

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.

1. If $x, y \in V$ are [[orthogonal|0TS7VZJBWD]], then $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$.
2. If $x_1, \dots, x_k \in V$ are pairwise orthogonal, then $\norm{x_1 + \dots + x_k}^2 = \norm{x_1}^2 + \dots + \norm{x_k}^2$.
3. For all $x, y \in V$, the identity $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ holds if and only if $\operatorname{Re}\ip{x}{y} = 0$.
4. If $\mathbb{K} = \mathbb{R}$, then the converse of part 1 holds: the identity $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ implies $x \perp y$.
5. If $\mathbb{K} = \mathbb{C}$, then the converse of part 1 fails: in $\mathbb{C}$, the vectors $x = 1$ and $y = i$ satisfy the identity, but $\ip{x}{y} = -i$.

## Remarks

### Why each hypothesis is needed

- Part 1 needs orthogonality. For $x = y = (1, 0)$ in $\mathbb{R}^2$, $\norm{x + y}^2 = 4$, but $\norm{x}^2 + \norm{y}^2 = 2$.
- Part 2 needs the vectors to be pairwise orthogonal, not only consecutive ones. In $\mathbb{R}^2$, $x_1 = (1, 0)$, $x_2 = (0, 1)$ and $x_3 = (1, 0)$ give $\norm{(2, 1)}^2 = 5$, but the sum of the squares is $3$.
- The norm must be the induced norm. For the maximum norm on $\mathbb{R}^2$ and the vectors $(1, 1)$ and $(1, -1)$, $\norm{(2, 0)}^2 = 4$, but $1 + 1 = 2$, although the two vectors are orthogonal for the dot product.
- Part 4 needs $\mathbb{K} = \mathbb{R}$. The [[counterexample over $\mathbb{C}$|~9026ead5]] gives the details of part 5.

### Consequences

- If $x \perp y$, then $\norm{x + y} \geq \norm{x}$, with equality only for $y = 0$. This is the reason that an orthogonal projection gives the [[closest point|0MCDDSCB9Z]].
- Part 2 gives the length of a vector in an [[orthonormal basis|0S9GGTR0EX]]: $\norm{\sum_j a_j e_j}^2 = \sum_j |a_j|^2$. This is the finite form of [[Parseval's identity|047RFCNVSK]].
- Part 2 also proves that [[orthonormal families are linearly independent|0JWM6GJNQW]]: if $\sum_j a_j e_j = 0$, then $\sum_j |a_j|^2 = 0$.
- If $x \perp y$, then $\norm{x - y} = \norm{x + y}$, because $x \perp (-y)$ too.

### Converse

Over $\mathbb{R}$ the converse holds by part 4.
Over $\mathbb{C}$, $x \perp y$ holds if and only if both $\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2$ and $\norm{x + iy}^2 = \norm{x}^2 + \norm{y}^2$.
The reason is that $\operatorname{Re}\ip{x}{iy} = \operatorname{Re}(-i\ip{x}{y}) = \operatorname{Im}\ip{x}{y}$, so part 3 for $x$ and $iy$ detects the imaginary part.
For part 2, the identity for $k \geq 3$ vectors does not imply pairwise orthogonality even over $\mathbb{R}$.
In $\mathbb{R}^2$, the vectors $(1, 0)$, $(0, 1)$ and $(-1, 1)$ give $\norm{(0, 2)}^2 = 4 = 1 + 1 + 2$, but $(1, 0) \cdot (-1, 1) = -1$.

### Generalizations

- In a [[Hilbert space|HM2HHE3J51]], part 2 extends to convergent series of pairwise orthogonal vectors.
- Part 3 is the case $\ip{x}{y} = 0$ of the identity $\norm{x + y}^2 = \norm{x}^2 + 2\operatorname{Re}\ip{x}{y} + \norm{y}^2$, the law of cosines of an inner product space.

## Explanations

### L1 human

This is the theorem of Pythagoras for vectors.
Two orthogonal vectors are the legs of a right triangle, and their sum is the hypotenuse.
For $(3, 0)$ and $(0, 4)$ in the plane, the sum $(3, 4)$ has squared length $25 = 9 + 16$.
The theorem holds in every inner product space, also in spaces of functions.

### L2 human

Worked example: the Pythagorean theorem for functions.

1. On $\mathcal{P}_2(\mathbb{R})$ use the [[integral inner product|~8366abd2]] $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$.
2. Let $p = 1$ and $q = t - \frac12$. Then $\ip{p}{q} = \int_0^1 (t - \frac12) \, dt = \frac12 - \frac12 = 0$, so $p \perp q$.
3. The norms are $\norm{p}^2 = 1$ and $\norm{q}^2 = \int_0^1 (t - \frac12)^2 \, dt = \frac13 - \frac12 + \frac14 = \frac{1}{12}$.
4. The sum is $p + q = t + \frac12$, and $\norm{p + q}^2 = \frac13 + \frac12 + \frac14 = \frac{13}{12} = 1 + \frac{1}{12}$.

The typical use is to compute a length after a split into orthogonal pieces, as in least squares.
A trap: over $\mathbb{C}$ the identity does not prove orthogonality, as part 5 shows.

### L3 human

The theorem is the reason that orthogonal decompositions make length computations additive.
In an orthonormal basis it says that the coordinate map to $\mathbb{K}^n$ is an isometry.
In probability, the variance of a sum of uncorrelated random variables is the sum of the variances.
This is part 2 for the covariance inner product.
The failure of the converse over $\mathbb{C}$ shows that a complex inner product holds more information than the real inner product $\operatorname{Re}\ip{x}{y}$.
That real part is the inner product of $V$ viewed as a real space of twice the dimension.
