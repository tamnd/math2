---
tag: 0VGKB2NC4T
kind: example
name: Improper integral of x^p on an unbounded interval
msc: [40A10]
instance_of: [05KQ3F99BQ]
uses: [0VCTBJMEJF, 0Q3HYFT9RQ, 0K1N1Y4EGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Examples
---

## Example

Let $p$ be a real number. The [[improper integral|0VCTBJMEJF]] $\int_1^\infty x^p \, dx$ converges if and only if $p < -1$.
In this case,
$$\int_1^\infty x^p \, dx = -\frac{1}{p + 1}.$$
For $p \ne -1$, [[the power formula|0Q3HYFT9RQ]] gives $\int_1^b x^p \, dx = \frac{b^{p+1} - 1}{p + 1}$. This has a finite limit as $b \to \infty$ exactly when $p + 1 < 0$.
For $p = -1$, $\int_1^b \frac{dx}{x} = \ln b$, [[which tends to infinity|0K1N1Y4EGZ]].

## Remarks

This example parallels the [[$p$-series test|0ZNSSK8ZK1]] through the [[integral test|019QZ6RRVH]].
Mathlib states a form as `integrableOn_Ioi_rpow_iff`.

## Explanations

### L1 human

The function $x^p$ must decay faster than $1/x$ for the area over $[1, \infty)$ to be finite.
The function $1/x$ itself is just too slow.
