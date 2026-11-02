---
tag: YPJSH79SHQ
kind: concept
name: Approximation theory
msc: [41A65, 41A10, 41A50]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
same_as:
  wikidata: Q774123
  wikipedia: Approximation theory
---

## Summary

Approximation theory studies how well complicated functions can be replaced by simpler ones, such as polynomials, splines or rational functions.
It asks whether a [[best approximation|7N4988HN3P]] exists, whether it is unique, and how to recognize and compute it.
It also asks how fast the [[error of best approximation|YDN0T4MEX0]] decreases.
Its results give the error bounds behind numerical methods for computing functions, integrals and solutions of equations.

## Explanations

### L1 human

A computer can only add and multiply, so it evaluates $\sin x$ or $e^x$ through a simpler formula, often a polynomial, that stays close to the true function.
Approximation theory makes "close" precise, usually with a norm such as the largest gap between the two graphs.
For example, the [[Weierstrass approximation theorem|0JQE130DHW]] says that every continuous function on $[a, b]$ can be imitated by polynomials as closely as one likes.
The theory then asks which polynomial of a given degree is the best one and how small its error is.
