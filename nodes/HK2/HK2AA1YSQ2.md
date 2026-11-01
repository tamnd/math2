---
tag: HK2AA1YSQ2
kind: concept
name: Projective resolution
msc: [13D02, 18G10]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(algebra)
---

## Summary

A projective resolution of a module $M$ is an [[exact sequence|JB7ZBFBA9C]] of [[projective modules|BFFA03GE3V]] that ends in $M$.
It replaces $M$ by a complex of simple pieces that has the same homological information.
Every module has a projective resolution, and the derived functors such as [[Ext|4P7GBWJ4RR]] and [[Tor|DDQRERAQCV]] are computed from it.

## Explanations

### L1 human

Write $M$ as a quotient of a free module, then describe the relations by another free module, then the relations among the relations, and so on.
The chain of free modules that you get is a free resolution, a special kind of projective resolution.
For example, $\Z/n\Z$ is the quotient of $\Z$ by the multiples of $n$, and there are no further relations.
So $0 \to \Z \xrightarrow{n} \Z \to \Z/n\Z \to 0$ is a free resolution of $\Z/n\Z$.
