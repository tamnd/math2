---
tag: NGHY4VM088
kind: definition
name: Complementarity theory
msc: [90C33]
defines: JMTCEQ2J3Q
uses: [6VE4KA12VD, QFY1JR1TK4, 6QS7X5GVMY]
sources:
  - url: https://en.wikipedia.org/wiki/Complementarity_theory
---

## Definition

Let $F \colon \R^n \to \R^n$ be a map.
The *complementarity problem* $\mathrm{CP}(F)$ is to find $x \in \R^n$ such that
$$x \ge 0, \quad F(x) \ge 0, \quad x^T F(x) = 0,$$
where $\ge$ holds componentwise.
More generally, for a closed [[convex cone|6VE4KA12VD]] $K \subseteq \R^n$ with [[dual cone|QFY1JR1TK4]] $K^*$, the problem $\mathrm{CP}(K, F)$ is to find $x \in K$ with $F(x) \in K^*$ and $x^T F(x) = 0$.
*Complementarity theory* is the study of these problems: existence and uniqueness of solutions, their stability, and algorithms.

## Remarks

Since $x \ge 0$ and $F(x) \ge 0$, the condition $x^T F(x) = 0$ is the same as $x_i F_i(x) = 0$ for each $i$.

Example: $n = 1$ and $F(x) = x - 1$.
If $x > 0$, then $F(x) = 0$, so $x = 1$; if $x = 0$, then $F(0) = -1 < 0$ fails.
So $x = 1$ is the unique solution.

Non-example: for $n = 1$ and $F(x) = x + 1$, the point $x = 1$ is not a solution, since $F(1) = 2$ and $1 \cdot 2 \ne 0$; the only solution is $x = 0$.

When $F(x) = M x + q$ is affine, $\mathrm{CP}(F)$ is the linear complementarity problem.
For a closed convex cone $K$, $x$ solves $\mathrm{CP}(K, F)$ if and only if $x$ solves the [[variational inequality|6QS7X5GVMY]] "$x \in K$ and $(y - x)^T F(x) \ge 0$ for all $y \in K$".
