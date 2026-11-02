---
tag: NXMCYGCB59
kind: concept
name: Elliptic integral
msc: ["33E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
same_as:
  wikidata: Q1126603
  wikipedia: Elliptic integral
---

## Summary

An elliptic integral is an integral of a rational function of $t$ and $\sqrt{P(t)}$.
Here $P$ is a polynomial of degree $3$ or $4$ without repeated roots.
Such integrals arose from the arc length of the [[ellipse|0VKCCEXBJ1]] and in general cannot be written with elementary functions.
Legendre showed that every elliptic integral reduces to elementary functions and three standard integrals, of the first, second and third kind.
Inverting the integral of the first kind leads to the [[Jacobi elliptic functions|P071B692JF]].

## Explanations

### L1 human

Integrals with $\sqrt{1 - t^2}$ give the arcsine and the length of a circle arc.
Replacing the square root of a quadratic by the square root of a cubic or quartic gives an elliptic integral.
The simplest case is the length of an arc of an ellipse, which is the origin of the name.
For example, $\int_0^{x} dt / \sqrt{(1 - t^2)(1 - k^2 t^2)}$ with $0 < k < 1$ is an elliptic integral; for $k = 0$ it collapses to $\arcsin x$.
These integrals define new functions, which tables and computers evaluate like the logarithm or the sine.
