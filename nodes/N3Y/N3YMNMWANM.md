---
tag: N3YMNMWANM
kind: statement
role: theorem
name: Gauss–Markov theorem
msc: [62J05]
uses: [A06SGFCSCE, YM708KHV2W, 0V7G6WMFK0, 0BWGTN92FG, 0477R9PYAE, 01MMVW8CKC, D8VX6XQ3TT]
about: [YM708KHV2W, 41FVC4P5JB]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Markov_theorem
same_as:
  wikidata: Q428134
  wikipedia: Gauss–Markov theorem
---

## Statement

Let $X$ be a fixed real $n \times p$ matrix of rank $p$, and let $\beta \in \R^p$ be an unknown parameter.
Let $\varepsilon$ be a random vector in $\R^n$ and
$$y = X\beta + \varepsilon.$$
Assume the following.

1. $E[\varepsilon] = 0$.
2. $\operatorname{Cov}(\varepsilon) = \sigma^2 I_n$ for some unknown $\sigma^2 > 0$, so the errors are uncorrelated and [[homoscedastic|D8VX6XQ3TT]].

Let $\hat\beta = (X^T X)^{-1} X^T y$ be the [[ordinary least squares|YM708KHV2W]] estimator.
Let $\tilde\beta = C y$ be any estimator with $C$ a fixed $p \times n$ matrix such that $E[\tilde\beta] = \beta$ for every $\beta \in \R^p$.
Then $\hat\beta$ is [[unbiased|0BWGTN92FG]], and the matrix $\operatorname{Cov}(\tilde\beta) - \operatorname{Cov}(\hat\beta)$ is [[positive semidefinite|01MMVW8CKC]].
In particular, $\operatorname{Var}(c^T \tilde\beta) \ge \operatorname{Var}(c^T \hat\beta)$ for every $c \in \R^p$.

## Remarks

Write $C = (X^T X)^{-1} X^T + D$.
Unbiasedness for every $\beta$ forces $D X = 0$.
Then $\operatorname{Cov}(\tilde\beta) = \sigma^2 C C^T = \sigma^2 (X^T X)^{-1} + \sigma^2 D D^T$, because the cross terms contain $D X$.
The matrix $D D^T$ is positive semidefinite, which gives the claim.

For the model $y_i = \mu + \varepsilon_i$, the estimator $\hat\beta$ is the sample mean.
Here the theorem says that the sample mean has the smallest variance among all weighted averages $\sum_i c_i y_i$ with $\sum_i c_i = 1$.

The errors need not be normal or independent.
If the [[covariance matrix|0V7G6WMFK0]] of $\varepsilon$ is not a multiple of $I_n$, then ordinary least squares is still unbiased but in general no longer best.
The theorem compares only linear unbiased estimators: a biased estimator, such as a ridge estimator, can have a smaller mean squared error.

## Explanations

### L1 human

In a linear model with well-behaved noise, the least squares fit is the most precise estimator among those that are linear in the data and correct on average.
"Best linear unbiased estimator", or BLUE, is the short name for this property.
It is the main reason why least squares is the default method for fitting linear models.

### L2 human

The hypotheses are only about the first two moments of the errors: mean zero, equal variances and no correlation.
When the errors are also normal, a stronger result holds: least squares is then the minimum-variance unbiased estimator among all unbiased estimators, linear or not.
When the variances differ or the errors are correlated with a known covariance structure, one transforms the model to restore the hypotheses.
That leads to generalized and weighted least squares.
The theorem says nothing about biased estimators, and shrinkage methods trade a small bias for a large drop in variance.
