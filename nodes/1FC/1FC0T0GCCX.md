---
tag: 1FC0T0GCCX
kind: statement
role: theorem
name: Gauss's hypergeometric theorem
msc: ["33C05", "33B15"]
uses: [428M453CR2, 0H5SYBSED9]
about: [428M453CR2, 463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Statement

Let $a, b, c \in \C$ with $c \notin \set{0, -1, -2, \ldots}$ and $\operatorname{Re}(c - a - b) > 0$, and let $\Gamma$ be the [[gamma function|0H5SYBSED9]].
Then the [[hypergeometric series|428M453CR2]] converges at $z = 1$, and
$${}_2F_1(a, b; c; 1) = \frac{\Gamma(c) \, \Gamma(c - a - b)}{\Gamma(c - a) \, \Gamma(c - b)}.$$

## Remarks

When moreover $\operatorname{Re} c > \operatorname{Re} b > 0$, put $z = 1$ in [[Euler's integral representation|812THX456R]]: the integral becomes the beta integral $B(b, c - a - b)$, and the gamma factors simplify to the right side.
Abel's theorem on power series identifies the value of the series at $1$ with the limit of the function as $z \to 1^-$.
The general case follows by analytic continuation in the parameters, or from a contiguous relation.

Example: for $a = b = 1$, $c = 3$ the series is $\sum_{n \ge 0} \frac{n! \, n!}{(n+2)!/2 \cdot n!} = \sum_{n \ge 0} \frac{2}{(n+1)(n+2)} = 2$, and the right side is $\frac{\Gamma(3) \Gamma(1)}{\Gamma(2) \Gamma(2)} = 2$.

With $a = -n$ for an integer $n \ge 0$, the theorem gives the [[Chu–Vandermonde identity|4YK46R1QDR]].

The condition $\operatorname{Re}(c - a - b) > 0$ is needed: for $a = b = 1$, $c = 2$ one has $c - a - b = 0$, and the series $\sum_n \frac{1}{n+1}$ diverges.

## Explanations

### L1 human

The hypergeometric series is an infinite sum depending on three parameters.
At the edge point $z = 1$ the sum can be computed in closed form, as a ratio of gamma function values.
This one formula evaluates a huge number of special series.

### L2 human

The theorem is the basic summation formula for ${}_2F_1$, and most closed-form evaluations of ${}_3F_2$ and higher series, such as those of Pfaff–Saalschütz and Dixon, are its relatives.
It also gives the connection coefficients between the solutions at $0$ and at $1$ of the hypergeometric equation, since these are values of ${}_2F_1$ at $1$.
The terminating case, Chu–Vandermonde, is a polynomial identity behind many binomial sums.
