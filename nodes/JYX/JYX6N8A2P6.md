---
tag: JYX6N8A2P6
kind: statement
role: theorem
name: Favard's theorem on trigonometric approximation
msc: [41A44, 42A10, 41A17]
uses: [9K1W9Q49NR, J3NJQ5FZJ5, 0ATF6Q0633, YDN0T4MEX0]
about: [9K1W9Q49NR]
sources:
  - url: https://en.wikipedia.org/wiki/Favard_constant
---

## Statement

Let $r \ge 1$ and $n \ge 1$ be integers, and let $K_r$ be the [[Favard constant|9K1W9Q49NR]].
Let $f \colon \R \to \R$ be $2\pi$-[[periodic|0ATF6Q0633]], with $f^{(r-1)}$ absolutely continuous and $\abs{f^{(r)}} \le 1$ almost everywhere.
Then there is a real [[trigonometric polynomial|J3NJQ5FZJ5]] $T$ of degree at most $n - 1$ such that
$$\max_{x \in \R} \abs{f(x) - T(x)} \le \frac{K_r}{n^r}.$$
The constant $K_r$ is sharp.
For each $n$, some $f$ of this class has distance exactly $K_r / n^r$ from the set of all such $T$.

## Remarks

The extremal function is the $r$-fold periodic integral of the square wave $\sgn \sin(nx)$, normalised to have mean $0$.
Its error of best approximation equals $K_r / n^r$, which explains the alternating series in the definition of $K_r$: they come from the Fourier series of the square wave.
The upper bound comes from explicit linear approximation methods, so it is attained by a linear operator.

Example: $r = 1$, $n = 1$.
A periodic function with $\abs{f'} \le 1$ has $\max f - \min f \le \pi$, so the best constant has error at most $\pi/2 = K_1$.
The triangle wave equal to $\abs{x}$ on $[-\pi, \pi]$ reaches this bound.

## Explanations

### L1 human

This is the best possible form of Jackson's inequality for functions with a bounded $r$-th derivative.
It says exactly how well trigonometric polynomials of degree below $n$ can approximate every such function at once.

### L2 human

Jackson's inequality gives the rate $n^{-r}$ with some constant; Favard's theorem gives the exact worst-case constant.
It is a model result for the theory of widths and optimal recovery, where one asks for the smallest error over a whole class.
The same constants appear in sharp inequalities between a function and its derivatives, such as the Kolmogorov inequalities.
