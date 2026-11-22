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

We prove that condition 1 implies condition 2 by a computation with diagonal matrices.
For the converse we first treat a finite family by strong induction on $n = \dim V$, and then we reduce an infinite family to a finite one.

*From a common diagonal basis to commuting maps.*

1. Assume condition 1, with the basis $\mathcal{B}$.
   Two [[diagonal matrices|0Q9PGXD9E4]] commute, because their product in either order is diagonal with the products of the diagonal entries.
2. Matrices of maps multiply like the maps, so for $S, T \in \mathcal{F}$
   $$[S T]_{\mathcal{B}} = [S]_{\mathcal{B}} [T]_{\mathcal{B}} = [T]_{\mathcal{B}} [S]_{\mathcal{B}} = [T S]_{\mathcal{B}}.$$
   A map is determined by its matrix, so $S T = T S$, which is condition 2.

*A finite commuting family.*

3. We prove by strong induction on $n$ the following claim: commuting diagonalizable maps $T_1, \dots, T_r$ of $V$ have a common basis of eigenvectors.
4. If every $T_i$ is a scalar multiple of $\id_V$, then every basis of $V$ is a basis of eigenvectors of all of them.
   This case includes $n \le 1$, so the claim holds there.
5. Otherwise choose $j$ such that $T_j$ is not a scalar multiple of $\id_V$.
   Let $\lambda_1, \dots, \lambda_k$ be the distinct eigenvalues of $T_j$, and let $E_m = \ker(T_j - \lambda_m \id_V)$ be its [[eigenspaces|0AYEPBQMAW]].
6. Since $T_j$ is [[diagonalizable|0Y17PEKF24]], the [[characterization by eigenvectors|056SW1E0AC]] gives
   $$V = E_1 \oplus \dots \oplus E_k.$$
7. If $k = 1$, then $V = E_1$ and $T_j = \lambda_1 \id_V$, against the choice in step 5.
   So $k \ge 2$, and each $E_m$ is nonzero, so $\dim E_m < n$ for every $m$.
8. Each $T_i$ commutes with $T_j$, so it commutes with $T_j - \lambda_m \id_V$.
   By the result that [[kernels of commuting maps are invariant|8YNE1HTZEP]], each $E_m$ is $T_i$-invariant.
9. The restriction of a diagonalizable map to an invariant subspace is diagonalizable, by the [[minimal polynomial criterion|0MPAJRB23T]].
   So each $T_i|_{E_m}$ is diagonalizable.
10. The restrictions $T_i|_{E_m}$ commute pairwise, because $T_i T_l = T_l T_i$ holds on all of $V$ and so on $E_m$.
11. By step 7 and the induction hypothesis applied to $E_m$, there is a basis $\mathcal{B}_m$ of $E_m$ that consists of common eigenvectors of the maps $T_i|_{E_m}$.
12. The sum in step 6 is [[direct|041JTZCK9Q]], so the union $\mathcal{B}$ of $\mathcal{B}_1, \dots, \mathcal{B}_k$ is a basis of $V$.
13. Each vector of $\mathcal{B}$ is an eigenvector of each $T_i$, so every $T_i$ is diagonal in $\mathcal{B}$.
    This proves the claim.

*Any commuting family.*

14. Let $\mathcal{F}$ be any commuting family of diagonalizable maps, and let $W$ be its span in $\operatorname{End}(V)$.
    Then $\dim W \le \dim \operatorname{End}(V) = n^2$.
15. [[Every spanning set contains a basis|06MRNP4BNT]], so some finite subset $\{T_1, \dots, T_r\}$ of $\mathcal{F}$ is a basis of $W$.
16. By the claim, there is a basis $\mathcal{B}$ of $V$ in which $T_1, \dots, T_r$ are all diagonal.
17. Every $T \in \mathcal{F}$ is a linear combination $\sum_i c_i T_i$, so $[T]_{\mathcal{B}} = \sum_i c_i [T_i]_{\mathcal{B}}$ is a sum of diagonal matrices and is diagonal.
    This is condition 1.
18. For a set of matrices, apply steps 1 to 17 to the maps $x \mapsto A x$ on $F^n$.
    The matrix $P$ has the vectors of $\mathcal{B}$ as its columns.

## Idea

Commuting maps preserve each other's eigenspaces.
So we pick a member that is not a scalar, and its eigenspaces cut $V$ into smaller pieces that every member maps into themselves.
On each piece the restrictions are still diagonalizable and still commute, so induction finishes the job inside each piece.
An infinite family adds nothing new, since finitely many of its members span the same space of maps.

## Variants

For two maps $A$ and $B$ one can avoid the induction.
Let $\mu_1, \dots, \mu_k$ be the distinct eigenvalues of $B$, and write the projections onto its eigenspaces as Lagrange interpolation polynomials
$$\pi_j = \prod_{i \ne j} \frac{B - \mu_i \id_V}{\mu_j - \mu_i}.$$
Each $\pi_j$ is a polynomial in $B$, so it commutes with $A$, and it sends an eigenvector $w$ of $A$ to a common eigenvector of $A$ and $B$ or to $0$.
Since $w = \sum_j \pi_j w$ and the eigenvectors of $A$ span $V$, the vectors $\pi_j w$ span $V$, and a basis can be chosen among the nonzero ones.
