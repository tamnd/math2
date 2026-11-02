---
tag: C6GAHS1Z2P
kind: concept
name: Scott continuity
msc: [06B35, 68Q55]
sources:
  - url: https://en.wikipedia.org/wiki/Scott_continuity
same_as:
  wikidata: Q895815
  wikipedia: Scott continuity
---

## Summary

A map between partially ordered sets is Scott-continuous if it preserves suprema of directed subsets.
Scott-continuous maps are exactly the maps that are continuous for the [[Scott topologies|ZR8A03FV67]] on both sides.
In [[domain theory|Q2P5D74Q1V]] they model computable functions: the output on a limit of approximations is the limit of the outputs.
A Scott-continuous self-map of a pointed dcpo has a [[least fixed point|DBD64TH52D]], which gives meaning to recursive definitions.

## Explanations

### L1 human

Feed a program better and better approximations of its input.
If the program is well behaved, its outputs also improve, and the output for the full input is the limit of these outputs.
Scott continuity is this property stated for ordered sets: the map respects order and respects limits of directed families.
For example, on the subsets of $\N$ ordered by inclusion, the map $A \mapsto A \cup \set{0}$ is Scott-continuous, since it commutes with unions of directed families.
