---
tag: A53TSXZTW5
kind: concept
name: Univalence axiom
msc: [03B38, 55U35, 03F55]
uses: [ESVYD9CZ8C, EPAAKD80H9, XZG6MTSWCN]
sources:
  - url: https://en.wikipedia.org/wiki/Univalent_foundations
---

## Summary

The univalence axiom is an axiom of [[Martin-Löf type theory|ESVYD9CZ8C]] formulated by Vladimir Voevodsky.
It says that equality of types in a universe is the same as equivalence of types.
More precisely, the canonical map from identifications $A = B$ to equivalences $A \simeq B$ is itself an equivalence.
It is the central axiom of [[homotopy type theory|EPAAKD80H9]] and of univalent foundations.
It makes every construction respect equivalence, so that isomorphic structures can be used interchangeably, and it implies function extensionality.

## Explanations

### L1 human

Mathematicians often treat isomorphic objects as the same: two groups with the same multiplication table are "the same group".
In set theory this is only a habit, since isomorphic sets can be different sets.
The univalence axiom builds the habit into the foundations: two types that are equivalent are equal, and the ways in which they are equal match the equivalences between them.
Types behave like spaces up to [[homotopy equivalence|XZG6MTSWCN]], and equalities behave like paths between them.
For example, the type of booleans has two self-equivalences, the identity and the swap, so it has two different equalities with itself.
