---
tag: KV0F0E8YR2
kind: definition
name: Estimating equations
msc: [62F10, 62F12]
defines: WTXFYA093D
uses: [0TTNRP5PFQ, 0DCT0QZVQ1, 0AJN7WHBJZ, CP97GRVTQ0, 4503R8BVF8, 09J1H07VAH]
sources:
  - url: https://en.wikipedia.org/wiki/Estimating_equations
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a family of distributions on a set $\mathcal{X}$, with $\Theta \subseteq \R^k$.
An *estimating function* is a map $g \colon \mathcal{X} \times \Theta \to \R^k$.
It is *unbiased* if $E_\theta[g(X, \theta)] = 0$ for every $\theta \in \Theta$, where $X \sim P_\theta$ and $E_\theta$ is the [[expectation|0DCT0QZVQ1]].
For [[i.i.d.|0AJN7WHBJZ]] observations $X_1, \dots, X_n$, the *estimating equation* is
$$\sum_{i=1}^n g(X_i, \theta) = 0,$$
and an [[estimator|0TTNRP5PFQ]] $\hat{\theta}_n$ that solves it is an estimating-equation estimator.

## Remarks

Example: the [[score|CP97GRVTQ0]] $g(x, \theta) = \nabla_\theta \log f(x; \theta)$ is an unbiased estimating function under the usual regularity conditions, and its estimating equation gives the likelihood equations.

Example: in the [[method of moments|09J1H07VAH]] for a Poisson mean, $g(x, \lambda) = x - \lambda$ has $E_\lambda[X - \lambda] = 0$, and the equation $\sum_i (X_i - \lambda) = 0$ gives $\hat{\lambda} = \bar{X}$.

Non-example: for the Poisson mean, $g(x, \lambda) = x - 2\lambda$ has $E_\lambda[g(X, \lambda)] = -\lambda \ne 0$, so it is not unbiased, and its root $\bar{X}/2$ converges to $\lambda/2$, not to $\lambda$.

Estimators of this kind are the $\psi$-type [[M-estimators|4503R8BVF8]].
Under regularity conditions, $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} \mathcal{N}(0, A^{-1} B A^{-T})$ with $A = E_\theta[\nabla_\theta g(X, \theta)]$ and $B = E_\theta[g(X, \theta) g(X, \theta)^T]$.
