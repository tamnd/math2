---
tag: PRZMECS64Z
kind: definition
name: Asymptotically flat spacetime
msc: ["83C30", "83C40"]
defines: 3HTF65XMF7
uses: [BY4QYYS788, E4TDQZ7DDV, 3MCZ97SW6V, REDZ92MKXX, G49G4R1K04, 6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotically_flat_spacetime
---

## Definition

Let $(M, g)$ be a four-dimensional time-oriented [[Lorentzian manifold|BY4QYYS788]] that solves the [[Einstein field equations|3MCZ97SW6V]] $G_{ab} = 8\pi T_{ab}$ with zero cosmological constant, in units $G = c = 1$.
The following is Penrose's formulation, through a [[conformal compactification|E4TDQZ7DDV]].
Consider a Lorentzian manifold $(\tilde M, \tilde g)$ with boundary $\mathscr{I} = \partial \tilde M$ and interior $M$, and a smooth function $\Omega$ on $\tilde M$.
$(M, g)$ is *asymptotically flat at null infinity* if such data exist with:

1. $\tilde g = \Omega^2 g$ on $M$;
2. $\Omega > 0$ on $M$, while $\Omega = 0$ and $d\Omega \ne 0$ on $\mathscr{I}$;
3. $\mathscr{I}$ is the disjoint union of $\mathscr{I}^+$ and $\mathscr{I}^-$, each diffeomorphic to $\R \times S^2$. Future-directed null geodesics of $M$ can end on $\mathscr{I}^+$, and past-directed ones on $\mathscr{I}^-$;
4. the tensor $\Omega^{-2} T_{ab}$ extends smoothly to $\mathscr{I}$; in particular it suffices that $T_{ab} = 0$ near $\mathscr{I}$.

## Remarks

Clause 4 with the Einstein equations forces $\mathscr{I}$ to be a null hypersurface for $\tilde g$.
There is also a formulation at spatial infinity, which is the setting for the ADM energy.
It asks for coordinates on a spacelike slice with $g_{ij} = \delta_{ij} + O(1/r)$ and $\partial_k g_{ij} = O(1/r^2)$ as $r \to \infty$, and a suitable fall-off of the extrinsic curvature.
Complete definitions in the literature add further technical conditions, for example that every null generator of $\mathscr{I}^\pm$ is complete.

Example: [[Minkowski space|G49G4R1K04]] is asymptotically flat at null infinity, using its compactification into the Einstein static universe with $\Omega = 2 \cos U \cos V$, where $U = \arctan(t - r)$ and $V = \arctan(t + r)$.
The [[Schwarzschild metric|6Y50T68WKY]] is also asymptotically flat, and it is a vacuum solution, so clause 4 holds.

Non-example: de Sitter space solves the Einstein equations with a positive cosmological constant $\Lambda$, which acts as $T_{ab} = -\frac{\Lambda}{8\pi} g_{ab}$.
Then $\Omega^{-2} T_{ab} = -\frac{\Lambda}{8\pi} \Omega^{-4} \tilde g_{ab}$ blows up at the boundary, so clause 4 fails; indeed its conformal boundary is spacelike, not null.
