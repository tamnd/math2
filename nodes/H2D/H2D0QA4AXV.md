---
tag: H2D0QA4AXV
kind: example
name: A least-squares line through four points
msc: [65F20, 15A06]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0BYTQ4X1HC]
illustrates: [V9AH43ZY91, 4D7MRG4D91]
uses: [0W809K6AW0, 0EB9N0S33C]
sources:
  - book: isbn:9780321982384
    locator: Section 6.6
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Example
---

## Example

We fit a line $y = c + s t$ to the four points $(0, 1)$, $(1, 2)$, $(2, 2)$, $(3, 4)$.
A line through all four would solve $A x = y$ with
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}, \quad x = \begin{pmatrix} c \\ s \end{pmatrix}, \quad y = \begin{pmatrix} 1 \\ 2 \\ 2 \\ 4 \end{pmatrix}.$$

1. No exact solution: the first two equations give $c = 1$ and $s = 1$, and then the third gives $1 + 2 = 3 \ne 2$.
2. The columns of $A$ are independent, since $(1, 1, 1, 1)$ is not a multiple of $(0, 1, 2, 3)$. So the least-squares solution is unique, by [[existence and uniqueness|V9AH43ZY91]].
3. [[Normal equations|4D7MRG4D91]]: $A^{\mathsf{T}} A = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}$ and $A^{\mathsf{T}} y = \begin{pmatrix} 1 + 2 + 2 + 4 \\ 0 + 2 + 4 + 12 \end{pmatrix} = \begin{pmatrix} 9 \\ 18 \end{pmatrix}$.
4. $\det(A^{\mathsf{T}} A) = 56 - 36 = 20$. Cramer's rule gives $c = (9 \cdot 14 - 6 \cdot 18)/20 = 18/20 = 9/10$ and $s = (4 \cdot 18 - 6 \cdot 9)/20 = 18/20 = 9/10$.
5. The least-squares line is $y = 0.9 + 0.9 t$. Its values at $t = 0, 1, 2, 3$ are $A \hat x = (0.9, 1.8, 2.7, 3.6)$.
6. The residual is $r = y - A \hat x = (0.1, 0.2, -0.7, 0.4)$.
7. Orthogonality to the column space: $r \cdot (1, 1, 1, 1) = 0.1 + 0.2 - 0.7 + 0.4 = 0$ and $r \cdot (0, 1, 2, 3) = 0 + 0.2 - 1.4 + 1.2 = 0$. So $A^{\mathsf{T}} r = 0$.
8. The residual sum of squares is $\norm{r}^2 = 0.01 + 0.04 + 0.49 + 0.16 = 0.70$.

## Remarks

Step 7 is the check that every least-squares computation should end with.
The first equation of $A^{\mathsf{T}} r = 0$ says that the residuals add up to $0$, so the line passes through the mean point $(\bar t, \bar y) = (1.5, 2.25)$: indeed $0.9 + 0.9 \cdot 1.5 = 2.25$.
If the last point moves from $(3, 4)$ to $(3, 3)$, then $A^{\mathsf{T}} y = (8, 15)$, and the line becomes $y = 1.1 + 0.6 t$.
[[The line through three of the points|MH3VAGXW9R]] has a larger residual sum of squares.

## Explanations

### L1 human

The four points almost lie on a line, but not quite.
The least-squares line is the line that makes the sum of the squared vertical misses as small as possible.
Here it is $y = 0.9 + 0.9 t$, and the squared misses add up to $0.7$.

### L2 human

The method has three steps: write the model as $Ax \approx y$, solve $A^{\mathsf{T}} A x = A^{\mathsf{T}} y$, and check that $A^{\mathsf{T}} r = 0$.
The column of ones in $A$ is the intercept $c$; the column $(0, 1, 2, 3)$ holds the times $t_i$.
The typical use is to fit a trend to measured data.
The trap is to drop the column of ones, which fits a line through the origin instead.
