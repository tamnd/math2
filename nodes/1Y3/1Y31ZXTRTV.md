---
tag: 1Y31ZXTRTV
kind: definition
name: Poisson regression
msc: [62J12]
defines: STHTW16717
uses: [K6C48KMRKC, 0XB9GQTN9G, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_regression
---

## Definition

Let $x_1, \dots, x_n \in \R^p$ be known regressor vectors.
The *Poisson regression model* for responses $y_1, \dots, y_n \in \set{0, 1, 2, \dots}$ states three things.
The $y_i$ are independent, $y_i$ has the [[Poisson distribution|0XB9GQTN9G]] with mean $\mu_i > 0$, and
$$\log \mu_i = x_i^T \beta$$
for an unknown $\beta \in \R^p$.

## Remarks

It is the [[generalized linear model|K6C48KMRKC]] with Poisson responses and the log link, which is the canonical link.
The log-likelihood is $\ell(\beta) = \sum_i \big( y_i x_i^T \beta - e^{x_i^T \beta} - \log y_i! \big)$, a concave function.
The [[maximum likelihood|0FREPFKNS7]] estimate solves $\sum_i (y_i - \mu_i) x_i = 0$.

Example: with only an intercept, $x_i = 1$, the likelihood equation gives $\sum_i (y_i - e^{\beta}) = 0$, so $e^{\hat\beta} = \bar y$, the mean count.

When $y_i$ counts events over an exposure $t_i > 0$, one takes $\log \mu_i = \log t_i + x_i^T \beta$; the known term $\log t_i$ is an *offset*, and $e^{x_i^T \beta}$ is the rate per unit of exposure.

Non-example: if the counts have variance larger than their mean, the hypothesis that $y_i$ is Poisson fails (overdispersion).
The point estimates remain consistent when the mean is correctly specified, but the usual standard errors are too small.
