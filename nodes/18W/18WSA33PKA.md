---
tag: 18WSA33PKA
kind: example
name: Computing the generalized eigenspaces of a 3 × 3 matrix
msc: ["15A18", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
instance_of: [0AJ035ZTZE, 01H6QKWGDH]
not_instance_of:
  - target: 07SQCNV233
    note: the eigenvalue 2 has algebraic multiplicity 2 but its eigenspace is the line spanned by (1, 1, 0)
illustrates: [PHZ684KGWS, 0Z3GDY89T5]
uses: [07PNDWA7CE, 0SAAHC36J9, 0VSSPAFM2C, 0AYEPBQMAW]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Examples
  - book: isbn:9780134860244
    locator: Section 7.1
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 & 1 \\ -1 & 3 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$
over $\R$.
We find both generalized eigenspaces and check that they fill $\R^3$.

1. Expand $\det(t I - A)$ along the third row, which has the single entry $t - 1$:
$$p_A(t) = (t - 1) \big( (t - 1)(t - 3) + 1 \big) = (t - 1)(t^2 - 4t + 4) = (t - 1)(t - 2)^2.$$
2. So the eigenvalues are $1$, with algebraic multiplicity $1$, and $2$, with algebraic multiplicity $2$.
3. Subtract $2I$:
$$M = A - 2I = \begin{pmatrix} -1 & 1 & 1 \\ -1 & 1 & 1 \\ 0 & 0 & -1 \end{pmatrix}.$$
   The equation $M(x, y, z) = 0$ reads $-x + y + z = 0$ twice and $-z = 0$, so $z = 0$ and $x = y$.
4. So the [[eigenspace|0AYEPBQMAW]] of $2$ is only the line spanned by $(1, 1, 0)$.
5. Square $M$, row by column:
$$M^2 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & -1 \\ 0 & 0 & 1 \end{pmatrix}.$$
   So $\ker M^2$ is the plane $z = 0$.
6. Multiply once more: $M^3 = M^2 M$ has the rows $(0, 0, 1)$, $(0, 0, 1)$ and $(0, 0, -1)$, so $M^3 = -M^2$ and $\ker M^3 = \ker M^2$.
7. So the [[generalized eigenspace|07PNDWA7CE]] $V_2 = \ker M^3$ is the plane $z = 0$, of dimension $2$, as the multiplicity predicts.
8. For the eigenvalue $1$, the matrix $A - I$ has the rows $(0, 1, 1)$, $(-1, 2, 1)$ and $(0, 0, 0)$.
   Its kernel is given by $z = -y$ and $x = y$, so it is spanned by $(1, 1, -1)$, and $V_1$ is this line.
9. The vector $(1, 1, -1)$ is not in the plane $z = 0$, and $1 + 2 = 3$, so $\R^3 = V_1 \oplus V_2$.
10. The vector $(0, 1, 0)$ has $M(0, 1, 0) = (1, 1, 0) \ne 0$ and $M^2(0, 1, 0) = 0$.
    So it is a [[generalized eigenvector|0SAAHC36J9]] for $2$ of rank $2$.

## Remarks

The chain of kernels for $2$ stops at $k = 2$, which equals the algebraic multiplicity, although $n = 3$.
The vectors $(1, 1, -1)$, $(1, 1, 0)$ and $(0, 1, 0)$ form a basis, and the matrix of $A$ in this basis is
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}.$$
Check the last column: $A(0, 1, 0)$ is the second column of $A$, namely $(1, 3, 0) = (1, 1, 0) + 2 \cdot (0, 1, 0)$.
This is the Jordan normal form of $A$.

Every vector of $V_2$ has rank at most $2$, and the vectors of rank exactly $2$ are those of the plane that lie off the line $\R (1, 1, 0)$.
The same matrix gives a worked [[Jordan-Chevalley decomposition|4P9QZRCJND]].

## Explanations

### L1 human

The matrix has two eigenvalues, $1$ once and $2$ twice.
For $2$ there is only one line of eigenvectors, so we also look at the vectors that need two steps to vanish.
They fill a plane.
That plane and the line for $1$ together make up all of space.

### L2 human

Check that $(1, 1, -1)$ is an eigenvector for $1$ and lies outside $V_2$.

1. Multiply: $A(1, 1, -1) = (1 + 1 - 1, \; -1 + 3 - 1, \; -1) = (1, 1, -1)$.
2. So $(A - I)(1, 1, -1) = 0$.
3. Its third coordinate is $-1 \ne 0$, so it is not in the plane $V_2$.

The typical use is to compute $\ker (A - \lambda I)^k$ for $k = 1, 2, \dots$ until the dimension reaches the algebraic multiplicity.
Watch out: a stop at $k = 1$ gives only a line for $2$, and the pieces do not fill $\R^3$.

### L3 human

The two generalized eigenspaces are the primary components of $\R^3$ as an $\R[t]$-module, for the factors $t - 1$ and $(t - 2)^2$ of the minimal polynomial.
The projection onto $V_1$ along $V_2$ is the polynomial $M^2 = (A - 2I)^2$ in $A$, as the [[decomposition into generalized eigenspaces|0Z3GDY89T5]] predicts.
