---
tag: WFREP1QRPQ
kind: definition
name: Riemann surface
msc: [30F10, 30F20, 14H55]
defines: 5K0N8QMV6Q
uses: [0CNQXVBHCX, 0MXB4CKHFW, 0D939CMME7, 05GZ11PWRY, 0NVPNC12JY, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_surface
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
A *complex chart* on $X$ is a [[homeomorphism|05GZ11PWRY]] $\varphi \colon U \to V$ from an open set $U \subseteq X$ onto an open set $V \subseteq \C$.
Two charts $\varphi_1 \colon U_1 \to V_1$ and $\varphi_2 \colon U_2 \to V_2$ are *compatible* if the transition map
$$\varphi_2 \circ \varphi_1^{-1} \colon \varphi_1(U_1 \cap U_2) \to \varphi_2(U_1 \cap U_2)$$
is [[holomorphic|0DG0Z72CQD]], and likewise $\varphi_1 \circ \varphi_2^{-1}$.
A *complex atlas* on $X$ is a family of pairwise compatible charts whose domains form an [[open cover|0NVPNC12JY]] of $X$.
Two atlases are equivalent if their union is again an atlas.
A *complex structure* on $X$ is an equivalence class of complex atlases.
A *Riemann surface* is a topological space $X$ with a complex structure such that:

1. $X$ is [[Hausdorff|0MXB4CKHFW]], and
2. $X$ is [[connected|0D939CMME7]].

## Remarks

Some authors also require $X$ to be second countable; by Radó's theorem this holds automatically for every Riemann surface.
So a Riemann surface is the same as a connected complex manifold of dimension one.

Example: the [[Riemann sphere|0CDMXGPSES]] $\hat\C = \C \cup \set{\infty}$ with the two charts $\varphi_1(z) = z$ on $\C$ and $\varphi_2(z) = 1/z$ on $\hat\C \setminus \set{0}$, where $\varphi_2(\infty) = 0$.
On $\varphi_1(\C \setminus \set{0}) = \C \setminus \set{0}$ the transition map is $z \mapsto 1/z$, which is holomorphic there; its inverse is the same map.

Non-example: the closed unit disc $\set{z : \abs{z} \le 1}$ is not a Riemann surface for any atlas.
A boundary point has no open neighbourhood homeomorphic to an open subset of $\C$, so the domains of charts cannot cover $X$.
