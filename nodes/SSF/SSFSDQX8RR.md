---
tag: SSFSDQX8RR
kind: statement
role: theorem
name: Pitman–Koopman–Darmois theorem
msc: [62B05, "62E10"]
uses: [EP9VPZ0S6G, WP4TGXJQJG, 00MRN0FARV, 0ZY9DX8FBF]
about: [EP9VPZ0S6G, WP4TGXJQJG]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_family
---

## Statement

Let $\set{f_\theta : \theta \in \Theta}$ be a family of [[probability densities|0ZY9DX8FBF]] on $\R$ with the following properties.

1. There is an open interval $I$, the same for all $\theta$, such that $f_\theta(x) > 0$ for $x \in I$ and $f_\theta(x) = 0$ for $x \notin I$.
2. Each $f_\theta$ is continuously differentiable on $I$.

Let $n \ge 2$ and let $X_1, \dots, X_n$ be [[independent and identically distributed|00MRN0FARV]] with density $f_\theta$.
Assume that there is a [[sufficient statistic|WP4TGXJQJG]] $T = (T_1, \dots, T_k) \colon I^n \to \R^k$ for $\theta$ that is continuously differentiable, with $k < n$.
Then the family is an [[exponential family|EP9VPZ0S6G]] with at most $k$ terms: there are functions $h$, $u_1, \dots, u_k$, $\eta_1, \dots, \eta_k$ and $A$ such that
$$f_\theta(x) = h(x) \exp\Big( \sum_{i=1}^{k} \eta_i(\theta) u_i(x) - A(\theta) \Big), \qquad x \in I.$$

## Remarks

The converse is easy.
For an exponential family, the sums $\sum_{j=1}^{n} u_i(X_j)$, $i = 1, \dots, k$, form a sufficient statistic of dimension $k$ for every sample size $n$, by the factorization criterion.
So, among families with a fixed support, exponential families are exactly those with a sufficient statistic whose dimension does not grow with $n$.

The idea of the proof is to write the factorization of the joint density and take logarithms.
Differentiating in the $x_j$ shows that $\partial_x \log f_\theta(x)$ lies, as a function of $\theta$, in a space of dimension at most $k$.
Integrating in $x$ gives the exponential form.

The fixed support is necessary.
For the uniform densities on $(0, \theta)$, the maximum $\max_j X_j$ is sufficient and one-dimensional for every $n$.
Yet the support moves with $\theta$, and this family is not an exponential family.

## Explanations

### L1 human

Sometimes a whole sample can be squeezed into a few numbers without losing information about the parameter, for any sample size.
The theorem says that, when the range of possible values does not depend on the parameter, this only happens for exponential families.
So exponential families are the natural home of data compression in statistics.

### L2 human

The theorem explains why exponential families appear everywhere in classical parametric statistics.
Sufficient statistics of fixed dimension give conjugate priors, complete statistics and explicit minimum-variance unbiased estimators.
The result is named after Pitman, Koopman and Darmois.
The precise regularity conditions differ from one textbook to another, but some smoothness of the sufficient statistic is always needed to exclude pathological maps from $\R^n$ to $\R^k$.
