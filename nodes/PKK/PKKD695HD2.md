---
tag: PKKD695HD2
kind: definition
name: Semihereditary ring
msc: ["16E60"]
defines: 7NA22G672W
uses: [0B1261B5ED, 5N2CJZ47D4, BFFA03GE3V, 89VBQH8HNS]
sources:
  - url: https://en.wikipedia.org/wiki/Hereditary_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
The ring $R$ is *left semihereditary* if every finitely generated [[left ideal|5N2CJZ47D4]] of $R$ is a [[projective module|BFFA03GE3V]] as a left $R$-module.
*Right semihereditary* is defined in the same way with right ideals, and $R$ is *semihereditary* if it is both.

## Remarks

Example: every [[hereditary ring|89VBQH8HNS]] is semihereditary, since the condition is asked only of some of the left ideals.
A non-hereditary example is the ring $\overline{\Z}$ of all algebraic integers.
It is a [[Bézout domain|HGEX40P0Z0]], so every finitely generated ideal is principal, hence free of rank $0$ or $1$, hence projective.
It is not Noetherian, because $2^{1/2}, 2^{1/4}, 2^{1/8}, \dots$ generate a strictly increasing chain of principal ideals; and a hereditary domain is a Dedekind domain, which is Noetherian.
Non-example: the ring $\Z/4\Z$ is not semihereditary, because its ideal $2\Z/4\Z$ is finitely generated and not projective.
Equivalent form: $R$ is left semihereditary if and only if every finitely generated submodule of a projective left $R$-module is projective.
A commutative integral domain is semihereditary if and only if it is a [[Prüfer domain|2RDAA4PCK8]].
