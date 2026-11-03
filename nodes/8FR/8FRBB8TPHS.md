---
tag: 8FRBB8TPHS
kind: definition
name: Modern portfolio theory
msc: [91G10, 90C20]
defines: ZBDA8W9D6V
uses: [0WQNRCNY3M, 0477R9PYAE, 0V7G6WMFK0, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Modern_portfolio_theory
---

## Definition

Consider $n \ge 2$ risky assets whose returns form a random vector $R = (R_1, \dots, R_n)$.
Let $m = \mathbb{E}[R] \in \R^n$ be the vector of [[expected returns|0WQNRCNY3M]] and $\Sigma$ the [[covariance matrix|0V7G6WMFK0]] of $R$, assumed [[positive definite|0KX66CZMBB]].
A *portfolio* is a weight vector $w \in \R^n$ with $\sum_{i=1}^n w_i = 1$; negative weights are short positions.
Its return $w^T R$ has mean $w^T m$ and [[variance|0477R9PYAE]] $w^T \Sigma w$.

In *modern portfolio theory* (mean–variance analysis), an investor compares portfolios only by the pair (variance, mean).
For a target mean $\mu \in \R$, the *mean–variance problem* is
$$\text{minimise } w^T \Sigma w \quad \text{subject to } w^T m = \mu, \quad \sum_{i=1}^n w_i = 1.$$
A solution is a *minimum-variance portfolio* for the target $\mu$.

## Remarks

Example: two uncorrelated assets with variances $\sigma_1^2, \sigma_2^2 > 0$.
The weights $(w, 1 - w)$ give variance $w^2 \sigma_1^2 + (1 - w)^2 \sigma_2^2$.
This is smallest at $w = \sigma_2^2/(\sigma_1^2 + \sigma_2^2)$, with value $\sigma_1^2 \sigma_2^2/(\sigma_1^2 + \sigma_2^2)$, which is less than both $\sigma_1^2$ and $\sigma_2^2$.

Non-example: if $\Sigma$ is only positive semidefinite, the positive definiteness clause fails.
Then some non-zero combination of assets has zero variance, and minimum-variance portfolios need not be unique.

When $\Sigma$ is positive definite and $m$ is not a multiple of $(1, \dots, 1)$, the problem has a unique solution for every $\mu$.
The minimum-variance portfolios with mean at least that of the global minimum-variance portfolio form the efficient frontier.
