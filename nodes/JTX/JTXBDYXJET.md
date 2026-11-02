---
tag: JTXBDYXJET
kind: concept
name: Elliptic gamma function
msc: ["33E20", "33D05"]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_gamma_function
same_as:
  wikidata: Q615862
  wikipedia: Elliptic gamma function
---

## Summary

The elliptic gamma function $\Gamma(z; p, q)$ is a two-parameter generalisation of the [[q-gamma function|68P2VKSEP5]].
It is a double infinite product, and shifting $z$ to $qz$ multiplies it by a theta function in the base $p$.
In this way it stands to theta functions as the gamma function stands to linear functions.
It is the basic object of elliptic hypergeometric series and integrals.

## Explanations

### L1 human

The gamma function turns multiplication by $x$ into a shift: $\Gamma(x + 1) = x\, \Gamma(x)$.
The $q$-gamma function does the same with $q$-numbers in place of $x$.
The elliptic gamma function goes one step further and uses theta functions, which are infinite products with a second parameter $p$.
When $p = 0$ the theta function becomes the simple factor $1 - z$ and the theory falls back to the $q$-world.
