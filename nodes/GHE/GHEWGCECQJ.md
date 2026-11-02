---
tag: GHEWGCECQJ
kind: definition
name: Incompressible surface
msc: [57K30]
defines: 6N9GW98MR6
uses: [R20TB2KEQQ, VGJJVBZ1MQ, 7DS6B2BFK8]
sources:
  - url: https://en.wikipedia.org/wiki/Incompressible_surface
---

## Definition

Let $M$ be a compact [[3-manifold|R20TB2KEQQ]].
Let $S \subseteq M$ be a compact connected [[surface|VGJJVBZ1MQ]] that is neither a $2$-sphere nor a closed $2$-disk.
Assume that $S$ is either properly embedded in $M$ (that is, $S \cap \partial M = \partial S$) or contained in $\partial M$.
A *compressing disk* for $S$ is an embedded closed disk $D \subseteq M$ with $D \cap S = \partial D$ such that the curve $\partial D$ does not bound a disk in $S$.
The surface $S$ is *incompressible* if it has no compressing disk, and *compressible* otherwise.

## Remarks

Example: let $M = T^2 \times [0, 1]$ and $S = T^2 \times \set{1/2}$.
Let $D$ be a disk in $M$ with $D \cap S = \partial D$.
The inclusion $S \to M$ is a homotopy equivalence, so the loop $\partial D$, null-homotopic in $M$, is null-homotopic in $S$.
A null-homotopic simple closed curve in a surface bounds a disk in it, so $D$ is not a compressing disk, and $S$ is incompressible.

Non-example: let $M = D^2 \times S^1$ be a solid torus and $S = \partial M$.
The meridian disk $D = D^2 \times \set{1}$ meets $S$ in $\partial D$, and $\partial D$ represents a nonzero class in $\pi_1(S) \cong \Z^2$, so it bounds no disk in $S$.
Hence $D$ is a compressing disk and $S$ is compressible.

If $S$ is two-sided, the [[loop theorem|8YYJBVP68F]] shows that $S$ is incompressible if and only if the inclusion induces an injective map $\pi_1(S) \to \pi_1(M)$.
Some authors also call a $2$-sphere incompressible when it does not bound a $3$-ball in $M$.
