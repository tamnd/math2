---
tag: 6ZPKWE0VAZ
kind: concept
name: Schwarzian derivative
msc: [30C55, 30C35]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzian_derivative
same_as:
  wikidata: Q864589
  wikipedia: Schwarzian derivative
---

## Summary

The Schwarzian derivative of a locally injective holomorphic function $f$ is the expression $f'''/f' - \frac{3}{2}(f''/f')^2$.
It vanishes exactly for Möbius transformations and does not change when $f$ is composed on the left with a Möbius transformation.
So it measures how far $f$ is from being a Möbius map.
It appears in univalence criteria, in the theory of linear second order differential equations, and in Teichmüller theory.

## Explanations

### L1 human

The ordinary derivative is zero for constant functions, and the second derivative is zero for linear functions.
The Schwarzian derivative is a third order expression that is zero for all Möbius maps $z \mapsto (az + b)/(cz + d)$.
It ignores any Möbius map applied after $f$, so it only sees the part of $f$ that a Möbius map cannot explain.
For the exponential function it is the constant $-1/2$.
