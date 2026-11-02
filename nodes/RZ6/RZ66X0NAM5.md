---
tag: RZ66X0NAM5
kind: concept
name: Nef line bundle
msc: [14C20, 14C17]
sources:
  - url: https://en.wikipedia.org/wiki/Nef_line_bundle
same_as:
  wikidata: Q6987000
  wikipedia: Nef line bundle
---

## Summary

A line bundle on a proper variety is nef, short for numerically effective or numerically eventually free, when its degree on every curve is nonnegative.
Nef line bundles are the limits of [[ample line bundles|RRK8P6TXG2]]: on a projective variety, the nef cone is the closure of the ample cone.
Nefness is a numerical condition, so it depends only on intersection numbers with curves.
It is central in the [[minimal model program|Q8CTDCZH01]], where a minimal model is a variety with mild (terminal) singularities whose canonical divisor is nef.

## Explanations

### L1 human

Each line bundle on a variety has a degree on each curve inside the variety, an integer that counts zeros minus poles of a section restricted to the curve.
An ample bundle has positive degree on every curve.
A nef bundle is allowed degree zero on some curves, but never negative degree.
On the product $\mathbb{P}^1 \times \mathbb{P}^1$, pulling back $\mathcal{O}(1)$ from the first factor gives a nef bundle.
It has degree $1$ on the curves $\mathbb{P}^1 \times \set{q}$ and degree $0$ on the curves $\set{p} \times \mathbb{P}^1$, so it is nef but not ample.
