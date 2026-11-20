---
tag: A3KBTY9JW7
kind: proof
name: Proof of the theorem on the four fundamental subspaces
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 73DVECPAT6
uses: [0EWQEYRVA8, 5NKND0CPKP, 0TZAG60ZYT, 0PDVQEP0ZC, 05HQYM0R4G, 079D68S3AW, 06HTJNCMPA, 0QW084460E, 11CSKXQNG3]
methods: [0NTF6DMVAP, MKHVRNW68H]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_algebra
    locator: lead section
---

## Proof

1. By the [[definition of rank|0EWQEYRVA8]], $\dim \operatorname{Col}(A) = r$.
2. By the [[theorem on the free variables|5NKND0CPKP]], $\dim \operatorname{Null}(A) = n - r$.
3. The rows of $A$ are the columns of $A^\top$, so $\operatorname{Row}(A) = \operatorname{Col}(A^\top)$. So $\dim \operatorname{Row}(A) = \rank A^\top = r$, by [[row rank equals column rank|0TZAG60ZYT]].
4. The matrix $A^\top$ is $n \times m$ of rank $r$, by step 3. The [[theorem on the free variables|5NKND0CPKP]] for $A^\top$ gives $\dim \operatorname{Null}(A^\top) = m - r$. This proves part 1.
5. Now let $F = \R$, and let $a_1, \dots, a_m \in \R^n$ be the rows of $A$. By the [[matrix-vector product|0PDVQEP0ZC]], entry $i$ of $Ax$ is the [[dot product|05HQYM0R4G]] $a_i \cdot x$.
6. So $Ax = 0$ if and only if $a_i \cdot x = 0$ for every $i$.
7. The dot product is linear in each argument. So $x$ is orthogonal to every $a_i$ if and only if it is orthogonal to every combination of them, that is, to $\operatorname{Row}(A)$.
8. Steps 6 and 7 give $\operatorname{Null}(A) = \operatorname{Row}(A)^\perp$, by the [[definition of the orthogonal complement|079D68S3AW]].
9. Steps 5 to 8 for $A^\top$ give $\operatorname{Null}(A^\top) = \operatorname{Row}(A^\top)^\perp = \operatorname{Col}(A)^\perp$, by step 3 for $A^\top$. This proves part 2.
10. Let $v \in \operatorname{Row}(A) \cap \operatorname{Null}(A)$. By step 8, $v \cdot v = 0$, that is, $v_1^2 + \dots + v_n^2 = 0$. A sum of real squares is $0$ only if each term is $0$, so $v = 0$.
11. By the [[dimension formula for a sum|06HTJNCMPA]], $\dim(\operatorname{Row}(A) + \operatorname{Null}(A)) = r + (n - r) - 0 = n$.
12. A subspace of $\R^n$ of dimension $n$ is $\R^n$, by the [[dimension of a subspace|0QW084460E]]. With step 10, $\R^n = \operatorname{Row}(A) \oplus \operatorname{Null}(A)$.
13. Steps 10 to 12 for $A^\top$ give $\R^m = \operatorname{Col}(A) \oplus \operatorname{Null}(A^\top)$. This proves part 3.
14. Let $L \colon \operatorname{Row}(A) \to \R^m$, $L(u) = Au$. Its kernel is $\operatorname{Row}(A) \cap \operatorname{Null}(A) = \{0\}$ by step 10, so $L$ is injective.
15. Let $b \in \operatorname{Col}(A)$. By the [[theorem on the column space|11CSKXQNG3]], part 1, $b = Ax$ for some $x \in \R^n$.
16. By step 12, $x = u + w$ with $u \in \operatorname{Row}(A)$ and $w \in \operatorname{Null}(A)$. Then $b = Au + Aw = Au = L(u)$.
17. Also $L(u) = Au \in \operatorname{Col}(A)$ for every $u$, by the same theorem. So $L$ maps onto $\operatorname{Col}(A)$, and it is a linear isomorphism by steps 14 and 16. This proves part 4.

## Idea

The dimensions come from the rank, from the free variables and from row rank equals column rank.
Over $\R$, each equation of $Ax = 0$ says that $x$ is orthogonal to one row.
Positivity of $v \cdot v$ makes the row space and the null space meet only in $0$, and a dimension count gives the direct sums.

## Variants

The orthogonality can also be read from the [[dimension of the orthogonal complement|0E2NYPVSP9]] once $\operatorname{Null}(A) = \operatorname{Row}(A)^\perp$ is known.
Over a general field, the dual map gives the same dimension count without any inner product.
