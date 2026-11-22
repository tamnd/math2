---
tag: 7XVJ4ZCXTV
kind: example
name: A singular system cannot be solved with an inverse
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
not_instance_of:
  - target: FBQCE3HVMP
    note: the coefficient matrix has determinant 0, so it has no inverse; the system has infinitely many solutions for one right-hand side and none for another
uses: [FBQCE3HVMP, 0JTRMBQ1SA, 8XWC7RKNN1]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Solution set
---

## Example

The system $x + 2y = 3$, $2x + 4y = 6$ over $\mathbb{R}$ has infinitely many solutions, and no inverse matrix can pick one of them.
The coefficient matrix is
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad ad - bc = 1 \cdot 4 - 2 \cdot 2 = 0,$$
so $A$ has no inverse, by the [[2 × 2 formula|8XWC7RKNN1]].
The second equation is twice the first, so the system says only $x + 2y = 3$.
For each real number $t$, the pair $(x, y) = (3 - 2t, t)$ is a solution.
Check: $(3 - 2t) + 2t = 3$, and the second equation is twice this.
For $t = 0$ and $t = 1$ we get the two different solutions $(3, 0)$ and $(1, 1)$.

Change the right side to $(3, 7)$.
The equations $x + 2y = 3$ and $2x + 4y = 7$ would give
$$6 = 2(x + 2y) = 2x + 4y = 7,$$
which is false, so this system has no solution at all.

## Remarks

The same matrix gives many solutions for one right side and none for another, and never exactly one.
That is the general picture for a singular square matrix: by the [[Rouché-Capelli theorem|0HV1SKWPMS]], the system has either no solution or more than one, and over $\mathbb{R}$ more than one means infinitely many.
So the formula $x = A^{-1}b$ has no meaning here, and elimination is the method to use.
Geometrically, the two equations describe the same line in the first case and two parallel lines in the second.

## Explanations

### L1 human

The two equations say the same thing, so they do not fix the two unknowns.
There are many answers, and no inverse matrix can pick one.
If we change the second equation a little, the two lines become parallel and never meet.

### L2 human

Before using the inverse, test the matrix with the determinant or with row reduction.
Here the zero row after $R_2 \to R_2 - 2R_1$ shows the problem at once.
A trap: a calculator may still print a "solution" in floating point for a matrix that is nearly singular.
