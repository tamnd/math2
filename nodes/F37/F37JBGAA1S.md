---
tag: F37JBGAA1S
kind: concept
name: Atomic domain
msc: [13F15, 13G05]
specializes: [0QVD7WBFGN]
sources:
  - url: https://en.wikipedia.org/wiki/Atomic_domain
same_as:
  wikidata: Q257414
  wikipedia: Atomic domain
---

## Summary

An atomic domain is an [[integral domain|09S3PFBEPM]] in which every nonzero nonunit is a finite product of [[irreducible elements|052SDEPZH7]].
It asks for the existence of factorizations, but not for their uniqueness.
Every Noetherian domain is atomic, and more generally every domain with the ascending chain condition on principal ideals.
A [[unique factorisation domain|06YMXJMXYS]] is exactly an atomic domain in which every irreducible element is [[prime|0MNHXBSX3M]].

## Explanations

### L1 human

The irreducible elements are the "atoms" of multiplication: they cannot be split into two nonunit factors.
In an atomic domain, every nonzero nonunit can be broken down into atoms in at least one way.
In $\Z[\sqrt{-5}]$ this works, but the breakdown is not unique: $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$.
In the ring of all algebraic integers it fails completely: every nonzero nonunit $\alpha$ is $\sqrt{\alpha} \cdot \sqrt{\alpha}$, so there are no atoms at all.
