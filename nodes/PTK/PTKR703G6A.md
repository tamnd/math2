---
tag: PTKR703G6A
kind: concept
name: Clone
msc: [08A40]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
same_as:
  wikidata: Q838048
  wikipedia: Clone (algebra)
---

## Summary

A clone on a set $A$ is a set of finitary operations on $A$ that contains all [[projections|769B35T6WG]] and is closed under composition.
The term operations of any algebra with universe $A$ form a clone, and every clone arises in this way.
Clones let one compare algebras by what they can express, regardless of which basic operations were chosen.
Two algebras on the same set with the same clone of term operations have the same subalgebras, congruences and automorphisms.

## Explanations

### L1 human

Start with some operations on a set and allow yourself to plug operations into each other, repeat variables and ignore variables.
Everything you can build in this way forms a clone.
For example, on $\set{0, 1}$ the operations $\wedge$ and $\neg$ generate a clone that contains $x \vee y = \neg(\neg x \wedge \neg y)$.
In fact this clone contains every operation on $\set{0, 1}$.
A clone records the expressive power of a family of operations, not the particular family.
