---
tag: HNVW0E732J
kind: concept
name: Lie groupoid
msc: [22A22, 58H05]
specializes: [FH3C0T643F]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_groupoid
same_as:
  wikidata: Q6543824
  wikipedia: Lie groupoid
---

## Summary

A Lie groupoid is a [[groupoid|FH3C0T643F]] whose objects and arrows each form a [[smooth manifold|F45VQ47GPV]].
All its structure maps are smooth, and the source and target maps are submersions.
It generalises [[Lie groups|7JBRGCVJRB]], which are Lie groupoids with a single object, and also smooth group actions, foliations and principal bundles.
Lie groupoids give a common language for symmetries that vary from point to point, and they have Lie algebroids as their infinitesimal versions.

## Explanations

### L1 human

A group describes symmetries of one object; a groupoid describes symmetries between many objects.
An arrow goes from one object to another, and two arrows can be composed when they meet end to end.
In a Lie groupoid both the objects and the arrows form smooth spaces, and composing arrows is a smooth operation.
For example, take as objects the points of a manifold $M$, and as arrows from $x$ to $y$ the pairs $(y, x)$.
Composing $(z, y)$ with $(y, x)$ gives $(z, x)$.
