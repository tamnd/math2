---
tag: EAZMKENA4N
kind: concept
name: Fox H-function
msc: [33C60]
sources:
  - url: https://en.wikipedia.org/wiki/Fox_H-function
same_as:
  wikidata: Q8565199
  wikipedia: Fox H-function
---

## Summary

The Fox H-function is a generalisation of the [[Meijer G-function|19JNNN5KV7]].
In its [[Barnes integral|1PDGBGEHM2]] the gamma factors may have the form $\Gamma(b + B s)$ with a positive scale $B$, not only $\Gamma(b + s)$.
When all scales equal $1$, it is a Meijer G-function.
The extra freedom covers functions such as the Mittag-Leffler and Fox–Wright functions.
H-functions appear in fractional calculus and as densities in probability, for instance of products and quotients of independent random variables.

## Explanations

### L1 human

A Meijer G-function is described by a Mellin transform that is a ratio of gamma values at points $b + s$.
Fox allowed points $b + B s$ with any positive stretch $B$.
This small change brings in functions whose series have factorials of non-integer multiples of the index, such as $\sum_k z^k / \Gamma(\alpha k + 1)$.
A basic example is $H^{1, 0}_{0, 1}\left[ z \,\middle|\, (0, 1) \right] = e^{-z}$, which comes from the Mellin transform $\Gamma(s)$ of $e^{-z}$.
