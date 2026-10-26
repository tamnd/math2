---
tag: ~e4de59fe
kind: concept
name: Linear approximation
aliases: [linearisation, tangent-line-approximation]
msc: [26B05]
uses: [~5145a974, ~d7c5a467]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_approximation
    locator: Definition
same_as:
  wikidata: Q2071054
  wikipedia: Linear approximation
---

## Summary

A linear approximation of a function $f$ near a point $a$ replaces $f$ by an affine function. This function has the same value and the same derivative at $a$.
For a differentiable map $f$ from an open subset of $\mathbb{R}^n$ to $\mathbb{R}^m$, it is $f(x) \approx f(a) + Df(a)(x - a)$, where $Df(a)$ is the [[total derivative|~5145a974]].
The error is small compared with $\|x - a\|$ as $x \to a$.

## Remarks

For a function of one variable, the graph of the linear approximation is the tangent line. For a function of two variables, it is the [[tangent plane|~d7c5a467]].
For $f(x) = \sqrt{x}$ near $a = 4$, the approximation $\sqrt{x} \approx 2 + (x - 4)/4$ gives $\sqrt{4.1} \approx 2.025$, and the true value is $2.0248\ldots$.

## Explanations

### L1 human

Near a point, a smooth function looks like a straight line, or a flat plane in more variables.
So you can estimate values of the function near the point with simple linear arithmetic.
