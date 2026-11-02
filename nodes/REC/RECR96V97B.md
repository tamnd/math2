---
tag: RECR96V97B
kind: concept
name: Contravariant functor
msc: [18A05, 18A22]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Functor
---

## Summary

A contravariant functor is an assignment like a [[functor|28NQ0KRHD3]] that reverses the direction of [[morphisms|859F0TFVA3]]: it sends $f \colon A \to B$ to a morphism $F(B) \to F(A)$.
It is the same thing as an ordinary functor out of the [[opposite category|DAMK8XE1FR]].
The [[dual space|07JBSZE0V4]] construction, cohomology and [[presheaves|AND2WHZC8P]] are contravariant functors.
The hom functor $\Hom(-, X)$ is the basic example, and the Yoneda lemma is about such functors.

## Explanations

### L1 human

Some constructions turn arrows around.
A map of sets $f \colon A \to B$ pulls back each subset of $B$ to a subset of $A$, its preimage.
So "subsets of" sends $f$ to a map going backwards, from subsets of $B$ to subsets of $A$.
Such a backward rule that still respects identities and composition is a contravariant functor.
Composition flips order too: pulling back along $g \circ f$ is pulling back along $g$, then along $f$.
