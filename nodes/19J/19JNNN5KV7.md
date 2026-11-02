---
tag: 19JNNN5KV7
kind: concept
name: Meijer G-function
msc: [33C60]
sources:
  - url: https://en.wikipedia.org/wiki/Meijer_G-function
same_as:
  wikidata: Q1917756
  wikipedia: Meijer G-function
---

## Summary

The Meijer G-function $G^{m, n}_{p, q}$ is a very general special function defined by a [[Barnes integral|1PDGBGEHM2]] of a ratio of products of gamma functions.
Almost all classical special functions are particular G-functions, including the exponential function, the Bessel functions and every [[generalized hypergeometric function|VDBAW9PN88]] ${}_pF_q$ with $p \le q + 1$.
The class of G-functions is closed under many operations, such as multiplication by powers, differentiation, Laplace and Mellin transforms, and some integrals of products.
This makes it a tool for computing definite integrals in a systematic way, which is used in computer algebra systems.

## Explanations

### L1 human

The idea is to describe a function by its Mellin transform instead of by a series.
For the G-function, the Mellin transform is a ratio of products of gamma functions, and the function itself is recovered by a contour integral.
By choosing how many gamma factors go on top and on the bottom, one gets the exponential function, the Bessel functions, the hypergeometric functions and much more.
The simplest case is $G^{1, 0}_{0, 1}(- ; 0 \mid z) = e^{-z}$.
