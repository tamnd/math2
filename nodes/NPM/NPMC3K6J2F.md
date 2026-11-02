---
tag: NPMC3K6J2F
kind: concept
name: Derived functor
msc: [18G10, 18G15]
sources:
  - url: https://en.wikipedia.org/wiki/Derived_functor
same_as:
  wikidata: Q320245
  wikipedia: Derived functor
---

## Summary

The derived functors of a left exact functor $F$ are functors $R^n F$, for $n \ge 0$, with $R^0 F = F$.
They are computed by applying $F$ to an [[injective resolution|ZW3W6FX4PW]] and taking cohomology.
They turn a short exact sequence into a long exact sequence, and so measure how far $F$ is from being exact.
[[Ext|4P7GBWJ4RR]], [[Tor|DDQRERAQCV]], [[group cohomology|YXJXA0Q52R]] and sheaf cohomology are all derived functors.

## Explanations

### L1 human

Many natural functors keep injective maps injective but can destroy surjectivity, or the other way round.
The derived functors are correction terms that record exactly what is lost.
One computes them by replacing an object with a resolution by simple objects, applying the functor, and taking cohomology.
For abelian groups, the functor "elements killed by $2$" sends the surjection $\Z \to \Z/2\Z$ to the non-surjective map $0 \to \Z/2\Z$.
Its first derived functor is $\operatorname{Ext}^1(\Z/2\Z, -)$, which repairs this failure.
