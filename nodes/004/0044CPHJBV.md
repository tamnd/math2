---
tag: 0044CPHJBV
kind: definition
name: Natural logarithm
aliases: [logarithm]
msc: [33B10, 26A09]
defines: 04DXAFN2ES
uses: [0RMVS7RXZX, 0KN2V7840E, 00KAFBR32E]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Definition

For a real number $x > 0$, the natural logarithm $\ln x$ is the unique real number $y$ with $e^y = x$.
This defines a function $\ln \colon (0, \infty) \to \mathbb{R}$.

## Remarks

The number $y$ exists and is unique, because $\exp$ is a [[strictly increasing|0KN2V7840E]] continuous bijection from $\mathbb{R}$ onto $(0, \infty)$.
Some texts define instead $\ln x = \int_1^x \frac{dt}{t}$. Both definitions give the [[same function|0K1N1Y4EGZ]].
Other notations are $\log x$ and $\log_e x$. Mathlib defines `Real.log` for all reals, with $\log x = \log |x|$ and $\log 0 = 0$.

## Explanations

### L1 human

The logarithm answers the question: to which power must we raise $e$ to get $x$?
For example, $\ln 1 = 0$ and $\ln e = 1$.
