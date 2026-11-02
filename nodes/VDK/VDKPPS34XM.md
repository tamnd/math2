---
tag: VDKPPS34XM
kind: definition
name: Curse of dimensionality
msc: [65Y20, 41A63, 65D30]
defines: YS424FTY4E
uses: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Curse_of_dimensionality
---

## Definition

For each dimension $d \ge 1$, let $F_d$ be a class of real functions on $[0, 1]^d$ and let $S_d \colon F_d \to \R$ be a functional, such as the integral $S_d(f) = \int_{[0,1]^d} f$.
An algorithm with $n$ function values computes $f(x_1), \dots, f(x_n)$, where each point may depend on the earlier values, and outputs a number computed from these values.
Its worst-case error is the supremum of $\abs{S_d(f) - A(f)}$ over $f \in F_d$.
Let $n(\varepsilon, d)$ be the smallest $n$ such that some algorithm with $n$ function values has worst-case error at most $\varepsilon$.
The family of problems $(S_d, F_d)$ *suffers from the curse of dimensionality* if there are constants $C, \gamma, \varepsilon_0 > 0$ as follows.
For all $\varepsilon \le \varepsilon_0$ and infinitely many $d$,
$$n(\varepsilon, d) \ge C (1 + \gamma)^d.$$

## Remarks

Example: let $F_d$ be the functions $f$ on $[0, 1]^d$ with $\abs{f} \le 1$ and $\abs{f(x) - f(y)} \le \norm{x - y}_\infty$, and let $S_d$ be the integral.
Take an algorithm with $n \le 2^{d-1}$ values, and let $P$ be the points it uses for the input $0$.
The function $g(x) = \min\big(1, \operatorname{dist}_\infty(x, P)\big)$ lies in $F_d$ and vanishes on $P$, so the algorithm uses the same points and outputs the same number for $g$, $-g$ and $0$.
The set where $g < \frac14$ is covered by $n$ cubes of side $\frac12$, of total volume at most $n 2^{-d} \le \frac12$, so $\int g \ge \frac14 \cdot \frac12 = \frac18$.
Hence the error is at least $\frac18$ for $g$ or for $-g$, and $n(\varepsilon, d) > 2^{d-1}$ for $\varepsilon < \frac18$: the problem suffers from the curse.

Non-example: let $F_d$ be the functions $f(x) = h(x_1)$ that depend only on the first coordinate, where $h \colon [0, 1] \to \R$ satisfies $\abs{h} \le 1$ and $\abs{h(s) - h(t)} \le \abs{s - t}$.
A [[quadrature rule|ADSVMCY77A]] in the first variable alone reaches error $\varepsilon$ with a number of points independent of $d$, so no exponential lower bound holds.

In the information-based complexity literature the error is often normalized by the error of the zero algorithm; this changes constants but not the idea.
