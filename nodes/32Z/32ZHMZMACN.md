---
tag: 32ZHMZMACN
kind: concept
name: Delta functor
msc: [18G10]
sources:
  - url: https://en.wikipedia.org/wiki/Delta-functor
same_as:
  wikidata: Q5254536
  wikipedia: Delta-functor
---

## Summary

A delta functor, or $\delta$-functor, is a sequence of additive functors $T^0, T^1, T^2, \dots$ between abelian categories, together with connecting maps.
These turn each short exact sequence into a long exact sequence.
It is the axiomatic form of a cohomology theory.
The right [[derived functors|NPMC3K6J2F]] of a left exact functor form a universal $\delta$-functor, and universality is how one recognizes derived functors without resolutions.

## Explanations

### L1 human

Many cohomology theories share one feature: a short exact sequence gives a long exact sequence that runs through all degrees.
A delta functor keeps only this feature, as a list of functors with connecting maps between degrees.
It is universal if it is determined by its degree $0$ part.
For example, $\operatorname{Ext}^n(M, -)$ for $n \ge 0$ is a universal delta functor, determined by $\Hom(M, -)$.
