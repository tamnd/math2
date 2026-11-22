---
tag: TZETVDBJG9
kind: example
name: The form x² + xy + y² is positive definite
msc: [15A63]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RP20HFYM3]
uses: [00QN1N6MNT, 0HYC2RHD3M, 0WKEF78PMV, XNCV97HTZ8]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Example

Let $Q(x, y) = x^2 + xy + y^2$ on $\mathbb{R}^2$.
The coefficient $1$ of $xy$ is split between the two off-diagonal places, so the symmetric matrix of $Q$ is
$$A = \begin{pmatrix} 1 & 1/2 \\ 1/2 & 1 \end{pmatrix}.$$
Check: $x^{\mathsf{T}} A x = x^2 + \tfrac{1}{2} xy + \tfrac{1}{2} yx + y^2 = Q(x, y)$.
We show in three ways that $Q$ is [[positive definite|00QN1N6MNT]].

1. By [[completing the square|XNCV97HTZ8]], $Q = \left( x + \tfrac{1}{2} y \right)^2 + \tfrac{3}{4} y^2$. Both terms are at least $0$. If $Q(x, y) = 0$, then $y = 0$ and so $x = 0$. So $Q(v) > 0$ for every $v \ne 0$.
2. By eigenvalues, $A (1, 1)^{\mathsf{T}} = (\tfrac{3}{2}, \tfrac{3}{2})^{\mathsf{T}}$ and $A (1, -1)^{\mathsf{T}} = (\tfrac{1}{2}, -\tfrac{1}{2})^{\mathsf{T}}$. So the eigenvalues are $\tfrac{3}{2}$ and $\tfrac{1}{2}$, both positive, and [[the eigenvalue test|0HYC2RHD3M]] applies.
3. By minors, the leading minors are $1 > 0$ and $\det A = 1 - \tfrac{1}{4} = \tfrac{3}{4} > 0$. So [[Sylvester's criterion|0WKEF78PMV]] applies.

Check: the eigenvalues have sum $2 = \operatorname{tr} A$ and product $\tfrac{3}{4} = \det A$.

## Remarks

The three tests must agree, and they show different things.
The squares give a proof that a beginner can follow without matrices.
The eigenvalues give the shape of the level curve $Q = 1$: it is an ellipse with axes along $(1, 1)$ and $(1, -1)$.
The semi-axes are $1/\sqrt{\lambda}$, so they are $\sqrt{2/3} \approx 0.82$ along $(1, 1)$ and $\sqrt{2} \approx 1.41$ along $(1, -1)$.
The eigenvalues also give the extreme values on the unit circle: the minimum $\tfrac{1}{2}$ at $\pm (1, -1)/\sqrt{2}$ and the maximum $\tfrac{3}{2}$ at $\pm (1, 1)/\sqrt{2}$.

Change the cross coefficient and the answer changes.
The form $x^2 - xy + y^2$ is positive definite for the same reasons, since its determinant is again $\tfrac{3}{4}$.
The form $x^2 + 2xy + y^2 = (x + y)^2$ has determinant $0$, and it vanishes at $(1, -1)$, so it is only semidefinite.
The form $x^2 + 3xy + y^2$ has determinant $1 - \tfrac{9}{4} < 0$, and it is indefinite: it is $-1$ at $(1, -1)$.

## Explanations

### L1 human

The cross term $xy$ can be negative, but it is never large compared with $x^2 + y^2$.
At $(1, -1)$ the form is $1 - 1 + 1 = 1$, and at $(2, -1)$ it is $4 - 2 + 1 = 3$.
Writing the form as a square plus a positive multiple of a square shows that it never reaches $0$ except at the origin.

### L2 human

For a $2 \times 2$ form the minors test is the fastest: check the top left entry and the determinant.
Watch out for the off-diagonal entry.
The matrix has $\tfrac{1}{2}$ there, not $1$.
With $1$ the determinant would be $1 - 1 = 0$, and the test would wrongly say that the form is not positive definite.
