---
tag: 6G6ZHPR66X
kind: proof
name: Proof of the existence of an orthonormal basis by the Gram–Schmidt process
msc: [15A63, 46C05]
proves: 0Y85GYEGSF
uses: [0VGSYBWHV2, 0KG4D8AP6G, 09VYHEF2VT, 0FWJ0VW561, 0JWM6GJNQW, 0M4SXE5WW3, 0WK0Y8RH1M, 0VT6P0GNQR, 0WXBGBTA3D, 096V7H13H9, 0HR573CHNM]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorems 6.35 and 6.36
---

## Proof

We first prove the extension statement. The existence then follows by extending the empty family.

1. Let $V$ be an inner product space over $\R$ or $\C$ of finite dimension $n$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
2. Let $(e_i)_{i \in I}$ be an [[orthonormal family|09VYHEF2VT]] in $V$. Its vectors are distinct, since $\ip{e_i}{e_j} = 0 \ne 1 = \ip{e_i}{e_i}$ for $i \ne j$.
3. The family is [[linearly independent|0JWM6GJNQW]]. So its set of vectors [[extends to a basis|0M4SXE5WW3]] $B$ of $V$.
4. All bases of $V$ [[have the same cardinality|0WK0Y8RH1M]], so $B$ has $n$ elements. Hence the family is finite. Write it $e_1, \dots, e_m$ with $m \le n$.
5. List $B$ as $v_1, \dots, v_n$ with $v_i = e_i$ for $i \le m$. Let $u_1, \dots, u_n$ be the vectors of the [[Gram–Schmidt process|0VT6P0GNQR]] applied to $v_1, \dots, v_n$.
6. We show $u_j = e_j$ for $j \le m$, by induction on $j$. First, $u_1 = v_1 = e_1$.
7. Let $2 \le j \le m$ and assume $u_i = e_i$ for $i < j$. Then $u_j = e_j - \sum_{i<j} \frac{\ip{e_j}{e_i}}{\ip{e_i}{e_i}} e_i = e_j$, because $\ip{e_j}{e_i} = 0$ for $i \ne j$.
8. By the [[properties of the Gram–Schmidt vectors|0WXBGBTA3D]], $u_1, \dots, u_n$ are nonzero and pairwise orthogonal. Also $\operatorname{span}(u_1, \dots, u_n) = \operatorname{span}(v_1, \dots, v_n) = V$.
9. Set $f_j = u_j / \norm{u_j}$, which is defined since $u_j \ne 0$. Then $\ip{f_j}{f_j} = \ip{u_j}{u_j} / \norm{u_j}^2 = 1$.
10. For $i \ne j$, $\ip{f_i}{f_j} = \ip{u_i}{u_j} / (\norm{u_i} \norm{u_j}) = 0$, since $\norm{u_j}$ is real. So $f_1, \dots, f_n$ is an orthonormal family.
11. For $j \le m$, $f_j = e_j / \norm{e_j} = e_j$, since $\norm{e_j} = 1$.
12. The family $f_1, \dots, f_n$ is linearly independent by step 10 and [[the same result|0JWM6GJNQW]] as in step 3. It has $n = \dim V$ vectors, so it is [[a basis|096V7H13H9]] of $V$.
13. So $f_1, \dots, f_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$ that extends $e_1, \dots, e_m$. This proves the second claim.
14. The empty family is orthonormal, because the condition on pairs is vacuous. Applying step 13 to it gives an orthonormal basis of $V$. This proves the first claim.

## Idea

Extend the orthonormal family to any basis, then run Gram–Schmidt and normalise. The process leaves the first vectors alone, because they are already orthogonal unit vectors. The output is orthonormal, hence independent, and has the right number of vectors to be a basis.
