---
tag: 20QEAM8AX2
kind: concept
name: Artinian ring
msc: ["13E10", "16P20"]
specializes: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Artinian_ring
same_as:
  wikidata: Q713084
  wikipedia: Artinian ring
---

## Summary

An Artinian ring is a ring in which every decreasing chain of ideals stops after finitely many steps.
For commutative rings, Artinian rings are exactly the [[Noetherian rings|0670T59HGE]] in which every prime ideal is maximal, by the [[Akizuki–Hopkins–Levitzki theorem|C7X657TF19]].
By the [[structure theorem for Artinian rings|HE7MP4HP6Q]], a commutative Artinian ring is a finite product of Artinian local rings.
Finite rings, fields and finite-dimensional algebras over a field are Artinian.

## Explanations

### L1 human

In an Artinian ring you cannot keep shrinking ideals forever: every decreasing chain becomes constant.
Such rings are small in a precise sense, like finite-dimensional algebras.
For example, $\Z/12\Z$ has only six ideals, so any decreasing chain of ideals must stop.
The ring $\Z$ is not Artinian, because $(2) \supset (4) \supset (8) \supset \cdots$ never stops.
