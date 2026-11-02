---
tag: TVMHQ338YS
kind: definition
name: Orientability
msc: [57N65, 57R99]
defines: 702SNFQG0W
uses: [F45VQ47GPV, J7P32JQTVE, 0ZCSMYHTBP, 0QJJAQ6ZYZ, M0Q5CFJ7ZH, QQQ9B1DK4P]
sources:
  - url: https://en.wikipedia.org/wiki/Orientability
---

## Definition

Let $n \ge 1$ and let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$.
A smooth [[atlas|J7P32JQTVE]] $\set{(U_i, \varphi_i)}$ of $M$ is *oriented* if each transition map $\varphi_j \circ \varphi_i^{-1}$ has a positive [[Jacobian determinant|0ZCSMYHTBP]] at every point of $\varphi_i(U_i \cap U_j)$.
$M$ is *orientable* if it has an oriented smooth atlas.

## Remarks

The circle $S^1$ is orientable.
The stereographic charts $\varphi_N(x, y) = x/(1 - y)$ and $\varphi_S(x, y) = x/(1 + y)$ have transition map $t \mapsto 1/t$, whose derivative $-1/t^2$ is negative; replacing $\varphi_S$ by $-\varphi_S$ gives transition map $t \mapsto -1/t$ with derivative $1/t^2 > 0$.

The open [[Möbius strip|04AJE0M271]] is not orientable.
Following charts around the central circle forces a transition map with negative Jacobian determinant somewhere, so no atlas meets the condition.
The real projective plane and the Klein bottle are not orientable either, since they contain an open Möbius strip.

Equivalently, $M$ is orientable if and only if it has a nowhere vanishing differential form of degree $n$.
An orientation of $M$ is a choice of [[orientation|0QJJAQ6ZYZ]] of each tangent space that is given by the charts of one oriented atlas.
A connected orientable manifold has exactly two orientations.
For a [[topological manifold|QQQ9B1DK4P]], orientability is defined with [[singular homology|M0Q5CFJ7ZH]].
Each local group $H_n(M, M \setminus \set{x}; \Z)$ is infinite cyclic.
An orientation is a choice of generator at each point $x$ that is locally constant in $x$.
For smooth manifolds the two notions agree.
