---
tag: K290RBT8GB
kind: concept
name: Struve function
msc: [33C10]
sources:
  - url: https://en.wikipedia.org/wiki/Struve_function
same_as:
  wikidata: Q2607374
  wikipedia: Struve function
---

## Summary

The Struve function $\mathbf{H}_\nu$ is a particular solution of Bessel's equation with a power of $z$ on the right-hand side.
It complements the [[Bessel functions|CZCMRDWDYW]], which solve the equation with right-hand side $0$.
It appears in acoustics, for the radiation of a vibrating piston, and in problems of water waves and optics.

## Explanations

### L1 human

Bessel's equation without a right-hand side describes free vibrations of a round object.
Adding a forcing term that is a power of $z$ gives a new equation, and the Struve function is its standard solution.
Every other solution is the Struve function plus a combination of Bessel functions.
For example, $\mathbf{H}_{1/2}(x) = \sqrt{\frac{2}{\pi x}}\,(1 - \cos x)$ for $x > 0$.
