---
tag: WWCJ7CR2R3
kind: concept
name: Hilbert class field
msc: [11R37, 11R29]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_class_field
same_as:
  wikidata: Q2916820
  wikipedia: Hilbert class field
---

## Summary

The Hilbert class field of a number field $K$ is the largest abelian extension of $K$ that is unramified at every place.
By [[class field theory|BEKCEYHCHX]], its Galois group over $K$ is isomorphic to the [[ideal class group|WQ46BD3ARY]] of $K$, so its degree is the [[class number|KTKK9B1X41]].
A prime ideal of $K$ splits completely in it exactly when it is principal.
So the class group, an arithmetic object, is realised as a Galois group.

## Explanations

### L1 human

The class group measures how far the ring of integers of a field is from having unique factorisation.
The Hilbert class field is a bigger field that makes this measure visible as a group of symmetries.
For $K = \Q(\sqrt{-5})$, with class number $2$, the Hilbert class field is $K(i) = \Q(\sqrt{-5}, i)$, an extension of degree $2$.
Every ideal of $K$ becomes principal in the Hilbert class field: for example $(2, 1 + \sqrt{-5})$ is generated there by $1 + i$.
