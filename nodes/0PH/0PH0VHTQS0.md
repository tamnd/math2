---
tag: 0PH0VHTQS0
kind: definition
name: Moment
msc: ["60E05"]
defines: 01XAHPADBA
uses: [0DCT0QZVQ1, 01ZWX875AT]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_(mathematics)
    locator: Formulation
---

## Definition

Let $X$ be a real random variable and let $k \ge 1$ be an integer with $E[|X|^k] < \infty$.
The $k$-th moment of $X$ is
$$m_k = E[X^k].$$
The $k$-th absolute moment is $E[|X|^k]$.

## Remarks

By the [[law of the unconscious statistician|01ZWX875AT]], $m_k = \int x^k \, \mu_X(dx)$. So the moments depend only on the law $\mu_X$ of $X$.
The first moment is the mean. The variance is $m_2 - m_1^2$.
If $E[|X|^k] < \infty$, then $E[|X|^j] < \infty$ for each $j \le k$.
The [[Cauchy distribution|0NA6Q82YR7]] has no moments of order $k \ge 1$.

## Explanations

### L1 human

Moments are numbers that sum up the shape of a distribution.
The first gives the center, the second with the first gives the spread, and the higher ones describe asymmetry and the weight of the tails.
