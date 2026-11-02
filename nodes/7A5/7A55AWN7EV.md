---
tag: 7A55AWN7EV
kind: definition
name: M-estimator
msc: [62F10, 62F35, 62G35]
defines: 4503R8BVF8
uses: [0TTNRP5PFQ, 0FREPFKNS7, 0QNRBHWV35]
sources:
  - url: https://en.wikipedia.org/wiki/M-estimator
---

## Definition

Let $X_1, \dots, X_n$ be observations with values in a set $\mathcal{X}$, and let $\Theta$ be a parameter set.
Let $\rho \colon \mathcal{X} \times \Theta \to \R$ be a function.
An *M-estimator* with loss $\rho$ is an [[estimator|0TTNRP5PFQ]] $\hat{\theta}_n$ that minimizes
$$\theta \mapsto \sum_{i=1}^n \rho(X_i, \theta)$$
over $\Theta$.

## Remarks

When $\Theta \subseteq \R^k$ is open and $\rho$ is differentiable in $\theta$ with gradient $\psi(x, \theta) = \nabla_\theta \rho(x, \theta)$, an interior minimizer solves $\sum_{i=1}^n \psi(X_i, \theta) = 0$.
An estimator defined as a root of such an equation, for a given function $\psi$, is also called an M-estimator (of $\psi$-type), or a Z-estimator.

Example: with $\rho(x, \theta) = (x - \theta)^2$ on $\R$, the sum is minimized at the [[sample mean|0QNRBHWV35]], since its derivative $-2\sum_i (X_i - \theta)$ vanishes only at $\theta = \bar{X}$.
With $\rho(x, \theta) = \abs{x - \theta}$, the minimizers are the sample medians.
With $\rho(x, \theta) = -\log f(x; \theta)$ for a family of densities, the M-estimator is the [[maximum likelihood estimator|0FREPFKNS7]].

Non-example: the midrange $(\min_i X_i + \max_i X_i)/2$ minimizes $\max_i \abs{X_i - \theta}$, a maximum over the observations rather than a sum of terms $\rho(X_i, \theta)$, so this description does not exhibit it as an M-estimator.

Under regularity conditions, $\sqrt{n}(\hat{\theta}_n - \theta_0)$ is asymptotically normal with the sandwich covariance $A^{-1} B A^{-T}$, where $A = E[\nabla_\theta \psi(X, \theta_0)]$ and $B = E[\psi(X, \theta_0)\psi(X, \theta_0)^T]$, and $\theta_0$ minimizes $E[\rho(X, \theta)]$.
