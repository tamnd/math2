---
tag: SAHAEZNCVD
kind: concept
name: Homological algebra
msc: [18G35, 18G10]
sources:
  - url: https://en.wikipedia.org/wiki/Homological_algebra
same_as:
  wikidata: Q579978
  wikipedia: Homological algebra
---

## Summary

Homological algebra is the part of algebra that studies [[chain complexes|WQ82C0M3QB]], their [[homology|2J4JJJYP22]], and the [[exact sequences|JB7ZBFBA9C]] and functors built from them.
It grew out of algebraic topology, where homology groups of spaces are computed from chain complexes, and out of the study of syzygies of modules.
Its main tools include [[abelian categories|Y9CZ3MTNF1]], [[projective|YXMXAGVC1Q]] and [[injective objects|5QRFTBF4PG]], resolutions, [[derived functors|NPMC3K6J2F]] such as [[Ext|4P7GBWJ4RR]] and [[Tor|DDQRERAQCV]], [[spectral sequences|GG8AYV847V]] and [[derived categories|5ST7NVJFSM]].
It provides a common language for algebraic topology, algebraic geometry, commutative algebra and representation theory.

## Explanations

### L1 human

Homological algebra studies sequences of objects joined by maps in which applying two maps in a row always gives zero.
The homology measures how far such a sequence is from being exact, that is, how much of what one map kills is not produced by the previous map.
In topology this measures holes: a loop that is not the boundary of any surface detects a hole.
In algebra the same machinery measures, for example, how far a module is from being free.
A small example is $0 \to \Z \xrightarrow{2} \Z \to 0$, whose homology at the second $\Z$ is $\Z/2\Z$; this records that multiplication by $2$ is not onto.
