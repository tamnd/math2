---
tag: NTEFMRR3HR
kind: concept
name: Condenser capacity
msc: [31B15, 31A15, 30C85]
specializes: [A1KWT817JX]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Summary

A condenser is a pair $(K, \Omega)$ of a compact set $K$ inside an open set $\Omega \subseteq \R^n$.
Its capacity is the least Dirichlet energy $\int_\Omega \abs{\nabla u}^2 \, dx$ of a function that is at least $1$ on $K$ and vanishes near the boundary of $\Omega$.
It is the case $p = 2$ of the [[variational capacity|A1KWT817JX]].
Condenser capacity works in every dimension, including the plane.
It is a basic tool in the theory of quasiconformal maps through the conformal modulus of ring domains.

## Explanations

### L1 human

A physical capacitor has two conductors: an inner plate $K$ and an outer shell, the boundary of $\Omega$.
Hold $K$ at voltage $1$ and the shell at voltage $0$.
The capacity is the charge needed to keep this voltage difference, and it equals the energy of the electric field between the plates.
For two concentric spheres of radii $r < R$ in space, the capacity is $4 \pi r R / (R - r)$, which grows without bound as the two spheres come close.
As $R$ tends to infinity it tends to $4 \pi r$, the [[capacity|4YZVFGJVSZ]] of a single ball.
