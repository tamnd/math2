---
tag: Z04Y9W8CSY
kind: proof
name: Proof of the Fredholm alternative for matrices
msc: ["15A06"]
topics: [S6559D61BP]
audience: ug1
proves: 4HH8C9V8JQ
uses: [11CSKXQNG3, 5NKND0CPKP, 0TZAG60ZYT, 09GK5PS824, 0EWQEYRVA8, 0QW084460E]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_alternative
    locator: Linear algebra
---

## Proof

We show that the column space of $A$ equals the space $S$ cut out by the conditions, by one inclusion and a count of dimensions.

1. Let $r = \rank A$. By the [[theorem on the column space|11CSKXQNG3]], $\operatorname{Col}(A) = \{Ax : x \in F^n\}$, and $\dim \operatorname{Col}(A) = r$.
2. So $Ax = b$ has a solution if and only if $b \in \operatorname{Col}(A)$.
3. Let $N = \operatorname{Null}(A^\top) = \{y \in F^m : A^\top y = 0\}$, and let $S = \{b \in F^m : y^\top b = 0 \text{ for all } y \in N\}$. The set $S$ is a subspace of $F^m$, since each condition $y^\top b = 0$ is linear in $b$.
4. Inclusion. Let $b = Ax$ and $y \in N$. By the [[transpose of a product|09GK5PS824]], $y^\top A = (A^\top y)^\top = 0^\top$. So $y^\top b = (y^\top A) x = 0$. Hence $\operatorname{Col}(A) \subseteq S$.
5. Dimension of $N$. The matrix $A^\top$ is $n \times m$. By the [[theorem on the free variables|5NKND0CPKP]], $\dim N = m - \rank(A^\top)$.
6. By the theorem that [[row rank equals column rank|0TZAG60ZYT]], $\rank(A^\top) = r$. So $\dim N = m - r$. Put $k = m - r$.
7. Dimension of $S$. Let $y_1, \dots, y_k$ be a basis of $N$, and let $Y$ be the $k \times m$ matrix with rows $y_1^\top, \dots, y_k^\top$.
8. Then $S = \operatorname{Null}(Y)$, since $b \in S$ if and only if $y_i^\top b = 0$ for each $i$, by linearity in $y$.
9. The columns of $Y^\top$ are $y_1, \dots, y_k$, which are linearly independent. So $\rank(Y^\top) = k$, by the [[definition of the rank|0EWQEYRVA8]]. Since row rank equals column rank, $\rank Y = k$ too.
10. By the theorem on the free variables, $\dim S = \dim \operatorname{Null}(Y) = m - k = r$.
11. By steps 1, 4 and 10, $\operatorname{Col}(A)$ is a subspace of $S$ of the same dimension $r$. By the [[theorem on the dimension of a subspace|0QW084460E]], $\operatorname{Col}(A) = S$.
12. Part 1. By steps 2 and 11, $Ax = b$ is solvable if and only if $b \in S$, that is, $y^\top b = 0$ for all $y \in N$.
13. Part 2. Case (b) says exactly that $b \notin S$. By step 12, this is the negation of case (a). So exactly one of (a) and (b) holds.
14. Part 3, with $m = n$. By the theorem on the free variables, $\dim \operatorname{Null}(A) = n - r$. By step 6, $\dim N = n - r$ too.
15. If $r = n$, then $\operatorname{Null}(A) = \{0\}$, so $Ax = b$ has at most one solution. Also $\operatorname{Col}(A)$ is a subspace of $F^n$ of dimension $n$, so $\operatorname{Col}(A) = F^n$ by the theorem on the dimension of a subspace. So case (a) holds.
16. If $r < n$, then $\dim \operatorname{Null}(A) = n - r \ge 1$, so $Ax = 0$ has a solution $x \ne 0$. So case (b) holds, and $\dim N = n - r \ge 1$ gives $y \ne 0$ with $A^\top y = 0$.
17. Cases (a) and (b) exclude each other: in case (a) with $b = 0$, the only solution of $Ax = 0$ is $x = 0$. Together with steps 15 and 16, exactly one case holds. $\blacksquare$

## Idea

Every solvable right side $b = Ax$ satisfies $y^\top b = 0$ for every $y$ with $A^\top y = 0$.
So the column space lies inside the space $S$ cut out by these conditions.
Both spaces have dimension $r$, because row rank equals column rank, so they are equal.

## Variants

- Over $\R$, the statement is $\operatorname{Col}(A) = \operatorname{Null}(A^\top)^\perp$, which follows from the [[four fundamental subspaces|73DVECPAT6]] and $(W^\perp)^\perp = W$.
- With duality: the image of a linear map is the annihilator of the kernel of its dual map. This proof belongs to the duality sub-area and uses the [[dual map|0AZ5ARP287]].
- Part 3 also follows from the [[rank-nullity theorem|0W4FSW1TVB]]: an endomorphism of a finite-dimensional space is injective if and only if it is surjective.
