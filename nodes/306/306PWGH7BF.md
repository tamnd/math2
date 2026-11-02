---
tag: 306PWGH7BF
kind: concept
name: Frame
msc: [06D22, 18F70]
specializes: [D7A0ZGZT5S, NG943XNQWH]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Heyting_algebra
---

## Summary

A frame is a complete lattice in which finite meets distribute over arbitrary joins.
The open sets of any topological space form a frame, and frames are the algebraic objects of [[pointless topology|CYEMGH98WN]].
As ordered sets, frames are exactly the complete [[Heyting algebras|NG943XNQWH]]; the word "frame" signals that the maps considered preserve finite meets and arbitrary joins.

## Explanations

### L1 human

Look at the open sets of a space, ordered by inclusion.
Any union of open sets is open, and the intersection of two open sets is open.
Moreover, intersecting with one open set $U$ commutes with taking unions: $U \cap \bigcup_i V_i = \bigcup_i (U \cap V_i)$.
A frame is any complete lattice with this one distributive law.
It captures what topology needs from open sets, without mentioning points.
