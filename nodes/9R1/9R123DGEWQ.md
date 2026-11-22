---
tag: 9R123DGEWQ
kind: proof
name: Proof of the rank factorization theorem
msc: ["15A03", "15A23"]
topics: [S6559D61BP]
audience: ug1
proves: 5JGAG62VN8
uses: [0EWQEYRVA8, 0VTQTPQGAV, 076JGP6R3T, 11CSKXQNG3, E4GKK727ZM, 0NNR68BFRY, 0W4FSW1TVB, 08ZDRN6H41]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_factorization
    locator: Existence
---

## Proof

We put a basis of the column space into $C$ and the coordinates of the columns of $A$ in that basis into $R$; the four parts then follow by reading the product $CR$ in different ways.
Let $A$ be an $m \times n$ matrix over a field $F$ of rank $r \ge 1$, with columns $a_1, \dots, a_n$.

1. By the [[definition of rank|0EWQEYRVA8]], $\operatorname{Col}(A)$ has dimension $r$, so it has a [[basis|0VTQTPQGAV]] $c_1, \dots, c_r$.
Let $C$ be the $m \times r$ matrix with these columns.
2. The column space of $C$ is the span of $c_1, \dots, c_r$, so $\operatorname{Col}(C) = \operatorname{Col}(A)$ and $\rank C = r$.
3. Each column $a_k$ lies in $\operatorname{Col}(A)$, so $a_k = \sum_{l=1}^r \rho_{lk} c_l$ for unique scalars $\rho_{lk}$.
Let $R = (\rho_{lk})$, an $r \times n$ matrix.
4. By the definition of the [[matrix product|076JGP6R3T]], column $k$ of $CR$ is $\sum_l \rho_{lk} c_l = a_k$, so $A = CR$.
5. The map $y \mapsto Cy$ from $F^r$ to $F^m$ is injective, because $Cy = \sum_l y_l c_l = 0$ forces $y = 0$ by independence.
6. Column $k$ of $A$ is $C$ times column $k$ of $R$, so $y \mapsto Cy$ maps $\operatorname{Col}(R)$ onto $\operatorname{Col}(A)$.
7. Restricted to $\operatorname{Col}(R)$, this map is injective by step 5 and has image $\operatorname{Col}(A)$ by step 6.
So the [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim \operatorname{Col}(R) = \dim \operatorname{Col}(A) = r$, that is, $\rank R = r$.
This proves part 1.
8. For part 2, let $R_0$ be the reduced row echelon form of $A$, with pivot columns $p_1 < \dots < p_r$.
By the [[pivot basis theorem|11CSKXQNG3]], $a_{p_1}, \dots, a_{p_r}$ is a basis of $\operatorname{Col}(A)$, so we may take $c_i = a_{p_i}$ in step 1.
9. In the [[reduced form|0NNR68BFRY]], column $p_i$ is the unit vector $e_i$, and the last $m - r$ rows are zero.
So every column of $R_0$ is a combination of its pivot columns: column $k$ of $R_0$ equals $\sum_{i=1}^r (R_0)_{ik}$ times column $p_i$ of $R_0$.
10. By the [[theorem on row equivalence|E4GKK727ZM]], $A$ and $R_0$ have the same null space, so a linear relation holds among the columns of $A$ exactly when it holds among the same columns of $R_0$.
11. Steps 9 and 10 give $a_k = \sum_{i=1}^r (R_0)_{ik} a_{p_i}$.
By the uniqueness in step 3, $R$ consists of the first $r$ rows of $R_0$, which are its nonzero rows.
This proves part 2.
12. For part 3, let $\rho_l$ be row $l$ of $R$.
Entry $(i, k)$ of $CR$ is $\sum_l (c_l)_i \rho_{lk}$, so $A = \sum_{l=1}^r c_l \rho_l$, a sum of $r$ products of a column with a row.
13. The columns of $c_l \rho_l$ are the vectors $\rho_{lk} c_l$, all multiples of $c_l$, so $\rank(c_l \rho_l) \le 1$.
14. Each row $\rho_l$ is nonzero.
Indeed, by step 7, $\operatorname{Col}(R)$ is a subspace of $F^r$ of dimension $r$, so it is all of $F^r$ and contains the unit vector $e_l$.
If row $l$ of $R$ were zero, every vector in $\operatorname{Col}(R)$ would have entry $l$ equal to $0$, which $e_l$ does not.
Since also $c_l \ne 0$, some column $\rho_{lk} c_l$ is nonzero, and $c_l \rho_l$ has rank exactly $1$.
15. Now let $A' = \sum_{l=1}^s u_l v_l^{\mathsf{T}}$ be any sum of $s$ matrices of rank at most $1$, written as column times row.
Column $k$ of $A'$ is $\sum_l (v_l)_k u_l$, so $\operatorname{Col}(A')$ lies in the span of $u_1, \dots, u_s$.
By the [[Steinitz exchange lemma|08ZDRN6H41]], that span has dimension at most $s$, so $\rank A' \le s$.
This proves part 3.
16. For part 4, let $\rank A = 1$.
Part 1 with $r = 1$ gives $A = CR$ with $C = u$ a nonzero column and $R = v^{\mathsf{T}}$ a nonzero row.
17. Conversely, let $A = uv^{\mathsf{T}}$ with $u \ne 0$ and $v \ne 0$.
Column $k$ of $A$ is $v_k u$, and some $v_k$ is nonzero, so $\operatorname{Col}(A) = \operatorname{span}(u)$ and $\rank A = 1$.
This proves part 4.

## Idea

Choose a basis of the column space as the columns of $C$, and record in $R$ the coordinates of each column of $A$ in that basis.
The pivot columns of $A$ give one such basis, and the reduced form records the coordinates, because row operations keep the relations among the columns.
For example, if column 4 of $A$ equals column 1 plus twice column 3, and columns 1 and 3 are the pivots, then column 4 of $R$ is $(1, 2)$.
Expanding the product $CR$ column by row writes $A$ as a sum of $r$ rank-one matrices.

## Variants

The proof that [[row rank equals column rank by a factorization|S1C1ATEFW1]] starts from the factorization of step 4.
Each row of $A = CR$ is a combination of the $r$ rows of $R$, so the row space has dimension at most $r$.

Over $\mathbb{R}$, the singular value decomposition gives another rank factorization, $A = \sum_{l=1}^r \sigma_l u_l v_l^{\mathsf{T}}$ with orthonormal $u_l$ and orthonormal $v_l$.
