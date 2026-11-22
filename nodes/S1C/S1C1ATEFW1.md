---
tag: S1C1ATEFW1
kind: proof
name: Proof that row rank equals column rank by a factorization A = CR
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 0TZAG60ZYT
uses: [069MCGX635, 03AJKXH1AV, 09DXWYRD43, 0ZC9YTXZRY, 032Q9FB8MT, 08ZDRN6H41, 0QW084460E, 0QK7FPE6VE, 0KCQ9Y3QKA, 0DTY8B9HMS, 03GSZ8RTZJ]
methods: [S3QADD13E9]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proof using linear combinations
---

## Proof

We prove that the row rank is at most the column rank for every matrix, and then we apply this inequality to the transpose.
Let $A = (a_{ik})$ be an $m \times n$ matrix over a field $F$, with rows in $F^n$ and columns $\alpha_1, \dots, \alpha_n$ in $F^m$.

1. The [[row space|069MCGX635]] $\operatorname{Row}(A)$ is a subspace of $F^n$, and the [[column space|03AJKXH1AV]] $\operatorname{Col}(A)$ is a subspace of $F^m$.
These ambient spaces have dimensions $n$ and $m$, by the [[dimension of the coordinate space|0QK7FPE6VE]].
2. So both subspaces are finite-dimensional, by the [[dimension of a subspace|0QW084460E]], and we put $r = \dim \operatorname{Col}(A)$ and $d = \dim \operatorname{Row}(A)$.
3. We claim that $d \le r$.
If $r = 0$, every column of $A$ is zero, so $A = 0$, $\operatorname{Row}(A) = \{0\}$, and $d = 0 = r$.
4. Let $r \ge 1$, and let $\gamma_1, \dots, \gamma_r$ be a [[basis|0KCQ9Y3QKA]] of $\operatorname{Col}(A)$.
Let $C = (c_{il})$ be the $m \times r$ matrix with columns $\gamma_1, \dots, \gamma_r$.
5. Each column $\alpha_k$ lies in $\operatorname{Col}(A)$, so there are scalars $\rho_{lk} \in F$ with $\alpha_k = \sum_{l=1}^r \rho_{lk} \gamma_l$.
Let $R = (\rho_{lk})$, an $r \times n$ matrix.
6. Entry $i$ of the equation in step 5 reads
$$a_{ik} = \sum_{l=1}^r c_{il} \rho_{lk} \quad \text{for all } i \text{ and } k.$$
By the definition of the [[matrix product|032Q9FB8MT]], this says $A = CR$.
7. Now read the same equation with $i$ fixed and $k$ running.
It says that row $i$ of $A$ equals $\sum_{l=1}^r c_{il} \cdot (\text{row } l \text{ of } R)$.
8. So every row of $A$ lies in the [[span|0DTY8B9HMS]] $X \subseteq F^n$ of the $r$ rows of $R$, and $\operatorname{Row}(A) \subseteq X$.
9. A basis of $\operatorname{Row}(A)$ is an independent family of $d$ vectors in $X$, and $X$ is spanned by $r$ vectors.
The [[Steinitz exchange lemma|08ZDRN6H41]] gives $d \le r$, which proves the claim for every matrix.
10. The [[transpose|09DXWYRD43]] $A^{\mathsf{T}}$ has entries $(A^{\mathsf{T}})_{ki} = a_{ik}$, so its rows are the columns of $A$ and its columns are the rows of $A$.
Hence $\operatorname{Row}(A^{\mathsf{T}})$ and $\operatorname{Col}(A)$ have the same dimension, and so do $\operatorname{Col}(A^{\mathsf{T}})$ and $\operatorname{Row}(A)$.
11. The claim applied to $A^{\mathsf{T}}$ gives
$$r = \dim \operatorname{Row}(A^{\mathsf{T}}) \le \dim \operatorname{Col}(A^{\mathsf{T}}) = d.$$
12. Steps 9 and 11 give $d = r$, and by the definition of the [[rank|0ZC9YTXZRY]] this is $\rank A^{\mathsf{T}} = \rank A$.

## Idea

Choose a basis of the column space and write every column of $A$ in it.
This writes $A$ as a product $CR$ in which $R$ has only $r$ rows.
The same product, read row by row instead of column by column, says that every row of $A$ is a combination of those $r$ rows.
So the row space has dimension at most $r$, and the transpose gives the reverse inequality.

For example, the matrix with rows $(1, 2, 3)$ and $(2, 4, 6)$ has column space spanned by $\gamma_1 = (1, 2)$.
Then $C = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and $R = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$, and both rows of $A$ are multiples of the single row of $R$.

## Variants

The [[proof by row reduction|WK6YWCWJD0]] reaches the same equality by counting pivots, and it needs the theory of the reduced form.
The [[proof by orthogonality|4JYHHBC6J7]] works only over ordered fields such as $\mathbb{R}$.
The factorization of step 6 is the [[rank factorization|5JGAG62VN8]] of $A$, and when $C$ is taken to be the pivot columns of $A$, the matrix $R$ is the reduced row echelon form with its zero rows removed.
