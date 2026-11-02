---
tag: 74VCDYQDGP
kind: concept
name: NIP theory
msc: [03C45]
sources:
  - url: https://en.wikipedia.org/wiki/NIP_(model_theory)
same_as:
  wikidata: Q17144130
  wikipedia: NIP (model theory)
---

## Summary

A NIP theory is a complete first-order theory in which no formula has the independence property.
A formula has the independence property when, with suitable parameters, it can cut out every subset of arbitrarily large finite sets.
NIP theories include both the [[stable theories|T7JW5QY6KR]] and the [[o-minimal theories|DTWHAW1N0V]].
The condition says that every definable family of sets has finite [[VC dimension|KCFXR9K3GD]], which links model theory with learning theory and combinatorics.

## Explanations

### L1 human

Fix a formula and think of it as a way to choose subsets, one subset for each value of the parameter.
A formula is "wild" if, for every $n$, there are $n$ points such that every one of the $2^n$ subsets of them can be chosen.
NIP means that no formula is wild in this way.
On the real line with its order, the formula $x < y$ only chooses initial segments, so among two points $a < b$ it can never choose $\set{b}$ alone.
In the random graph, the edge relation can choose every subset of any finite set of vertices, so its theory is not NIP.
