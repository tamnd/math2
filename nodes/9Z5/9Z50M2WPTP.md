---
tag: 9Z50M2WPTP
kind: concept
name: Hermite interpolation
msc: [41A05, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite_interpolation
same_as:
  wikidata: Q44451
  wikipedia: Hermite interpolation
---

## Summary

Hermite interpolation finds a polynomial that matches, at each node, a prescribed value and prescribed derivatives up to some order.
It extends [[polynomial interpolation|SS1YMS2NPC]], which prescribes values only, and Taylor polynomials, which prescribe derivatives at a single point.
If $N$ conditions are imposed in total, there is exactly one polynomial of degree at most $N - 1$ that satisfies them.
It can be computed with the Newton form using [[divided differences|N5ZHV4HWDC]] with repeated nodes, and it underlies cubic Hermite splines and Gaussian quadrature.

## Explanations

### L1 human

Ordinary interpolation asks a curve to pass through given points.
Hermite interpolation also asks it to have given slopes there, and possibly given curvature and more.
Passing through $(0, 0)$ and $(1, 1)$ with slope $0$ at both points gives four conditions, and the cubic $3x^2 - 2x^3$ meets all of them.
This curve leaves and arrives flat, which is why it is used to join pieces of curves smoothly.
The [[definition|DZQ4EW6907]] states the conditions.
