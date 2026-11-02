---
tag: 3RGBA24QVA
kind: concept
name: Galois category
msc: [14F35, 18B99]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck%27s_Galois_theory
---

## Summary

A Galois category is a [[category|A2DE66937D]] with a [[functor|28NQ0KRHD3]] to finite sets, called a fibre functor.
The pair satisfies axioms modelled on finite covering spaces and on finite separable field extensions.
The main theorem says that such a category is equivalent to the category of finite sets with a continuous action of a [[profinite group|KA0YDB6QXE]].
This group is the automorphism group of the fibre functor.
It is the abstract frame of [[Grothendieck's Galois theory|CX7BDQ47ZK]].
With finite étale covers of a connected scheme it defines the [[étale fundamental group|KJ11DAXMR0]].

## Explanations

### L1 human

Classical Galois theory and the theory of covering spaces share one pattern: a group acts on a fibre, and the objects correspond to sets with an action of that group.
A Galois category isolates the properties needed for this pattern.
Its objects behave like finite covers, and the fibre functor sends each one to the finite set of points above a base point.
For example, finite sets with an action of a finite group $G$, with the functor that forgets the action, form a Galois category, and the group it recovers is $G$.
