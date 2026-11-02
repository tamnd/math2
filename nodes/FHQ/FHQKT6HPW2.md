---
tag: FHQKT6HPW2
kind: concept
name: Compact quantum group
msc: [46L67, 20G42, 58B32]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_quantum_group
same_as:
  wikidata: Q5155316
  wikipedia: Compact quantum group
---

## Summary

A compact quantum group is a unital C*-algebra with a coassociative comultiplication that satisfies a cancellation condition.
It was introduced by Stanisław Woronowicz as the noncommutative analogue of a compact group, seen through its algebra of continuous functions.
Every compact group gives one, and there are genuinely quantum examples such as $SU_q(2)$.
Much of the theory of compact groups survives: there is a unique Haar state, and finite-dimensional representations behave as in Peter–Weyl theory.

## Explanations

### L1 human

A compact group $G$ can be described by the algebra $C(G)$ of continuous functions on it.
The group law becomes a map $\Delta$ that sends a function $f$ to the function $(s, t) \mapsto f(st)$ of two variables.
A compact quantum group keeps this kind of map but allows the algebra to be noncommutative.
For example, the circle group gives the algebra $C(S^1)$ with $\Delta(z) = z \otimes z$ for the coordinate function $z$.
Deforming such examples with a parameter $q$ gives quantum groups that have no underlying set of points.
