---
tag: CH4C4K2B0S
kind: proof
name: Proof of the block triangular form for an invariant subspace
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: ENVF51H5S3
methods: [0NTF6DMVAP]
uses: [0PFPWKBDTJ, 0YYMY95FWS, 0BZ81AJNWF, 0SVR29SV1V, 0SXDQ6TN00, 096V7H13H9, 0J9TVTNB4K, 0TYMASG33Y]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Proof

We read off the columns of the matrix one block at a time, and then we take the determinant of a block triangular matrix.

1. Let $1 \le i \le k$.
   Since $U$ is invariant, $T(u_i) \in U$, so $T(u_i) = \sum_{l=1}^{k} a_{li} u_l$ for some $a_{li} \in F$, because $u_1, \dots, u_k$ is a basis of $U$.
2. By the definition of the [[matrix of a linear map|0YYMY95FWS]], column $i$ of $[T]_{\mathcal{B}}$ holds the coordinates of $T(u_i)$ in $\mathcal{B}$.
   By step 1 these are $a_{1i}, \dots, a_{ki}$ followed by $n - k$ zeros, so the lower left block is $0$.
3. The [[restriction|0PFPWKBDTJ]] satisfies $T|_U(u_i) = T(u_i) = \sum_l a_{li} u_l$.
   So $A = (a_{li})$ is the matrix of $T|_U$ in the basis $u_1, \dots, u_k$.
4. Let $k < j \le n$, and expand $T(v_j)$ in the basis $\mathcal{B}$:
$$T(v_j) = \sum_{l=1}^{k} b_{lj} u_l + \sum_{m=k+1}^{n} c_{mj} v_m.$$
   Column $j$ of $[T]_{\mathcal{B}}$ consists of the $b_{lj}$ and then the $c_{mj}$.
5. In the [[quotient space|0SVR29SV1V]], $u_l + U = 0 + U$, since $u_l \in U$.
   So the quotient operator gives
$$\bar T(v_j + U) = T(v_j) + U = \sum_{m=k+1}^{n} c_{mj} (v_m + U).$$
6. The cosets $v_{k+1} + U, \dots, v_n + U$ span $V / U$.
   Indeed, each $v \in V$ is a combination of the vectors of $\mathcal{B}$, and the terms in the $u_l$ vanish modulo $U$, as in step 5.
7. By the [[dimension of a quotient space|0SXDQ6TN00]], $\dim(V / U) = n - k$.
   A spanning family of $n - k$ vectors in a space of dimension $n - k$ is a basis, by the [[right-size criterion|096V7H13H9]].
8. By steps 5 and 7, $C = (c_{mj})$ is the matrix of $\bar T$ in the basis $v_{k+1} + U, \dots, v_n + U$.
   Together with steps 2 and 3, this proves part 1.
9. By the [[definition of the characteristic polynomial of a linear map|0BZ81AJNWF]], $p_T = \det(t I_n - [T]_{\mathcal{B}})$.
   This does not depend on the basis, since the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
10. By part 1, the matrix $t I_n - [T]_{\mathcal{B}}$ is block upper triangular over the commutative ring $F[t]$:
$$t I_n - [T]_{\mathcal{B}} = \begin{pmatrix} t I_k - A & -B \\ 0 & t I_{n-k} - C \end{pmatrix}.$$
11. By the [[determinant of a block triangular matrix|0J9TVTNB4K]], $p_T = \det(t I_k - A) \det(t I_{n-k} - C)$.
12. By steps 3 and 8, the two factors are $p_{T|_U}$ and $p_{\bar T}$.
    If $k = 0$ or $k = n$, one block is empty and its factor is $1$, so the formula still holds, and this proves part 2.

## Idea

Invariance of $U$ means that $T$ sends the first $k$ basis vectors into their own span, and that is exactly the zero block.
Modulo $U$ the first $k$ basis vectors vanish, so the lower right block is all that remains of $T$ on the quotient.
Once the matrix is block triangular, the determinant of $tI - [T]$ factors along the diagonal blocks, and part 2 follows.

## Variants

A proof without matrices uses the fact that the characteristic polynomial is multiplicative on short exact sequences of $F[x]$-modules, which can itself be proved with exterior powers.
Over an algebraically closed field, one can also prove part 2 by comparing roots with multiplicities after triangularizing $T|_U$ and $\bar T$ and lifting the two flags to one flag of $V$.
