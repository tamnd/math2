---
tag: Z97HVFD6JE
kind: concept
name: Parametrix
msc: [58J40, 35S05, 35A08]
sources:
  - url: https://en.wikipedia.org/wiki/Parametrix
same_as:
  wikidata: Q2051684
  wikipedia: Parametrix
---

## Summary

A parametrix of a differential operator is an approximate inverse: an operator whose composites with the given operator differ from the identity by smoothing operators.
For operators on $\R^n$ it is the same as an approximate [[fundamental solution|K2NK9A8M5F]], one whose error is a smooth function instead of zero.
Every [[elliptic operator|MT9P2X85V8]] has a parametrix, which can be built as a [[pseudo-differential operator|FF27N0BWTP]] from the inverse of the principal symbol.
Parametrices are the main tool for proving elliptic regularity and the Fredholm property of elliptic operators on compact manifolds.

## Explanations

### L1 human

Inverting a differential operator exactly is usually hard, and often impossible because the operator has a kernel.
A parametrix gives up exactness but keeps what matters for smoothness: it inverts the operator up to an error that turns every input, however rough, into a smooth output.
Such errors are harmless for questions of regularity, and on a compact manifold they behave like finite-rank errors.
For the operator $-d^2/dx^2$ on the circle, dividing each Fourier coefficient $c_n$ with $n \ne 0$ by $n^2$ is a parametrix, and its error only sees the average of the function.
