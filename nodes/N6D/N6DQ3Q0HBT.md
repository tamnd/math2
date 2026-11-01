---
tag: N6DQ3Q0HBT
kind: concept
name: Adjunction space
msc: [54B17, 54B15]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Adjunction_space
same_as:
  wikidata: Q4683190
  wikipedia: Adjunction space
---

## Summary

An adjunction space is obtained by gluing a space $Y$ onto a space $X$.
The gluing uses a continuous map $f$ from a subspace $A$ of $Y$ into $X$.
Each point $a$ of $A$ is identified with its image $f(a)$, and the result carries the [[quotient topology|0NQ1H2X495]].
Attaching cells to build CW complexes and the mapping cylinder are special cases.

## Explanations

### L1 human

Think of $X$ as a base and $Y$ as a piece you want to stick onto it.
A part $A$ of $Y$ is the glue strip, and the map $f$ says where on $X$ each glue point lands.
After gluing, nothing else changes: the rest of $Y$ stays attached only through $A$.
For example, glue a closed disc onto a circle $X$ by sending the boundary circle of the disc onto $X$ by the identity.
The result is again a closed disc.
If instead the boundary wraps twice around $X$, the result is the real projective plane.
