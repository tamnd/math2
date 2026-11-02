---
tag: T7V2VPY61S
kind: concept
name: Fenchel conjugate
msc: [52A41, 26B25, 90C46]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_conjugate
same_as:
  wikidata: Q3075186
  wikipedia: Convex conjugate
---

## Summary

The Fenchel conjugate, or convex conjugate, of a function $f$ on a vector space is the function $f^*$ on the dual space given by $f^*(y) = \sup_x \big(\ip{y}{x} - f(x)\big)$.
It is always [[convex|07Q7CNM5WF]] and lower semicontinuous, and for proper convex lower semicontinuous $f$ one has $f^{**} = f$.
It extends the classical [[Legendre transformation|ZQYMWVT1TT]] to functions that need not be differentiable.
It is the basic tool of duality in convex optimization.

## Explanations

### L1 human

Think of the graph of $f$ and of all lines of slope $y$ that stay below it.
The highest such line crosses the vertical axis at height $-f^*(y)$.
So $f^*$ records, slope by slope, how the graph of $f$ is supported from below.
For example, the conjugate of $f(x) = \frac12 x^2$ is $f^*(y) = \frac12 y^2$.
A convex function can be rebuilt from its conjugate, which makes this a kind of "Fourier transform" of convex analysis.
