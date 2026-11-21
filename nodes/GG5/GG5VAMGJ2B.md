---
tag: GG5VAMGJ2B
kind: example
name: A diagonal matrix with nonzero diagonal entries is invertible
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
instance_of: [0EB9N0S33C]
uses: [0TWTS88TWN, 044JNC7ZAA, 032Q9FB8MT, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Matrix operations
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Definition
---

## Example

Let $D$ be the [[diagonal matrix|044JNC7ZAA]] over $\mathbb{Q}$ with diagonal entries $2$, $3$ and $-1$, and let $E$ be the diagonal matrix of their reciprocals:
$$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & -1 \end{pmatrix}, \qquad E = \begin{pmatrix} \tfrac{1}{2} & 0 & 0 \\ 0 & \tfrac{1}{3} & 0 \\ 0 & 0 & -1 \end{pmatrix}.$$
We check that $E$ is the [[inverse|0TWTS88TWN]] of $D$.

1. Two diagonal matrices multiply entry by entry on the diagonal. Entry $(i, k)$ of $DE$ is $\sum_j d_{ij} e_{jk} = d_{ii} e_{ik}$, since $d_{ij} = 0$ for $j \ne i$, and this is $0$ for $i \ne k$.
2. So $DE$ is diagonal with entries $2 \cdot \tfrac{1}{2} = 1$, $3 \cdot \tfrac{1}{3} = 1$ and $(-1)(-1) = 1$, which means $DE = I_3$.
3. In the same way $ED$ is diagonal with entries $\tfrac{1}{2} \cdot 2$, $\tfrac{1}{3} \cdot 3$ and $(-1)(-1)$, all equal to $1$, so $ED = I_3$.
4. By steps 2 and 3, $D$ is invertible and $D^{-1} = E$.

Check on a vector: $D$ sends $(1, 1, 1)$ to $(2, 3, -1)$, and $E$ sends $(2, 3, -1)$ back to $(1, 1, 1)$.

## Remarks

The same computation works for every size.
Over a field, $\operatorname{diag}(d_1, \dots, d_n)$ is invertible when each $d_i \ne 0$, and its inverse is $\operatorname{diag}(d_1^{-1}, \dots, d_n^{-1})$.

Now change one entry to $0$.
If $d_k = 0$, then $D e_k = 0$ for the standard basis vector $e_k$, so $D$ sends a nonzero vector to $0$ and is singular.
For example, $\operatorname{diag}(2, 0, -1)$ sends $(0, 1, 0)$ to $(0, 0, 0)$.

The field matters too.
Over $\mathbb{Z}$ the matrix $D$ is singular, because the only candidate inverse has the entries $\tfrac{1}{2}$ and $\tfrac{1}{3}$, which are not integers.

## Explanations

### L1 human

The matrix $D$ stretches the first coordinate by $2$, stretches the second by $3$, and flips the sign of the third.
To undo it, we shrink the first coordinate by $2$, shrink the second by $3$, and flip the third sign back.

### L2 human

Diagonal matrices are the one family where the inverse is taken entry by entry, because they multiply entry by entry on the diagonal.
This is why diagonal matrices are so useful after diagonalization: inverting them costs $n$ divisions.
Watch out: for a matrix that is not diagonal, inverting each entry gives the wrong answer.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ the true inverse is $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, not $\begin{pmatrix} 1/2 & 1 \\ 1 & 1 \end{pmatrix}$.
