---
tag: TB40Y3SNSX
kind: concept
name: Faithful module
msc: [16D10]
sources:
  - url: https://en.wikipedia.org/wiki/Annihilator_(ring_theory)
---

## Summary

A faithful module over a ring $R$ is a [[module|0NZ8JA25WK]] on which no nonzero element of $R$ acts as zero.
Equivalently, its [[annihilator|HB4XDKJTW8]] is zero, so $R$ embeds in the endomorphism ring of the additive group of the module.
It is the module version of a [[faithful action|0P7G9NGG2G]] of a group.
Faithful simple modules define primitive rings, a central class in the structure theory of rings.

## Explanations

### L1 human

A module is faithful when the ring can be fully seen through its action on the module.
In a faithful module, two different ring elements always act in different ways.
The integers act faithfully on $\Z$, since $n \cdot 1 = n$ is nonzero for $n \ne 0$.
They do not act faithfully on $\Z/5\Z$, since $5$ acts as zero there.
