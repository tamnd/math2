---
tag: A6Z3GR2RWP
kind: definition
name: James–Stein estimator
msc: [62J07, 62C15, 62F10]
defines: 709T196XCT
uses: [0XN3K7RSZY, 0SSS6ERQ0S, GPBSS1V3SS, N26TSVRH2S]
sources:
  - url: https://en.wikipedia.org/wiki/James–Stein_estimator
---

## Definition

Let $p \ge 3$ and let $X$ have the [[multivariate normal distribution|0XN3K7RSZY]] on $\R^p$ with unknown mean $\theta \in \R^p$ and covariance matrix $\sigma^2 I_p$, where $\sigma^2 > 0$ is known.
The *James–Stein estimator* of $\theta$ is the [[estimator|0SSS6ERQ0S]]
$$\delta_{JS}(X) = \Big( 1 - \frac{(p - 2) \sigma^2}{\norm{X}^2} \Big) X,$$
where $\norm{\cdot}$ is the Euclidean norm.

## Remarks

The estimator is defined with probability $1$, since $X \ne 0$ almost surely.
It is a [[shrinkage estimator|GPBSS1V3SS]] toward $0$; shrinking toward a fixed point $\nu \in \R^p$ gives $\nu + \big(1 - (p - 2)\sigma^2 / \norm{X - \nu}^2\big)(X - \nu)$.
When $\norm{X}^2 < (p - 2)\sigma^2$ the factor is negative; the *positive-part* estimator replaces the factor by its positive part, and it has even smaller risk.

Under the loss $\norm{a - \theta}^2$, the estimators $(1 - c\sigma^2/\norm{X}^2) X$ have [[risk|N26TSVRH2S]] $p\sigma^2 - (2c(p - 2) - c^2) \sigma^4 E_\theta[1/\norm{X}^2]$.
This is below $p\sigma^2$, the risk of $X$, exactly when $0 < c < 2(p - 2)$, and it is smallest for $c = p - 2$, the James–Stein choice.

Example: $p = 3$, $\sigma = 1$ and the observation $X = (1, 1, 1)$.
Then $\norm{X}^2 = 3$, the factor is $1 - 1/3 = 2/3$, and $\delta_{JS}(X) = (2/3, 2/3, 2/3)$.

Non-example: the same formula with $c = 2(p - 2)$ in place of $p - 2$.
It also shrinks toward $0$, but by the risk formula above its risk equals $p\sigma^2$ for every $\theta$, so it gives no improvement over $X$.
