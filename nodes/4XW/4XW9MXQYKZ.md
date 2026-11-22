---
tag: 4XW9MXQYKZ
kind: proof
name: Proof of existence and uniqueness of least-squares solutions
msc: [65F20, 15A06]
topics: [8GQVME4SZZ]
audience: ug1
proves: V9AH43ZY91
uses: [0MCDDSCB9Z, 0Q8HZTJC7G, 0F0RPPJ2TT, 0PQ2GGY1QV, 0CRMGPAH83, 0PDVQEP0ZC]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - book: isbn:9780321982384
    locator: Section 6.5
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
---

## Proof

We identify the vectors $Ax$ with the points of the column space, and then we apply the best approximation theorem to that subspace.
Let $U = \operatorname{Col}(A) \subseteq \R^m$ be the [[column space|0F0RPPJ2TT]], and let $p = P_U b$ be the [[orthogonal projection|0Q8HZTJC7G]] of $b$ onto $U$.

1. The subspace $U$ is spanned by the $n$ columns of $A$, so it is finite-dimensional, and the projection $p$ is defined.
2. By the [[matrix-vector product|0PDVQEP0ZC]], $Ax = x_1 a_1 + \dots + x_n a_n$, where $a_1, \dots, a_n$ are the columns, so as $x$ runs over $\R^n$ the vector $Ax$ runs over all of $U$.
3. We prove the backward direction of part 2, so let $A \hat x = p$.
4. For every $x$ the vector $Ax$ lies in $U$, so part 1 of the [[best approximation theorem|0MCDDSCB9Z]] gives $\norm{b - A \hat x} = \norm{b - p} \le \norm{b - Ax}$, and $\hat x$ is a least-squares solution.
5. For part 1, note that $p \in U$, so step 2 gives some $\hat x$ with $A \hat x = p$, and step 4 shows that it is a least-squares solution.
6. For the forward direction of part 2, let $\hat x$ be a least-squares solution, so that $\norm{b - A \hat x} \le \norm{b - Ax}$ for all $x$.
7. By step 2 this inequality says $\norm{b - A \hat x} \le \norm{b - u}$ for every $u \in U$, so $A \hat x$ is a closest point of $U$ to $b$.
8. Part 2 of the best approximation theorem says that the closest point is unique and equals $p$, so $A \hat x = p$.
9. For part 3, fix one least-squares solution $\hat x$; by part 2, a vector $x$ is a least-squares solution exactly when $Ax = p = A \hat x$.
10. The equation $Ax = A \hat x$ means $A(x - \hat x) = 0$, that is, $x = \hat x + z$ with $z$ in the [[null space|0PQ2GGY1QV]] $\operatorname{Nul}(A)$.
11. For part 4, part 3 shows that the solution is unique exactly when $\operatorname{Nul}(A) = \{0\}$.
12. The condition $\operatorname{Nul}(A) = \{0\}$ says that $x_1 a_1 + \dots + x_n a_n = 0$ only for $x = 0$, which is the definition of [[linear independence|0CRMGPAH83]] of the columns.

This proves all four parts.

## Idea

The set of all vectors $Ax$ is the column space, so minimizing $\norm{b - Ax}$ over $x$ is the same problem as finding the point of the column space closest to $b$.
The best approximation theorem says that this point exists, is unique and is the projection $p$.
The only freedom left is the choice of $x$ with $Ax = p$, and two such choices differ by a vector of the null space.

## Variants

There is a proof by calculus.
The function $f(x) = \norm{Ax - b}^2$ is a convex quadratic with gradient $2 A^{\mathsf{T}} (Ax - b)$.
For a convex differentiable function, the minimizers are exactly the critical points, so the minimizers are the solutions of the [[normal equations|4D7MRG4D91]].
Existence then needs a separate argument, for example that $A^{\mathsf{T}} b$ lies in the column space of $A^{\mathsf{T}}$, which equals the column space of $A^{\mathsf{T}} A$.
