---
tag: 67YR9SNGTX
kind: concept
name: Parametricity
msc: [68N18, 68Q55, 03B40]
uses: [SVNYKTGQ48]
sources:
  - url: https://en.wikipedia.org/wiki/Parametricity
same_as:
  wikidata: Q17144895
  wikipedia: Parametricity
---

## Summary

Parametricity is the property that a polymorphic program acts in the same way at every type.
The reason is that it cannot inspect the type it is used at.
John C. Reynolds made it precise in 1983 with a relational interpretation of the types of [[System F|SVNYKTGQ48]].
He proved that all terms of System F are parametric.
Its consequences are statements about all terms of a given type, which Philip Wadler called "theorems for free".
It is a main tool for reasoning about abstraction and data hiding in programming languages.

## Explanations

### L1 human

A function of type $\forall \alpha.\, \alpha \to \alpha$ receives a value of some type it knows nothing about.
It cannot add to it, compare it or build a new one, so the only thing it can return is its argument.
So every such function is the identity, and one learns this from the type alone.
In the same way, a function of type $\forall \alpha.\, \mathsf{List}\ \alpha \to \mathsf{List}\ \alpha$ can only rearrange, drop or copy list entries, so it commutes with applying any function to every entry.
