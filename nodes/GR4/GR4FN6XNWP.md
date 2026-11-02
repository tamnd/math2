---
tag: GR4FN6XNWP
kind: definition
name: Probit model
msc: [62J12, 62P20]
defines: XCR3V8SJ01
uses: [K6C48KMRKC, 0386Y0Z7Y7, 0H8H7ZTHW2, 05AQE0QR0D, JN1PJ5AJJS]
sources:
  - url: https://en.wikipedia.org/wiki/Probit_model
---

## Definition

Let $x_1, \dots, x_n \in \R^p$ be known regressor vectors, and let $\Phi$ be the [[cumulative distribution function|0H8H7ZTHW2]] of the standard [[normal distribution|05AQE0QR0D]].
The *probit model* for responses $y_1, \dots, y_n \in \set{0, 1}$ states three things.
The $y_i$ are independent, $y_i$ has the [[Bernoulli distribution|0386Y0Z7Y7]] with parameter $p_i$, and
$$p_i = \Phi(x_i^T \beta)$$
for an unknown $\beta \in \R^p$.

## Remarks

Equivalent latent variable form: let $y_i^* = x_i^T \beta + \varepsilon_i$ with independent $\varepsilon_i \sim N(0, 1)$, and $y_i = 1$ if $y_i^* > 0$ and $y_i = 0$ otherwise.
Then $P(y_i = 1) = P(\varepsilon_i > -x_i^T \beta) = \Phi(x_i^T \beta)$, by the symmetry of the normal distribution.
The error variance is fixed at $1$ because $\beta$ and the scale of $\varepsilon_i$ cannot be identified separately from binary data.

It is the [[generalized linear model|K6C48KMRKC]] with Bernoulli responses and link $g = \Phi^{-1}$, which is not the canonical link.

Example: with $x_i = (1, t_i)$ and $\beta = (-1, 0.5)$, at $t = 2$ one gets $p = \Phi(0) = 1/2$.

Non-example: the model $p_i = 1/(1 + e^{-x_i^T \beta})$ uses the logistic function instead of $\Phi$; it is [[logistic regression|JN1PJ5AJJS]], not the probit model.
Its latent errors are logistic, with variance $\pi^2/3$, so its coefficients are typically larger than probit coefficients by a factor of roughly $1.6$ to $1.8$.
