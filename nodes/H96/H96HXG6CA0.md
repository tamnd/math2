---
tag: H96HXG6CA0
kind: concept
name: Regular singular point
msc: [34M03, 34M35]
specializes: [QK2J038VB4]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_singular_point
same_as:
  wikidata: Q3925845
  wikipedia: Regular singular point
---

## Summary

A regular singular point of a linear differential equation is a [[singular point|QK2J038VB4]] where the coefficients blow up only mildly.
In the normalised equation, the coefficient of $y^{(n-k)}$ has a pole of order at most $k$ there.
At such a point the solutions grow at most like a power of the distance to the point.
The [[Frobenius method|W8ZWXC2HQS]] then finds solutions of the form $(z - z_0)^r$ times a power series.
Bessel, Legendre and hypergeometric equations all have regular singular points.
See the [[definition|BMD7KQQA9C]].

## Explanations

### L1 human

Some singular points are tame and some are wild.
At a tame one, the solutions behave like powers $z^r$, perhaps with a logarithm, times nice series.
The model is the Euler equation $z^2 y'' + a z y' + b y = 0$, solved by $y = z^r$ whenever $r(r - 1) + a r + b = 0$.
At a wild, irregular point, solutions can behave like $e^{1/z}$ instead.
