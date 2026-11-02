---
tag: 1XG9GSHZ3N
kind: concept
name: Degree of a projective variety
msc: [14C17, 14N05]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_an_algebraic_variety
same_as:
  wikidata: Q5251838
  wikipedia: Degree of an algebraic variety
---

## Summary

Let $X \subseteq \mathbb{P}^n$ be a [[projective variety|A4H4CZ2V35]] of dimension $d$.
Its degree is the number of points in which $X$ meets a general linear subspace of dimension $n - d$.
Algebraically, it is $d!$ times the leading coefficient of the [[Hilbert polynomial|RMH4FBCFDA]] of $X$.
It extends the degree of a polynomial to varieties and is the basic quantity in [[Bézout's theorem|KWNVF194D8]].

## Explanations

### L1 human

A plane curve given by an equation of degree $e$ meets a general line in exactly $e$ points, so its degree is $e$.
For a surface in space one cuts with a general line instead, and for a curve in space with a general plane.
The twisted cubic, the image of $t \mapsto (t, t^2, t^3)$, meets a general plane $a + bx + cy + dz = 0$ where the cubic $a + bt + ct^2 + dt^3$ vanishes, that is, in $3$ points.
So its degree is $3$.
The degree depends on how the variety sits in projective space, not only on the variety itself.
