---
tag: ~0dfea35d
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

Let $U = \operatorname{Col}(A) \subseteq \R^m$, the [[column space|0F0RPPJ2TT]], and let $p = P_U b$ be the [[orthogonal projection|0Q8HZTJC7G]] of $b$ onto $U$.

1. $U$ is spanned by the $n$ columns of $A$, so it is a finite-dimensional subspace of $\R^m$, and $p$ is defined.
2. As $x$ runs over $\R^n$, the vector $Ax$ runs over all of $U$, because $Ax$ is the combination of the columns of $A$ with coefficients $x_1, \dots, x_n$, by the [[matrix-vector product|0PDVQEP0ZC]].
3. Part 2, backward direction: let $A \hat x = p$. For every $x$, the vector $Ax$ lies in $U$, so the [[best approximation theorem|0MCDDSCB9Z]], part 1, gives $\norm{b - A \hat x} = \norm{b - p} \le \norm{b - Ax}$. So $\hat x$ is a least-squares solution.
4. Part 1: $p \in U$, so by step 2 there is $\hat x$ with $A \hat x = p$. By step 3 it is a least-squares solution.
5. Part 2, forward direction: let $\hat x$ be a least-squares solution. Then $A \hat x \in U$, and $\norm{b - A \hat x} \le \norm{b - Ax}$ for all $x$. By step 2, this says $\norm{b - A \hat x} \le \norm{b - u}$ for every $u \in U$.
6. So $A \hat x$ is a closest point of $U$ to $b$, and by part 2 of the best approximation theorem, $A \hat x = p$.
7. Part 3: let $\hat x$ be a least-squares solution. By part 2, a vector $x$ is a least-squares solution exactly when $Ax = p = A \hat x$, that is, when $A(x - \hat x) = 0$.
8. So the least-squares solutions are the vectors $\hat x + z$ with $z$ in the [[null space|0PQ2GGY1QV]] $\operatorname{Nul}(A)$.
9. Part 4: by part 3, the solution is unique exactly when $\operatorname{Nul}(A) = \set{0}$.
10. $\operatorname{Nul}(A) = \set{0}$ means that $x_1 a_1 + \dots + x_n a_n = 0$ only for $x = 0$, where $a_j$ are the columns. This is the definition of [[linear independence|0CRMGPAH83]] of the columns.

## Idea

The set of all $Ax$ is the column space, so minimizing $\norm{Ax - b}$ over $x$ is the same as finding the closest point of the column space to $b$.
That point is the projection $p$, and it is unique.
The freedom left is the choice of $x$ with $Ax = p$, which is a coset of the null space.

## Variants

A proof by calculus: $f(x) = \norm{Ax - b}^2$ is a quadratic function with gradient $2 A^{\mathsf{T}} (Ax - b)$.
Its minimizers are its critical points, because $f$ is convex, and this gives the [[normal equations|~b9f67439]].
