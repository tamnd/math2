---
tag: YT9XQ7NNJZ
kind: proof
name: Proof of the formulas for the orthogonal projection
msc: [15A04, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
proves: AK3JJ5HHG2
uses: [0Q8HZTJC7G, 0SP7P0G7KQ, GQF2KG1R1N, 0EX045E2BP, 0EB9N0S33C, 0EVHJFTG9Z, 0PDVQEP0ZC]
methods: [0NTF6DMVAP]
sources:
  - book: isbn:9780321982384
    locator: Section 6.3
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Formulas
---

## Proof

We use one test throughout: a candidate $p$ equals $Pv$ as soon as $p \in U$ and $v - p \in U^\perp$.
The test is valid because, by the [[orthogonal decomposition|0SP7P0G7KQ]], each $v \in V$ is $v = u + u'$ with unique $u \in U$ and $u' \in U^\perp$, and $Pv = u$ by the [[definition|0Q8HZTJC7G]].

1. Linearity: for $v, w \in V$ and $a, b \in \mathbb{K}$ we can write
$$av + bw = \bigl(aPv + bPw\bigr) + \bigl(a(v - Pv) + b(w - Pw)\bigr),$$
where the first bracket lies in the subspace $U$ and the second in the subspace $U^\perp$, so the test gives $P(av + bw) = aPv + bPw$.
2. For $u \in U$ the splitting $u = u + 0$ passes the test, so $Pu = u$.
3. For every $v$ we have $Pv \in U$, so step 2 gives $P(Pv) = Pv$, and hence $P^2 = P$.
4. The image of $P$ lies in $U$ by the definition and contains $U$ by step 2, so the image is $U$.
5. If $v \in U^\perp$, the splitting $v = 0 + v$ passes the test, so $Pv = 0$.
6. Conversely, if $Pv = 0$, then $v = Pv + (v - Pv) = v - Pv$ lies in $U^\perp$, so the kernel of $P$ is $U^\perp$, which completes part 1.
7. Part 2 is part 2 of the orthogonal decomposition theorem, which builds the component in $U$ as $\sum_{i} \ip{v}{e_i} e_i$.
8. For part 3, set $e_i = u_i / \norm{u_i}$; these $k = \dim U$ vectors are pairwise orthogonal of norm $1$, so they form an orthonormal basis of $U$.
9. Linearity in the first argument and conjugate linearity in the second give
$$\ip{v}{e_i} e_i = \frac{1}{\norm{u_i}^2} \ip{v}{u_i} u_i = \frac{\ip{v}{u_i}}{\ip{u_i}{u_i}} u_i,$$
so part 2 turns into part 3.
10. For the invertibility in part 4, let $x \in \mathbb{K}^k$ with $A^* A x = 0$; the rule $(BC)^* = C^* B^*$ for the [[conjugate transpose|0EX045E2BP]] gives
$$\norm{Ax}^2 = (Ax)^* (Ax) = x^* (A^* A x) = 0.$$
11. So $Ax = 0$, and since $Ax$ is the combination of the columns of $A$ with coefficients $x_j$ and the columns are [[linearly independent|0EVHJFTG9Z]], we get $x = 0$.
12. Hence the $k \times k$ matrix $A^* A$ has null space $\{0\}$, so it is [[invertible|0EB9N0S33C]].
13. For the formula in part 4, let $v \in \mathbb{K}^n$, set $c = (A^* A)^{-1} A^* v$ and $p = A c$, and note that $p$ is a combination of the columns of $A$, so $p \in U$.
14. The error satisfies
$$A^* (v - p) = A^* v - A^* A (A^* A)^{-1} A^* v = A^* v - A^* v = 0,$$
so $v - p$ lies in the null space of $A^*$.
15. By the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]], the null space of $A^*$ is $\operatorname{Col}(A)^\perp = U^\perp$, so $v - p \in U^\perp$.
16. The test gives $Pv = p = A (A^* A)^{-1} A^* v$, and over $\R$ we have $A^* = A^{\mathsf{T}}$, which proves part 4.
17. For part 5, entry $(i, j)$ of $Q^* Q$ is $q_i^* q_j = \ip{q_j}{q_i}$, which is $1$ for $i = j$ and $0$ otherwise because the columns are orthonormal.
18. So $Q^* Q = I$, and part 4 gives $P = Q I^{-1} Q^* = Q Q^*$.

## Idea

The orthogonal projection is pinned down by two conditions: the answer lies in $U$, and the error is orthogonal to $U$.
Each formula visibly produces a vector of $U$, so the only work is a short computation that shows the error is orthogonal to $U$.
For the matrix formula, the error condition reads $A^* (v - p) = 0$, which is a linear system for the coefficients of $p$, and the formula is its solution.

## Variants

Part 4 also follows from part 5 by the [[QR decomposition|0ERWG4NXQ9]].
If $A = Q R$ with orthonormal columns in $Q$ and an invertible upper triangular $R$, then $A^* A = R^* R$, and
$$A (A^* A)^{-1} A^* = Q R \, R^{-1} (R^*)^{-1} \, R^* Q^* = Q Q^*.$$
Since $Q$ and $A$ have the same column space, part 5 finishes the argument.
