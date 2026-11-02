---
tag: WGYXR97NPK
kind: concept
name: Projective cover
msc: [16D40, 16L30]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_cover
same_as:
  wikidata: Q7249465
  wikipedia: Projective cover
---

## Summary

A projective cover of a [[module|0NZ8JA25WK]] $M$ is a surjection from a [[projective module|BFFA03GE3V]] onto $M$ that is as small as possible.
This means that its kernel is a superfluous submodule.
When it exists it is unique up to isomorphism.
It is the dual notion of the [[injective hull|QCJN05GN64]], which always exists, whereas projective covers exist only over special rings.
The rings over which every finitely generated module has a projective cover are the [[semiperfect rings|ZRC2S3ECFK]].
Those over which every left module has one are the left [[perfect rings|49Y9Q949PK]].

## Explanations

### L1 human

Every module is a quotient of a projective module, for instance of a free module, but usually in many ways and with a lot of waste.
A projective cover is a most economical way to do it: no proper piece of the projective module already maps onto $M$.
For example, over the ring $\Z/4$, the map $\Z/4 \to \Z/2$ is a projective cover, since the kernel $2\Z/4\Z$ is too small to help any proper submodule fill everything.
Over the integers, the module $\Z/2$ has no projective cover.
