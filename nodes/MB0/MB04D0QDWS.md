---
tag: MB04D0QDWS
kind: proof
name: Proof of simultaneous diagonalization by Cholesky reduction
msc: [15A22, 15B57]
topics: [SS4EVPKT3A]
audience: ug2
proves: K559AQ9H67
methods: [01XM7JEKHY, 0NTF6DMVAP]
uses: [0WKG8CYY6A, 0DGZBQWZWN, 09GK5PS824, 04CPJ6AF00, FBSAPTP1PR, 0C2F40MEBC]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Simultaneous diagonalization
---

## Proof

We change coordinates with the Cholesky factor of $B$ so that $B$ becomes $I$, and then we diagonalize the new form of $A$ with a unitary matrix, which keeps $I$ unchanged.
Throughout, $(XY)^* = Y^* X^*$ by the [[transpose of a product|09GK5PS824]] with conjugated entries.

*Part 1.*

1. By the [[Cholesky decomposition|0WKG8CYY6A]], $B = L L^*$ with $L$ lower triangular with positive diagonal entries. So $\det L > 0$, and $L$ is [[invertible|FBSAPTP1PR]].
2. Write $L^{-*} = (L^{-1})^*$. Then $L^* L^{-*} = (L^{-1} L)^* = I$, so $L^{-*} = (L^*)^{-1}$.
3. Let $C = L^{-1} A L^{-*}$. Then $C^* = (L^{-*})^* A^* (L^{-1})^* = L^{-1} A L^{-*} = C$, since $A^* = A$, so $C$ is Hermitian.
4. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $C = W D W^*$ with $W$ unitary and $D$ real diagonal, so $W^* C W = D$.
5. Let $P = L^{-*} W$. It is a product of invertible matrices, so it is invertible.
6. By step 2, $P^* B P = W^* L^{-1} (L L^*) L^{-*} W = W^* W = I$.
7. By steps 3 and 4, $P^* A P = W^* (L^{-1} A L^{-*}) W = W^* C W = D$.

*Part 2.*

8. By step 6, $B P = (P^*)^{-1}$. By step 7, $A P = (P^*)^{-1} D = B P D$.
9. Column $i$ of $B P D$ is $\lambda_i B p_i$, because $D$ is diagonal. So $A p_i = \lambda_i B p_i$.
10. The $(i, j)$ entry of $P^* B P$ is $p_i^* B p_j$, and by step 6 it is $\delta_{ij}$.

*Part 3.*

11. By steps 6 and 7, $P^* (A - \lambda B) P = D - \lambda I$ for every $\lambda \in \C$.
12. Here $\det P^* = \overline{\det P}$, because the determinant formula commutes with conjugation and with transposition. By the [[multiplicativity of the determinant|04CPJ6AF00]], $\abs{\det P}^2 \det(A - \lambda B) = \prod_i (\lambda_i - \lambda)$.
13. Since $\abs{\det P}^2 > 0$, the polynomial $\det(A - \lambda B)$ is a nonzero multiple of $\prod_i (\lambda_i - \lambda)$. So its roots are the $\lambda_i$, with multiplicity.
14. By step 6, $B = (P^*)^{-1} P^{-1}$, so $B^{-1} = P P^*$. With step 7 this gives $B^{-1} A = P (P^* A P) P^{-1} = P D P^{-1}$.
15. So $B^{-1} A$ is similar to $D$. Similar matrices have the same characteristic polynomial, so the eigenvalues of $B^{-1} A$ are the $\lambda_i$.

*Part 4.*

16. The map $y \mapsto P y$ is a bijection of $\C^n$, because $P$ is invertible. For $x = P y$, step 7 gives $x^* A x = y^* D y = \sum_i \lambda_i \abs{y_i}^2$.
17. If all $\lambda_i \ge 0$, then $x^* A x \ge 0$ for every $x$. If all $\lambda_i > 0$ and $x \ne 0$, then $y \ne 0$, so $x^* A x > 0$.
18. Conversely, $x = p_i$ corresponds to $y = e_i$, and step 16 gives $p_i^* A p_i = \lambda_i$. So if $A$ is positive semidefinite, then $\lambda_i \ge 0$, and if $A$ is positive definite, then $\lambda_i > 0$, because $p_i \ne 0$.

*Part 5.*

19. If $A$ and $B$ are real, then $L$ is real by the real case of the Cholesky decomposition, and so $C$ is real symmetric.
20. By the real case of the spectral theorem, $W$ can be chosen real orthogonal. Then $P = (L^{-1})^{\mathsf{T}} W$ is real, and steps 6 and 7 hold with $^{\mathsf{T}}$ in place of $^*$.

## Idea

A positive definite matrix $B$ is an inner product in disguise.
The Cholesky factor $L$ gives coordinates in which that inner product is the standard one, so $B$ becomes $I$.
In these coordinates $A$ becomes the Hermitian matrix $L^{-1} A L^{-*}$.
The spectral theorem diagonalizes it with a unitary matrix, and a unitary change of coordinates does not disturb $I$.
So one change of coordinates handles both matrices.

## Variants

Any invertible $S$ with $B = S S^*$ can replace the Cholesky factor.
For example, the [[positive definite square root|EQ98KW1ZN4]] $S = B^{1/2}$ gives $C = B^{-1/2} A B^{-1/2}$ and $P = B^{-1/2} W$.
The Cholesky factor is preferred in computation because it is cheaper to find.

One can also avoid the factorization altogether.
The matrix $B^{-1} A$ is self-adjoint for the inner product $\ip{x}{y}_B = y^* B x$, since $\ip{B^{-1} A x}{y}_B = y^* A x = \ip{x}{B^{-1} A y}_B$.
The spectral theorem in that inner product space gives a $B$-orthonormal basis of eigenvectors of $B^{-1} A$, and these vectors are the columns of $P$.
