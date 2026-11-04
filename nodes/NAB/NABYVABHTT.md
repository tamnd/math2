---
tag: NABYVABHTT
kind: proof
name: Proof that independent random variables are uncorrelated
msc: [60A05]
proves: 077GN9HDR6
uses: [0E9502NT92, 05AW1G0WE1, 0DJ8W3HP2D, 0P7PTC8DDE, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Covariance
    locator: Uncorrelatedness and independence
---

## Proof

We expand the covariance and use the product rule for independent variables.

1. Let $X$ and $Y$ be [[independent|0E9502NT92]] real random variables with $E[X^2] < \infty$ and $E[Y^2] < \infty$.
2. For each real $x$, $\abs{x} \le (1 + x^2)/2$, because $(\abs{x} - 1)^2 \ge 0$. The integral of nonnegative functions is monotone.
3. So $E[\abs{X}] \le (1 + E[X^2])/2 < \infty$. Thus $X$ is integrable, and in the same way $Y$ is integrable. Let $m = E[X]$ and $n = E[Y]$ be their [[expected values|0DCT0QZVQ1]].
4. By the [[product rule for independent variables|05AW1G0WE1]], $XY$ is integrable and $E[XY] = mn$.
5. Pointwise, $(X - m)(Y - n) = XY - nX - mY + mn$.
6. Each term on the right is integrable. By [[linearity of expectation|0P7PTC8DDE]],
$$E[(X - m)(Y - n)] = E[XY] - n E[X] - m E[Y] + mn = E[XY] - mn.$$
7. By the definition of the [[covariance|0DJ8W3HP2D]] and steps 4 and 6, $\operatorname{Cov}(X, Y) = mn - mn = 0$.
8. So $X$ and $Y$ are uncorrelated.

## Idea

The covariance equals $E[XY] - E[X] E[Y]$. Independence makes the mean of the product equal to the product of the means, so this difference is $0$.
