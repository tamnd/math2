---
tag: WQPB6GXD0M
kind: statement
role: theorem
name: Wilks' theorem
msc: [62F05, "62E20"]
uses: [YM1BNA80RC, 0RFMMBHFTV, 0JDAQHWA9N, 0AJN7WHBJZ]
about: [YM1BNA80RC]
sources:
  - url: https://en.wikipedia.org/wiki/Wilks%27_theorem
same_as:
  wikidata: Q56273825
  wikipedia: Wilks' theorem
---

## Statement

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] with density $f_\theta$, where $\theta$ lies in an open set $\Theta \subseteq \R^k$.
Assume the standard regularity conditions for the asymptotic normality of the maximum likelihood estimator, with a positive definite Fisher information.
Let $\Theta_0 \subseteq \Theta$ be the set of $\theta$ whose first $q$ coordinates equal fixed values, with $1 \le q \le k$.
Let $\lambda_n$ be the [[likelihood-ratio statistic|YM1BNA80RC]] of $H_0 \colon \theta \in \Theta_0$ based on $X_1, \dots, X_n$.
If the true $\theta$ lies in $\Theta_0$, then $-2 \log \lambda_n$ [[converges in distribution|0JDAQHWA9N]] to the [[chi-squared distribution|0RFMMBHFTV]] with $q$ degrees of freedom as $n \to \infty$.

## Remarks

The number $q$ is the difference between the dimension of $\Theta$ and the dimension of $\Theta_0$.
Proof idea: expand the log-likelihood to second order around the unrestricted and the restricted maximum likelihood estimates.
The difference becomes a quadratic form in an asymptotically normal vector, which has a limiting chi-squared law with $q$ degrees of freedom.
Example: for an i.i.d. $\mathcal{N}(\mu, \sigma^2)$ sample and $H_0 \colon \mu = 0$, here $k = 2$ and $q = 1$, so one rejects when $-2 \log \lambda_n$ exceeds the $1 - \alpha$ quantile of $\chi^2_1$.
The hypothesis that the true parameter is an interior point matters.
For a variance component tested at the boundary value $0$, the limit law is a mixture of $\chi^2_0$ and $\chi^2_1$ rather than $\chi^2_1$.

## Explanations

### L1 human

The likelihood-ratio test needs a threshold, and for that one needs the law of its statistic when the null hypothesis holds.
Wilks' theorem says that for large samples this law is almost always the same: a chi-squared law.
Its only parameter is the number of constraints that the null hypothesis imposes.

### L2 human

This is why likelihood-ratio tests are used everywhere: one computes $-2 \log \lambda_n$ and compares it with a chi-squared quantile.
The score test and the Wald test have the same limiting chi-squared law under the null hypothesis, and the three tests are asymptotically equivalent.
The theorem needs regularity: smooth densities, identifiability, and a true parameter in the interior of the parameter set.
It is an asymptotic statement, so for small samples the chi-squared approximation can be poor.
