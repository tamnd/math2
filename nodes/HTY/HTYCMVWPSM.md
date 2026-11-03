---
tag: HTYCMVWPSM
kind: definition
name: Vortex lattice method
msc: [76M23, 76G25]
defines: PZ5KHM9YEM
uses: [ZXKV1HSQMW, TZM7XNR4V0, 84K7TEWZ2Z, 0GT4WWGWH2, YFM3DBFHWV]
sources:
  - url: https://en.wikipedia.org/wiki/Vortex_lattice_method
---

## Definition

Consider a thin lifting surface $S$ in a steady, incompressible, inviscid and irrotational [[flow|84K7TEWZ2Z]] with free stream velocity $\mathbf{V}_\infty$.
The *vortex lattice method* approximates the flow as follows.

1. The surface $S$, or its projection on a mean plane, is divided into $N$ quadrilateral panels, arranged in rows along the span and the chord.
2. On panel $j$ a horseshoe vortex of unknown constant circulation $\Gamma_j$ is placed.
It has a bound segment on the quarter-chord line of the panel and two semi-infinite trailing segments from its ends, parallel to the free stream.
3. On panel $i$ a control point $P_i$ is placed at the middle of its three-quarter-chord line, with unit normal $\mathbf{n}_i$ to the surface.
4. Let $a_{ij}$ be the normal component at $P_i$ of the velocity induced by horseshoe vortex $j$ with unit circulation, computed with the [[Biot–Savart law|ZXKV1HSQMW]].
The circulations solve the linear system
$$\sum_{j=1}^{N} a_{ij}\, \Gamma_j = -\mathbf{V}_\infty \cdot \mathbf{n}_i, \qquad i = 1, \dots, N.$$

Let $\mathbf{l}_j$ be the bound segment of panel $j$ as a vector, and $\rho$ the density.
The [[Kutta–Joukowski theorem|TZM7XNR4V0]] gives the force $\rho\, \mathbf{V}_\infty \times \Gamma_j \mathbf{l}_j$ on this segment, and the total force is the sum.

## Remarks

Example: take a rectangular flat wing at small angle of attack $\alpha$, with one chordwise row of $N$ spanwise panels.
It gives an $N \times N$ [[linear system|0GT4WWGWH2]] whose right side has the same value, of size $V_\infty \sin\alpha$, in each row.
Its solution is a discrete span load that falls off towards the tips.
Non-example: a scheme that puts each control point on the bound vortex of its own panel fails clause 3.
It breaks down because the Biot–Savart velocity is singular on the vortex.
With one chordwise panel the method is a discrete version of [[lifting-line theory|YFM3DBFHWV]].
The placement of the vortex at $1/4$ and the control point at $3/4$ of the panel chord makes a single panel reproduce the thin airfoil lift slope $2\pi$ exactly.
