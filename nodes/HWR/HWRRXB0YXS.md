---
tag: HWRRXB0YXS
kind: concept
name: Digamma function
msc: ["33B15"]
sources:
  - url: https://en.wikipedia.org/wiki/Digamma_function
same_as:
  wikidata: Q905326
  wikipedia: Digamma function
---

## Summary

The digamma function $\psi$ is the logarithmic derivative of the [[gamma function|0H5SYBSED9]], $\psi(z) = \Gamma'(z)/\Gamma(z)$.
It turns the product rule $\Gamma(z+1) = z\,\Gamma(z)$ into the sum rule $\psi(z+1) = \psi(z) + 1/z$.
At positive integers it gives the [[harmonic numbers|0NANDX7V02]] shifted by the [[Euler–Mascheroni constant|00C5P9JZBK]].
It is the first member of the family of [[polygamma functions|3J3QGKPMZQ]].

## Explanations

### L1 human

The gamma function grows very fast, so it is often easier to look at its logarithm.
The digamma function is the slope of $\log \Gamma$.
Because $\Gamma(n+1) = n!$, the slope of $\log \Gamma$ changes by $1/n$ when one steps from $n$ to $n+1$.
So the values at whole numbers add up the fractions $1, \frac12, \frac13, \ldots$.
For example, $\psi(1) = -\gamma \approx -0.5772$ and $\psi(4) = 1 + \frac12 + \frac13 - \gamma$.
