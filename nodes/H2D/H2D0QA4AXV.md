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

We fit a line $y = c + st$ to the four points $(0, 1)$, $(1, 2)$, $(2, 2)$ and $(3, 4)$.
A line through all four points would solve $Ax = y$ with
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}, \quad x = \begin{pmatrix} c \\ s \end{pmatrix}, \quad y = \begin{pmatrix} 1 \\ 2 \\ 2 \\ 4 \end{pmatrix}.$$

1. There is no exact solution: the first two equations give $c = 1$ and $s = 1$, and then the third equation $c + 2s = 2$ fails, since $1 + 2 = 3$.
2. The columns $(1, 1, 1, 1)$ and $(0, 1, 2, 3)$ are not multiples of each other, so they are independent, and the least-squares solution is unique by [[existence and uniqueness|V9AH43ZY91]].
3. The [[normal equations|4D7MRG4D91]] need two products:
$$A^{\mathsf{T}} A = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}, \qquad A^{\mathsf{T}} y = \begin{pmatrix} 1 + 2 + 2 + 4 \\ 0 + 2 + 4 + 12 \end{pmatrix} = \begin{pmatrix} 9 \\ 18 \end{pmatrix}.$$
4. The determinant is $\det(A^{\mathsf{T}} A) = 56 - 36 = 20$, and Cramer's rule gives
$$c = \frac{9 \cdot 14 - 6 \cdot 18}{20} = \frac{18}{20} = \frac{9}{10}, \qquad s = \frac{4 \cdot 18 - 6 \cdot 9}{20} = \frac{18}{20} = \frac{9}{10}.$$
5. So the least-squares line is $y = 0.9 + 0.9t$, and its values at $t = 0, 1, 2, 3$ are $A \hat x = (0.9, 1.8, 2.7, 3.6)$.
6. The residual is $r = y - A \hat x = (0.1, 0.2, -0.7, 0.4)$.
7. The residual is orthogonal to both columns:
$$r \cdot (1, 1, 1, 1) = 0.1 + 0.2 - 0.7 + 0.4 = 0, \qquad r \cdot (0, 1, 2, 3) = 0 + 0.2 - 1.4 + 1.2 = 0.$$
8. The residual sum of squares is $\norm{r}^2 = 0.01 + 0.04 + 0.49 + 0.16 = 0.70$.

## Remarks

Step 7 is the check that every least-squares computation should end with, because $A^{\mathsf{T}} r = 0$ is exactly the condition of the normal equations.
Its first half says that the residuals add up to $0$.
So the line passes through the mean point $(\bar t, \bar y) = (1.5, 2.25)$, and indeed $0.9 + 0.9 \cdot 1.5 = 2.25$.

The fit reacts to every point.
If the last point moves from $(3, 4)$ to $(3, 3)$, then $A^{\mathsf{T}} y = (8, 15)$, and Cramer's rule gives $c = (112 - 90)/20 = 1.1$ and $s = (60 - 48)/20 = 0.6$.
So the new line is $y = 1.1 + 0.6t$, with a smaller slope.
The best line passes through none of the four original points, and [[the line through three of the points|MH3VAGXW9R]] has the larger residual sum of squares $1$.

## Explanations

### L1 human

The four points almost lie on a line, but not quite.
For each candidate line, measure how far each point is above or below it, square these misses, and add.
The least-squares line is the one with the smallest total.
Here it is $y = 0.9 + 0.9t$, and its squared misses add up to $0.7$.

### L2 human

The method has three steps: write the model as $Ax \approx y$, solve $A^{\mathsf{T}} A x = A^{\mathsf{T}} y$, and check that $A^{\mathsf{T}} r = 0$.
The column of ones in $A$ belongs to the intercept $c$, and the column $(0, 1, 2, 3)$ holds the times $t_i$.
The typical use is to fit a trend to measured data, and a parabola or any other model that is linear in its parameters only adds columns to $A$.
Watch out: if you drop the column of ones, you fit a line through the origin, which here is $y = \tfrac{9}{7} t$ and not the best line.
