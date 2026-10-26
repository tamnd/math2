---
tag: 0DJ8W3HP2D
kind: definition
name: Covariance
msc: [60A05]
defines: 0KBFAWYRTE
uses: [0DCT0QZVQ1, 007QED3E0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Covariance
    locator: Definition
---

## Definition

Let $X$ and $Y$ be real random variables on one probability space with $E[X^2] < \infty$ and $E[Y^2] < \infty$.
The covariance of $X$ and $Y$ is
$$\operatorname{Cov}(X, Y) = E\left[(X - E[X]) \, (Y - E[Y])\right].$$
$X$ and $Y$ are uncorrelated if $\operatorname{Cov}(X, Y) = 0$.

## Remarks

An equivalent formula is $\operatorname{Cov}(X, Y) = E[XY] - E[X] \, E[Y]$.
The covariance of $X$ with itself is the [[variance|007QED3E0Y]]: $\operatorname{Cov}(X, X) = \operatorname{Var}(X)$.
The covariance is symmetric and bilinear: $\operatorname{Cov}(aX + bY, Z) = a \operatorname{Cov}(X, Z) + b \operatorname{Cov}(Y, Z)$. It does not change when one adds constants to $X$ or $Y$.
The Cauchy–Schwarz inequality gives $|\operatorname{Cov}(X, Y)| \le \sigma_X \sigma_Y$.

## Explanations

### L1 human

Covariance says whether two quantities tend to move in the same direction.
Height and weight of people have positive covariance. The size of a covariance depends on the units, so one often uses the correlation coefficient to compare.
