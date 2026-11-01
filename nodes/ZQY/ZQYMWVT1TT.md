---
tag: ZQYMWVT1TT
kind: concept
name: Legendre transformation
msc: [26A51, 44A15, 52A41]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_transformation
same_as:
  wikidata: Q908652
  wikipedia: Legendre transformation
---

## Summary

The Legendre transformation turns a strictly [[convex function|07Q7CNM5WF]] $f$ into a new function $f^*$ of the slope $p = f'(x)$.
It records the same information as $f$, but with slopes as the variable instead of points.
Applied twice it gives back $f$, and the derivatives of $f$ and $f^*$ are inverse functions of each other.
It is the classical case of the convex conjugate and is used in mechanics, thermodynamics and optimization; the [[definition|HKPHRSN3ER]] gives the precise formula.

## Explanations

### L1 human

A convex curve can be described by its points, or by its tangent lines.
Each tangent line has a slope $p$ and meets the vertical axis at some height; the Legendre transform $f^*(p)$ is minus that height.
So $f^*$ lists the tangent lines of the graph, one for each slope.
For $f(x) = x^2 / 2$ the tangent at $x$ has slope $p = x$, and one finds $f^*(p) = p^2 / 2$, the same function.
