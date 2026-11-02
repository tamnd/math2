---
tag: S1G61TDW0K
kind: concept
name: Exact functor
msc: ["18E10", 18G10]
specializes: [KAN07YC9T2]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_functor
same_as:
  wikidata: Q381725
  wikipedia: Exact functor
---

## Summary

An exact functor is an [[additive functor|KAN07YC9T2]] between [[abelian categories|Y9CZ3MTNF1]] that sends [[short exact sequences|KJKNJMGKZZ]] to short exact sequences.
Many natural functors, such as $\Hom(M, -)$ and $M \otimes -$, preserve only part of the exactness; they are called left exact or right exact.
Measuring how far such a functor is from being exact is the purpose of derived functors such as [[Ext|4P7GBWJ4RR]] and [[Tor|DDQRERAQCV]].

## Explanations

### L1 human

An exact sequence records how an object is built from a subobject and a quotient.
An exact functor carries this information over without loss: the image of a subobject stays a subobject, and the image of the quotient stays the quotient.
For example, tensoring abelian groups with $\Q$ is exact.
Tensoring with $\Z/2\Z$ is not: it turns the injective map "multiply by $2$" on $\Z$ into the zero map on $\Z/2\Z$.
