---
tag: 0J7PHRBNNS
kind: statement
role: corollary
name: Logarithm of a quotient
msc: [33B10]
uses: [0K2FNY6DYV]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For all real $x > 0$ and $y > 0$,
$$\ln \frac{x}{y} = \ln x - \ln y.$$

## Remarks

Apply the [[product rule for logarithms|0K2FNY6DYV]] to $x = \frac{x}{y} \cdot y$.
With $x = 1$ it gives $\ln(1/y) = -\ln y$.
Mathlib states it as `Real.log_div`.

## Explanations

### L1 human

The logarithm of a quotient is the difference of the logarithms.
Division becomes subtraction.
