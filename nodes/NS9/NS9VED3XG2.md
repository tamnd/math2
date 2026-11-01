---
tag: NS9VED3XG2
kind: concept
name: Kuratowski closure axioms
msc: [54A05]
sources:
  - url: https://en.wikipedia.org/wiki/Kuratowski_closure_axioms
same_as:
  wikidata: Q10286397
  wikipedia: Kuratowski closure axioms
---

## Summary

The Kuratowski closure axioms are four rules for an operation that sends each subset of a set to a larger subset.
An operation that obeys them is a closure operator, and the closure operators on a set correspond exactly to the topologies on that set.
So a [[topological space|0CQHFPGJ45]] can be described by its [[closure|0QEAJB91GZ]] operation instead of by its [[open sets|02BH3MCBQB]].

## Explanations

### L1 human

The closure of a set adds to it all the points that are "infinitely close" to it.
Kuratowski picked out four simple rules that this operation always obeys.
Nothing comes from nothing, and a set lies in its closure.
Closing twice is the same as closing once, and the closure of a union is the union of the closures.
Any operation with these four rules comes from one and only one topology.
For example, on $\R$ the closure of the open interval $(0, 1)$ is $[0, 1]$, and closing $[0, 1]$ again gives nothing new.
