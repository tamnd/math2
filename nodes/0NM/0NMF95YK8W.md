---
tag: 0NMF95YK8W
kind: statement
role: proposition
name: Variance as the mean of the square minus the square of the mean
aliases: [computational-formula-for-variance]
msc: [60A05]
uses: [007QED3E0Y, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance
    locator: Definition
---

## Statement

Let $X$ be a real random variable with $E[X^2] < \infty$. Then
$$\operatorname{Var}(X) = E[X^2] - (E[X])^2.$$

## Remarks

Proof: with $\mu = E[X]$, $(X - \mu)^2 = X^2 - 2\mu X + \mu^2$. By [[linearity of expectation|0P7PTC8DDE]], $E[(X - \mu)^2] = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2$.
As a corollary, $(E[X])^2 \le E[X^2]$.
For a fair die, $E[X^2] = 91/6$ and $E[X] = 7/2$, so $\operatorname{Var}(X) = 91/6 - 49/4 = 35/12$.
In floating-point arithmetic, this formula can lose much precision when $E[X^2]$ and $(E[X])^2$ are close.

## Explanations

### L1 human

This formula is often the fastest way to compute a variance: find the average of the squares and subtract the square of the average.
