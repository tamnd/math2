---
tag: 06JZGMYTYD
kind: statement
role: theorem
name: Power series of the exponential function
msc: [33B10]
uses: [0RMVS7RXZX, 043SJ5RF59, 0EX9GFJ0B3, 0BWXV7GADW]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Power series
---

## Statement

For every real $x$,
$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}.$$
This series is the [[Maclaurin series|043SJ5RF59]] of the exponential function. Its partial sums converge to $e^x$ uniformly on each bounded interval.

## Remarks

By the [[derivative rule|0EX9GFJ0B3]], every derivative of $\exp$ at $0$ equals $\exp(0) = 1$. So the Maclaurin coefficients are $1/n!$.
With the series as the definition of $\exp$, the first claim holds by definition. Uniform convergence follows from [[the result on power series|0BWXV7GADW]].
The partial sums give good approximations near $0$. For example, $1 + x + x^2/2$ approximates $e^x$ with error $O(x^3)$.

## Explanations

### L1 human

The exponential function equals the sum of its Taylor polynomials at $0$.
Adding more terms gives better approximations of $e^x$, for every $x$.
