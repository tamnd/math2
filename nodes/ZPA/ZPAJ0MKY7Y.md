---
tag: ZPAJ0MKY7Y
kind: concept
name: Subtyping
msc: [68N15, 03B40]
uses: [AVVQEG0MRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Subtyping
same_as:
  wikidata: Q2713292
  wikipedia: Subtyping
---

## Summary

Subtyping is a relation $S <: T$ between types meaning that a value of type $S$ can be used wherever a value of type $T$ is expected.
A [[type system|AVVQEG0MRJ]] with subtyping lets a term have several types, ordered from more specific to more general.
It models inheritance in object-oriented languages and the inclusion of numeric types, such as integers in reals.
Its rules for functions are contravariant in the argument and covariant in the result, which is the main subtle point.

## Explanations

### L1 human

A record with fields for a name and an age can be passed to any function that only needs the name.
So the type of records with a name and an age is a subtype of the type of records with a name.
More information makes a type more specific, and a more specific value is accepted where a general one is asked for.
For functions the direction flips on the input: a function that accepts every animal can stand in for a function that only needs to accept cats.
