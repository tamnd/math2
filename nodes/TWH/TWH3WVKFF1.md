---
tag: TWH3WVKFF1
kind: concept
name: Finite type invariant
msc: [57K16, 57K10]
specializes: [GZQ5ZE3X6G]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_type_invariant
same_as:
  wikidata: Q1443624
  wikipedia: Finite type invariant
---

## Summary

A finite type invariant, or Vassiliev invariant, is a [[knot invariant|GZQ5ZE3X6G]] whose extension to knots with double points vanishes once there are enough double points.
They behave like polynomials on the space of knots, with the number of double points playing the role of the degree.
Many classical invariants, such as the coefficients of the Conway polynomial and of the suitably expanded [[Jones polynomial|4SPC17FPXE]], are of finite type.
The [[Kontsevich integral|727ZEPVSTC]] is universal among rational finite type invariants.

## Explanations

### L1 human

Allow a knot to pass through itself at a point, making a double point.
An invariant can be extended to such singular knots by taking the difference of its values on the two ways to resolve the double point.
An invariant has finite type $n$ when this extension is always zero on knots with more than $n$ double points.
This is like a polynomial of degree $n$, whose $(n+1)$-st differences all vanish.
It is open whether finite type invariants can tell apart every pair of different knots.
