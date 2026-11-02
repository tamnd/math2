---
tag: RVXDSY04KG
kind: concept
name: Epimorphism
msc: [18A20]
specializes: [859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Epimorphism
same_as:
  wikidata: Q1347208
  wikipedia: Epimorphism
---

## Summary

An epimorphism is a [[morphism|859F0TFVA3]] $f$ that can be cancelled on the right: $g_1 \circ f = g_2 \circ f$ implies $g_1 = g_2$.
It is the categorical version of a [[surjective function|01RVCMSN5N]], and the dual notion of a [[monomorphism|Y2NP1JFR86]].
In the categories of sets and of groups, the epimorphisms are exactly the surjective homomorphisms.
In other categories an epimorphism need not be surjective: the inclusion of the integers into the rationals is an epimorphism of rings.

## Explanations

### L1 human

A surjective map reaches every point of its target.
An epimorphism is defined without points: two maps out of the target that agree after $f$ must already be equal.
If $f$ missed a point $b$, two maps that differ only at $b$ would agree after $f$; so for sets an epimorphism must be surjective.
For rings the situation is different.
A ring homomorphism out of $\Q$ is fixed by its values on $\Z$, because $1/n$ must go to the inverse of the image of $n$.
So $\Z \to \Q$ is an epimorphism of rings although it is far from surjective.
