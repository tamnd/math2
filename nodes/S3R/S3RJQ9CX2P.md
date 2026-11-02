---
tag: S3RJQ9CX2P
kind: concept
name: Mixing
msc: [37A25, 28D05]
specializes: [AZRPHS478B]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
same_as:
  wikidata: Q4350572
  wikipedia: Mixing (mathematics)
---

## Summary

A [[measure-preserving transformation|556WBDAHNP]] of a probability space is mixing, or strongly mixing, when any two events become independent in the long run.
The points of $B$ that land in $A$ after $n$ steps form a set whose measure tends to $\mu(A)\mu(B)$.
Mixing implies [[weak mixing|2MGZFRH5PX]], which implies [[ergodicity|AZRPHS478B]].
It is the basic way to say that a system forgets its initial state.

## Explanations

### L1 human

Pour a drop of dye into a glass of water and stir.
After a long time, any region of the glass holds a share of dye equal to its share of the volume.
Mixing says exactly this for a measure-preserving map: the image of any set spreads out evenly over the whole space.
The doubling map $x \mapsto 2x \bmod 1$ on $[0,1)$ is mixing.
A rotation of a circle is never mixing, because a small arc stays a small arc and just moves around.
