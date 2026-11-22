---
tag: GP4XSY4FNH
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

Let $Q(x, y) = 5x^2 + 4xy + 2y^2$.
Half of the coefficient $4$ goes into each off-diagonal place, so the symmetric matrix of $Q$ is $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$.
We find the principal axes of the curve $Q = 1$, as in [[the principal axis theorem|0PR5P9Z4KM]].

1. The trace is $7$ and the determinant is $10 - 4 = 6$, so the characteristic polynomial is $t^2 - 7t + 6 = (t - 6)(t - 1)$, and the eigenvalues are $6$ and $1$.
2. The vectors $(2, 1)$ and $(-1, 2)$ are [[eigenvectors|0B5H4208Z9]] for $6$ and $1$, since $A(2, 1)^{\mathsf{T}} = (12, 6)^{\mathsf{T}}$ and $A(-1, 2)^{\mathsf{T}} = (-1, 2)^{\mathsf{T}}$.
3. They are orthogonal, since $2 \cdot (-1) + 1 \cdot 2 = 0$, and each has length $\sqrt{5}$. So the unit eigenvectors are $p_1 = (2, 1)/\sqrt{5}$ and $p_2 = (-1, 2)/\sqrt{5}$.
4. The matrix $P$ with columns $p_1$ and $p_2$ has $\det P = (4 + 1)/5 = 1$. So it is the rotation by the angle $\theta$ with $\tan \theta = \tfrac{1}{2}$, about $26.57^\circ$.
5. The change of variables $(x, y)^{\mathsf{T}} = P (u, v)^{\mathsf{T}}$ reads $x = (2u - v)/\sqrt{5}$ and $y = (u + 2v)/\sqrt{5}$.
6. Substitute term by term:
$$5x^2 = \frac{20u^2 - 20uv + 5v^2}{5}, \qquad 4xy = \frac{8u^2 + 12uv - 8v^2}{5}, \qquad 2y^2 = \frac{2u^2 + 8uv + 8v^2}{5}.$$
7. Add the three terms. The $uv$ terms give $-20 + 12 + 8 = 0$, so $Q = (30u^2 + 5v^2)/5 = 6u^2 + v^2$.
8. So the curve is $6u^2 + v^2 = 1$, an [[ellipse|0VKCCEXBJ1]] with semi-axis $1/\sqrt{6} \approx 0.408$ along $p_1$ and semi-axis $1$ along $p_2$.

Check: the point $(u, v) = (1/\sqrt{6}, 0)$ is $(x, y) = (2, 1)/\sqrt{30}$, and there $Q = (20 + 8 + 2)/30 = 1$.
The point $(u, v) = (0, 1)$ is $(x, y) = (-1, 2)/\sqrt{5}$, and there $Q = (5 - 8 + 8)/5 = 1$.

## Remarks

The long axis lies along the eigenvector of the smallest eigenvalue, and the short axis along the eigenvector of the largest.
The reason is that the semi-axis in the direction $p_i$ is $1/\sqrt{\lambda_i}$, so a large eigenvalue means a short axis.
The area of the ellipse is $\pi \cdot \tfrac{1}{\sqrt{6}} \cdot 1 = \pi/\sqrt{\det A}$.

Change the right side and only the size changes: $Q = c$ with $c > 0$ is the same ellipse scaled by $\sqrt{c}$.
Change the matrix to $\begin{pmatrix} 5 & 2 \\ 2 & -2 \end{pmatrix}$, the form $5x^2 + 4xy - 2y^2$, and the determinant becomes $-14 < 0$, so the eigenvalues have opposite signs and the curve is a hyperbola.
The same matrix $A$ appears in [[the Rayleigh quotient example|3FXAQ6P15S]], where $6$ and $1$ are the largest and smallest values of $Q$ on the unit circle.

## Explanations

### L1 human

The equation has an $xy$ term, so the ellipse is tilted against the grid.
Turning the axes by about $26.57^\circ$ removes the $xy$ term.
In the turned axes the equation $6u^2 + v^2 = 1$ shows an ellipse that is $1$ unit long on one side of the center and about $0.41$ units on the other.

### L2 human

The steps are always the same: write the symmetric matrix, find its eigenvalues, find unit eigenvectors, and substitute.
Watch out for the matrix: the off-diagonal entry is $2$, half of the coefficient $4$ of $xy$.
With $4$ in that place the determinant would be $10 - 16 < 0$, and you would wrongly find a hyperbola.
Also keep the order: $u$ goes with the eigenvalue $6$ and $v$ with $1$, because $p_1$ is the first column of $P$.
