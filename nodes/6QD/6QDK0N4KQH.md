---
tag: 6QDK0N4KQH
kind: definition
name: Constructive function theory
msc: [41A25, 41A27, 41A10]
defines: B9NEZNTRPT
uses: [YPJSH79SHQ, YDN0T4MEX0, AXCJBSQZWF]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_function_theory
---

## Definition

Let $f$ be a function on $[a, b]$, or a $2\pi$-periodic function, in a fixed normed space.
Let $E_n(f)$ be the [[error of best approximation|YDN0T4MEX0]] of $f$ by algebraic, respectively trigonometric, polynomials of degree at most $n$.
*Constructive function theory* is the part of [[approximation theory|YPJSH79SHQ]] that characterizes classes of functions by the behaviour of the sequence $(E_n(f))_{n \ge 0}$ as $n \to \infty$.
Its results are of two kinds.

1. Direct theorems: a smoothness condition on $f$, often a bound on its [[modulus of continuity|AXCJBSQZWF]], implies an upper bound for $E_n(f)$.
2. Inverse theorems: an upper bound for $E_n(f)$ implies a smoothness condition on $f$.

## Remarks

Example: for $2\pi$-periodic continuous $f$, the uniform norm, and $0 < \alpha < 1$, one has $E_n(f) = O(n^{-\alpha})$ if and only if $\abs{f(x) - f(y)} \le M \abs{x - y}^\alpha$ for some constant $M$ and all $x, y$.
The direction from smoothness to the rate is a direct theorem of Jackson type, and the converse is an inverse theorem of Bernstein type.

Non-example: the statement that $E_n(f) \to 0$ for every continuous $f$ is a result of approximation theory.
But it gives no rate and distinguishes no class of functions, so it is not of this kind.
