---
tag: VWBVKT794W
kind: concept
name: Perfect field
msc: [12F15, 12F10]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_field
same_as:
  wikidata: Q2997817
  wikipedia: Perfect field
---

## Summary

A perfect field is a field over which every [[irreducible polynomial|03FKX7Z5DC]] has distinct roots.
Equivalently, it has characteristic $0$, or it has characteristic $p > 0$ and every element is a $p$-th power.
Over a perfect field every algebraic extension is [[separable|0WCX7NB4N7]], so Galois theory applies without restrictions.
The fields $\Q$, $\R$, $\C$, all [[finite fields|0ZXZ82FTX2]] and all algebraically closed fields are perfect.

## Explanations

### L1 human

In characteristic $p$ the map $x \mapsto x^p$ is the [[Frobenius endomorphism|0T3WVTD675]], and it is always one-to-one.
A field of characteristic $p$ is perfect when this map is also onto, so each element has a $p$-th root.
In a finite field a one-to-one map from the field to itself is automatically onto, so finite fields are perfect.
The field $\F_p(t)$ of rational functions is not perfect, since $t$ has no $p$-th root in it.
Imperfect fields are where inseparable polynomials such as $x^p - t$ appear.
