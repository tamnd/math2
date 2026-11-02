---
tag: KCCHH87H6E
kind: concept
name: Representable functor
msc: [18A25, 18A40]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Representable_functor
same_as:
  wikidata: Q386320
  wikipedia: Representable functor
---

## Summary

A set-valued [[functor|28NQ0KRHD3]] is representable when it is naturally isomorphic to a [[hom functor|VJXS8AK67E]] $\Hom(A, -)$ or $\Hom(-, A)$ for some object $A$, called a representing object.
Representability is the formal language of universal properties: products, kernels, free objects and many other constructions are representing objects of suitable functors.
The representing object is unique up to unique isomorphism.

## Explanations

### L1 human

Some ways of producing sets from objects are secretly of the form "all arrows from a fixed object $A$".
For example, in the category of sets, consider the functor that sends a set $X$ to the set of its subsets.
It is the same as "all functions from $X$ to the two-point set $\{0, 1\}$", because a subset is described by its indicator function.
So the power set functor, viewed as contravariant, is represented by $\{0, 1\}$.
Recognising a functor as representable tells you that one object and one special element carry all the information.
