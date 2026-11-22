---
tag: 62XEH0NYE1
kind: example
name: A Jordan block is not similar to the identity
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0E89HQATM8
    note: the matrix with rows (1, 1) and (0, 1) and the identity matrix I_2 have the same trace, determinant and characteristic polynomial, but they are not similar, since every matrix similar to I_2 equals I_2
uses: [027KDW2K72, 06DW9BAWB1, 0PBFS92AJP]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
---

## Example

Two matrices can agree in trace, determinant and characteristic polynomial and still not be similar.
Over a field $F$, let
$$J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix},$$
the [[Jordan block|0PBFS92AJP]] of size $2$ with eigenvalue $1$, and let $I_2$ be the [[identity matrix|06DW9BAWB1]].

1. The traces agree: $\operatorname{tr} J = 1 + 1 = 2 = \operatorname{tr} I_2$.
2. The determinants agree: $\det J = 1 \cdot 1 - 1 \cdot 0 = 1 = \det I_2$.
3. The characteristic polynomials agree, since both $xI - J$ and $xI - I_2$ are upper triangular with diagonal entries $x - 1$:
   $$\det(xI - J) = (x - 1)^2 = \det(xI - I_2).$$
4. Now let $P$ be any invertible $2 \times 2$ matrix over $F$.
   Then $P^{-1}I_2P = P^{-1}P = I_2$.
5. So the only matrix [[similar|027KDW2K72]] to $I_2$ is $I_2$ itself.
   Since $J \ne I_2$, the matrix $J$ is not similar to $I_2$.

## Remarks

Other invariants do see the difference.
The matrix $J - I_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has rank $1$, while $I_2 - I_2 = 0$ has rank $0$.
The minimal polynomial of $I_2$ is $x - 1$.
The minimal polynomial of $J$ is $(x - 1)^2$, because $J - I_2 \ne 0$ but $(J - I_2)^2 = 0$.
In size $4$, even the minimal polynomial is not enough, as the [[example with five equal invariants|J4Q3B9ZNHF]] shows.

The example also shows that $J$ is not diagonalizable.
A diagonal matrix with characteristic polynomial $(x - 1)^2$ has both diagonal entries equal to $1$, so it is $I_2$, and $J$ is not similar to $I_2$.

The same argument works for every scalar matrix $cI$: it is similar only to itself.
If we replace the entry $1$ in the corner of $J$ by any $t \ne 0$, the new matrix is still not similar to $I_2$, and it is similar to $J$ by $P = \operatorname{diag}(1, t)$.

## Explanations

### L1 human

The identity matrix is the same in every basis, so nothing else is similar to it.
The matrix $J$ has the same trace and determinant as $I_2$, but it is a shear that slides the plane sideways, not the motion that leaves everything in place.
So the two matrices describe different motions.

### L2 human

Similar matrices share all their invariants, but the converse fails.
The rank of $J - I_2$ measures how far $J$ is from the scalar matrix $I_2$, and it is $1$, not $0$.
Watch out: to show that two matrices are not similar, one differing invariant is enough; to show that they are similar, you must find $P$ or use a complete set of invariants such as a canonical form.
