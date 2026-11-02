---
tag: MRCBJ0WDR0
kind: definition
name: Generalized method of moments
msc: [62F10, 62P20]
defines: ZPVMCCDYZ5
uses: [09J1H07VAH, WTXFYA093D, 0880F9EQCP, 0AJN7WHBJZ, 0DCT0QZVQ1, 0VEFSSKX18, 0TTNRP5PFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_method_of_moments
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] observations with values in a set $\mathcal{X}$, and let $\Theta \subseteq \R^k$ be a parameter set.
Let $g \colon \mathcal{X} \times \Theta \to \R^m$ with $m \ge k$ be a moment function such that the true parameter $\theta_0$ satisfies $E[g(X_1, \theta_0)] = 0$, where $E$ is the [[expectation|0DCT0QZVQ1]].
Let $\hat{g}_n(\theta) = \frac{1}{n}\sum_{i=1}^n g(X_i, \theta)$, and let $W_n$ be an $m \times m$ [[positive semidefinite|0880F9EQCP]] weight matrix computed from the data.
The *generalized method of moments estimator* is an [[estimator|0TTNRP5PFQ]]
$$\hat{\theta}_n \in \operatorname*{arg\,min}_{\theta \in \Theta} \; \hat{g}_n(\theta)^T \, W_n \, \hat{g}_n(\theta).$$

## Remarks

If $m = k$ and the equations $\hat{g}_n(\theta) = 0$ have a solution, then that solution is the estimator for every positive definite $W_n$.
This is the [[method of moments|09J1H07VAH]], a case of [[estimating equations|WTXFYA093D]].
When $m > k$ the model is over-identified, and the choice of $W_n$ matters.
Under regularity conditions, the choice $W_n \to S^{-1}$ in probability, with $S = E[g(X_1, \theta_0) g(X_1, \theta_0)^T]$ nonsingular, gives the smallest asymptotic variance, $(G^T S^{-1} G)^{-1}$ with $G = E[\nabla_\theta g(X_1, \theta_0)]$.

Example: for [[Poisson|0VEFSSKX18]]($\lambda$) data, take $g(x, \lambda) = (x - \lambda, \; x^2 - \lambda - \lambda^2)^T$, with $m = 2 > k = 1$.
Both components have mean zero at the true $\lambda$, since $E X = \lambda$ and $E X^2 = \lambda + \lambda^2$.

Non-example: in a normal model with the two parameters $(\mu, \sigma^2)$, take the single condition $E[X - \mu] = 0$, so $m = 1 < k = 2$.
The clause $m \ge k$ fails, and the objective does not depend on $\sigma^2$, so it cannot determine $\sigma^2$.
