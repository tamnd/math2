---
tag: 37R4QJCARA
kind: concept
name: Resurgent function
msc: [34M30, "30E15", 40G10]
sources:
  - url: https://en.wikipedia.org/wiki/Resurgent_function
same_as:
  wikidata: Q108530228
  wikipedia: Resurgent function
---

## Summary

Resurgent functions are a class of analytic functions introduced by Jean Écalle to study divergent series.
A resurgent series is a formal series whose Borel transform converges near $0$.
This Borel transform must also continue analytically along every path that avoids a discrete set of singular points.
Many divergent series of analysis are resurgent, such as [[Stirling's series|K29QYWB6A5]] and the formal solutions of many analytic differential equations.
The singularities in the Borel plane link the divergent series to exponentially small terms.
This is the base of [[Borel summation|8DJPSYSHGJ]] beyond its simplest cases.

## Explanations

### L1 human

A divergent series with factorially growing coefficients can be tamed by dividing its $n$-th coefficient by $n!$.
The result is a convergent power series, a function on a small disc.
The series is resurgent when this function can be continued everywhere, except at some isolated points that can be walked around.
For example, $\sum_{n \ge 0} (-1)^n n! \, z^{-n-1}$ becomes $\sum_{n \ge 0} (-1)^n \zeta^n = \frac{1}{1 + \zeta}$, which continues to all of $\C$ except $\zeta = -1$.
The name says that the same information "resurges" at each singular point.
