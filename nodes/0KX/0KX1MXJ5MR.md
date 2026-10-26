---
tag: 0KX1MXJ5MR
kind: statement
role: proposition
name: Radius of convergence of the binomial series
msc: [30B10]
uses: [0HB0XKDXHH, 0JBMYAA9QH]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_series
    locator: Conditions for convergence
---

## Statement

Let $\alpha$ be a real number that is not a natural number.
Then the [[binomial series|0HB0XKDXHH]] $\sum_{k=0}^{\infty} \binom{\alpha}{k} x^k$ has radius of convergence $1$.

## Remarks

The coefficients are nonzero, and $\binom{\alpha}{k+1} / \binom{\alpha}{k} = (\alpha - k)/(k + 1)$. Its absolute value tends to $1$, so the [[ratio formula|0JBMYAA9QH]] gives $R = 1$.
At $x = \pm 1$ the behavior depends on $\alpha$. For $\alpha > 0$ the series converges absolutely at both endpoints.
Mathlib states the result as `binomialSeries_radius_eq_one`.

## Explanations

### L1 human

Unless the series stops after finitely many terms, it converges exactly inside $(-1, 1)$, plus possibly some endpoints.
This matches the fact that $(1 + x)^{\alpha}$ has trouble at $x = -1$.
