---
tag: ZE1FSZ6GJF
kind: definition
name: Tikhonov regularization
msc: [47A52, 45Q05, 65R30]
defines: M68V0M5A3R
uses: [HM2HHE3J51, 03TM135G0N, 6HSJBJ8TTQ, 0YY8VX28JR]
sources:
  - url: https://en.wikipedia.org/wiki/Ridge_regression
---

## Definition

Let $X$ and $Y$ be real or complex [[Hilbert spaces|HM2HHE3J51]], let $K \colon X \to Y$ be a [[bounded linear operator|03TM135G0N]] with [[adjoint|6HSJBJ8TTQ]] $K^*$, let $y \in Y$ and let $\alpha > 0$.
The *Tikhonov regularized solution* of $K x = y$ with parameter $\alpha$ is the unique minimizer $x_\alpha \in X$ of the Tikhonov functional
$$J_\alpha(x) = \norm{K x - y}^2 + \alpha \norm{x}^2.$$
It is given by
$$x_\alpha = (K^* K + \alpha I)^{-1} K^* y.$$
*Tikhonov regularization* is the method that approximates solutions of $K x = y$ by $x_\alpha$, with $\alpha$ chosen according to the noise level of the data.

## Remarks

The operator $K^* K + \alpha I$ satisfies $\ip{(K^* K + \alpha I) x}{x} \ge \alpha \norm{x}^2$, so it is invertible with inverse of norm at most $1/\alpha$; the minimizer is characterized by the normal equation $(K^* K + \alpha I) x = K^* y$.
So $x_\alpha$ exists, is unique, and depends continuously on $y$.

If $y$ lies in the range of $K$, then $x_\alpha \to K^\dagger y$ as $\alpha \to 0$, where $K^\dagger y$ is the solution of smallest norm, given by the [[Moore–Penrose inverse|0YY8VX28JR]].
For noisy data $y^\delta$ with $\norm{y^\delta - y} \le \delta$, the choice $\alpha(\delta) \to 0$ with $\delta^2 / \alpha(\delta) \to 0$ gives $x_{\alpha(\delta)}^\delta \to K^\dagger y$ as $\delta \to 0$.
For compact $K$ with singular system $(\sigma_n, v_n, u_n)$, $x_\alpha = \sum_n \frac{\sigma_n}{\sigma_n^2 + \alpha} \ip{y}{u_n} v_n$, so the unbounded factors $1/\sigma_n$ of [[Picard's criterion|MPB3QF09E5]] are replaced by factors bounded by $1/(2\sqrt{\alpha})$.

Example: $X = Y = \R$ and $K x = k x$ with $k \ne 0$.
Then $J_\alpha(x) = (k x - y)^2 + \alpha x^2$ has derivative $2k(k x - y) + 2\alpha x$, which vanishes at $x_\alpha = k y / (k^2 + \alpha)$, in agreement with the formula.

Non-example: the case $\alpha = 0$ is excluded.
For $K = 0$ on $X = Y = \R$, every $x$ minimizes $\norm{K x - y}^2$, so there is no unique minimizer.

In finite dimensions, with $K$ a data matrix, $x_\alpha$ is the [[ridge regression|3KZW2930V2]] estimator.

## Explanations

### L1 human

The method adds a penalty $\alpha \norm{x}^2$ on the size of the solution to the misfit $\norm{K x - y}^2$, and takes the best compromise.
