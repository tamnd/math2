---
tag: 5Y3DYMPVEG
kind: definition
name: Ordinary least squares
msc: [62J05]
defines: YM708KHV2W
uses: [41FVC4P5JB, 0BYTQ4X1HC, 0ZC9YTXZRY, 0EB9N0S33C, 0B8KZRT28M, 0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_least_squares
---

## Definition

Consider the [[linear regression|41FVC4P5JB]] model $y = X \beta + \varepsilon$ with an $n \times p$ design matrix $X$ and response $y \in \R^n$.
The *ordinary least squares* [[estimator|0SSS6ERQ0S]] of $\beta$ is a vector $\hat\beta \in \R^p$ that minimises the residual sum of squares
$$S(b) = \abs{y - X b}^2 = \sum_{i=1}^n (y_i - x_i^T b)^2, \qquad b \in \R^p.$$
If $X$ has [[rank|0ZC9YTXZRY]] $p$, then $X^T X$ is [[invertible|0EB9N0S33C]] and the minimiser is unique:
$$\hat\beta = (X^T X)^{-1} X^T y.$$

## Remarks

The minimisers are exactly the solutions of the normal equations $X^T X b = X^T y$.
The fitted vector $\hat y = X \hat\beta = H y$, with $H = X (X^T X)^{-1} X^T$, is the [[orthogonal projection|0B8KZRT28M]] of $y$ onto the column space of $X$.
So the residual vector $y - \hat y$ is orthogonal to every column of $X$.

Example: fit $y = b_0 + b_1 t$ to the points $(0, 0)$, $(1, 1)$, $(2, 3)$.
Here $\bar t = 1$ and $\bar y = 4/3$, so $b_1 = \sum (t_i - \bar t)(y_i - \bar y) / \sum (t_i - \bar t)^2 = 3/2$ and $b_0 = \bar y - b_1 \bar t = -1/6$.
Check: the residuals are $1/6$, $-1/3$, $1/6$, which sum to $0$ and are orthogonal to $(0, 1, 2)$.
Non-example: if two columns of $X$ are equal, $X$ has rank less than $p$ and $X^T X$ is singular.
Then $S$ has infinitely many minimisers, so the formula above does not apply and $\beta$ is not identified.
