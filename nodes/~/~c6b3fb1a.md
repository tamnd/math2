---
tag: ~c6b3fb1a
kind: statement
role: theorem
name: Derivative of cosine
msc: [33B10, 26A24]
uses: [~45dd0733, ~f9b6abe8]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Derivative of the cosine function
---

## Statement

The cosine function is differentiable on $\mathbb{R}$, and $\cos'(x) = -\sin x$ for all real $x$.

## Remarks

[[Differentiate the power series|~f9b6abe8]] term by term. The derivative of $\frac{(-1)^n x^{2n}}{(2n)!}$ is $-\frac{(-1)^{n-1} x^{2n-1}}{(2n-1)!}$ for $n \ge 1$.
So $\sin'' = -\sin$ and $\cos'' = -\cos$. Both functions solve $f'' + f = 0$.
Mathlib states it as `Real.hasDerivAt_cos`.

## Explanations

### L1 human

The slope of the cosine curve at $x$ is $-\sin x$.
The cosine curve falls where the sine is positive.
