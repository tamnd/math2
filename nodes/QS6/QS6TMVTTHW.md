---
tag: QS6TMVTTHW
kind: definition
name: Haken manifold
msc: [57K30]
defines: 7DP7H8M5B2
uses: [R20TB2KEQQ, 702SNFQG0W, 6N9GW98MR6]
sources:
  - url: https://en.wikipedia.org/wiki/Haken_manifold
---

## Definition

Let $M$ be a compact connected [[orientable|702SNFQG0W]] [[3-manifold|R20TB2KEQQ]].
The manifold $M$ is *irreducible* if every embedded $2$-sphere in $M$ bounds an embedded $3$-ball in $M$.
The manifold $M$ is a *Haken manifold* if:

1. $M$ is irreducible, and
2. $M$ contains a properly embedded two-sided [[incompressible surface|6N9GW98MR6]].

## Remarks

Example: the $3$-torus $T^3 = T^2 \times S^1$ is irreducible, since its universal cover $\R^3$ is irreducible by Alexander's theorem.
The torus $T^2 \times \set{1}$ is two-sided, and the inclusion $\Z^2 \to \Z^3$ on fundamental groups is injective, so it is incompressible.
Hence $T^3$ is Haken.

Non-example: the $3$-sphere $S^3$ is irreducible by Alexander's theorem, but it is not Haken.
A closed surface $S \subseteq S^3$ of positive genus has $\pi_1(S) \ne 1 = \pi_1(S^3)$, so by the loop theorem it is compressible.

Every closed orientable irreducible $3$-manifold with infinite first homology group is Haken.
For non-orientable manifolds, irreducible is replaced by $P^2$-irreducible, which also forbids embedded two-sided projective planes.
