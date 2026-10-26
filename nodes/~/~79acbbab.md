---
tag: ~79acbbab
kind: example
name: Improper integral of x^p on an unbounded interval
msc: [40A10]
instance_of: [~0b6dbd59]
uses: [~6383ded3, ~2ae1a598, ~5a4b36b7]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Examples
---

## Example

Let $p$ be a real number. The [[improper integral|~6383ded3]] $\int_1^\infty x^p \, dx$ converges if and only if $p < -1$.
In this case,
$$\int_1^\infty x^p \, dx = -\frac{1}{p + 1}.$$
For $p \ne -1$, [[the power formula|~2ae1a598]] gives $\int_1^b x^p \, dx = \frac{b^{p+1} - 1}{p + 1}$. This has a finite limit as $b \to \infty$ exactly when $p + 1 < 0$.
For $p = -1$, $\int_1^b \frac{dx}{x} = \ln b$, [[which tends to infinity|~5a4b36b7]].

## Remarks

This example parallels the [[$p$-series test|~2ade9cef]] through the [[integral test|~2af9eb66]].
Mathlib states a form as `integrableOn_Ioi_rpow_iff`.

## Explanations

### L1 human

The function $x^p$ must decay faster than $1/x$ for the area over $[1, \infty)$ to be finite.
The function $1/x$ itself is just too slow.
