---
tag: NECFJN169C
kind: concept
name: Hyperfunction
msc: [46F15, 32A45]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperfunction
same_as:
  wikidata: Q1567017
  wikipedia: Hyperfunction
---

## Summary

A hyperfunction on an open set of the real line is a formal difference of boundary values of holomorphic functions.
One function lives above the real axis and the other below it.
Hyperfunctions were introduced by Mikio Sato and generalize distributions.
They form a flabby sheaf, so local hyperfunctions can always be glued and extended.
They are the basic objects of algebraic analysis of linear partial differential equations.

## Explanations

### L1 human

Take a holomorphic function $F$ above the real axis and another one below it.
Their "jump" across the real axis, $F(x + i0) - G(x - i0)$, is a hyperfunction, even when neither limit exists as a function.
Adding the same holomorphic function on both sides does not change the jump, so such pairs count as the same hyperfunction.
For example, the jump of $-1/(2\pi i z)$ across the real axis is the Dirac delta.
