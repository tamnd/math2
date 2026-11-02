---
tag: C9X05EDS5F
kind: statement
role: theorem
name: Radó's theorem on triangulation of surfaces
msc: [57Q15, 57K20]
uses: [QQQ9B1DK4P, YH170WBQ6M, 3VX06XRVZG]
about: [YH170WBQ6M]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulation_(topology)
  - url: https://en.wikipedia.org/wiki/Rad%C3%B3%27s_theorem_(Riemann_surfaces)
---

## Statement

Let $S$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $2$, that is, a Hausdorff, second-countable space locally homeomorphic to $\R^2$.
Then $S$ has a [[triangulation|YH170WBQ6M]].

## Remarks

Tibor Radó proved the theorem in 1925.
One proof covers $S$ by countably many closed disks coming from charts, and modifies their boundary circles so that, on each compact part, they meet in finitely many points.
The pieces cut out by these circles are bounded by Jordan curves, so the [[Schoenflies theorem|3VX06XRVZG]] shows that they are closed disks, which can then be divided into triangles.
For example, the torus is triangulable, with as few as $7$ vertices.
The theorem is the reason why the classification of closed surfaces, first proved for triangulated surfaces, applies to all closed topological surfaces.
The triangulation is also unique up to piecewise linear homeomorphism, so every surface has a unique piecewise linear structure.
A related result, also called Radó's theorem, says that every connected Riemann surface is second-countable; its proof uses the same kind of construction.

## Explanations

### L1 human

Every surface, however it is given, can be cut into triangles glued edge to edge.
This lets one count vertices, edges and triangles, and so compute the Euler characteristic of any closed surface.

### L2 human

In a course on surfaces, theorems are often proved first for triangulated surfaces, using the combinatorics of the triangles.
Radó's theorem removes this hypothesis.
The analogous statement holds in dimension $3$ by Moise's theorem, but fails in dimension $4$, where some topological manifolds have no triangulation.
