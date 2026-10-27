---
tag: 0VEFSSKX18
kind: definition
name: Poisson distribution
msc: ["60E05"]
defines: 0XB9GQTN9G
uses: [0WF4EJP91W, 0WFCGVMRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_distribution
    locator: Probability mass function
inventory: [J45TZDMRRN]
---

## Definition

Let $\lambda > 0$.
The Poisson distribution with parameter $\lambda$ is the distribution on $\{0, 1, 2, \dots\}$ with the [[probability mass function|0WF4EJP91W]]
$$p(k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for } k = 0, 1, 2, \dots$$
Here $k!$ is the [[factorial|0WFCGVMRRC]] of $k$. One writes $X \sim \operatorname{Poisson}(\lambda)$.

## Remarks

The values add up to $1$ because $\sum_{k \ge 0} \lambda^k / k! = e^{\lambda}$.
The mean and the variance are both $\lambda$.
It is the limit of the [[binomial distribution|0VRWZDWW6B]] with parameters $n$ and $\lambda / n$ as $n \to \infty$. This is the [[Poisson limit theorem|0XKTZRWTXX]].
Siméon Denis Poisson introduced the distribution in 1837.

## Explanations

### L1 human

The Poisson distribution counts rare events that happen at random, such as calls to a help desk in one hour.
If $\lambda = 2$ calls come per hour on average, the chance of no call in an hour is $e^{-2} \approx 0.135$.
