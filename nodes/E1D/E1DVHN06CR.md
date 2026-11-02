---
tag: E1DVHN06CR
kind: concept
name: ℓ-adic cohomology
msc: [14F20, 14G15]
sources:
  - url: https://en.wikipedia.org/wiki/%C3%89tale_cohomology
---

## Summary

Let $X$ be a variety over a separably closed field, and let $\ell$ be a prime different from the characteristic.
The $\ell$-adic cohomology of $X$ is the inverse limit of the [[étale cohomology|7YX76G0838]] groups of $X$ with coefficients $\Z/\ell^n\Z$.
It gives modules over the [[$\ell$-adic integers|GBN9F8FAQ3]], and after tensoring, vector spaces over $\Q_\ell$, a field of characteristic $0$.
These groups behave like the singular cohomology of a complex variety, with Poincaré duality, a Künneth formula and a Lefschetz trace formula.
They are the cohomology used in the proof of the [[Weil conjectures|81TXP32VDM]], and the Galois action on them gives [[Galois representations|JQEYEQJY2G]].

## Explanations

### L1 human

Étale cohomology with finite coefficients $\Z/n\Z$ works well, but one wants coefficients in a field of characteristic $0$, like $\Q$ in topology.
Coefficients $\Q$ directly give the wrong answer, so one takes the coefficients $\Z/\ell, \Z/\ell^2, \Z/\ell^3, \ldots$ and passes to the limit.
For an elliptic curve over an algebraically closed field, the first $\ell$-adic cohomology is a $2$-dimensional space over $\Q_\ell$.
It is dual to the space built from the [[Tate module|4CSMQFTGD8]], made of the points of order $\ell^n$ of the curve.
