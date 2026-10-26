---
tag: 039JAF7ZAN
kind: example
name: Integral of exp(-x) over the half line
msc: [40A10]
instance_of: [05KQ3F99BQ]
uses: [0VCTBJMEJF, 06D0EWR2DV]
sources:
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Convergence of the integral
---

## Example

The [[improper integral|0VCTBJMEJF]] of $e^{-x}$ over $[0, \infty)$ converges, and
$$\int_0^\infty e^{-x} \, dx = 1.$$
For $b > 0$, [[the exponential formula|06D0EWR2DV]] with $c = -1$ gives $\int_0^b e^{-x} \, dx = 1 - e^{-b}$. This tends to $1$ as $b \to \infty$.

## Remarks

It is the case $s = 1$ of the [[gamma function|0V3FZMVB4K]]: $\Gamma(1) = 1$.
Mathlib states it as `integral_exp_neg_Ioi_zero`.

## Explanations

### L1 human

The region under $e^{-x}$ is infinitely long, but its area is finite.
The area is exactly $1$.
