---
tag: X1CZSG8JEC
kind: example
name: An upper triangular matrix similar to a diagonal matrix
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0E89HQATM8]
illustrates: [191HBJ7PVZ]
uses: [027KDW2K72, 0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
---

## Example

A matrix that is not diagonal can become diagonal in a better basis.
Over $\mathbb{R}$, let
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}, \qquad P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.$$

1. The determinant is $\det P = 1 \cdot 1 - 1 \cdot 0 = 1 \ne 0$, so $P$ is [[invertible|0TWTS88TWN]], and the formula for a $2 \times 2$ inverse gives $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
2. Check: $P^{-1}P = \begin{pmatrix} 1 & 1 - 1 \\ 0 & 1 \end{pmatrix} = I_2$.
3. We multiply on the right first, with the [[matrix product|076JGP6R3T]]:
   $$AP = \begin{pmatrix} 1 + 0 & 1 + 1 \\ 0 + 0 & 0 + 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}.$$
4. Then on the left; $P^{-1}$ subtracts row 2 from row 1:
   $$P^{-1}(AP) = \begin{pmatrix} 1 - 0 & 2 - 2 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = D.$$
5. So $D = P^{-1}AP$, and $D$ is [[similar|027KDW2K72]] to $A$.
6. The columns of $P$ explain the result: $A(1, 0) = (1, 0)$ and $A(1, 1) = (1 + 1, 0 + 2) = 2(1, 1)$.
7. The invariants agree, as the [[theorem on similarity invariants|191HBJ7PVZ]] requires.
   The traces are $1 + 2 = 3$ for both, the determinants are $1 \cdot 2 - 1 \cdot 0 = 2$ and $1 \cdot 2 = 2$, and both characteristic polynomials are $(x - 1)(x - 2)$.

## Remarks

In the basis $(1, 0)$, $(1, 1)$ of $\mathbb{R}^2$, the map $x \mapsto Ax$ has the diagonal matrix $D$.
This is the [[change of basis formula|0MQXVZEBMT]], with $P$ as the change of basis matrix.
The columns of $P$ are eigenvectors of $A$, and the diagonal entries of $D$ are the matching eigenvalues.

The order of the columns of $P$ matters.
With the columns exchanged, $P' = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ gives $P'^{-1}AP' = \operatorname{diag}(2, 1)$, which is also similar to $A$.
If we change the entry $2$ of $A$ to $1$, the matrix becomes the Jordan block $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, and then [[no diagonal matrix is similar to it|62XEH0NYE1]].

## Explanations

### L1 human

The matrix $A$ is not diagonal, but it becomes diagonal in a better basis.
The new basis vectors are $(1, 0)$ and $(1, 1)$, and $A$ only stretches them, by $1$ and by $2$.
So in the new basis the matrix is $\operatorname{diag}(1, 2)$.

### L2 human

Similarity to a diagonal matrix means that the columns of $P$ are eigenvectors.
Here the two eigenvalues $1$ and $2$ are distinct, and a $2 \times 2$ matrix with two distinct eigenvalues always has a basis of eigenvectors.
The trace and the determinant of $A$ are then the sum and the product of the diagonal entries of $D$.
Watch out: the eigenvalues of a triangular matrix are its diagonal entries, but only the first standard basis vector is sure to be an eigenvector; here $e_2 = (0, 1)$ goes to $(1, 2)$, which is not a multiple of $e_2$.
