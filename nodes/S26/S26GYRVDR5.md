---
tag: S26GYRVDR5
kind: example
name: Octonionic projective plane
msc: [51A35, 17D05, 51H20]
instance_of: [7F4HSNJJH8]
not_instance_of:
  - target: HPX85PA8NX
    note: the octonions are not associative, so Desargues's theorem fails
uses: [1HRMT3DSX2, DANFNN8C4Y, 5Z19Y02MME]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_plane
same_as:
  wikidata: Q16858508
  wikipedia: Cayley plane
---

## Example

Let $\mathbb{O}$ be the [[octonions|1HRMT3DSX2]], the $8$-dimensional real division algebra that is alternative but not associative.
The *octonionic projective plane* $\mathbb{O}P^2$, also called the Cayley plane, has the following points and lines.

1. Affine points $(x, y)$ with $x, y \in \mathbb{O}$, points $(m)$ with $m \in \mathbb{O}$, and one more point $(\infty)$.
2. Lines $[m, b] = \set{(x, y) : y = x m + b} \cup \set{(m)}$ for $m, b \in \mathbb{O}$, lines $[c] = \set{(c, y) : y \in \mathbb{O}} \cup \set{(\infty)}$ for $c \in \mathbb{O}$, and the line at infinity $\set{(m) : m \in \mathbb{O}} \cup \set{(\infty)}$.

This is a [[projective plane|DANFNN8C4Y]].
The key check concerns two affine points $(x_1, y_1)$ and $(x_2, y_2)$ with $x_1 \ne x_2$.
They lie on a line $[m, b]$ exactly when $(x_1 - x_2) m = y_1 - y_2$ and $b = y_1 - x_1 m$.
In an alternative division algebra, $a m = c$ with $a \ne 0$ has the unique solution $m = a^{-1} c$, since $a (a^{-1} c) = c$.

It is a [[Moufang plane|7F4HSNJJH8]], since it is coordinatized by the alternative division ring $\mathbb{O}$.
It is not a [[Desarguesian plane|HPX85PA8NX]]: a Desarguesian plane is coordinatized by an associative division ring, and $\mathbb{O}$ is not associative.

## Remarks

As a topological space $\mathbb{O}P^2$ is a compact manifold of dimension $16$.
For its natural Riemannian metric, its group of isometries is the compact Lie group $F_4$.
Its group of continuous collineations is a real form of $E_6$.
There is no octonionic projective space of dimension $3$ or more.
Indeed, [[Desargues's theorem|5Z19Y02MME]] holds in every projective space of dimension at least $3$, which would force the coordinates to be associative.

## Explanations

### L1 human

The real, complex and quaternionic numbers each give a projective plane, built from lines through the origin.
The octonions are a larger number system whose multiplication is not associative, so the usual construction with lines through the origin breaks down.
Still, one can write down points and lines with octonion coordinates, and they obey the rules of a projective plane.
This plane is special: it satisfies a weak form of Desargues's theorem but not the full theorem, and there is no octonionic projective space of dimension $3$ or more.
