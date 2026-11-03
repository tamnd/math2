---
tag: AYW3HY3PZP
kind: definition
name: Unscented Kalman filter
msc: ["93E11", 60G35, 93C10]
defines: H6AWC7DNNE
uses: [DFM9YXF9AG, 0V7G6WMFK0, 0BJVDCF38Y, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Unscented_transform
---

## Definition

Let $\kappa$ be a real number with $n + \kappa > 0$.
Let $m \in \R^n$ and let $P$ be a symmetric positive semidefinite $n \times n$ matrix.
Choose a matrix $S$ with $S S^T = (n + \kappa) P$, for example a [[square root|0BJVDCF38Y]] of $(n + \kappa) P$, and let $s_1, \dots, s_n$ be its columns.
The *sigma points* of $(m, P)$ are $\chi_0 = m$, $\chi_i = m + s_i$ and $\chi_{n+i} = m - s_i$ for $1 \le i \le n$, with weights $W_0 = \kappa/(n + \kappa)$ and $W_i = W_{n+i} = 1/(2(n + \kappa))$.
The *unscented transform* of $(m, P)$ under a map $g \colon \R^n \to \R^d$ is the pair
$$\bar y = \sum_{i=0}^{2n} W_i\, g(\chi_i), \qquad P_y = \sum_{i=0}^{2n} W_i\, \big(g(\chi_i) - \bar y\big)\big(g(\chi_i) - \bar y\big)^T.$$
Consider the model $x_k = f(x_{k-1}) + w_k$, $z_k = h(x_k) + v_k$ with independent noises of mean $0$.
The noises have [[covariances|0V7G6WMFK0]] $Q_k$ and $R_k$, with $R_k$ [[positive definite|0KX66CZMBB]].
The *unscented Kalman filter* computes, for $k = 1, 2, \dots$:

1. the prediction: if the unscented transform of $(\hat x_{k-1|k-1}, P_{k-1|k-1})$ under $f$ is $(\bar x, \bar P)$, put $\hat x_{k|k-1} = \bar x$ and $P_{k|k-1} = \bar P + Q_k$;
2. with the sigma points $\chi_i$ of $(\hat x_{k|k-1}, P_{k|k-1})$, the predicted measurement $\hat z_k = \sum_i W_i h(\chi_i)$, the covariances $P_{zz} = \sum_i W_i (h(\chi_i) - \hat z_k)(h(\chi_i) - \hat z_k)^T + R_k$ and $P_{xz} = \sum_i W_i (\chi_i - \hat x_{k|k-1})(h(\chi_i) - \hat z_k)^T$;
3. the update $K_k = P_{xz} P_{zz}^{-1}$, $\hat x_{k|k} = \hat x_{k|k-1} + K_k (z_k - \hat z_k)$ and $P_{k|k} = P_{k|k-1} - K_k P_{zz} K_k^T$.

## Remarks

The sigma points have weighted mean $m$, since the weights sum to $1$ and the points come in symmetric pairs.
Their weighted covariance is $\sum_{i=1}^{2n} W_i (\chi_i - m)(\chi_i - m)^T = \frac{1}{n + \kappa} \sum_{i=1}^n s_i s_i^T = \frac{S S^T}{n + \kappa} = P$.
Example: if $g(x) = A x + b$ is affine, then $\bar y = A m + b$ and $P_y = A P A^T$, the exact mean and covariance; so for a linear model the unscented Kalman filter is the [[Kalman filter|DFM9YXF9AG]].
For $n = 1$, $g(x) = x^2$, $m = 0$, $P = 1$ and $\kappa = 2$, the sigma points are $0$, $\pm\sqrt{3}$ with weights $2/3$, $1/6$, $1/6$.
So $\bar y = 1$, which is the exact mean $\mathbb{E}[X^2]$ of a standard Gaussian $X$.
Non-example: the linearization of $g(x) = x^2$ at $m = 0$ predicts the mean $g(0) = 0$, which is wrong; this is the error that the unscented transform avoids.
A widely used scaled variant uses parameters $\alpha$, $\beta$, $\kappa$ and different weights for the mean and the covariance.
