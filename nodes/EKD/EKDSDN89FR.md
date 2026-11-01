---
tag: EKDSDN89FR
kind: definition
name: Polynomial interpolation
msc: [41A05, 65D05]
defines: SS1YMS2NPC
uses: [0QA8CHH8MG, 0Q9EZS90GY, 0DPF6WRZW6, 0KJVQV3E0F]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_interpolation
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]], let $n \ge 0$, let $x_0, \dots, x_n \in K$ be pairwise distinct, and let $y_0, \dots, y_n \in K$.
An interpolation polynomial of the data $(x_i, y_i)$ is a polynomial $p \in K[x]$ such that:

1. $p = 0$ or $\deg p \le n$;
2. $p(x_i) = y_i$ for $i = 0, \dots, n$.

## Remarks

There is exactly one interpolation polynomial.
Uniqueness: the difference of two of them has degree at most $n$ and $n + 1$ roots, so it is $0$ by the [[bound on the number of roots|0KJVQV3E0F]].
Existence: the [[Lagrange formula|237KR6FRCK]] gives one.
Equivalently, the coefficients solve a linear system whose matrix has the nonzero [[Vandermonde determinant|0P84B554AS]].
Example: for $(0, 1)$, $(1, 3)$, $(2, 7)$ the interpolation polynomial is $x^2 + x + 1$.
Non-example: $x^2 + x + 1 + x(x - 1)(x - 2)$ takes the same values at $0, 1, 2$, but it has degree $3 > 2$, so clause 1 fails.

## Explanations

### L1 human

The degree bound is what makes the answer unique.
Without it, you can add any multiple of $(x - x_0) \cdots (x - x_n)$ and still pass through the points.
