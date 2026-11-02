---
tag: P5HCD49REV
kind: definition
name: Moufang plane
msc: [51A35, 17D05]
defines: 7F4HSNJJH8
uses: [DANFNN8C4Y, 0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Moufang_plane
---

## Definition

A [[projective plane|DANFNN8C4Y]] is a *Moufang plane* if it satisfies the little Desargues property for every line $\ell$ and every point $O$ on $\ell$:

1. let $ABC$ and $A'B'C'$ be triangles with no vertex on $\ell$, with $A \ne A'$, $B \ne B'$, $C \ne C'$, and with $AA'$, $BB'$, $CC'$ through $O$;
2. suppose the points $AB \cap A'B'$ and $AC \cap A'C'$ lie on $\ell$;
3. then the point $BC \cap B'C'$ also lies on $\ell$.

## Remarks

So three [[collinear|0AFNNTRTJE]] intersection points are required only when the centre $O$ lies on the axis $\ell$.
Equivalently, every line of the plane is a translation line, that is, the group of elations with axis $\ell$ acts transitively on the points off $\ell$.
A projective plane is a Moufang plane exactly when it can be coordinatized by an alternative division ring.

Example: $\mathbb{P}^2(k)$ over a field $k$ is a Moufang plane.
Check: Desargues's theorem holds in $\mathbb{P}^2(k)$ for all triangles in perspective, in particular when the centre lies on the axis.

By the Artin–Zorn theorem every finite alternative division ring is a field, so every finite Moufang plane is Desarguesian.

Non-example: the Hall plane of order $9$ is a finite [[non-Desarguesian plane|HYE5FT4M34]].
So by the previous sentence it is not a Moufang plane: the little Desargues property fails in it for some line $\ell$ and point $O$.
