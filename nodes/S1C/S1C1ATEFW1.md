---
tag: S1C1ATEFW1
kind: proof
name: Proof that row rank equals column rank by a factorization A = CR
msc: [15A03]
proves: 0TZAG60ZYT
uses: [069MCGX635, 03AJKXH1AV, 09DXWYRD43, 0ZC9YTXZRY, 032Q9FB8MT, 08ZDRN6H41, 0QW084460E, 0QK7FPE6VE, 0KCQ9Y3QKA, 0DTY8B9HMS, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proof using linear combinations
---

## Proof

We first prove that the row rank is at most the column rank for every matrix, and then apply this to the transpose.

1. Let $A = (a_{ik})$ be an $m \times n$ matrix over $F$. We view its rows as vectors of $F^n$ and its columns as vectors of $F^m$.
2. Let $\operatorname{Row}(A) \subseteq F^n$ be the [[row space|069MCGX635]] and $\operatorname{Col}(A) \subseteq F^m$ the [[column space|03AJKXH1AV]]. The spaces $F^n$ and $F^m$ have dimensions $n$ and $m$ by [[the dimension of the coordinate space|0QK7FPE6VE]].
3. So both spaces are finite-dimensional by the [[dimension of a subspace|0QW084460E]], and they have a [[dimension|03GSZ8RTZJ]]. Let $r = \dim \operatorname{Col}(A)$ and $d = \dim \operatorname{Row}(A)$.
4. Claim: $d \le r$. If $r = 0$, then every column of $A$ is $0$. So $A = 0$, $\operatorname{Row}(A) = \{0\}$, and $d = 0 = r$.
5. Let $r \ge 1$, and let $(\gamma_1, \dots, \gamma_r)$ be a [[basis|0KCQ9Y3QKA]] of $\operatorname{Col}(A)$. Let $C = (c_{il})$ be the $m \times r$ matrix with columns $\gamma_1, \dots, \gamma_r$.
6. Each column $\alpha_k$ of $A$ lies in $\operatorname{Col}(A)$. So $\alpha_k = \sum_{l=1}^r \rho_{lk} \gamma_l$ for some scalars $\rho_{lk} \in F$. Let $R = (\rho_{lk})$, an $r \times n$ matrix.
7. Comparing entry $i$ in step 6 gives $a_{ik} = \sum_{l=1}^r c_{il} \rho_{lk}$ for all $i$ and $k$. By the definition of the [[matrix product|032Q9FB8MT]], this says $A = CR$.
8. Fix a row index $i$. By step 7, for each $k$, entry $k$ of row $i$ of $A$ is $\sum_{l=1}^r c_{il} \rho_{lk}$. So row $i$ of $A$ equals $\sum_{l=1}^r c_{il} \cdot (\text{row } l \text{ of } R)$.
9. Let $X \subseteq F^n$ be the [[span|0DTY8B9HMS]] of the $r$ rows of $R$. By step 8, every row of $A$ lies in $X$, so $\operatorname{Row}(A) \subseteq X$.
10. A basis of $\operatorname{Row}(A)$ is a linearly independent family of $d$ vectors of $X$. The $r$ rows of $R$ span $X$. By the [[Steinitz exchange lemma|08ZDRN6H41]], $d \le r$.
11. This proves the claim $\dim \operatorname{Row}(A) \le \dim \operatorname{Col}(A)$ for every matrix $A$.
12. Now let $A^T$ be the [[transpose|09DXWYRD43]], with entries $(A^T)_{ki} = a_{ik}$. Row $k$ of $A^T$ has entries $a_{1k}, \dots, a_{mk}$, which is column $k$ of $A$.
13. So the rows of $A^T$ are the columns of $A$, and the columns of $A^T$ are the rows of $A$. Hence $\operatorname{Row}(A^T) = \operatorname{Col}(A)$ and $\operatorname{Col}(A^T) = \operatorname{Row}(A)$.
14. Applying step 11 to $A^T$ gives $\dim \operatorname{Col}(A) = \dim \operatorname{Row}(A^T) \le \dim \operatorname{Col}(A^T) = \dim \operatorname{Row}(A)$.
15. Together with step 11, $\dim \operatorname{Row}(A) = \dim \operatorname{Col}(A)$.
16. By the definition of the [[rank|0ZC9YTXZRY]], $\rank A^T = \dim \operatorname{Col}(A^T) = \dim \operatorname{Row}(A) = \dim \operatorname{Col}(A) = \rank A$.

## Idea

Choose a basis of the column space and write every column of $A$ in it; this factors $A = CR$ with $R$ having only $r$ rows. The same factorization shows that every row of $A$ is a combination of those $r$ rows. So the row space is no bigger than the column space, and the transpose gives the reverse inequality.
