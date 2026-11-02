---
tag: PZZNV9SEF1
kind: definition
name: Holomorphic fiber bundle
msc: [32L05, 55R10]
defines: GB0D4XMZV3
uses: [CX4M8K61AB, JSGWAN2RJV, 3MQTWKBBBT, FX92PP3HZR]
sources:
  - url: https://en.wikipedia.org/wiki/Fiber_bundle
---

## Definition

Let $E$, $B$ and $F$ be [[complex manifolds|JSGWAN2RJV]].
A *holomorphic fiber bundle* over $B$ with fibre $F$ and total space $E$ is a surjective [[holomorphic map|3MQTWKBBBT]] $\pi \colon E \to B$ with the following property.
Each point of $B$ has an open neighbourhood $U$ and a [[biholomorphism|FX92PP3HZR]] $\varphi \colon \pi^{-1}(U) \to U \times F$ with $\mathrm{pr}_1 \circ \varphi = \pi$ on $\pi^{-1}(U)$.

## Remarks

The underlying smooth map is a [[fiber bundle|CX4M8K61AB]] in the usual sense.
On overlaps the trivializations differ by maps $(b, f) \mapsto (b, g_{ij}(b)(f))$, where each $g_{ij}(b)$ is a biholomorphism of $F$ that depends holomorphically on $b$.
When $F = \C^r$ and each $g_{ij}(b)$ is linear, the bundle is a holomorphic vector bundle.

Example: the map $\pi \colon \C^2 \setminus \set{0} \to \mathbb{P}^1$, $(z_0, z_1) \mapsto [z_0 : z_1]$, with fibre $F = \C^*$.
Over $U_0 = \set{z_0 \ne 0}$ the map $(z_0, z_1) \mapsto ([z_0 : z_1], z_0)$ is a biholomorphism $\pi^{-1}(U_0) \to U_0 \times \C^*$, with inverse $([1 : w], c) \mapsto (c, c w)$, and similarly over $U_1$.

Non-example: $\pi \colon \C^2 \to \C$, $(z, w) \mapsto zw$.
Each fibre over $t \ne 0$ is biholomorphic to $\C^*$, but the fibre over $0$ is the union of the two axes, which is not a manifold.
So no neighbourhood of $0$ has a trivialization.

By a theorem of Fischer and Grauert, a proper holomorphic submersion between connected complex manifolds whose fibres are all biholomorphic to one another is a holomorphic fiber bundle.
