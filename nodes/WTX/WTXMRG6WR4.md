---
tag: WTXMRG6WR4
kind: definition
name: Gosper's algorithm
msc: [33F10, 68W30, 39A10]
defines: NHMJQBS04M
uses: [0XDK9CGYKJ, Q75YRG25JK, 0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Gosper%27s_algorithm
---

## Definition

Let $t_k$ be a hypergeometric term in $k$ over a field of characteristic $0$.
This means that $t_k \ne 0$ and that $r(k) = t_{k+1}/t_k$ is a [[rational function|0XDK9CGYKJ]] of $k$.
*Gosper's algorithm* takes $t_k$ and either returns a hypergeometric term $T_k$ with $T_{k+1} - T_k = t_k$, or reports that no such term exists.
It runs as follows.

1. Write $r(k) = \dfrac{a(k)}{b(k)}\cdot\dfrac{c(k+1)}{c(k)}$ with polynomials $a, b, c$ such that $\gcd\big(a(k), b(k + h)\big) = 1$ for every integer $h \ge 0$ (a [[polynomial gcd|Q75YRG25JK]] condition).
2. Search for a polynomial $x(k)$ with
$$a(k)\,x(k + 1) - b(k - 1)\,x(k) = c(k),$$
using a bound on its degree computed from $a$, $b$, $c$ and linear algebra on its coefficients.
3. If such an $x$ exists, return $T_k = \dfrac{b(k - 1)\,x(k)}{c(k)}\,t_k$. Otherwise report that $t_k$ has no hypergeometric indefinite sum.

## Remarks

Check of step 3: with $y(k) = b(k-1)x(k)/c(k)$, one has $T_{k+1} - T_k = \big(y(k + 1)r(k) - y(k)\big)t_k$, and $y(k+1)r(k) - y(k) = \big(a(k)x(k+1) - b(k-1)x(k)\big)/c(k) = 1$ by step 2.
Gosper's theorem says that the method is complete: if some hypergeometric $T_k$ works, then $T_k/t_k$ is rational and the equation in step 2 has a polynomial solution.
Example: $t_k = k\cdot k!$ has $r(k) = (k + 1)^2/k$; take $a(k) = k + 1$, $b(k) = 1$, $c(k) = k$, which satisfy the gcd condition.
The equation $(k + 1)x(k + 1) - x(k) = k$ has the solution $x = 1$, so $T_k = k!$ for $k \ge 1$, and indeed $(k + 1)! - k! = k\cdot k!$.
Non-example: for $t_k = 1/(k + 1)$ the algorithm reports failure, since the partial sums are harmonic numbers, which are not a hypergeometric term.
The equation of step 2 is a linear [[recurrence|0FYX44GP92]] with polynomial coefficients for the unknown polynomial $x$.
