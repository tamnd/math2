---
tag: SYDSCH64X8
kind: example
name: Pseudoinverse of a 3 × 2 matrix with independent columns
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
instance_of: [0YY8VX28JR]
illustrates: [Q9YN0F60ZW]
uses: [0PSRCMCM5X, 000NPTMX6J, 4D7MRG4D91]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linearly independent columns
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix},$$
the matrix of [[the 3 by 2 SVD example|GK1B93DKD3]].
Its columns are independent, so we can compute $A^+$ with an ordinary inverse and then confirm it with the SVD.

1. The Gram matrix is $A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with determinant $4 - 1 = 3$, so it is invertible and
$$(A^{\mathsf{T}} A)^{-1} = \frac13 \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.$$
2. Multiply by $A^{\mathsf{T}}$:
$$A^+ = (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} = \frac13 \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} = \frac13 \begin{pmatrix} 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix}.$$
3. The SVD gives the same matrix. It has $\sigma_1 = \sqrt3$, $v_1 = \frac{1}{\sqrt2}(1, 1)$, $u_1 = \frac{1}{\sqrt6}(2, 1, 1)$, and $\sigma_2 = 1$, $v_2 = \frac{1}{\sqrt2}(1, -1)$, $u_2 = \frac{1}{\sqrt2}(0, 1, -1)$. Check: $A v_1 = \frac{1}{\sqrt2}(2, 1, 1) = \sqrt3 \, u_1$ and $A v_2 = \frac{1}{\sqrt2}(0, 1, -1) = u_2$.
4. The two terms of $V \Sigma^+ U^{\mathsf{T}}$ are
$$\frac{1}{\sqrt3} v_1 u_1^{\mathsf{T}} = \frac16 \begin{pmatrix} 2 & 1 & 1 \\ 2 & 1 & 1 \end{pmatrix}, \qquad v_2 u_2^{\mathsf{T}} = \frac12 \begin{pmatrix} 0 & 1 & -1 \\ 0 & -1 & 1 \end{pmatrix},$$
and their sum is $\frac16 \begin{pmatrix} 2 & 4 & -2 \\ 2 & -2 & 4 \end{pmatrix}$, the matrix of step 2.
5. The product $A^+ A = \frac13 \begin{pmatrix} 1 + 2 & 1 - 1 \\ 1 - 1 & 1 + 2 \end{pmatrix} = I_2$ is symmetric, which is condition 4. Then $A A^+ A = A I_2 = A$ and $A^+ A A^+ = I_2 A^+ = A^+$, which are conditions 1 and 2.
6. The other product is
$$A A^+ = \frac13 \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix},$$
which is symmetric, so condition 3 holds and all four Penrose conditions are checked.
7. With $u_3 = \frac{1}{\sqrt3}(1, -1, -1)$, one finds $A A^+ = I_3 - u_3 u_3^{\mathsf{T}}$. So $A A^+$ is the orthogonal projection onto the plane $x_1 - x_2 - x_3 = 0$, which contains both columns of $A$ and so is the column space.
8. For $b = (1, 2, 3)$, we get $A^+ b = \frac13 (1 + 4 - 3, \ 1 - 2 + 6) = \left(\frac23, \frac53\right)$. Check with the [[normal equations|4D7MRG4D91]]: $A^{\mathsf{T}} A \left(\frac23, \frac53\right) = \left(\frac43 + \frac53, \frac23 + \frac{10}{3}\right) = (3, 4)$, and $A^{\mathsf{T}} b = (1 + 2, 1 + 3) = (3, 4)$.

## Remarks

With independent columns, $A^+ A = I_2$, so $A^+$ is a left inverse of $A$.
It is not a right inverse, since $A A^+$ is a $3 \times 3$ matrix of rank $2$ and cannot be $I_3$.

Other left inverses exist.
For example, $X = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ picks the second and third rows, and $X A = I_2$.
But $A X$ has rows $(0, 1, 1)$, $(0, 1, 0)$ and $(0, 0, 1)$, so it is not symmetric and condition 3 fails.
For any left inverse, conditions 1, 2 and 4 hold at once because $X A = I_2$, so condition 3 alone picks $A^+$ out of all the left inverses.

If we make the columns dependent, for example by changing the second column to $(2, 2, 0)$, the Gram matrix becomes singular, and only the SVD route of steps 3 and 4 still works.

## Explanations

### L1 human

When the columns of a matrix are independent, the pseudoinverse has a formula with an ordinary inverse of a small square matrix.
We compute it with that formula and again with the SVD, and the two answers agree.
The result undoes $A$ from the left, so $A^+ A$ is the identity, but not from the right.

### L2 human

The formula $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$ is the matrix that solves the normal equations, so it gives the unique least-squares solution, as step 8 checks.
Steps 3 and 4 show that it agrees with $V \Sigma^+ U^{\mathsf{T}}$, as the [[theorem on the pseudoinverse|Q9YN0F60ZW]] predicts.
This is the typical case in data fitting, where there are more equations than unknowns and the columns are independent.
Watch out: the left inverse $X$ in the remarks also gives $X A = I_2$, but it fails condition 3, so not every left inverse is the pseudoinverse.
