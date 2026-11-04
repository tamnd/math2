---
tag: PNJ1QTXA8T
kind: proof
name: Proof of the spectral theorem for Hermitian matrices
msc: [15A18, 15B57]
proves: 0DGZBQWZWN
uses: [0EKZCX4K3P, 0EX045E2BP, 0VGSYBWHV2, 0MB8HQW495, 06J4PXRG22, 0D6RMJ10M9, 0QRBVFJ50X, 0N28QN4CYA, 0753Y2X5K6, 0Q9PGXD9E4, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
---

## Proof

We apply the spectral theorem to the map $x \mapsto Ax$ on $\C^n$ with the standard inner product.

1. Let $A$ be a [[Hermitian|0EKZCX4K3P]] $n \times n$ complex matrix, so $A^* = A$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]. Write vectors of $\C^n$ as columns.
2. For $x, y \in \C^n$, set $\ip{x}{y} = y^* x = \sum_{i=1}^{n} x_i \overline{y_i}$. It is linear in $x$, and $\ip{y}{x} = \overline{\ip{x}{y}}$. Also $\ip{x}{x} = \sum_i \abs{x_i}^2 > 0$ for $x \ne 0$.
3. So $\ip{\cdot}{\cdot}$ is an [[inner product|0VGSYBWHV2]] on $\C^n$. Let $T \colon \C^n \to \C^n$ be $T(x) = Ax$.
4. For a product of matrices, $(MN)^* = N^* M^*$, since $\overline{\sum_k m_{jk} n_{ki}} = \sum_k \overline{n_{ki}}\, \overline{m_{jk}}$. Also $(M^*)^* = M$. Hence $\ip{Ax}{y} = y^* A x = (A^* y)^* x = \ip{x}{A^* y} = \ip{x}{Ay}$.
5. So $T$ is [[self-adjoint|0MB8HQW495]]. By the [[spectral theorem|06J4PXRG22]], $\C^n$ has an orthonormal basis $u_1, \dots, u_n$ with $A u_j = \lambda_j u_j$ and $\lambda_j \in \R$.
6. Let $U$ be the $n \times n$ matrix with columns $u_1, \dots, u_n$. Let $D$ be the [[diagonal matrix|0Q9PGXD9E4]] with diagonal entries $\lambda_1, \dots, \lambda_n$, which is real.
7. The $(i, j)$ entry of $U^* U$ is $u_i^* u_j = \ip{u_j}{u_i} = \delta_{ij}$. So $U^* U = I_n$, and $U$ is [[unitary|0D6RMJ10M9]].
8. By the [[one-sided inverse theorem|0753Y2X5K6]], also $U U^* = I_n$.
9. By the definition of [[matrix multiplication|076JGP6R3T]], column $j$ of $AU$ is $A u_j = \lambda_j u_j$, and column $j$ of $UD$ is $\lambda_j u_j$. So $AU = UD$.
10. Multiplying on the right by $U^*$ and using step 8 gives $A = A U U^* = U D U^*$. This proves the first claim.
11. Now let $A$ be a real [[symmetric matrix|0N28QN4CYA]], so $A^T = A$. Use $\R^n$ with $\ip{x}{y} = y^T x$, which is an inner product by the real case of step 2.
12. As in step 4, $\ip{Ax}{y} = y^T A x = (A^T y)^T x = \ip{x}{Ay}$. So $x \mapsto Ax$ is self-adjoint on $\R^n$.
13. The spectral theorem gives an orthonormal basis $q_1, \dots, q_n$ of $\R^n$ with $A q_j = \lambda_j q_j$ and $\lambda_j \in \R$.
14. Let $Q$ have columns $q_1, \dots, q_n$, and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. As in step 7, $Q^T Q = I_n$, so $Q$ is real and [[orthogonal|0QRBVFJ50X]].
15. As in steps 8 to 10, $Q Q^T = I_n$ and $AQ = QD$. So $A = Q D Q^T$, and $Q = Q^*$ shows that $U = Q$ can be chosen real.

## Idea

A Hermitian matrix acts on $\C^n$ as a self-adjoint map for the standard inner product. The spectral theorem gives an orthonormal basis of eigenvectors. Put these as the columns of $U$: orthonormal columns make $U$ unitary, and $AU = UD$ becomes $A = UDU^*$.
