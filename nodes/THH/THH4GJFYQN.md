---
tag: THH4GJFYQN
kind: definition
name: Generalized linear model
msc: [62J12]
defines: K6C48KMRKC
uses: [EP9VPZ0S6G, 41FVC4P5JB, 0WQNRCNY3M, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_linear_model
---

## Definition

Let $x_1, \dots, x_n \in \R^p$ be known regressor vectors.
A *generalized linear model* for independent responses $y_1, \dots, y_n$ consists of three parts.

1. Random component: each $y_i$ has the density $f(y; \theta_i, \phi) = \exp\big( (y \theta_i - b(\theta_i))/a(\phi) + c(y, \phi) \big)$ with respect to a fixed measure.
This is an [[exponential family|EP9VPZ0S6G]] with natural parameter $\theta_i$, dispersion parameter $\phi > 0$, and fixed functions $a, b, c$.
2. Linear predictor: $\eta_i = x_i^T \beta$ for an unknown $\beta \in \R^p$.
3. Link: a known strictly monotone differentiable function $g$ such that $g(\mu_i) = \eta_i$, where $\mu_i = E[y_i]$ is the [[expected value|0WQNRCNY3M]] of $y_i$.

## Remarks

In the random component, $\mu_i = b'(\theta_i)$ and $\operatorname{Var}(y_i) = a(\phi) \, b''(\theta_i)$.
The link $g$ with $g(b'(\theta)) = \theta$ is the *canonical link*; with it, $\theta_i = x_i^T \beta$.

Example: the normal distribution $N(\mu, \sigma^2)$ has the form of clause 1 with $\theta = \mu$, $b(\theta) = \theta^2/2$ and $a(\phi) = \phi = \sigma^2$.
With the identity link, $\mu_i = x_i^T \beta$, and the model is normal [[linear regression|41FVC4P5JB]].
Example: for Bernoulli responses with the logit link $g(\mu) = \log(\mu/(1 - \mu))$ one gets logistic regression; for Poisson responses with the log link one gets Poisson regression.

Non-example: the model $y_i = x_i^T \beta + \varepsilon_i$ with independent standard Cauchy errors $\varepsilon_i$ is not a generalized linear model.
The Cauchy location family is not of the form of clause 1, and $y_i$ has no expected value, so clause 3 cannot hold either.

The coefficients are estimated by [[maximum likelihood|0FREPFKNS7]]; with the canonical link the likelihood equations are $\sum_i (y_i - \mu_i) x_i = 0$.
