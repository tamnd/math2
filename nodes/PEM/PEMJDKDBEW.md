---
tag: PEMJDKDBEW
kind: definition
name: Semidefinite programming
msc: [90C22, 90C25]
defines: 2RTN2X4R2N
uses: [0VR671PHE5, 01MMVW8CKC, 0XC1RDBY7A, PAPN0JNEKN]
sources:
  - url: https://en.wikipedia.org/wiki/Semidefinite_programming
---

## Definition

Let $\mathbb{S}^n$ be the space of real [[symmetric|0VR671PHE5]] $n \times n$ matrices with the inner product $\ip{A}{B} = \tr(A B)$, where $\tr$ is the [[trace|0XC1RDBY7A]].
Write $X \succeq 0$ when $X$ is [[positive semidefinite|01MMVW8CKC]].
Let $C, A_1, \dots, A_m \in \mathbb{S}^n$ and $b \in \R^m$.
The *semidefinite program* with these data is: minimise $\ip{C}{X}$ over $X \in \mathbb{S}^n$ subject to
$$\ip{A_i}{X} = b_i \quad (i = 1, \dots, m) \quad \text{and} \quad X \succeq 0.$$

## Remarks

The positive semidefinite matrices form a closed convex cone in $\mathbb{S}^n$, so this is a [[conic optimization|PAPN0JNEKN]] problem.
Its dual is: maximise $b^T y$ over $y \in \R^m$ subject to $C - \sum_{i=1}^m y_i A_i \succeq 0$, a *linear matrix inequality*.

Example: take $m = 1$, $A_1 = I$ and $b_1 = 1$.
For $X \succeq 0$ with $\tr X = 1$, write $X = \sum_j \lambda_j v_j v_j^T$ with $\lambda_j \ge 0$, $\sum_j \lambda_j = 1$ and orthonormal $v_j$; then $\tr(C X) = \sum_j \lambda_j v_j^T C v_j \ge \lambda_{\min}(C)$, with equality for $X = v v^T$ where $v$ is a unit eigenvector for $\lambda_{\min}(C)$.
So the optimal value is the smallest eigenvalue of $C$.

Non-example: adding the constraint $\rank X = 1$ gives a problem that is not a semidefinite program, since the matrices of rank $1$ do not form a convex set.

When all the $A_i$ and $C$ are diagonal, the problem reduces to a linear program in the diagonal entries of $X$.
