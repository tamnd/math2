---
tag: TFCWC3N41W
kind: definition
name: Pivotal quantity
msc: [62F25, "62E15"]
defines: PXFYDT3M52
uses: [0DKRR22AEQ, 0QB913WM5E]
sources:
  - url: https://en.wikipedia.org/wiki/Pivotal_quantity
---

## Definition

Let $X$ be a random sample whose law $P_\theta$ depends on an unknown parameter $\theta$ in a set $\Theta$.
A *pivotal quantity* is a function $g(X, \theta)$ of the sample and the parameter with the following property.
The [[law|0QB913WM5E]] of the [[random variable|0DKRR22AEQ]] $g(X, \theta)$ under $P_\theta$ is the same for every $\theta \in \Theta$.

## Remarks

Example: let $X_1, \dots, X_n$ be i.i.d. $\mathcal{N}(\mu, \sigma^2)$ with $\theta = (\mu, \sigma^2)$ unknown, let $\bar X$ be the sample mean and $S$ the sample standard deviation.
Then $T = \sqrt{n}(\bar X - \mu)/S$ has Student's t-distribution with $n - 1$ degrees of freedom for every $\theta$, so $T$ is a pivotal quantity.
Non-example: in the same model, $\sqrt{n}(\bar X - \mu)$ is not pivotal, since its law $\mathcal{N}(0, \sigma^2)$ depends on $\sigma^2$.
A pivotal quantity need not be a statistic, since it may involve $\theta$.
If $P_\theta(a \le g(X, \theta) \le b) = 1 - \alpha$ for every $\theta$, then the set $\set{\theta : a \le g(X, \theta) \le b}$ is a [[confidence region|0K4NMMJBG2]] of level $1 - \alpha$.
