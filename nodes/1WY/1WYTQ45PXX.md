---
tag: 1WYTQ45PXX
kind: proof
name: Proof of the principal axis theorem from the spectral theorem
msc: [15A63, 15A18]
topics: [6TSCEW8QMK]
audience: ug1
proves: 0PR5P9Z4KM
methods: [0NTF6DMVAP]
uses: [04CPJ6AF00, 0ZZQ2E1MTE, 0DGZBQWZWN, 0N28QN4CYA, 0QRBVFJ50X, 0753Y2X5K6, 09GK5PS824, 0TYMASG33Y, 053QVHF6N7, 0B5H4208Z9, 0ZND7NQ970, 09VYHEF2VT]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_axis_theorem
    locator: Formal statement
---

## Proof

We take the orthogonal matrix that the spectral theorem gives, substitute $x = Py$ into $Q$, and then identify the diagonal entries and the columns.

1. The matrix $A$ is real and [[symmetric|0N28QN4CYA]].
   So the [[spectral theorem|0DGZBQWZWN]] gives an [[orthogonal|0QRBVFJ50X]] matrix $P$ and a real diagonal matrix $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ with $A = P D P^{\mathsf{T}}$.
2. Since $P$ is orthogonal, $P^{\mathsf{T}} P = I$, and the [[one-sided inverse theorem|0753Y2X5K6]] also gives $P P^{\mathsf{T}} = I$.
3. By steps 1 and 2, $P^{\mathsf{T}} A P = (P^{\mathsf{T}} P) D (P^{\mathsf{T}} P) = D$.
4. Let $y \in \mathbb{R}^n$ and $x = Py$.
   By the rule for the [[transpose of a product|09GK5PS824]], $x^{\mathsf{T}} = y^{\mathsf{T}} P^{\mathsf{T}}$, so $Q(x) = y^{\mathsf{T}} (P^{\mathsf{T}} A P) y = y^{\mathsf{T}} D y$.
5. Since $D$ is diagonal, $y^{\mathsf{T}} D y = \lambda_1 y_1^2 + \dots + \lambda_n y_n^2$.
   This is the formula of the statement.
6. Let $p_1, \dots, p_n$ be the columns of $P$.
   The $(i, j)$ entry of $P^{\mathsf{T}} P = I$ is $p_i^{\mathsf{T}} p_j$, so the columns form an [[orthonormal family|09VYHEF2VT]], and in particular each $p_i$ is nonzero.
7. Multiplying $A = P D P^{\mathsf{T}}$ on the right by $P$ and using step 2 gives $AP = PD$.
   Column $i$ of $AP$ is $A p_i$, and column $i$ of $PD$ is $\lambda_i p_i$, so $A p_i = \lambda_i p_i$.
8. By steps 6 and 7, each $p_i$ is an [[eigenvector|0B5H4208Z9]] of $A$, and each $\lambda_i$ is an [[eigenvalue|0ZND7NQ970]] of $A$ with eigenvector $p_i$.
9. By step 2, $P^{-1} = P^{\mathsf{T}}$, so $D = P^{-1} A P$ and the [[characteristic polynomials of A and D agree|0TYMASG33Y]].
   Hence $\det(tI - A) = (t - \lambda_1) \cdots (t - \lambda_n)$.
10. By [[the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues of $A$, repeated by multiplicity, are exactly $\lambda_1, \dots, \lambda_n$.
11. By [[the transpose rule|0ZZQ2E1MTE]] and [[multiplicativity|04CPJ6AF00]] of the determinant, $(\det P)^2 = \det(P^{\mathsf{T}}) \det(P) = \det(P^{\mathsf{T}} P) = 1$, so $\det P = \pm 1$.
12. If $\det P = -1$, replace $p_1$ by $-p_1$.
   The new column is still a unit eigenvector for $\lambda_1$ and orthogonal to the others, and the determinant changes sign, so now $\det P = 1$.
13. The replacement changes $y_1$ into $-y_1$, and $\lambda_1 y_1^2$ does not change.
   So the formula of step 5 holds for a $P$ with $\det P = 1$, and the theorem is proved.

## Idea

The spectral theorem already says that a symmetric matrix is diagonal in a suitable orthonormal basis.
The principal axis theorem is the same fact written for the form.
In the coordinates $y = P^{\mathsf{T}} x$ the matrix of $Q$ is $P^{\mathsf{T}} A P = D$, so the cross terms vanish and the eigenvalues remain as the coefficients of the squares.
The last steps only tidy up: they show that the coefficients are the eigenvalues, and that a reflection can be traded for a rotation by flipping one axis.

## Variants

One can prove the spectral theorem and this theorem together by a variational argument.
The form $Q$ is continuous on the compact unit sphere, so it has a maximum there, and the [[Rayleigh quotient statement|T7MFPSY009]] shows that a point of maximum is an eigenvector.
The orthogonal complement of that eigenvector is mapped into itself by $A$, so induction on the dimension gives the rest, as in [[the variational proof of the real spectral theorem|GHGBEV51GZ]].

[[The diagonalization theorem|0Z3FEWZ8HA]] reaches a diagonal form faster, by completing squares, and it works over every field of characteristic not $2$.
Its change of variables is not orthogonal, however, so its coefficients are not the eigenvalues, and only their signs agree with the ones here.
