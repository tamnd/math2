---
tag: F03A4MKA5V
kind: conjecture
name: Voronoi's conjecture on parallelohedra
msc: [52C22, 52B11, 11H06]
uses: [MR2JWBCZQZ, V1R1R88GV6, WN9V7WSJKF]
about: [MR2JWBCZQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelohedron
history:
  posed_by: "Georgy Voronoy"
  first_stated: "1908"
---

## Statement

Let $d \ge 1$ and let $P \subset \R^d$ be a [[parallelohedron|MR2JWBCZQZ]].
Then there are a [[lattice|WN9V7WSJKF]] $\Lambda \subset \R^d$ and an affine bijection $A \colon \R^d \to \R^d$ such that $A(P)$ is the [[Voronoi cell|V1R1R88GV6]] of $\Lambda$.

## Remarks

The converse holds: the Voronoi cell of every lattice is a parallelohedron.
Voronoi proved the conjecture for primitive parallelohedra, those whose tiling has exactly $d + 1$ tiles at each vertex.
Delone proved it in dimensions $d \le 4$.
Erdahl proved it for parallelohedra that are zonotopes.
The general case is open.

## Explanations

### L1 human

A parallelohedron is a convex tile that fills space when you only slide copies of it.
Every lattice gives such a tile: the region of points nearer to one lattice point than to all others.
Voronoi guessed that this is the only source of such tiles, once you allow stretching and shearing.
