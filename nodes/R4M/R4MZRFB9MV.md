---
tag: R4MZRFB9MV
kind: definition
name: Incomplete gamma function
msc: ["33B20"]
defines: YB7ZV0HG7K
uses: [0H5SYBSED9, 0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_gamma_function
---

## Definition

Let $s$ and $x$ be real numbers.
1. For $s > 0$ and $x \ge 0$, the *lower incomplete gamma function* is
$$\gamma(s, x) = \int_0^x t^{s-1} e^{-t}\, dt.$$
2. For $x > 0$ and any real $s$, the *upper incomplete gamma function* is the [[improper integral|0VCTBJMEJF]]
$$\Gamma(s, x) = \int_x^\infty t^{s-1} e^{-t}\, dt.$$

## Remarks

For $s > 0$ and $x > 0$, $\gamma(s, x) + \Gamma(s, x) = \Gamma(s)$, the [[gamma function|0H5SYBSED9]].

Example: for $s = 1$, $\gamma(1, x) = \int_0^x e^{-t}\, dt = 1 - e^{-x}$ and $\Gamma(1, x) = e^{-x}$, and their sum is $1 = \Gamma(1)$.
Integration by parts gives $\gamma(s+1, x) = s\,\gamma(s, x) - x^s e^{-x}$.

Non-example of a valid argument: for $s = 0$ the lower integral $\int_0^x t^{-1} e^{-t}\, dt$ diverges at $0$, so $\gamma(0, x)$ is not defined.
The upper function is still defined: $\Gamma(0, x) = E_1(x)$ is the [[exponential integral|EV6ZDQ0NDY]].

The quotient $P(s, x) = \gamma(s, x)/\Gamma(s)$ is the regularised lower incomplete gamma function, the distribution function of the [[gamma distribution|0B80PAQD3C]] with shape $s$ and scale $1$.
Both functions extend to complex arguments: $\gamma(s, x)$ for $\operatorname{Re} s > 0$, and $\Gamma(s, x)$ by analytic continuation.
