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

1. The matrix $A$ is real and [[symmetric|0N28QN4CYA]]. By the [[spectral theorem|0DGZBQWZWN]], $A = P D P^T$ with $P$ [[orthogonal|0QRBVFJ50X]] and $D$ real diagonal.
2. Let $\lambda_1, \dots, \lambda_n$ be the diagonal entries of $D$. By definition $P^T P = I$, and the [[one-sided inverse theorem|0753Y2X5K6]] gives $P P^T = I$.
3. By step 2, $P^T A P = P^T P D P^T P = D$.
4. Let $y \in \R^n$ and $x = Py$. By the [[transpose of a product|09GK5PS824]], $Q(x) = y^T P^T A P y = y^T D y$.
5. By step 3, $y^T D y = \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$. This is the formula of the statement.
6. Let $p_1, \dots, p_n$ be the columns of $P$. The $(i, j)$ entry of $P^T P = I$ is $p_i^T p_j$. So the columns form an [[orthonormal family|09VYHEF2VT]] for the dot product, and each $p_i \ne 0$.
7. From $A = P D P^T$ and $P^T P = I$ we get $AP = PD$. Comparing column $i$ gives $A p_i = \lambda_i p_i$.
8. By steps 6 and 7, each $p_i$ is an [[eigenvector|0B5H4208Z9]] of $A$, and each $\lambda_i$ is an [[eigenvalue|0ZND7NQ970]] of $A$.
9. Since $D = P^{-1} A P$, the [[characteristic polynomials agree|0TYMASG33Y]]. So $\det(tI - A) = (t - \lambda_1) \cdots (t - \lambda_n)$.
10. By [[the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues of $A$ are exactly $\lambda_1, \dots, \lambda_n$, each with its multiplicity.
11. So $Q(Py) = \sum_i \lambda_i y_i^2$, where the $\lambda_i$ are the eigenvalues of $A$ and the columns of $P$ are orthonormal eigenvectors of $A$.
12. By [[the transpose rule|0ZZQ2E1MTE]] and [[multiplicativity|04CPJ6AF00]], $\det(P)^2 = \det(P^T) \det(P) = \det(P^T P) = 1$. So $\det P = \pm 1$.
13. If $\det P = -1$, replace $p_1$ by $-p_1$. It is still a unit eigenvector for $\lambda_1$, orthogonal to the others, and now $\det P = 1$.
14. The formula of step 11 does not change, since $y_1^2 = (-y_1)^2$. So $P$ can be chosen with $\det P = 1$.

## Idea

The spectral theorem rotates coordinates so that $A$ becomes diagonal.
In the new coordinates $y = P^T x$, the cross terms of $Q$ vanish, and only the eigenvalues remain as coefficients of the squares.

## Variants

- One can prove the spectral theorem and this theorem together. The maximum of $Q$ on the unit sphere is attained at an eigenvector, as in [[the extreme value theorem for the Rayleigh quotient|T7MFPSY009]]. Then one restricts $Q$ to the orthogonal complement and uses induction.
- [[The diagonalization theorem|0Z3FEWZ8HA]] gives a diagonal form faster, by completing squares, but not with an orthogonal $P$.
