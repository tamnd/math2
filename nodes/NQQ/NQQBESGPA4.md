---
tag: NQQBESGPA4
kind: concept
name: Conway polynomial
msc: [11T06, "12E20"]
specializes: [HQ7KMZYPSQ]
sources:
  - url: https://en.wikipedia.org/wiki/Conway_polynomial_(finite_fields)
same_as:
  wikidata: Q5166747
  wikipedia: Conway polynomial (finite fields)
---

## Summary

A Conway polynomial $C_{p,n}$ is a fixed choice of [[primitive polynomial|HQ7KMZYPSQ]] of degree $n$ over $\F_p$.
The choices for different $n$ are compatible, so the fields $\F_{p^n}$ built from them fit together as subfields.
Computer algebra systems use Conway polynomials as a standard model of [[finite fields|0ZXZ82FTX2]], so that results from different programs agree.

## Explanations

### L1 human

There are many ways to build the field with $p^n$ elements, one for each irreducible polynomial of degree $n$.
A Conway polynomial picks one of them by a fixed rule: the first in a dictionary order among the primitive polynomials that fit with the smaller choices.
For $p = 2$, the first ones are $x + 1$, $x^2 + x + 1$, $x^3 + x + 1$ and $x^4 + x + 1$.
