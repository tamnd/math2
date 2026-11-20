---
tag: PNJ1QTXA8T
kind: proof
name: Proof of the spectral theorem for Hermitian matrices
msc: ["15A18", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 0DGZBQWZWN
uses: [0EKZCX4K3P, 0EX045E2BP, 0VGSYBWHV2, 0MB8HQW495, 06J4PXRG22, 0D6RMJ10M9, 0QRBVFJ50X, 0N28QN4CYA, 0753Y2X5K6, 0Q9PGXD9E4, 076JGP6R3T]
methods: [0NTF6DMVAP, DX2H7AD66G]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Proof

We apply the operator theorems to the map $x \mapsto Ax$ with the standard inner product.

1. Let $A$ be a [[Hermitian|0EKZCX4K3P]] $n \times n$ complex matrix, so $A^* = A$. Here $A^*$ is the [[conjugate transpose|0EX045E2BP]]. Write vectors of $\mathbb{C}^n$ as columns.
2. For $x, y \in \mathbb{C}^n$, set $\ip{x}{y} = y^* x = \sum_{i=1}^{n} x_i \overline{y_i}$. This is linear in $x$, and $\ip{y}{x} = \overline{\ip{x}{y}}$. Also $\ip{x}{x} = \sum_i \abs{x_i}^2 > 0$ for $x \neq 0$.
3. So $\ip{\cdot}{\cdot}$ is an [[inner product|0VGSYBWHV2]] on $\mathbb{C}^n$. Let $T \colon \mathbb{C}^n \to \mathbb{C}^n$ be $T(x) = Ax$.
4. For matrices, $(MN)^* = N^* M^*$, because $\overline{\sum_k m_{jk} n_{ki}} = \sum_k \overline{n_{ki}}\, \overline{m_{jk}}$. Also $(M^*)^* = M$. Hence $\ip{Ax}{y} = y^* A x = (A^* y)^* x = \ip{x}{A^* y} = \ip{x}{Ay}$.
5. So $T$ is [[self-adjoint|0MB8HQW495]] on the complex inner product space $\mathbb{C}^n$.
6. By part 3 of [[the real spectral theorem|06J4PXRG22]], $\mathbb{C}^n$ has an orthonormal basis $u_1, \dots, u_n$ with $A u_j = \lambda_j u_j$.
7. By the same part 3, all eigenvalues of $T$ are real. So $\lambda_j \in \mathbb{R}$ for every $j$.
8. Let $U$ be the $n \times n$ matrix with the columns $u_1, \dots, u_n$. Let $D$ be the [[diagonal matrix|0Q9PGXD9E4]] with the diagonal entries $\lambda_1, \dots, \lambda_n$. By step 7, $D$ is real.
9. The $(i, j)$ entry of $U^* U$ is $u_i^* u_j = \ip{u_j}{u_i}$. This is $1$ for $i = j$ and $0$ otherwise. So $U^* U = I_n$, and $U$ is [[unitary|0D6RMJ10M9]].
10. By [[the one-sided inverse theorem|0753Y2X5K6]], also $U U^* = I_n$.
11. By the definition of [[matrix multiplication|076JGP6R3T]], column $j$ of $AU$ is $A u_j = \lambda_j u_j$. Column $j$ of $UD$ is also $\lambda_j u_j$. So $AU = UD$.
12. Multiply on the right by $U^*$ and use step 10. This gives $A = A U U^* = U D U^*$, which proves part 1.
13. Part 2. Let $A$ be a real [[symmetric matrix|0N28QN4CYA]], so $A^T = A$. On $\mathbb{R}^n$, use $\ip{x}{y} = y^T x$. This is an inner product by the real case of step 2.
14. As in step 4, $\ip{Ax}{y} = y^T A x = (A^T y)^T x = \ip{x}{Ay}$. So $x \mapsto Ax$ is self-adjoint on $\mathbb{R}^n$.
15. By part 1 of [[the real spectral theorem|06J4PXRG22]], $\mathbb{R}^n$ has an orthonormal basis $q_1, \dots, q_n$ with $A q_j = \lambda_j q_j$ and $\lambda_j \in \mathbb{R}$.
16. Let $Q$ have the columns $q_1, \dots, q_n$, and let $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. As in step 9, $Q^T Q = I_n$. So $Q$ is a real [[orthogonal matrix|0QRBVFJ50X]].
17. As in steps 10 to 12, $Q Q^T = I_n$ and $AQ = QD$. So $A = Q D Q^T$, which proves part 2.

## Idea

A Hermitian matrix acts on $\mathbb{C}^n$ as a self-adjoint map for the standard inner product.
The spectral theorem for self-adjoint operators gives an orthonormal basis of eigenvectors with real eigenvalues.
Put the basis vectors as the columns of $U$: orthonormal columns make $U$ unitary, and $AU = UD$ becomes $A = U D U^*$.
For a real symmetric matrix, the real spectral theorem gives real eigenvectors, so $U$ can be real.

## Variants

- Part 1 also follows from [[the complex spectral theorem|04CW1P44VD]]. A self-adjoint map is [[normal|0ENZN5G4CV]], so it has an orthonormal eigenbasis. Its eigenvalues are real by [[the theorem on real eigenvalues|0C4NT4GT3X]].
- Part 2 does not follow from part 1 alone. Part 1 gives a unitary $U$, which can have non-real entries. Real eigenvectors exist because the real and the imaginary parts of a complex eigenvector of a real matrix are eigenvectors too.
- [[The variational proof|GHGBEV51GZ]] gives both parts directly: it finds the eigenvectors one by one as maximizers of the quadratic form on spheres.
