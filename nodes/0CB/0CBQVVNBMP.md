---
tag: 0CBQVVNBMP
kind: definition
name: Kurtosis
msc: ["62E10"]
defines: 0FGAJSPX8E
uses: [0ZT24EC90K, 0VTN5RKNC5, 07RXBVTVZB]
sources:
  - url: https://en.wikipedia.org/wiki/Kurtosis
    locator: Pearson moments
  - url: https://en.wikipedia.org/wiki/Kurtosis
    locator: Excess kurtosis
---

## Definition

Let $X$ be a real random variable with $E[X^4] < \infty$, mean $\mu$ and standard deviation $\sigma > 0$.
The kurtosis of $X$ is
$$\operatorname{Kurt}(X) = E\left[\left(\frac{X - \mu}{\sigma}\right)^4\right] = \frac{\mu_4}{\sigma^4},$$
where $\mu_4$ is the fourth [[central moment|0ZT24EC90K]]. The excess kurtosis is $\operatorname{Kurt}(X) - 3$.

## Remarks

Every [[normal distribution|07RXBVTVZB]] has kurtosis $3$, so its excess kurtosis is $0$.
For every $X$, $\operatorname{Kurt}(X) \ge 1$. The Bernoulli distribution with $p = 1/2$ reaches this bound.
Distributions with positive excess kurtosis are called leptokurtic. Those with negative excess kurtosis are called platykurtic.
The kurtosis does not change under $X \mapsto aX + b$ with $a \ne 0$.

## Explanations

### L1 human

Kurtosis compares the tails of a distribution with those of the normal distribution.
A high kurtosis means that rare extreme values are more frequent than for a normal variable with the same variance.
