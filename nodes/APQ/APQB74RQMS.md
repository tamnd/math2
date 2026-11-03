---
tag: APQB74RQMS
kind: definition
name: Data assimilation
msc: [86A22, 62M20, "93E11"]
defines: TKT0QAPWW8
uses: [0JWRJX2RMP, PCMW7KN5P4, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Data_assimilation
---

## Definition

Let the state of a system be a vector $x \in \R^n$.
Let $x_b \in \R^n$ be a background estimate of $x$, with error assumed to have mean zero and covariance $B$, a symmetric positive definite $n \times n$ matrix.
Let $y \in \R^m$ be observations related to the state by $y = H(x) + \varepsilon$, where $H \colon \R^n \to \R^m$ is the observation operator.
The error $\varepsilon$ has mean zero and symmetric positive definite covariance $R$, and it is independent of the background error.
*Data assimilation* is the estimation of $x$ from $x_b$ and $y$ under these error models; the estimate $x_a$ is called the *analysis*.
In the [[Bayesian|0JWRJX2RMP]] formulation with Gaussian errors, the analysis is the maximiser of the posterior density, that is the minimiser of
$$J(x) = \frac12 (x - x_b)^T B^{-1} (x - x_b) + \frac12 \left(y - H(x)\right)^T R^{-1} \left(y - H(x)\right).$$

## Remarks

If $H$ is linear, given by an $m \times n$ matrix also written $H$, the minimiser is
$$x_a = x_b + K (y - H x_b), \qquad K = B H^T (H B H^T + R)^{-1},$$
and its error covariance is $(I - K H) B$.
This follows by setting the gradient $B^{-1}(x - x_b) - H^T R^{-1}(y - H x)$ to zero; $K$ is the Kalman gain.
It is then also the best linear unbiased estimate, without the Gaussian assumption, and it is a weighted [[least squares|0BYTQ4X1HC]] solution.

Example: with $n = m = 1$, $H = 1$, $x_b = 10$, $B = 4$, $y = 12$ and $R = 1$, the gain is $K = 4/5$, the analysis is $x_a = 10 + 0.8 \cdot 2 = 11.6$, and its variance is $0.2 \cdot 4 = 0.8$, smaller than both $B$ and $R$.

Non-example: replacing the model values by the observations at observed points is not an analysis in this sense.
It ignores the error statistics and the unobserved variables, and it produces imbalanced initial states.

Sequential methods, such as the Kalman filter and its ensemble versions, apply this update at each observation time and propagate $B$ with the model.
Variational methods, such as 3D-Var and four-dimensional variational assimilation, minimise $J$ or its extension over a time window.
Viewed as an [[inverse problem|PCMW7KN5P4]], the background term regularises the problem of recovering $x$ from incomplete data.
