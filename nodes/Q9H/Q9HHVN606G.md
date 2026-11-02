---
tag: Q9HHVN606G
kind: concept
name: Bialgebra
msc: [16T10]
specializes: [3CTW1P4HBP, A06RA8KB0T]
sources:
  - url: https://en.wikipedia.org/wiki/Bialgebra
same_as:
  wikidata: Q494141
  wikipedia: Bialgebra
---

## Summary

A bialgebra is a vector space that is both an [[associative algebra|3CTW1P4HBP]] and a [[coalgebra|A06RA8KB0T]] in a compatible way.
The compatibility is that the comultiplication and the counit are algebra homomorphisms.
Group algebras, monoid algebras, polynomial rings and universal enveloping algebras of Lie algebras are bialgebras.
The compatibility lets one form tensor products of modules, which is the key feature of [[Hopf algebras|7XFYP0N84H]] and quantum groups.

## Explanations

### L1 human

In a bialgebra one can multiply two elements into one and split one element into pairs.
The rule linking the two says that splitting a product is the same as splitting each factor and multiplying the pieces.
For a group algebra, each group element $g$ splits as $g \otimes g$, and indeed $gh$ splits as $gh \otimes gh = (g \otimes g)(h \otimes h)$.
This structure is what makes it possible to let a group act on a tensor product of two representations at once.
