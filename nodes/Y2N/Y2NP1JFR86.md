---
tag: Y2NP1JFR86
kind: concept
name: Monomorphism
msc: [18A20]
specializes: [859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Monomorphism
same_as:
  wikidata: Q1945067
  wikipedia: Monomorphism
---

## Summary

A monomorphism is a [[morphism|859F0TFVA3]] $f$ that can be cancelled on the left: $f \circ g_1 = f \circ g_2$ implies $g_1 = g_2$.
It is the categorical version of an [[injective function|09NWETVTNY]].
In the categories of sets, groups, rings and vector spaces, the monomorphisms are exactly the injective homomorphisms.
Its dual notion is the [[epimorphism|RVXDSY04KG]].

## Explanations

### L1 human

An injective function never sends two different points to the same point.
A category has no points, so a monomorphism is defined by looking at maps into the domain instead.
The arrow $f$ is a monomorphism if two maps $g_1$, $g_2$ that look the same after $f$ were already the same.
For sets, test with maps from a one-point set: they pick out points $a_1$, $a_2$, and $f(a_1) = f(a_2)$ must force $a_1 = a_2$.
So in the category of sets, monomorphisms are the injective functions.
