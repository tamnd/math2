---
tag: AYTEC1KET8
kind: definition
name: Logistic regression
msc: [62J12]
defines: JN1PJ5AJJS
uses: [K6C48KMRKC, 0386Y0Z7Y7, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Logistic_regression
---

## Definition

Let $x_1, \dots, x_n \in \R^p$ be known regressor vectors.
The *logistic regression model* for responses $y_1, \dots, y_n \in \set{0, 1}$ states three things.
The $y_i$ are independent, $y_i$ has the [[Bernoulli distribution|0386Y0Z7Y7]] with parameter $p_i$, and
$$\log \frac{p_i}{1 - p_i} = x_i^T \beta$$
for an unknown $\beta \in \R^p$.
Equivalently, $p_i = \sigma(x_i^T \beta)$, where $\sigma(t) = 1/(1 + e^{-t})$ is the logistic function.

## Remarks

It is the [[generalized linear model|K6C48KMRKC]] with Bernoulli responses and the logit link $g(\mu) = \log(\mu / (1 - \mu))$, which is the canonical link.
The log-likelihood is $\ell(\beta) = \sum_i \big( y_i x_i^T \beta - \log(1 + e^{x_i^T \beta}) \big)$, a concave function.
The [[maximum likelihood|0FREPFKNS7]] estimate solves $\sum_i (y_i - p_i) x_i = 0$ and has no closed formula in general.
For a regressor $x_{ij}$, the number $e^{\beta_j}$ is the odds ratio for a unit increase of $x_{ij}$ with the other regressors fixed.

Example: with $x_i = (1, t_i)$ and $\beta = (-2, 0.5)$, at $t = 4$ the log-odds is $0$, so $p = \sigma(0) = 1/2$; at $t = 6$ it is $1$, so $p = e/(1 + e) \approx 0.73$.

Non-example: suppose the data are perfectly separated, that is, some $\gamma \in \R^p$ has $x_i^T \gamma > 0$ whenever $y_i = 1$ and $x_i^T \gamma < 0$ whenever $y_i = 0$.
Then $\ell(c\gamma)$ increases to $0$ as $c \to \infty$, while $\ell < 0$ everywhere, so the maximum likelihood estimate does not exist.
The model is still defined, but this fitting method fails.
