---
tag: B7YND5ZVMF
kind: definition
name: Cubic spline
msc: [41A15, 65D07]
defines: V42H0R3EKX
uses: [84TJ8KQ926, 1G0B73WPX8, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_interpolation
---

## Definition

Let $k \ge 1$ and let $a = t_0 < t_1 < \cdots < t_k = b$ be knots.
A *cubic spline* with these knots is a function $s \colon [a, b] \to \R$ such that:

1. for each $i = 1, \dots, k$, the restriction of $s$ to $[t_{i-1}, t_i]$ is a [[polynomial function|1G0B73WPX8]] of degree at most $3$;
2. $s$ is twice continuously differentiable on $[a, b]$.

A cubic spline is *natural* if moreover $s''(a) = s''(b) = 0$.

## Remarks

This is the [[spline|84TJ8KQ926]] of degree $3$.
Writing $s_i$ for the piece on $[t_{i-1}, t_i]$, clause 2 says that $s_i(t_i) = s_{i+1}(t_i)$, $s_i'(t_i) = s_{i+1}'(t_i)$ and $s_i''(t_i) = s_{i+1}''(t_i)$ for $1 \le i \le k - 1$, where $'$ is the [[derivative|0V1EJCT8G6]].
The cubic splines with fixed knots form a vector space of dimension $k + 3$.
Given values at all knots, there is exactly one natural cubic spline taking them.

Example: knots $-1 < 0 < 1$ and $s(x) = 0$ for $x \le 0$, $s(x) = x^3$ for $x \ge 0$.
At $0$ both pieces have value, first derivative and second derivative $0$, so $s$ is a cubic spline.
It is not natural, since $s''(1) = 6 \ne 0$.

Non-example: $s(x) = \abs{x}$ on $[-1, 1]$ with the knots $-1 < 0 < 1$ satisfies clause 1, since its pieces $-x$ and $x$ are polynomials.
It fails clause 2: its first derivative jumps from $-1$ to $1$ at $0$.
