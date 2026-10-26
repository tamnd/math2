---
tag: 0GQ3H7VW3V
kind: definition
name: Skewness
msc: ["62E10"]
defines: 0YVQKBNV2R
uses: [0ZT24EC90K, 0VTN5RKNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Skewness
    locator: Fisher's moment coefficient of skewness
---

## Definition

Let $X$ be a real random variable with $E[|X|^3] < \infty$, mean $\mu$ and standard deviation $\sigma > 0$.
The skewness of $X$ is
$$\gamma_1 = E\left[\left(\frac{X - \mu}{\sigma}\right)^3\right] = \frac{\mu_3}{\sigma^3},$$
where $\mu_3$ is the third [[central moment|0ZT24EC90K]].

## Remarks

A distribution that is symmetric about its mean has skewness $0$. The converse is false.
Positive skewness usually means a longer tail on the right. Negative skewness usually means a longer tail on the left.
The skewness does not change under $X \mapsto aX + b$ with $a > 0$. For $a < 0$, it changes sign.
The exponential distribution has skewness $2$.

## Explanations

### L1 human

Skewness tells to which side a distribution leans.
Incomes have positive skewness: most values are moderate, and a few are very large.
