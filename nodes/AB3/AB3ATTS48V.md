---
tag: AB3ATTS48V
kind: statement
role: theorem
name: Log-convexity of the gamma function
msc: [33B15, 26A51]
uses: [0V3FZMVB4K, E97P413DKM]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Bohr%E2%80%93Mollerup_theorem
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]] on $(0, \infty)$.
Then $\Gamma$ is [[logarithmically convex|E97P413DKM]]: the function $x \mapsto \ln \Gamma(x)$ is convex on $(0, \infty)$.
Equivalently, for all $x, y > 0$ and $\lambda \in [0, 1]$,
$$\Gamma(\lambda x + (1 - \lambda) y) \le \Gamma(x)^{\lambda} \, \Gamma(y)^{1 - \lambda}.$$

## Remarks

Write $t^{\lambda x + (1-\lambda) y - 1} e^{-t} = \big(t^{x-1}e^{-t}\big)^{\lambda}\big(t^{y-1}e^{-t}\big)^{1-\lambda}$ and apply [[Hölder's inequality|JQ9WXC729D]] with exponents $1/\lambda$ and $1/(1-\lambda)$ to Euler's integral; this gives the inequality.
A second proof: the second derivative is $(\ln\Gamma)''(x) = \sum_{n \ge 0} \frac{1}{(x + n)^2} > 0$, so $\ln \Gamma$ is even strictly convex.
Example: with $x = 1$, $y = 3$ and $\lambda = \tfrac12$ the inequality says $\Gamma(2) = 1 \le \sqrt{\Gamma(1)\Gamma(3)} = \sqrt{2}$.
Log-convexity implies ordinary convexity of $\Gamma$, so $\Gamma$ has a single minimum on $(0, \infty)$, near $x \approx 1.4616$.
In Mathlib the statement is `Real.convexOn_log_Gamma`.

## Explanations

### L1 human

The graph of $\ln \Gamma$ on the positive axis bends upward everywhere.
This is a strong form of convexity for $\Gamma$ itself.

### L2 human

Log-convexity is the property that singles out $\Gamma$ among all functions with $f(1) = 1$ and $f(x + 1) = x f(x)$: this is the [[Bohr–Mollerup theorem|QFF87AXWN2]].
It gives inequalities such as Gautschi's bounds for ratios $\Gamma(x + s)/\Gamma(x + 1)$.
The positivity of $(\ln\Gamma)''$ says that the [[digamma function|HWRRXB0YXS]] is strictly increasing on $(0, \infty)$.
