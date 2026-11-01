---
tag: MF4N3VGGFV
kind: concept
name: Group extension
msc: ["20E22", 20J06]
sources:
  - url: https://en.wikipedia.org/wiki/Group_extension
same_as:
  wikidata: Q3041173
  wikipedia: Group extension
---

## Summary

A group extension is a group $G$ with a [[normal subgroup|0CB0DX5BVV]] $N$ and a [[quotient group|0KYX2N69J0]] $G/N$ isomorphic to a given group $Q$.
It is the way to build a group out of two smaller pieces.
The extension problem asks for all groups $G$ that can be built from given $N$ and $Q$.
Every finite group is built from simple groups by repeated extensions, along a [[composition series|0XV2A49X6Q]].

## Explanations

### L1 human

A group extension glues a group $N$ and a group $Q$ together into a bigger group $G$.
Inside $G$ you find a copy of $N$ as a normal subgroup, and when you collapse that copy to a point, what is left is $Q$.
The same two pieces can be glued in different ways.
For example, both $\Z/4\Z$ and $\Z/2\Z \times \Z/2\Z$ have a subgroup of order $2$ with quotient of order $2$.
So both are extensions of a group of order $2$ by a group of order $2$, but they are not isomorphic.
