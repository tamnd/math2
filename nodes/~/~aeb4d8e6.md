---
tag: ~aeb4d8e6
kind: example
name: The principal axes of the ellipse 5x² + 4xy + 2y² = 1
msc: [15A63, 15A18, 51N20]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR]
illustrates: [0PR5P9Z4KM]
uses: [0PR5P9Z4KM, 0B5H4208Z9, 0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_axis_theorem
    locator: Motivation
  - book: isbn:9780321982384
---

## Example

Let $Q(x, y) = 5x^2 + 4xy + 2y^2$, with symmetric matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$.
We find the principal axes of the curve $Q = 1$, as in [[the principal axis theorem|0PR5P9Z4KM]].

1. The characteristic polynomial is $t^2 - 7t + 6 = (t - 6)(t - 1)$, since $\tr A = 7$ and $\det A = 10 - 4 = 6$.
2. The vectors $(2, 1)$ and $(-1, 2)$ are [[eigenvectors|0B5H4208Z9]] for $6$ and $1$: $A (2, 1)^T = (12, 6)^T$ and $A (-1, 2)^T = (-1, 2)^T$.
3. The unit eigenvectors $p_1 = \frac{1}{\sqrt 5}(2, 1)$ and $p_2 = \frac{1}{\sqrt 5}(-1, 2)$ are orthogonal, because $2 \cdot (-1) + 1 \cdot 2 = 0$.
4. The matrix $P$ with columns $p_1, p_2$ has $\det P = \frac15 (4 + 1) = 1$, so it is a rotation by $\theta = \arctan \frac12 \approx 26.57^\circ$.
5. The new coordinates are given by $x = \frac{2u - v}{\sqrt 5}$ and $y = \frac{u + 2v}{\sqrt 5}$.
6. Substitution: $5x^2 = (20u^2 - 20uv + 5v^2)/5$, $4xy = (8u^2 + 12uv - 8v^2)/5$ and $2y^2 = (2u^2 + 8uv + 8v^2)/5$.
7. The sum is $(30u^2 + 0 \cdot uv + 5v^2)/5 = 6u^2 + v^2$.
8. So the curve is $6u^2 + v^2 = 1$, an [[ellipse|0VKCCEXBJ1]] with semi-axis $1/\sqrt 6 \approx 0.408$ along $p_1$ and semi-axis $1$ along $p_2$.
9. Check: $(u, v) = (1/\sqrt 6, 0)$ gives $(x, y) = (2, 1)/\sqrt{30}$ and $Q = (20 + 8 + 2)/30 = 1$; $(u, v) = (0, 1)$ gives $(x, y) = (-1, 2)/\sqrt 5$ and $Q = (5 - 8 + 8)/5 = 1$.

## Remarks

The long axis lies along the eigenvector of the smallest eigenvalue, and the short axis along that of the largest.
This is because the semi-axis in direction $p_i$ is $1/\sqrt{\lambda_i}$.
The area of the ellipse is $\pi \cdot \frac{1}{\sqrt 6} \cdot 1 = \pi / \sqrt{\det A}$.
The same matrix appears in [[the Rayleigh quotient example|3FXAQ6P15S]], where $6$ and $1$ are the extreme values on the unit circle.

## Explanations

### L1 human

The equation has an $xy$ term, so the ellipse is tilted.
Turning the axes by about $26.57^\circ$ removes the $xy$ term.
In the new axes, the equation $6u^2 + v^2 = 1$ shows an ellipse with half-widths $0.408$ and $1$.

### L2 human

The steps are always the same: the matrix, its eigenvalues, unit eigenvectors, then substitution.
A trap: the coefficient of $xy$ in the matrix is halved; the matrix has $2$, not $4$, off the diagonal.
Another trap: the order of the eigenvalues fixes the order of the new variables; here $u$ goes with $6$ and $v$ with $1$.
