---
tag: KCVKGSYJR9
kind: definition
name: Ridge regression
msc: [62J07, 62J05]
defines: 3KZW2930V2
uses: [YM708KHV2W, 0BYTQ4X1HC, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Ridge_regression
---

## Definition

Let $X$ be a real $n \times p$ matrix, let $y \in \R^n$, and let $\lambda > 0$.
The *ridge regression estimator* with parameter $\lambda$ is the minimiser of
$$\norm{y - X b}^2 + \lambda \norm{b}^2$$
over $b \in \R^p$, where $\norm{\cdot}$ is the Euclidean norm.
It equals
$$\hat\beta_\lambda = (X^T X + \lambda I_p)^{-1} X^T y.$$

## Remarks

The matrix $X^T X + \lambda I_p$ is [[positive definite|0KX66CZMBB]] for $\lambda > 0$, so the minimiser exists and is unique for every $X$, whatever its rank.
The formula comes from setting the gradient $-2 X^T (y - X b) + 2 \lambda b$ to zero.

Example: take $p = 1$, $X = (1, 2)^T$, $y = (1, 2)^T$ and $\lambda = 1$.
Then $X^T X = 5$ and $X^T y = 5$, so $\hat\beta_1 = 5/6$, while the [[ordinary least squares|YM708KHV2W]] slope is $1$.

Non-example: with $\lambda = 0$ the problem is plain [[least squares|0BYTQ4X1HC]], and if $X^T X$ is singular, for example when two columns of $X$ are equal, the minimiser is not unique.

In practice the regressors are usually standardised and the intercept is not penalised.
For each $\lambda > 0$ there is $t > 0$ such that $\hat\beta_\lambda$ also minimises $\norm{y - Xb}^2$ under the constraint $\norm{b}^2 \le t$.
In a normal linear model, $\hat\beta_\lambda$ is the posterior mode for a centred normal prior on $\beta$.
