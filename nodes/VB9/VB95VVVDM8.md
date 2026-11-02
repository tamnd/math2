---
tag: VB95VVVDM8
kind: definition
name: Banach manifold
msc: [58B99, 46T05]
defines: 9K15AMGBV9
uses: [06GZ956657, 06EH97V2A7, 0QT00PB5G2, 02BH3MCBQB, 0MXB4CKHFW, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_manifold
---

## Definition

Let $M$ be a [[Hausdorff space|0MXB4CKHFW]] and let $k \ge 1$ be an integer or $\infty$.
A *chart* on $M$ is a pair $(U, \varphi)$ with $U \subseteq M$ open.
Here $\varphi$ is a [[homeomorphism|0QT00PB5G2]] from $U$ onto an [[open subset|02BH3MCBQB]] of a real [[Banach space|06GZ956657]] $E$.
A *$C^k$ atlas* on $M$ is a family of charts $(U_i, \varphi_i)_{i \in I}$ such that:

1. The sets $U_i$ cover $M$.
2. For all $i, j \in I$, the transition map $\varphi_j \circ \varphi_i^{-1} \colon \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j)$ is of class $C^k$ in the sense of the [[Fréchet derivative|06EH97V2A7]].

Two $C^k$ atlases are equivalent if their union is a $C^k$ atlas.
A *Banach manifold of class $C^k$* is a space $M$ with an equivalence class of $C^k$ atlases.
If all charts take values in the same Banach space $E$, the manifold is *modelled on* $E$.

## Remarks

When every model space is $\R^n$, this is the definition of a [[smooth manifold|F45VQ47GPV]] of class $C^k$.
When every model space is a Hilbert space, $M$ is a Hilbert manifold.
Some authors start from a set instead of a Hausdorff space and give it the topology defined by the charts.

Example: an open subset $U$ of a Banach space $E$, with the single chart $(U, \id)$, is a Banach manifold.
So the invertible elements of the Banach algebra of bounded operators on $E$ form a Banach manifold, since they form an open subset.
The unit sphere of a Hilbert space is a Banach manifold, with charts given by projections onto tangent hyperplanes.

Non-example: on $\R$, the charts $(\R, \id)$ and $(\R, x \mapsto x^3)$ do not form a $C^1$ atlas together.
The transition map $x \mapsto x^{1/3}$ is not differentiable at $0$, so clause 2 fails.
