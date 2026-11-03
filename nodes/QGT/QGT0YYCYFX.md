---
tag: QGT0YYCYFX
kind: definition
name: Duality gap
msc: [90C46, 49N15]
defines: AXBPKPSENT
uses: [QRXXH28W3A]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_gap
---

## Definition

Consider a minimization problem with optimal value $p^* \in [-\infty, \infty]$.
Let $d^* \in [-\infty, \infty]$ be the optimal value of its [[Lagrange dual problem|QRXXH28W3A]].
The *duality gap* is $p^* - d^*$, defined whenever $p^*$ and $d^*$ are not both $+\infty$ or both $-\infty$.
*Strong duality* holds if $p^* = d^*$.
Let $x$ be primal feasible and $(\lambda, \nu)$ dual feasible.
The number $f_0(x) - g(\lambda, \nu)$ is the duality gap of the pair.

## Remarks

Weak duality $d^* \le p^*$ gives $p^* - d^* \ge 0$ when it is defined.
The gap of a pair satisfies $f_0(x) - g(\lambda, \nu) \ge f_0(x) - p^* \ge 0$, so a small gap certifies that $x$ is nearly optimal.
Strong duality holds for linear programs with a finite optimal value, and for convex problems under [[Slater's condition|BSRSKXPJPQ]].

Example with a positive gap: let $D = \set{0, 2}$, $f_0(x) = -x$ and $f_1(x) = x - 1$.
The only feasible point is $x = 0$, so $p^* = 0$.
The dual function is $g(\lambda) = \min(-\lambda, \lambda - 2)$, which is largest at $\lambda = 1$, so $d^* = -1$.
The duality gap is $1$.

Example with zero gap: minimize $x^2$ over $\R$ subject to $1 - x \le 0$, where $p^* = d^* = 1$.
