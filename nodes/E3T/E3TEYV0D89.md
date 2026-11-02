---
tag: E3TEYV0D89
kind: definition
name: Noncentral chi-squared distribution
msc: ["62E15", "60E05"]
defines: RK84ANP6BP
uses: [07RXBVTVZB, 0RFMMBHFTV, 0E9502NT92, 0VEFSSKX18]
sources:
  - url: https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
---

## Definition

Let $k$ be a positive integer and let $\mu_1, \dots, \mu_k$ be real numbers.
Let $X_1, \dots, X_k$ be [[independent|0E9502NT92]] random variables with $X_i \sim \mathcal{N}(\mu_i, 1)$, the [[normal distribution|07RXBVTVZB]] with mean $\mu_i$ and variance $1$.
The distribution of
$$Q = \sum_{i=1}^k X_i^2$$
depends only on $k$ and on $\lambda = \sum_{i=1}^k \mu_i^2$.
It is the *noncentral chi-squared distribution* with $k$ degrees of freedom and noncentrality parameter $\lambda$, written $\chi'^2_k(\lambda)$.

## Remarks

For $\lambda = 0$ it is the [[chi-squared distribution|0RFMMBHFTV]] with $k$ degrees of freedom.
Its mean is $k + \lambda$ and its variance is $2(k + 2\lambda)$.
Its density is a [[Poisson|0VEFSSKX18]] mixture of central chi-squared densities:
$$f(x) = \sum_{j=0}^{\infty} e^{-\lambda/2} \frac{(\lambda/2)^j}{j!} f_{k + 2j}(x), \quad x > 0,$$
where $f_m$ is the chi-squared density with $m$ degrees of freedom.

Example: if $X \sim \mathcal{N}(\mu, 1)$, then $X^2 \sim \chi'^2_1(\mu^2)$, and $E(X^2) = 1 + \mu^2$ agrees with the mean $k + \lambda$.

Non-example: the variances must be $1$.
If $X \sim \mathcal{N}(0, 4)$, then $X^2$ has mean $4$ and variance $32$.
A $\chi'^2_1(\lambda)$ variable with mean $4$ has $\lambda = 3$ and variance $2(1 + 6) = 14$, so $X^2$ has no noncentral chi-squared distribution with one degree of freedom.
