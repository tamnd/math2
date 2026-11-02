---
tag: YZMPRMQ6GA
kind: definition
name: Calabi–Yau manifold
msc: [14J32, 32Q25]
defines: STYAB4PFDW
uses: [W05VYY4HBR]
sources:
  - url: https://en.wikipedia.org/wiki/Calabi%E2%80%93Yau_manifold
---

## Definition

Let $X$ be a compact connected Kähler manifold of complex dimension $n$, and let $K_X$ be its [[canonical bundle|W05VYY4HBR]], the bundle of holomorphic $n$-forms.
The manifold $X$ is a *Calabi–Yau manifold* if $K_X$ is holomorphically trivial, that is, if $X$ has a holomorphic $n$-form that vanishes nowhere.

## Remarks

Several stricter definitions are in use.
Many authors also ask that $H^0(X, \Omega^i_X) = 0$ for $0 < i < n$, or that $X$ be simply connected, or that the holonomy group of a Ricci-flat Kähler metric be exactly $SU(n)$.
Example: a smooth quintic hypersurface $X \subset \mathbb{P}^4$ has $K_X = \mathcal{O}_X(5 - 5) = \mathcal{O}_X$ by the adjunction formula, so it is Calabi–Yau.
Example: an elliptic curve $\C/\Lambda$ has the nowhere vanishing form $dz$.
Non-example: $\mathbb{P}^1$ has $K = \mathcal{O}(-2)$, which has no nonzero sections, so it is not Calabi–Yau.
A complex torus of dimension $2$ has trivial canonical bundle, but $H^0(X, \Omega^1) \cong \C^2$, so it fails the stricter definition.
