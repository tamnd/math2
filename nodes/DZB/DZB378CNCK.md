---
tag: DZB378CNCK
kind: concept
name: Inverse limit
msc: [18A30]
specializes: [CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_limit
same_as:
  wikidata: Q2634828
  wikipedia: Inverse limit
---

## Summary

An inverse limit, or projective limit, is the [[limit|CHS5AFJGWE]] of a system of objects indexed by a [[directed set|D9RY4667K6]].
Its maps go from later objects to earlier ones.
It collects the compatible families of elements, one in each object of the system.
The [[p-adic integers|V6TJAFZ4MD]] and the [[profinite groups|KA0YDB6QXE]] are inverse limits of finite objects.
The dual notion is the [[direct limit|X9HEQ29Q49]].

## Explanations

### L1 human

Think of a sequence of ever finer pictures of the same thing, each one able to forget detail and give the previous one.
The inverse limit is the object whose points are whole towers of compatible pictures.
For example, take the rings $\Z/p\Z$, $\Z/p^2\Z$, $\Z/p^3\Z$, and so on, with reduction maps between them.
A point of the inverse limit is a sequence of residues $a_n$ modulo $p^n$, with $a_{n+1}$ reducing to $a_n$.
These sequences form the ring of $p$-adic integers.
