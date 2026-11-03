---
tag: 90VRF3WE0Q
kind: definition
name: Ensemble Kalman filter
msc: [86A22, "93E11", 62M20]
defines: H6QW728ZFF
uses: [0V7G6WMFK0, HWP11G3HTN]
sources:
  - url: https://en.wikipedia.org/wiki/Ensemble_Kalman_filter
---

## Definition

Let the state of a system at time $t_k$ be a vector in $\R^n$.
Let the model $M_k \colon \R^n \to \R^n$ map the state at $t_k$ to the state at $t_{k+1}$.
Let the observation at $t_k$ be $y_k = H x_k + \varepsilon_k$, where $H$ is an $m \times n$ matrix.
The noise $\varepsilon_k$ is Gaussian with mean $0$ and positive definite [[covariance matrix|0V7G6WMFK0]] $R$ of size $m \times m$.
Fix an ensemble size $N \ge 2$.
The *ensemble Kalman filter* carries an ensemble $x^{(1)}, \dots, x^{(N)}$ of states and repeats two steps.

1. Forecast step: replace each member by $x^{f,(i)} = M_k(x^{(i)})$, possibly plus a sample of model noise.
2. Analysis step: compute the ensemble mean $\bar x^f = \frac{1}{N} \sum_i x^{f,(i)}$ and the sample covariance
$$P^f = \frac{1}{N - 1} \sum_{i=1}^{N} (x^{f,(i)} - \bar x^f)(x^{f,(i)} - \bar x^f)^T.$$
Set the gain $K = P^f H^T (H P^f H^T + R)^{-1}$.
Draw independent perturbations $\varepsilon^{(i)}$ with mean $0$ and covariance $R$, and replace each member by
$$x^{a,(i)} = x^{f,(i)} + K \big( y_{k+1} + \varepsilon^{(i)} - H x^{f,(i)} \big).$$

The ensemble mean after the analysis step is the estimate of the state, and the spread of the ensemble is the estimate of its uncertainty.

## Remarks

Example: for a scalar state with $H = 1$, forecast members with sample variance $P^f = 1$ and $R = 1$, the gain is $K = 1/2$.
Each member moves halfway toward its perturbed observation, as in the scalar Kalman filter with the same variances.
For a linear model and Gaussian noise, the ensemble mean and covariance converge to those of the Kalman filter as $N \to \infty$; the sampling is a [[Monte Carlo method|HWP11G3HTN]].

Non-example: with $N = 1$ the sample covariance is not defined, and there is no gain to compute; the condition $N \ge 2$ fails.

The perturbed observations $\varepsilon^{(i)}$ keep the analysis spread consistent with the Kalman filter.
Square-root variants update the ensemble deterministically without perturbing the observations.
For small ensembles in large models, the sample covariance is usually damped at long distances (localisation) and inflated by a factor slightly above $1$.
