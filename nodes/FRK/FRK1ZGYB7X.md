---
tag: FRK1ZGYB7X
kind: concept
name: Lambda cube
msc: [03B40, 03B38, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/Lambda_cube
same_as:
  wikidata: Q2036661
  wikipedia: Lambda cube
---

## Summary

The lambda cube is a family of eight typed lambda calculi, arranged as the vertices of a cube.
It starts from the [[simply typed lambda calculus|2DP940895E]] and adds three kinds of dependency independently.
They are terms depending on types, types depending on types, and types depending on terms.
Adding all three gives the [[calculus of constructions|TKMY3F6KSA]]; adding only the first gives [[System F|SVNYKTGQ48]].
Henk Barendregt introduced it in 1991 to compare these systems inside one framework of [[type theory|Q48KGV33AH]].

## Explanations

### L1 human

In the simplest typed language, programs take values and return values.
One can then allow three extra features, each on or off.
Programs may take types as inputs, as a sorting function that works for every type of items.
Types may take types as inputs, as "list of" turns a type into a new type.
Types may take values as inputs, as "vector of length $n$".
The eight choices of on and off are the corners of a cube.
