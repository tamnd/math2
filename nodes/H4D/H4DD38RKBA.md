---
tag: H4DD38RKBA
kind: definition
name: Empirical likelihood
msc: [62G10, 62G15, 62G20]
defines: BFQBHBN5F5
uses: [0AJN7WHBJZ, 05FSTXM92W, 0TCHAS04WK, 0RFMMBHFTV]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_likelihood
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] random vectors in $\R^d$, and let $\mu \in \R^d$.
The *empirical likelihood ratio* for the mean $\mu$ is
$$\mathcal{R}(\mu) = \max\Big\{ \prod_{i=1}^{n} n w_i \;:\; w_i \ge 0, \ \sum_{i=1}^{n} w_i = 1, \ \sum_{i=1}^{n} w_i X_i = \mu \Big\},$$
with $\mathcal{R}(\mu) = 0$ when no weights satisfy the constraints.
More generally, for a parameter $\theta$ defined by $E[m(X, \theta)] = 0$, the constraint $\sum_i w_i X_i = \mu$ is replaced by $\sum_i w_i m(X_i, \theta) = 0$.

## Remarks

The factor $n$ makes the unconstrained maximum equal to $1$: without the mean constraint, $\prod w_i$ is largest at $w_i = 1/n$.
Feasible weights exist exactly when $\mu$ lies in the [[convex hull|0TCHAS04WK]] of $X_1, \dots, X_n$.
When $\mu$ is in the interior of the hull, the maximiser is $w_i = \frac{1}{n(1 + \lambda^{T}(X_i - \mu))}$, where $\lambda \in \R^d$ solves $\sum_i \frac{X_i - \mu}{1 + \lambda^{T}(X_i - \mu)} = 0$.
Owen's theorem: if $\mu_0 = E[X_1]$ and the covariance matrix of $X_1$ is finite and nonsingular, then $-2 \ln \mathcal{R}(\mu_0)$ converges in distribution to the [[chi-squared distribution|0RFMMBHFTV]] with $d$ degrees of freedom.
So $\set{\mu : -2\ln\mathcal{R}(\mu) \le c}$, with $c$ the $(1-\alpha)$-quantile of $\chi^2_d$, is an asymptotic confidence region of level $1 - \alpha$.

Example: $\mu = \bar X$.
The weights $w_i = 1/n$ satisfy the constraint, so $\mathcal{R}(\bar X) = 1$, the largest possible value.

Non-example: data $(1, 2, 3)$ in $\R$ and $\mu = 5$.
No weighted average of $1, 2, 3$ equals $5$, because $5$ is outside the convex hull $[1, 3]$, so $\mathcal{R}(5) = 0$.
