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

We write the orthogonality condition of best approximation as one linear equation for each column of $A$, and then we compare the null spaces of $A$ and $A^{\mathsf{T}} A$.
Let $U = \operatorname{Col}(A)$, let $a_1, \dots, a_n$ be the columns of $A$, and let $p$ be the orthogonal projection of $b$ onto $U$.

1. By [[existence and uniqueness of least-squares solutions|V9AH43ZY91]], $\hat x$ is a least-squares solution if and only if $A \hat x = p$.
2. The vector $A \hat x$ lies in $U$, so the characterization part of the [[best approximation theorem|0MCDDSCB9Z]] says that $A \hat x = p$ holds if and only if $b - A \hat x \in U^\perp$.
3. The columns span $U$, and a vector is orthogonal to a subspace exactly when it is orthogonal to a spanning set, by the [[basic properties of complements|T5Q51M5BAK]].
4. So $b - A \hat x \in U^\perp$ holds if and only if $b - A \hat x$ is orthogonal to every column $a_j$, and steps 1 and 2 now give part 2.
5. Row $j$ of $A^{\mathsf{T}}$ is $a_j^{\mathsf{T}}$, so entry $j$ of $A^{\mathsf{T}} (b - A \hat x)$ is $a_j \cdot (b - A \hat x)$.
6. Hence $b - A \hat x$ is orthogonal to every column if and only if $A^{\mathsf{T}} (b - A \hat x) = 0$, that is, $A^{\mathsf{T}} A \hat x = A^{\mathsf{T}} b$, and this proves part 1.
7. For part 3, existence and uniqueness gives a least-squares solution, and by part 1 it solves the normal equations.
8. For part 4, first let $Ax = 0$; then $A^{\mathsf{T}} A x = A^{\mathsf{T}} 0 = 0$, so $\operatorname{Nul}(A) \subseteq \operatorname{Nul}(A^{\mathsf{T}} A)$.
9. Conversely, let $A^{\mathsf{T}} A x = 0$, and compute the squared length of $Ax$:
$$\norm{Ax}^2 = (Ax)^{\mathsf{T}} (Ax) = x^{\mathsf{T}} (A^{\mathsf{T}} A x) = x^{\mathsf{T}} 0 = 0.$$
10. A vector of length $0$ is the zero vector, so $Ax = 0$, and $\operatorname{Nul}(A^{\mathsf{T}} A) \subseteq \operatorname{Nul}(A)$.
11. Both matrices have $n$ columns and the same null space, so [[rank-nullity|TR48YQGCCA]] gives $\rank(A^{\mathsf{T}} A) = n - \dim \operatorname{Nul}(A) = \rank A$.
12. For part 5, the [[invertible matrix theorem|ACDFDABVQK]] says that the square matrix $A^{\mathsf{T}} A$ is invertible if and only if its null space is $\{0\}$.
13. By part 4, this holds if and only if $\operatorname{Nul}(A) = \{0\}$, which means that the columns of $A$ are [[linearly independent|0CRMGPAH83]].
14. When $A^{\mathsf{T}} A$ is invertible, the normal equations have the unique solution $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} b$, and by part 1 this is the unique least-squares solution.
15. Over $\C$ the same steps work with $A^*$ in place of $A^{\mathsf{T}}$, since entry $j$ of $A^* y$ is $\ip{y}{a_j}$ and $\norm{Ax}^2 = x^* A^* A x$.

This proves all five parts.

## Idea

The best approximation is the point where the error is perpendicular to the subspace.
Perpendicular to the column space means perpendicular to each column, which is one linear equation for each column, and these $n$ equations together read $A^{\mathsf{T}} (b - A \hat x) = 0$.
Steps 5 and 6 are the statement $\operatorname{Col}(A)^\perp = \operatorname{Nul}(A^{\mathsf{T}})$ from the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]], proved here on the spot.
The identity $x^{\mathsf{T}} A^{\mathsf{T}} A x = \norm{Ax}^2$ is what links the null spaces of $A$ and $A^{\mathsf{T}} A$.

## Variants

There is a proof by calculus.
Expand the squared error:
$$f(x) = \norm{Ax - b}^2 = x^{\mathsf{T}} A^{\mathsf{T}} A x - 2\, b^{\mathsf{T}} A x + b^{\mathsf{T}} b.$$
Its gradient is $2 (A^{\mathsf{T}} A x - A^{\mathsf{T}} b)$.
The function is convex, so its minimizers are exactly its critical points, and these are the solutions of the normal equations.
