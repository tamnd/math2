---
tag: JNW9GKADDN
kind: problem
name: Triangulation conjecture
msc: [57Q15, 57K40, 57R58]
uses: [QQQ9B1DK4P, V8GZ0W1ZZ5, YH170WBQ6M, 0QT00PB5G2]
about: [YH170WBQ6M, QQQ9B1DK4P]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulation_(topology)
  - url: https://arxiv.org/abs/1607.08163
history:
  posed_by: "Hellmuth Kneser"
  first_stated: "1926"
---

## Problem

Let $n \ge 0$ and let $M$ be an $n$-dimensional [[topological manifold|QQQ9B1DK4P]].
Does $M$ admit a [[triangulation|YH170WBQ6M]]?
That is, is there a [[simplicial complex|V8GZ0W1ZZ5]] $K$ whose geometric realization $\abs{K}$ is [[homeomorphic|0QT00PB5G2]] to $M$?
The triangulation conjecture asserts that the answer is yes for every manifold.

## Remarks

The question was raised by Hellmuth Kneser in 1926.
The conjecture holds in dimensions $n \le 3$.
For $n \le 1$ this is elementary, for $n = 2$ it is [[Radó's theorem|C9X05EDS5F]], and for $n = 3$ it follows from [[Moise's theorem|SV0816DJP9]].
It fails in dimension $4$: the closed [[$E_8$ manifold|BNDRN0G9BR]] of Michael Freedman is not triangulable, which follows from properties of the [[Casson invariant|33GY6P5A4T]].
It fails in every dimension $n \ge 5$.
Galewski and Stern, and independently Matumoto, reduced this case to a question about [[homology 3-spheres|HK8NS02NNE]] and homology cobordism.
Ciprian Manolescu answered that question in 2013 with $\mathrm{Pin}(2)$-equivariant Seiberg–Witten Floer homology, which gives closed non-triangulable manifolds of each dimension $n \ge 5$.
The conjecture asks for any simplicial triangulation, not one that is combinatorial.
The stronger question whether every manifold has a piecewise linear structure was settled negatively earlier, by Kirby and Siebenmann in 1969, through the [[Kirby–Siebenmann class|E4NJER1RFQ]].
Every smooth manifold is triangulable, so the counterexamples are manifolds without a smooth structure.

## Explanations

### L1 human

A triangulation cuts a space into points, segments, triangles, tetrahedra and their higher analogues, glued along common faces.
Surfaces and three-dimensional manifolds can always be cut up this way.
The conjecture said that every manifold, in every dimension, can be cut up like this.
It turned out to be false: in dimension four and in every higher dimension there are manifolds that admit no such decomposition at all.
