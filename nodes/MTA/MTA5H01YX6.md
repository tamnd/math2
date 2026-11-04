---
tag: MTA5H01YX6
kind: proof
name: Proof of simultaneous diagonalisation of commuting diagonalisable matrices
msc: [15A20, 15A27]
proves: 0FK17N4DKA
uses: [0Y17PEKF24, 0Q9PGXD9E4, 0MPAJRB23T, 0BNEXSKNRV, 0KJVQV3E0F, 0B5H4208Z9, 06MRNP4BNT, 056SW1E0AC]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 5.2
---

## Proof

Necessity is a computation. For sufficiency we split eigenvectors of $A$ into eigenvectors of $B$ with polynomials in $B$.

1. Suppose $P$ is invertible and $P^{-1} A P = D_1$ and $P^{-1} B P = D_2$ are [[diagonal|0Q9PGXD9E4]]. The product of two diagonal matrices is diagonal with the products of the diagonal entries, so $D_1 D_2 = D_2 D_1$.
2. Then $A B = P D_1 P^{-1} P D_2 P^{-1} = P D_1 D_2 P^{-1} = P D_2 D_1 P^{-1} = B A$. So $A B = B A$ is necessary.
3. Conversely, let $A B = B A$. If $n = 0$, then $P = I_0$ works, so let $n \ge 1$. Since $B$ is [[diagonalisable|0Y17PEKF24]], its minimal polynomial is $m_B = (t - \mu_1) \cdots (t - \mu_l)$ with pairwise distinct $\mu_j \in F$, by the [[minimal polynomial criterion|0MPAJRB23T]]. Here $l \ge 1$, since the constant $1$ does not annihilate $B$.
4. For each $j$, let $f_j = \prod_{i \ne j} (t - \mu_i)$ and $c_j = f_j(\mu_j) \ne 0$. Let $h = \sum_j c_j^{-1} f_j$. Then $h(\mu_i) = 1$ for each $i$, since $f_j(\mu_i) = 0$ for $j \ne i$.
5. The polynomial $h - 1$ has degree at most $l - 1$ and $l$ roots. A nonzero polynomial has [[at most as many roots as its degree|0KJVQV3E0F]], so $h = 1$. Hence $\sum_j c_j^{-1} f_j(B) = I_n$, using the [[value at $B$|0BNEXSKNRV]].
6. Since $A$ commutes with $B$, it commutes with each power of $B$, hence with $g(B)$ for every polynomial $g$.
7. Let $w$ be an [[eigenvector|0B5H4208Z9]] of $A$, with $A w = \lambda w$. Let $u_j = c_j^{-1} f_j(B) w$. By step 5, $w = u_1 + \cdots + u_l$.
8. By step 6, $A u_j = c_j^{-1} f_j(B) A w = \lambda u_j$.
9. Since $(t - \mu_j) f_j = m_B$, we get $(B - \mu_j I_n) u_j = c_j^{-1} m_B(B) w = 0$. So $B u_j = \mu_j u_j$.
10. By steps 8 and 9, each nonzero $u_j$ is an eigenvector of both $A$ and $B$. Call such a vector a common eigenvector, and let $S$ be the set of common eigenvectors.
11. By step 7, every eigenvector of $A$ is a sum of elements of $S$.
12. Since $A$ is diagonalisable, $F^n$ has a basis of eigenvectors of $A$, by the [[characterisation by eigenvectors|056SW1E0AC]]. With step 11, $S$ spans $F^n$.
13. [[Every spanning set contains a basis|06MRNP4BNT]]. So there is a basis $v_1, \dots, v_n$ of $F^n$ contained in $S$.
14. Let $P$ be the matrix with columns $v_1, \dots, v_n$. Each $v_i$ is an eigenvector of $A$ and of $B$. By the [[formula for $P^{-1} A P$|056SW1E0AC]], both $P^{-1} A P$ and $P^{-1} B P$ are diagonal.

## Idea

Commuting matrices preserve each other's eigenspaces. Concretely, the interpolation polynomials in $B$ that add up to $I_n$ split each eigenvector of $A$ into pieces. Each piece is an eigenvector of $B$ and still an eigenvector of $A$. So common eigenvectors span the space, and a basis of them diagonalises both matrices.
