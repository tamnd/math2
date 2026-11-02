---
tag: X30G4V7VAJ
kind: concept
name: Separated morphism
msc: [14A15]
specializes: [JXRKH6P1Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_morphism_(algebraic_geometry)
---

## Summary

A separated morphism $X \to Y$ is a [[morphism of schemes|JXRKH6P1Z4]] whose diagonal $X \to X \times_Y X$ is a [[closed immersion|WWRWYSJDET]].
It is the scheme version of the Hausdorff property, which fails for the Zariski topology itself.
A scheme is separated if its morphism to $\operatorname{Spec} \Z$ is separated; all affine and all projective schemes are separated.

## Explanations

### L1 human

A topological space is Hausdorff exactly when the diagonal $\set{(x, x)}$ is closed in $X \times X$ with the product topology.
Zariski topologies are almost never Hausdorff, but the same diagonal test works when one uses the fiber product of schemes.
The standard failure is the line with two origins: two copies of the line glued everywhere except at $0$.
There the two copies of the line agree away from $0$ but not at $0$, much like a sequence with two limits, and the diagonal is not closed.
