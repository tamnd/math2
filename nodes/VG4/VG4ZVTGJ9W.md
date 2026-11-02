---
tag: VG4ZVTGJ9W
kind: definition
name: Smooth structure
msc: [57R55, 58A05]
defines: R2TQ82PCNB
uses: [QQQ9B1DK4P, J7P32JQTVE, 0QT00PB5G2, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Smooth_structure
---

## Definition

Let $M$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $n$.
A chart $(U, \varphi)$ on $M$ is an open set $U \subseteq M$ with a [[homeomorphism|0QT00PB5G2]] $\varphi$ from $U$ onto an open subset of $\R^n$.
Two charts $(U, \varphi)$ and $(V, \psi)$ are *smoothly compatible* if $U \cap V = \emptyset$, or if the transition map $\psi \circ \varphi^{-1} \colon \varphi(U \cap V) \to \psi(U \cap V)$ is [[smooth|0V33BNKZ9S]] with smooth inverse.
A *smooth [[atlas|J7P32JQTVE]]* on $M$ is a family of pairwise smoothly compatible charts whose domains cover $M$.
A *smooth structure* on $M$ is a smooth atlas $\mathcal{A}$ that is maximal.
This means that every chart that is smoothly compatible with all charts of $\mathcal{A}$ already belongs to $\mathcal{A}$.

## Remarks

Every smooth atlas is contained in a unique maximal smooth atlas, so a smooth structure is usually given by any one atlas.
Example: on $\R^n$ the single chart $(\R^n, \id)$ is a smooth atlas, and the maximal atlas containing it is the standard smooth structure.
Non-example: the atlas $\set{(\R, \id), (\R, t \mapsto t^3)}$ on $\R$ is not a smooth atlas.
The transition map $t \mapsto t^{1/3}$ is not differentiable at $0$, so the two charts are not smoothly compatible.
Each of the two charts alone defines a smooth structure; the two structures are different but diffeomorphic.
Two smooth structures on $M$ are usually counted as the same when they are diffeomorphic, not only when they are equal.
