---
tag: CNTDX0S8FX
kind: definition
name: Quadratic programming
msc: [90C20]
defines: ERSZ4ADRCY
uses: [0VR671PHE5, 01MMVW8CKC]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_programming
---

## Definition

Let $Q$ be a real [[symmetric|0VR671PHE5]] $n \times n$ matrix, let $c \in \R^n$, let $A$ be a real $m \times n$ matrix and let $b \in \R^m$.
The *quadratic program* with these data is: minimise
$$f(x) = \tfrac12 x^T Q x + c^T x$$
over $x \in \R^n$ subject to $A x \le b$, where $\le$ holds componentwise.
*Quadratic programming* is the study and solution of such problems.

## Remarks

Equality constraints $E x = d$ can be added, or written as two inequalities.
The program is *convex* when $Q$ is [[positive semidefinite|01MMVW8CKC]].

Example: minimise $(x_1 - 1)^2 + (x_2 - 1)^2$ subject to $x_1 + x_2 \le 1$, $x_1 \ge 0$, $x_2 \ge 0$.
Up to the constant $2$, this is $f(x) = \tfrac12 x^T Q x + c^T x$ with $Q = 2I$ symmetric, $c = (-2, -2)^T$, and the constraints linear.
Its solution is $(1/2, 1/2)$.

Non-example: minimise $x_1^2 + x_2^2$ subject to $x_1^2 + x_2^2 \ge 1$ is not a quadratic program in this sense, because the constraint is quadratic, not linear; such problems are quadratically constrained quadratic programs.
