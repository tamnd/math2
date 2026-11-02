---
tag: NA5X6JVK5J
kind: definition
name: Weighted least squares
msc: [62J05]
defines: H5CGZHBR58
uses: [P142WXJCF3, YM708KHV2W, D8VX6XQ3TT]
sources:
  - url: https://en.wikipedia.org/wiki/Weighted_least_squares
---

## Definition

Let $X$ be a real $n \times p$ matrix with rows $x_1^T, \dots, x_n^T$ and rank $p$, let $y \in \R^n$, and let $w_1, \dots, w_n > 0$ be weights.
Let $W$ be the diagonal matrix with diagonal entries $w_1, \dots, w_n$.
The *weighted least squares estimator* is the minimiser of
$$\sum_{i=1}^n w_i (y_i - x_i^T b)^2$$
over $b \in \R^p$, which is
$$\hat\beta_{\mathrm{WLS}} = (X^T W X)^{-1} X^T W y.$$

## Remarks

Example: take $p = 1$ and $X$ the column of ones, so that $x_i^T b = b$.
The function $\sum_i w_i (y_i - b)^2$ has derivative $-2 \sum_i w_i (y_i - b)$, which vanishes at $b = \sum_i w_i y_i / \sum_i w_i$, the weighted mean.
The formula agrees: $X^T W X = \sum_i w_i$ and $X^T W y = \sum_i w_i y_i$.

Non-example: if some weight is negative, the objective need not be bounded below.
With $n = 1$, $p = 1$, $x_1 = 1$ and $w_1 = -1$, the function $-(y_1 - b)^2$ has no minimum.

In a model $y = X\beta + \varepsilon$ with uncorrelated errors and $\operatorname{Var}(\varepsilon_i) = \sigma_i^2$, the choice $w_i = 1/\sigma_i^2$ gives the [[generalized least squares|P142WXJCF3]] estimator with $\Omega = \operatorname{diag}(\sigma_1^2, \dots, \sigma_n^2)$.
This is the usual remedy for known [[heteroscedasticity|D8VX6XQ3TT]].
With all weights equal it is [[ordinary least squares|YM708KHV2W]].
