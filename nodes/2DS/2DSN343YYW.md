---
tag: 2DSN343YYW
kind: statement
role: theorem
name: Koksma–Hlawka inequality
msc: [11K38, 65D30, 65C05]
uses: [A8251BHCMP, 8QA5DEWNYD, DWJF7ABPR1, XSPX1KW9AQ, 54MY2XHVGB, DAR3QJ5H7Y]
about: [ABSRB2KXA6, XSPX1KW9AQ]
sources:
  - url: https://en.wikipedia.org/wiki/Low-discrepancy_sequence
---

## Statement

Let $s \ge 1$ and let $x_1, \ldots, x_N$ be points of $[0,1)^s$.
For $t = (t_1, \ldots, t_s) \in [0,1]^s$, let $A(t)$ be the number of indices $i$ with $x_i \in [0,t_1) \times \cdots \times [0,t_s)$.
The *star discrepancy* of the points is
$$D_N^* = \sup_{t \in [0,1]^s} \abs{\frac{A(t)}{N} - t_1 t_2 \cdots t_s}.$$
Let $f \colon [0,1]^s \to \R$ have finite variation $V(f)$ in the sense of Hardy and Krause.
Then
$$\abs{\frac{1}{N} \sum_{i=1}^{N} f(x_i) - \int_{[0,1]^s} f(u) \, du} \le V(f) \, D_N^*.$$

## Remarks

For $s = 1$ this is Koksma's inequality, and $V(f)$ is the ordinary [[total variation|8QA5DEWNYD]] of $f$ on $[0,1]$.
In that case the proof writes the error as a Riemann–Stieltjes integral $\int_0^1 \big(A(t)/N - t\big) \, df(t)$ by integration by parts, and bounds the integrand by $D_N^*$.
In higher dimension the same idea works with a multivariate integration by parts, which produces one term for each face of the cube.
The Hardy–Krause variation collects the variations of $f$ on all these faces.
The bound separates the two sources of error: $V(f)$ depends only on the integrand, and $D_N^*$ depends only on the points.
For a [[low-discrepancy sequence|XSPX1KW9AQ]] such as the [[Halton sequence|54MY2XHVGB]], $D_N^* = O\big((\log N)^s / N\big)$, so the [[quasi-Monte Carlo|ABSRB2KXA6]] error is $O\big((\log N)^s / N\big)$ for every $f$ of finite variation.
This beats the rate $N^{-1/2}$ of plain [[Monte Carlo integration|DAR3QJ5H7Y]] for large $N$.
The hypothesis of finite variation is needed: the indicator of a ball in $[0,1]^2$ has infinite Hardy–Krause variation, and the bound gives nothing for it.

## Explanations

### L1 human

To approximate the average of a function over a cube, one averages its values at $N$ sample points.
The inequality says the error is at most a product of two numbers.
One number measures how much the function wiggles.
The other measures how unevenly the points fill the cube.
So well-spread points give small errors for every function that does not wiggle too much.

### L2 human

The inequality is the basic error bound of quasi-Monte Carlo integration.
It turns the design of good integration rules into the purely geometric task of finding point sets with small star discrepancy.
Halton, Sobol and other digital sequences reach $D_N^* = O\big((\log N)^s / N\big)$.
The bound is sharp in a worst-case sense.
But $V(f)$ is often hard to compute, and it is infinite for simple functions with jumps along surfaces not aligned with the axes.
Variants replace $D_N^*$ and $V(f)$ by other pairs of dual quantities, for example $L^2$ discrepancy and a Sobolev-type norm.
