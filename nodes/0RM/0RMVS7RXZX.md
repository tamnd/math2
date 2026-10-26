---
tag: 0RMVS7RXZX
kind: definition
name: Exponential function
msc: [33B10, 26A09]
defines: 0J0FCWV32D
uses: [0VP56B4EMX, 0PVJRACB9H]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Power series
---

## Definition

The exponential function $\exp \colon \mathbb{R} \to \mathbb{R}$ is defined by
$$\exp(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots.$$

## Remarks

The [[power series|0VP56B4EMX]] converges absolutely for every real $x$, because [[its radius of convergence is infinite|0PVJRACB9H]].
One also writes $e^x$ for $\exp(x)$, where $e = \exp(1)$ is the number [[e|0MVCFMW7S4]].
Other common definitions use the limit $\lim_{n \to \infty} (1 + x/n)^n$, or the equation $f' = f$ with $f(0) = 1$. They give the same function.
Mathlib defines `Real.exp` as the real part of the complex exponential series.

## Explanations

### L1 human

The exponential function is an infinite polynomial with the coefficients $1/n!$.
It grows faster than every polynomial, and its derivative is itself.
