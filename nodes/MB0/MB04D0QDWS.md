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

*Part 1.*

1. By the [[Cholesky decomposition|0WKG8CYY6A]], $B = L L^*$ with $L$ lower triangular with positive diagonal entries. So $\det L > 0$, and $L$ is [[invertible|FBSAPTP1PR]].
2. Write $L^{-*} = (L^{-1})^*$. By the rule $(XY)^* = Y^* X^*$ from the [[transpose of a product|09GK5PS824]], $L^* L^{-*} = (L^{-1} L)^* = I$. So $L^{-*} = (L^*)^{-1}$.
3. Let $C = L^{-1} A L^{-*}$. Then $C^* = (L^{-*})^* A^* (L^{-1})^* = L^{-1} A L^{-*} = C$, since $A^* = A$. So $C$ is Hermitian.
4. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $C = W D W^*$ with $W$ unitary and $D$ real diagonal. So $W^* C W = D$.
5. Let $P = L^{-*} W$. It is a product of invertible matrices, so it is invertible.
6. $P^* B P = W^* L^{-1} (L L^*) L^{-*} W = W^* W = I$, by step 2.
7. $P^* A P = W^* (L^{-1} A L^{-*}) W = W^* C W = D$, by steps 3 and 4.

*Part 2.*

8. By step 6, $B P = (P^*)^{-1}$. By step 7, $A P = (P^*)^{-1} D = B P D$.
9. Column $i$ of $B P D$ is $\lambda_i B p_i$, since $D$ is diagonal. So $A p_i = \lambda_i B p_i$.
10. The $(i, j)$ entry of $P^* B P$ is $p_i^* B p_j$. By step 6 it is $\delta_{ij}$.

*Part 3.*

11. By step 7 and step 6, $P^* (A - \lambda B) P = D - \lambda I$ for every $\lambda \in \C$.
12. By the [[multiplicativity of the determinant|04CPJ6AF00]], $\overline{\det P} \det(A - \lambda B) \det P = \prod_i (\lambda_i - \lambda)$. Here $\det P^* = \overline{\det P}$, because conjugation and transposition commute with the determinant formula.
13. Since $\abs{\det P}^2 > 0$, the polynomial $\det(A - \lambda B)$ is a nonzero multiple of $\prod_i (\lambda_i - \lambda)$. So its roots are the $\lambda_i$, with multiplicity.
14. By step 6, $B = (P^*)^{-1} P^{-1}$, so $B^{-1} = P P^*$. Then $B^{-1} A = P (P^* A P) P^{-1} = P D P^{-1}$, by step 7.
15. So $B^{-1} A$ is similar to $D$. Similar matrices have the same characteristic polynomial, so the eigenvalues of $B^{-1} A$ are the $\lambda_i$.

*Part 4.*

16. The map $y \mapsto P y$ is a bijection of $\C^n$, since $P$ is invertible. For $x = P y$, step 7 gives $x^* A x = y^* D y = \sum_i \lambda_i \abs{y_i}^2$.
17. If all $\lambda_i \ge 0$, then $x^* A x \ge 0$ for every $x$. If all $\lambda_i > 0$ and $x \ne 0$, then $y \ne 0$ and $x^* A x > 0$.
18. Conversely, for $x = p_i$, that is $y = e_i$, step 16 gives $x^* A x = \lambda_i$. So $A$ positive semidefinite gives $\lambda_i \ge 0$, and $A$ positive definite gives $\lambda_i > 0$.

*Part 5.*

19. If $A$ and $B$ are real, then $L$ is real by the real case of the Cholesky decomposition, and $C$ is real symmetric.
20. By the real case of the spectral theorem, $W$ can be chosen real orthogonal. Then $P = (L^{-1})^T W$ is real, and steps 6 and 7 hold with $^T$ in place of $^*$.

## Idea

The positive definite matrix $B$ is an inner product in disguise.
The Cholesky factor $L$ changes coordinates so that $B$ becomes the identity.
In these coordinates $A$ becomes the Hermitian matrix $L^{-1} A L^{-*}$, and the spectral theorem diagonalizes it with a unitary matrix, which keeps the identity unchanged.

## Variants

- Instead of the Cholesky factor, any invertible $S$ with $B = S S^*$ works, for example the [[positive definite square root|EQ98KW1ZN4]] $S = B^{1/2}$. Then $P = B^{-1/2} W$.
- One can also apply the spectral theorem to the operator $B^{-1} A$, which is self-adjoint for the inner product $\ip{x}{y}_B = y^* B x$.
