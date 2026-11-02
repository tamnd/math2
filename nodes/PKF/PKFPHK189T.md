---
tag: PKFPHK189T
kind: definition
name: Linear regression
msc: [62J05]
defines: 41FVC4P5JB
uses: [K3AMMSY8DD, 0WQNRCNY3M, 0477R9PYAE, 0KBFAWYRTE, 0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_regression
---

## Definition

Let $n \ge p \ge 1$.
Let $X$ be a known $n \times p$ real matrix, the *design matrix*, whose $i$-th row $x_i^T$ holds the explanatory variables of unit $i$.
The *linear regression model* for a response vector $y = (y_1, \ldots, y_n)^T$ is
$$y = X \beta + \varepsilon, \qquad \text{that is,} \qquad y_i = x_i^T \beta + \varepsilon_i,$$
where:

1. $\beta \in \R^p$ is an unknown vector of coefficients;
2. $\varepsilon = (\varepsilon_1, \ldots, \varepsilon_n)^T$ is a random error vector with [[mean|0WQNRCNY3M]] $\mathbb{E}\varepsilon = 0$;
3. the errors are uncorrelated with a common unknown [[variance|0477R9PYAE]] $\sigma^2 > 0$, that is, $\operatorname{Cov}(\varepsilon) = \sigma^2 I_n$.

Usually $X$ is assumed to have full column [[rank|0ZC9YTXZRY]] $p$, and often the errors are assumed normal.

## Remarks

Example: simple linear regression $y_i = \beta_0 + \beta_1 t_i + \varepsilon_i$ is the case $p = 2$ with rows $x_i^T = (1, t_i)$.
The model $y_i = \beta_0 + \beta_1 t_i + \beta_2 t_i^2 + \varepsilon_i$ is also a linear regression, with rows $(1, t_i, t_i^2)$, because it is linear in $\beta$.
Non-example: $y_i = \beta_0 e^{\beta_1 t_i} + \varepsilon_i$ is not linear in $(\beta_0, \beta_1)$, so it is a nonlinear regression model.
The conditions 2 and 3 are the Gauss–Markov conditions; when they hold and $X$ has full column rank, ordinary least squares is the best linear unbiased estimator of $\beta$.
Weaker forms allow correlated or heteroscedastic errors, which leads to generalised least squares.
