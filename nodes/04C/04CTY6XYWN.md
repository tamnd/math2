---
tag: 04CTY6XYWN
kind: definition
name: Correlation coefficient
msc: [62H20]
defines: 0DNN9B6Q2F
uses: [0DJ8W3HP2D, 0VTN5RKNC5]
sources:
  - url: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
    locator: For a population
---

## Definition

Let $X$ and $Y$ be real random variables on one probability space with finite and positive variances.
The correlation coefficient of $X$ and $Y$ is
$$\rho_{X, Y} = \operatorname{Corr}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \, \sigma_Y},$$
where $\operatorname{Cov}$ is the [[covariance|0DJ8W3HP2D]] and $\sigma_X$, $\sigma_Y$ are the [[standard deviations|0VTN5RKNC5]].

## Remarks

By the Cauchy–Schwarz inequality, $-1 \le \rho_{X, Y} \le 1$.
$|\rho_{X, Y}| = 1$ if and only if $Y = aX + b$ almost surely for some reals $a \ne 0$ and $b$. The sign of $\rho$ is the sign of $a$.
The coefficient does not depend on units: $\rho_{aX + b, \, cY + d} = \rho_{X, Y}$ if $a c > 0$.
For a sample of pairs $(x_i, y_i)$, the sample correlation coefficient $r$ uses sample means and sample sums of squares instead of expectations.

## Explanations

### L1 human

The correlation coefficient tells how close the points $(X, Y)$ are to a straight line.
A value near $1$ means a strong increasing linear relation, and a value near $-1$ means a strong decreasing one.
A value near $0$ means that there is no linear relation.
