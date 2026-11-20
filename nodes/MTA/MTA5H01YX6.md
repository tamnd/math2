---
tag: MTA5H01YX6
kind: proof
name: Proof of simultaneous diagonalization of commuting diagonalizable maps
msc: ["15A20", "15A27"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: 0FK17N4DKA
methods: [0ASJVEFA9J, B2D8PTFNN1, TFQ1845T84]
uses: [0Y17PEKF24, 0Q9PGXD9E4, 0MPAJRB23T, 8YNE1HTZEP, 056SW1E0AC, 06MRNP4BNT, 041JTZCK9Q, 0AYEPBQMAW]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 5.2
  - book: isbn:9780135367971
    locator: Section 6.5
---

## Proof

We prove necessity by a computation, then sufficiency for finite families by strong induction on $\dim V$, and then reduce any family to a finite one.

1. Assume condition 1, with a basis $\mathcal{B}$. Two [[diagonal matrices|0Q9PGXD9E4]] commute, since their product is diagonal with the products of the entries.
2. So $[S T]_{\mathcal{B}} = [S]_{\mathcal{B}} [T]_{\mathcal{B}} = [T]_{\mathcal{B}} [S]_{\mathcal{B}} = [T S]_{\mathcal{B}}$, and $S T = T S$. This proves condition 2.
3. For sufficiency, we first prove this claim by strong induction on $n$: a finite commuting family $T_1, \dots, T_r$ of diagonalizable maps of $V$ has a common basis of eigenvectors.
4. If every $T_i$ is a scalar multiple of $\id_V$, then every basis of $V$ works. This covers $n \le 1$.
5. Otherwise, choose $j$ with $T_j$ not scalar. Let $\lambda_1, \dots, \lambda_k$ be its distinct eigenvalues, and $E_m = \ker(T_j - \lambda_m \id_V)$.
6. Since $T_j$ is [[diagonalizable|0Y17PEKF24]], $V = E_1 \oplus \cdots \oplus E_k$, by the [[characterization by eigenvectors|056SW1E0AC]].
7. If $k = 1$, then $V = E_1$ and $T_j = \lambda_1 \id_V$, which contradicts step 5. So $k \ge 2$, and $\dim E_m < n$ for each $m$.
8. Each $T_i$ commutes with $T_j - \lambda_m \id_V$. So $E_m$ is $T_i$-invariant, by [[kernels of commuting maps are invariant|8YNE1HTZEP]].
9. Each restriction $T_i|_{E_m}$ is diagonalizable, by part 3 of the [[minimal polynomial criterion|0MPAJRB23T]].
10. The restrictions to $E_m$ commute, since $T_i T_l = T_l T_i$ on $V$.
11. By the induction hypothesis for $E_m$, there is a basis $\mathcal{B}_m$ of $E_m$ of common eigenvectors of the $T_i|_{E_m}$.
12. The sum in step 6 is [[direct|041JTZCK9Q]]. So the union $\mathcal{B}$ of $\mathcal{B}_1, \dots, \mathcal{B}_k$ is a basis of $V$.
13. Each vector of $\mathcal{B}$ is an eigenvector of each $T_i$. So all $T_i$ are diagonal in $\mathcal{B}$, which proves the claim.
14. Now let $\mathcal{F}$ be any commuting family of diagonalizable maps. Its span $W$ in $\operatorname{End}(V)$ has dimension at most $n^2$.
15. [[Every spanning set contains a basis|06MRNP4BNT]]. So some finite subset $\{T_1, \dots, T_r\}$ of $\mathcal{F}$ is a basis of $W$.
16. By the claim, there is a basis $\mathcal{B}$ of $V$ in which $T_1, \dots, T_r$ are diagonal.
17. Every $T \in \mathcal{F}$ is a linear combination $\sum_i c_i T_i$. So $[T]_{\mathcal{B}} = \sum_i c_i [T_i]_{\mathcal{B}}$ is diagonal. This proves condition 1.
18. For matrices, apply steps 1 to 17 to the maps $x \mapsto A x$ on $F^n$. The matrix $P$ has the basis $\mathcal{B}$ as columns.

## Idea

Commuting maps preserve each other's eigenspaces.
Choose a member that is not scalar; its eigenspaces are smaller invariant pieces.
On each piece, the restrictions are still diagonalizable and commuting, so induction applies.
An infinite family adds nothing new, since a finite part of it spans the same space of maps.

## Variants

One can avoid induction for two maps $A$ and $B$.
Write the projections onto the eigenspaces of $B$ as interpolation polynomials $\pi_j = \prod_{i \ne j} \frac{B - \mu_i}{\mu_j - \mu_i}$.
Each $\pi_j$ commutes with $A$, so it sends an eigenvector of $A$ to a common eigenvector or to $0$.
The pieces $\pi_j w$ of all eigenvectors $w$ of $A$ span $V$, and a basis can be chosen among them.
