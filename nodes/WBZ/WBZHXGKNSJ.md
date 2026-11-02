---
tag: WBZHXGKNSJ
kind: definition
name: Smooth manifold
msc: [58A05]
defines: F45VQ47GPV
uses: [QQQ9B1DK4P, 0QT00PB5G2, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_manifold
---

## Definition

Let $M$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $n$, so $M$ is Hausdorff, second countable and locally homeomorphic to $\R^n$.
A *chart* on $M$ is a pair $(U, \varphi)$ where $U \subset M$ is open and $\varphi \colon U \to \varphi(U)$ is a [[homeomorphism|0QT00PB5G2]] onto an open subset of $\R^n$.
Two charts $(U, \varphi)$ and $(V, \psi)$ are *smoothly compatible* if $U \cap V = \emptyset$ or the transition map
$$\psi \circ \varphi^{-1} \colon \varphi(U \cap V) \to \psi(U \cap V)$$
is a [[smooth|0V33BNKZ9S]] ($C^\infty$) map with smooth inverse.
A *smooth atlas* on $M$ is a family of pairwise smoothly compatible charts whose domains cover $M$.
A *smooth structure* is a smooth atlas that is maximal: it contains every chart that is smoothly compatible with all of its charts.
A *smooth manifold* of dimension $n$ is a topological manifold of dimension $n$ together with a smooth structure.

## Remarks

The unit circle $S^1 \subset \R^2$ is a smooth manifold.
Let $N = (0, 1)$ and $S = (0, -1)$, and let $\sigma_N \colon S^1 \setminus \set{N} \to \R$ and $\sigma_S \colon S^1 \setminus \set{S} \to \R$ be the stereographic projections, $\sigma_N(x, y) = x/(1 - y)$ and $\sigma_S(x, y) = x/(1 + y)$.
On the overlap, $\sigma_N \sigma_S = x^2/(1 - y^2) = 1$, so the transition map is $t \mapsto 1/t$ on $\R \setminus \set{0}$, which is smooth with smooth inverse.

The charts $(\R, \id)$ and $(\R, t \mapsto t^3)$ on $\R$ are not smoothly compatible.
The transition map $t \mapsto t^{1/3}$ is not differentiable at $0$.
Each of them alone defines a smooth structure on $\R$, and the two structures are different, although the resulting manifolds are diffeomorphic.

Every smooth atlas is contained in a unique maximal one, so in practice a smooth manifold is given by any smooth atlas.
Replacing $C^\infty$ by $C^k$ gives $C^k$ manifolds.

## Explanations

### L1 human

A smooth manifold is a space covered by coordinate charts in which every change of coordinates is a smooth map.
