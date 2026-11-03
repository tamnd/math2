---
tag: T9SH7GPV3J
kind: definition
name: Spectral risk measure
msc: [91G70, 91B05]
defines: QA3G11N6PG
uses: [0X60VE98HN, 0PNRKMRC55, YR1E91KSFA, KKVCHFGA14, C063APG9NT]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_risk_measure
---

## Definition

Let $\phi \colon [0, 1] \to [0, \infty)$ be a function with these properties:

1. $\phi$ is nondecreasing;
2. $\int_0^1 \phi(p) \, dp = 1$.

Such a $\phi$ is called a *risk spectrum*.
For an integrable loss $L$ with [[quantile function|0X60VE98HN]] $F_L^{-1}$, the *spectral risk measure* with spectrum $\phi$ is
$$\rho_\phi(L) = \int_0^1 \phi(p) \, F_L^{-1}(p) \, dp,$$
whenever this integral is finite.

## Remarks

Every $\rho_\phi$ is a [[coherent risk measure|YR1E91KSFA]]; it depends only on the law of $L$ and is additive for comonotone losses.
Example: $\phi = 1$ gives $\rho_\phi(L) = E[L]$.
Example: $\phi(p) = \frac{1}{1 - \alpha} \mathbf{1}_{[\alpha, 1]}(p)$ is nondecreasing with integral $1$, and gives the [[expected shortfall|KKVCHFGA14]] $\mathrm{ES}_\alpha(L)$.
Non-example: $\phi(p) = 2 \cdot \mathbf{1}_{[0, 1/2]}(p)$ has integral $1$ but is decreasing, so it fails clause 1; it puts its weight on the better half of the outcomes.
The [[value at risk|C063APG9NT]] $F_L^{-1}(\alpha)$ would need all weight at the single point $\alpha$, which is not given by any function $\phi$, and indeed it is not coherent.
In the profit convention $X = -L$, the same measure is written $-\int_0^1 \psi(p) F_X^{-1}(p) \, dp$ with a nonincreasing $\psi$.
