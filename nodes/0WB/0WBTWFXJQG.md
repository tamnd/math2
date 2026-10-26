---
tag: 0WBTWFXJQG
kind: concept
name: Integration by partial fractions
msc: [26A36]
uses: [0WCZH4AFMT, 0K1N1Y4EGZ, 065XW2V6C3]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_fraction_decomposition
    locator: Application to symbolic integration
---

## Summary

Integration by partial fractions is a method to integrate [[rational functions|0WCZH4AFMT]]. We write the rational function as a polynomial plus a sum of simple fractions. Each simple fraction has a known antiderivative.

## Remarks

Over $\mathbb{R}$, the simple fractions have the forms $\frac{A}{(x - r)^k}$ and $\frac{B x + C}{(x^2 + p x + q)^k}$, with $p^2 < 4 q$.
Their antiderivatives use powers, the [[logarithm|0K1N1Y4EGZ]], and the [[arctangent|065XW2V6C3]].
For example, $\frac{1}{x^2 - 1} = \frac{1}{2} \Big( \frac{1}{x - 1} - \frac{1}{x + 1} \Big)$.
So every rational function has an elementary antiderivative.

## Explanations

### L1 human

A complicated fraction of polynomials splits into a sum of simple fractions.
We can integrate each simple fraction by a standard formula.
