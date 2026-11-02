---
tag: PT9V59MJZZ
kind: concept
name: Gauss–Kronrod quadrature formula
msc: [65D32, 41A55]
specializes: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Kronrod_quadrature_formula
same_as:
  wikidata: Q5527852
  wikipedia: Gauss–Kronrod quadrature formula
---

## Summary

A Gauss–Kronrod quadrature formula extends an $n$-point [[Gauss–Legendre rule|RGGXDRCJVE]] by $n + 1$ new nodes into a rule with $2n + 1$ nodes.
The old nodes are kept, and the new nodes and all weights are chosen to give the highest possible [[degree of exactness|ZYT1JNT1Y0]].
The difference between the two results is a cheap estimate of the error of the integral.
For this reason Gauss–Kronrod pairs are the core of many adaptive integration programs.

## Explanations

### L1 human

To know how good an approximate integral is, one usually computes it twice with two rules and compares.
Two unrelated Gauss rules share almost no sample points, so the second computation costs almost as much as starting over.
The Kronrod idea reuses every sample of the first rule and only adds a few new ones in between.
For example, the popular pair "G7–K15" uses a $7$-point Gauss rule and a $15$-point Kronrod rule that needs only $8$ extra function values.
