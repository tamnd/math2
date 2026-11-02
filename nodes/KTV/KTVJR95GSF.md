---
tag: KTVJR95GSF
kind: definition
name: Spline
msc: [41A15, 65D07]
defines: 84TJ8KQ926
uses: [1G0B73WPX8, 0X3WGX95FE, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_(mathematics)
---

## Definition

Let $a < b$, let $k \ge 1$, and let $a = t_0 < t_1 < \cdots < t_k = b$ be points called *knots*.
Let $n \ge 1$ be an integer.
A *spline of degree $n$* with these knots is a function $s \colon [a, b] \to \R$ such that:

1. for each $i = 1, \dots, k$, the restriction of $s$ to $[t_{i-1}, t_i]$ is a [[polynomial function|1G0B73WPX8]] of degree at most $n$;
2. $s$ is $n - 1$ times continuously differentiable on $[a, b]$.

## Remarks

Splines of degree $0$ are usually taken to be step functions, constant on each $[t_{i-1}, t_i)$, with jumps allowed at the knots.
For $n = 1$, clause 2 asks that $s$ is [[continuous|0X3WGX95FE]], so $s$ is a broken line.
The splines of degree $n$ with fixed knots form a vector space of dimension $n + k$.
Some authors allow lower smoothness at some knots; this is encoded by repeating knots.

Example: with knots $-1 < 0 < 1$ and $n = 3$, the function $s(x) = 0$ for $x \le 0$ and $s(x) = x^3$ for $x \ge 0$ is a cubic spline.
Each piece is a polynomial of degree at most $3$.
At $0$ the values, first [[derivatives|0V1EJCT8G6]] and second derivatives of both pieces are $0$, so $s$ is twice continuously differentiable.

Non-example: with the same knots, $s(x) = 0$ for $x \le 0$ and $s(x) = x^2$ for $x \ge 0$ is not a cubic spline.
Its second derivative jumps from $0$ to $2$ at $0$, so clause 2 fails.
