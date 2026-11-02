---
tag: VDEFF7A5Q4
kind: definition
name: Errors-in-variables model
msc: [62J05, 62P20]
defines: 2XX0A85WSF
uses: [41FVC4P5JB, YM708KHV2W, 0AS800VAYX, 0KBFAWYRTE, 0477R9PYAE]
sources:
  - url: https://en.wikipedia.org/wiki/Errors-in-variables_model
---

## Definition

The *simple linear errors-in-variables model* for observed pairs $(x_i, y_i)$, $i = 1, \dots, n$, states that
$$y_i = \alpha + \beta \xi_i + \varepsilon_i, \qquad x_i = \xi_i + \eta_i,$$
where:

1. $\alpha, \beta \in \R$ are unknown parameters;
2. $\xi_i$ is the true value of the regressor, which is not observed;
3. $\varepsilon_i$ and $\eta_i$ are random errors with mean $0$, and $\eta_i$ is the *measurement error* of the regressor.

The multivariate version replaces $\beta \xi_i$ by $\beta^T \xi_i$ with $\xi_i, \eta_i \in \R^p$.

## Remarks

Assume that the $\xi_i$ are independent and identically distributed with [[variance|0477R9PYAE]] $\sigma_\xi^2 > 0$, and that the $\eta_i$ have variance $\sigma_\eta^2$.
Assume also that all the $\xi_i$, $\eta_i$, $\varepsilon_i$ are independent, with finite variances, that the $\eta_i$ are identically distributed, and that the $\varepsilon_i$ are identically distributed.
Then $\operatorname{Cov}(x_i, y_i) = \beta \sigma_\xi^2$ and $\operatorname{Var}(x_i) = \sigma_\xi^2 + \sigma_\eta^2$.
So the [[ordinary least squares|YM708KHV2W]] slope of $y$ on $x$ converges in probability to
$$\beta \, \frac{\sigma_\xi^2}{\sigma_\xi^2 + \sigma_\eta^2},$$
which differs from $\beta$ when $\beta \ne 0$ and $\sigma_\eta^2 > 0$; the slope is not [[consistent|0AS800VAYX]].

Example: $\beta = 2$ and $\sigma_\xi^2 = \sigma_\eta^2 = 1$ give the limit $1$.

Special case: if $\eta_i = 0$ for all $i$, the regressor is observed exactly and the model is ordinary [[linear regression|41FVC4P5JB]].
Error in the response alone is absorbed into $\varepsilon_i$ and does not bias the slope.

With normal $\xi_i$, $\eta_i$, $\varepsilon_i$, the parameters are not identified from the joint distribution of $(x_i, y_i)$ unless extra information is given, such as the ratio $\sigma_\varepsilon^2 / \sigma_\eta^2$.
