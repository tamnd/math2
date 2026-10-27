---
tag: 0V3FZMVB4K
kind: definition
name: Gamma function
msc: [33B15]
defines: 0H5SYBSED9
uses: [0VCTBJMEJF, 0FR1BDKK10]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
    locator: Main definition
inventory: [2VW1BD3795]
---

## Definition

For a real number $s > 0$, the gamma function is
$$\Gamma(s) = \int_0^\infty t^{s-1} e^{-t} \, dt.$$

## Remarks

The [[improper integral|0VCTBJMEJF]] converges at $0$ because $s > 0$, and at $\infty$ because $e^{-t}$ decays fast. Both claims follow from the [[comparison test|0FR1BDKK10]].
Integration by parts gives $\Gamma(s + 1) = s \, \Gamma(s)$. Also $\Gamma(1) = 1$, so [[$\Gamma$ extends the factorial|0FDCW77H44]].
The function extends to all real numbers except $0, -1, -2, \dots$, by the recursion. Mathlib defines this extension as `Real.Gamma`.
The notation $\Gamma$ is due to Adrien-Marie Legendre.

## Explanations

### L1 human

The gamma function is an integral that depends on a parameter $s$.
At positive integers it gives factorials, so it interpolates the factorial.
