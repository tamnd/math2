---
tag: BFFA03GE3V
kind: concept
name: Projective module
msc: [13C10, 16D40]
specializes: [0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
same_as:
  wikidata: Q942423
  wikipedia: Projective module
---

## Summary

A projective module is a module $P$ such that every linear map from $P$ lifts along every surjective linear map.
Equivalently, $P$ is a direct summand of a [[free module|0DZ9DKAKZR]].
Projective modules keep the most useful property of free modules, lifting of maps, but need not have a basis.
They are the building blocks of projective resolutions in homological algebra, and finitely generated projective modules correspond to vector bundles in geometry.

## Explanations

### L1 human

Free modules are the easiest modules: you can send a basis anywhere you like.
A projective module is a piece cut off from a free module, so it shares this freedom when you map out of it.
Every free module is projective.
Over the ring $\Z/6\Z \cong \Z/2\Z \times \Z/3\Z$, the module $\Z/2\Z$ is a piece of the free module $\Z/6\Z$, so it is projective, but it is too small to be free.
