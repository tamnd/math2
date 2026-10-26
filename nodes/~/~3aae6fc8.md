---
tag: ~3aae6fc8
kind: definition
name: Chi-squared distribution
msc: ["60E05", "62E15"]
defines: ~68465832
uses: [~abf473d0, ~ef650a31, ~ecb6d374, ~c7d91a3e, ~d24e2b84]
sources:
  - url: https://en.wikipedia.org/wiki/Chi-squared_distribution
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Chi-squared_distribution
    locator: Probability density function
---

## Definition

Let $k \ge 1$ be an integer and let $Z_1, \dots, Z_k$ be [[i.i.d.|~ef650a31]] standard normal random variables.
The chi-squared distribution with $k$ degrees of freedom, written $\chi^2_k$, is the law of
$$Q = Z_1^2 + Z_2^2 + \dots + Z_k^2.$$

## Remarks

It has the [[density|~ecb6d374]] $f(x) = \frac{x^{k/2 - 1} e^{-x/2}}{2^{k/2}\, \Gamma(k/2)}$ for $x > 0$, and $f(x) = 0$ for $x \le 0$. So $\chi^2_k$ is the [[gamma distribution|~c7d91a3e]] with shape $k/2$ and rate $1/2$.
If $Q \sim \chi^2_k$, then $E[Q] = k$ and $\operatorname{Var}(Q) = 2k$.
If $Q_1 \sim \chi^2_{k_1}$ and $Q_2 \sim \chi^2_{k_2}$ are independent, then $Q_1 + Q_2 \sim \chi^2_{k_1 + k_2}$.
For an i.i.d. $\mathcal{N}(\mu, \sigma^2)$ sample of size $n$ with [[sample variance|~d24e2b84]] $S_n^2$, $(n - 1) S_n^2 / \sigma^2 \sim \chi^2_{n - 1}$.

## Explanations

### L1 human

Square $k$ independent standard normal numbers and add them: the result has the chi-squared distribution with $k$ degrees of freedom.
Its mean is $k$, and it has values in $[0, \infty)$ only.
