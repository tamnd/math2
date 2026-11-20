---
tag: ~fcc4cf33
kind: example
name: An upper triangular matrix similar to a diagonal matrix
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0E89HQATM8]
illustrates: [~b354e4d1]
uses: [027KDW2K72, 0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}, \qquad P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$$
over $\R$.

1. $\det P = 1 \cdot 1 - 1 \cdot 0 = 1 \ne 0$, so $P$ is [[invertible|0TWTS88TWN]], with $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
2. Check: $P^{-1} P = \begin{pmatrix} 1 - 0 & 1 - 1 \\ 0 & 1 \end{pmatrix} = I_2$.
3. [[Product|076JGP6R3T]]: $AP = \begin{pmatrix} 1 + 0 & 1 + 1 \\ 0 + 0 & 0 + 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}$.
4. Product: $P^{-1}(AP) = \begin{pmatrix} 1 - 0 & 2 - 2 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = D$.
5. So $D = P^{-1} A P$, and $D$ is [[similar|027KDW2K72]] to $A$.
6. The columns of $P$ explain the result. $A(1, 0) = (1, 0)$ and $A(1, 1) = (1 + 1, 0 + 2) = 2(1, 1)$.
7. Invariants agree: $\operatorname{tr} A = 1 + 2 = 3 = \operatorname{tr} D$, and $\det A = 1 \cdot 2 - 1 \cdot 0 = 2 = \det D$.
8. The characteristic polynomials agree: $\det(xI - A) = (x - 1)(x - 2) = \det(xI - D)$.

## Remarks

- In the basis $(1, 0), (1, 1)$ of $\R^2$, the map $x \mapsto Ax$ has the diagonal matrix $D$. This is the [[change of basis formula|0MQXVZEBMT]] with $P$ the change of basis matrix.
- The order of the columns of $P$ matters. With the columns exchanged, the result is $\operatorname{diag}(2, 1)$, which is also similar to $A$.

## Explanations

### L1 human

The matrix $A$ is not diagonal, but it becomes diagonal in a better basis.
The new basis vectors are $(1, 0)$ and $(1, 1)$, and $A$ only stretches them, by $1$ and by $2$.

### L2 human

Similarity to a diagonal matrix means that the columns of $P$ are eigenvectors.
Here the eigenvalues $1$ and $2$ are distinct, so this always works.
The trace and the determinant are the sum and the product of the diagonal entries of $D$.
