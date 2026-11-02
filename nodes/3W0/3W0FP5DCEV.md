---
tag: 3W0FP5DCEV
kind: definition
name: Projective cover
msc: [16D40, 16L30]
defines: WGYXR97NPK
uses: [0B1261B5ED, 0NZ8JA25WK, 05WDSN597C, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_cover
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $M$ be a left $R$-[[module|0NZ8JA25WK]].
A [[submodule|05WDSN597C]] $K$ of a module $P$ is *superfluous* if for every submodule $L$ of $P$, $L + K = P$ implies $L = P$.
A *projective cover* of $M$ is a surjective $R$-linear map $p \colon P \to M$ such that:

1. $P$ is a [[projective module|BFFA03GE3V]].
2. The kernel $\ker p$ is superfluous in $P$.

## Remarks

If $p \colon P \to M$ and $p' \colon P' \to M$ are projective covers, there is an isomorphism $f \colon P \to P'$ with $p' \circ f = p$.
Example: let $R = \Z/4$ and $p \colon R \to \Z/2$ the reduction map.
The module $R$ is free, hence projective, and $\ker p = 2R$.
The submodules of $R$ are $0$, $2R$ and $R$, and $0 + 2R$ and $2R + 2R$ are not $R$, so $2R$ is superfluous and $p$ is a projective cover.
Non-example: over $R = \Z$, the reduction map $\Z \to \Z/2$ has kernel $2\Z$, and $2\Z + 3\Z = \Z$ with $3\Z \ne \Z$, so the kernel is not superfluous.
In fact the $\Z$-module $\Z/2$ has no projective cover at all.
Over a local ring $R$ with maximal ideal $\mathfrak m$, the map $R \to R / \mathfrak m$ is a projective cover, by Nakayama's lemma.
Bass proved two characterizations.
A ring is semiperfect if and only if every finitely generated left module has a projective cover.
A ring is left perfect if and only if every left module has a projective cover.
