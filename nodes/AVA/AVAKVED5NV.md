---
tag: AVAKVED5NV
kind: proof
name: Proof of the normal equations
msc: [65F20, 15A06]
topics: [8GQVME4SZZ]
audience: ug1
proves: 4D7MRG4D91
uses: [T5Q51M5BAK, V9AH43ZY91, 0MCDDSCB9Z, GQF2KG1R1N, 0PQ2GGY1QV, 0CRMGPAH83, ACDFDABVQK, TR48YQGCCA, 0W809K6AW0]
methods: [TFQ1845T84, MKHVRNW68H]
sources:
  - book: isbn:9780321982384
    locator: Section 6.5
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
---

## Proof

Let $U = \operatorname{Col}(A)$ and let $p$ be the orthogonal projection of $b$ onto $U$.

1. By part 2 of [[existence and uniqueness of least-squares solutions|V9AH43ZY91]], $\hat x$ is a least-squares solution if and only if $A \hat x = p$.
2. $A \hat x$ lies in $U$. By part 3 of the [[best approximation theorem|0MCDDSCB9Z]], $A \hat x = p$ holds if and only if $b - A \hat x \in U^\perp$.
3. $U^\perp$ is the set of vectors orthogonal to every column of $A$, by the definition of $\operatorname{Col}(A)$ as the span of the columns and part 3 of the [[basic properties of complements|T5Q51M5BAK]]. Steps 1 and 2 now give part 2.
4. By part 3 of the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]], $U^\perp = \operatorname{Col}(A)^\perp = \operatorname{Nul}(A^{\mathsf{T}})$.
5. So $b - A \hat x \in U^\perp$ if and only if $A^{\mathsf{T}} (b - A \hat x) = 0$, that is, $A^{\mathsf{T}} A \hat x = A^{\mathsf{T}} b$. With steps 1 and 2 this proves part 1 in both directions.
6. Part 3: by part 1 of existence and uniqueness, a least-squares solution exists, and by part 1 it solves the normal equations.
7. Part 4, first inclusion: if $Ax = 0$, then $A^{\mathsf{T}} A x = A^{\mathsf{T}} 0 = 0$.
8. Part 4, second inclusion: if $A^{\mathsf{T}} A x = 0$, then $\norm{Ax}^2 = (Ax)^{\mathsf{T}} (Ax) = x^{\mathsf{T}} (A^{\mathsf{T}} A x) = 0$. So $Ax = 0$.
9. Steps 7 and 8 give $\operatorname{Nul}(A^{\mathsf{T}} A) = \operatorname{Nul}(A)$. Both matrices have $n$ columns, so [[rank-nullity|TR48YQGCCA]] gives $\rank(A^{\mathsf{T}} A) = n - \dim \operatorname{Nul}(A) = \rank A$.
10. Part 5: by the [[invertible matrix theorem|ACDFDABVQK]], the square matrix $A^{\mathsf{T}} A$ is invertible if and only if its null space is $\set{0}$.
11. By step 9, this holds if and only if $\operatorname{Nul}(A) = \set{0}$, which means that the columns of $A$ are [[linearly independent|0CRMGPAH83]].
12. When $A^{\mathsf{T}} A$ is invertible, the normal equations have the unique solution $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} b$, and by part 1 this is the unique least-squares solution.
13. Over $\C$, the same steps work with $A^*$ in place of $A^{\mathsf{T}}$, using $\operatorname{Col}(A)^\perp = \operatorname{Nul}(A^*)$ and $\norm{Ax}^2 = x^* A^* A x$.

## Idea

The best approximation is characterized by an orthogonality condition: the residual is orthogonal to the column space.
Orthogonality to every column is one linear equation per column, and these equations together are $A^{\mathsf{T}} (b - A \hat x) = 0$.
The key identity $x^{\mathsf{T}} A^{\mathsf{T}} A x = \norm{Ax}^2$ links the null spaces of $A$ and $A^{\mathsf{T}} A$.

## Variants

By calculus: $f(x) = \norm{Ax - b}^2 = x^{\mathsf{T}} A^{\mathsf{T}} A x - 2 b^{\mathsf{T}} A x + b^{\mathsf{T}} b$ has gradient $2 (A^{\mathsf{T}} A x - A^{\mathsf{T}} b)$.
The function is convex, so its minimizers are exactly its critical points, which are the solutions of the normal equations.
