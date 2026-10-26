---
tag: 0EQFWKJ37J
kind: definition
name: Hyperbolic cosine
msc: [33B10]
defines: 036696EMG2
uses: [0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_functions
    locator: Exponential definitions
---

## Definition

The hyperbolic cosine is the function $\cosh \colon \mathbb{R} \to \mathbb{R}$ defined by
$$\cosh x = \frac{e^x + e^{-x}}{2}.$$

## Remarks

It is even, and $\cosh x \ge 1$, with equality only at $x = 0$.
Its power series is $\cosh x = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}$.
The graph of $\cosh$ is the catenary, the shape of a hanging chain. Mathlib defines it as `Real.cosh`.

## Explanations

### L1 human

The hyperbolic cosine is the even part of $e^x$.
Its graph looks like a parabola near $0$, but it grows exponentially.
