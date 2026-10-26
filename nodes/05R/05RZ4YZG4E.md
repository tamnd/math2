---
tag: 05RZ4YZG4E
kind: definition
name: Standard score
msc: [62P99]
defines: 0VXJHZ1G9J
uses: [0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_score
    locator: Calculation
---

## Definition

Let $X$ be a real random variable with mean $\mu = E[X]$ and standard deviation $\sigma > 0$.
The standard score, or $z$-score, of a real number $x$ is
$$z = \frac{x - \mu}{\sigma}.$$
The standardized random variable is $Z = (X - \mu)/\sigma$.

## Remarks

The standardized variable $Z$ has mean $0$ and variance $1$.
If $X \sim \mathcal{N}(\mu, \sigma^2)$, then $Z \sim \mathcal{N}(0, 1)$. So $P(X \le x) = \Phi(z)$, where $\Phi$ is the standard normal cumulative distribution function.
For a data set, one uses the sample mean and the sample standard deviation in place of $\mu$ and $\sigma$.

## Explanations

### L1 human

A $z$-score says how unusual a value is, in units of the standard deviation.
Suppose that test scores have mean $70$ and standard deviation $10$.
Then a score of $85$ has $z = 1.5$. It is one and a half standard deviations above the mean.
