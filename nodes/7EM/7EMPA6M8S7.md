---
tag: 7EMPA6M8S7
kind: concept
name: Jackson integral
msc: [05A30, 33D60]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson_integral
same_as:
  wikidata: Q6117826
  wikipedia: Jackson integral
---

## Summary

The Jackson integral, or $q$-integral, is a [[q-analog|GFSDMJHHVA]] of the [[Riemann integral|0W29TBTY12]].
It replaces the integral over $[0, a]$ by a weighted sum of the values of the function at the geometric sequence of points $a, aq, aq^2, \dots$.
It is the inverse of the [[q-derivative|PMJT3FZE0Y]] in the same way as an integral is the inverse of a derivative.
Many identities for basic hypergeometric series, such as $q$-beta integrals, are stated with it.

## Explanations

### L1 human

A Riemann sum cuts $[0, a]$ into pieces of equal length.
The Jackson integral instead cuts it at the points $a q^k$, so the pieces become shorter and shorter near $0$.
On each piece $[a q^{k+1}, a q^k]$ it takes the value at the right end times the length $(1 - q) a q^k$.
For example, $\int_0^1 x \, d_q x = \frac{1}{1 + q}$, which tends to $\frac12$ as $q \to 1$.
