---
tag: NCZP5MPR9Z
kind: definition
name: Desarguesian plane
msc: [51A30, 51A05]
defines: HPX85PA8NX
uses: [DANFNN8C4Y, 5Z19Y02MME, 0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_plane
---

## Definition

A [[projective plane|DANFNN8C4Y]] is *Desarguesian* if the conclusion of [[Desargues's theorem|5Z19Y02MME]] holds in it.
That is, let $ABC$ and $A'B'C'$ be triangles with $A \ne A'$, $B \ne B'$, $C \ne C'$ and distinct corresponding sides.
If $AA'$, $BB'$, $CC'$ pass through a common point, then $AB \cap A'B'$, $BC \cap B'C'$, $CA \cap C'A'$ are [[collinear|0AFNNTRTJE]].

## Remarks

A projective plane is Desarguesian exactly when it is isomorphic to $\mathbb{P}^2(D)$ for some division ring $D$, and then $D$ is determined up to isomorphism.

Example: $\mathbb{P}^2(\Q)$ is Desarguesian.
Check: it is $\mathbb{P}^2(k)$ for the field $k = \Q$, where Desargues's theorem holds.

Non-example: the projective completion of the [[Moulton plane|3V9GYYXM1H]] is not Desarguesian, since it contains two triangles in perspective from a point whose corresponding sides meet in three non-collinear points.

By Wedderburn's little theorem every finite division ring is a field, so the finite Desarguesian planes are the planes $\mathbb{P}^2(\F_q)$, of order $q$ a prime power.
Every Desarguesian plane is a [[Moufang plane|7F4HSNJJH8]].
