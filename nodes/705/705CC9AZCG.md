---
tag: 705CC9AZCG
kind: definition
name: Seifert fiber space
msc: [57K30, 57M50]
defines: 9V1GF5WMKA
uses: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Seifert_fiber_space
---

## Definition

Let $a \ge 1$ and $b$ be coprime integers, let $D^2$ be the closed unit disk and let $\rho \colon D^2 \to D^2$ be the rotation by the angle $2\pi b / a$.
The *fibered solid torus* $T(a, b)$ is the quotient of $D^2 \times [0, 1]$ by $(x, 0) \sim (\rho(x), 1)$, decomposed into the circles that are the images of the segments $\set{x} \times [0, 1]$.
Its central circle, the image of $\set{0} \times [0, 1]$, is called *regular* if $a = 1$ and *exceptional* if $a > 1$.

A *Seifert fiber space* is a closed [[3-manifold|R20TB2KEQQ]] $M$ with a decomposition of $M$ into disjoint circles, the *fibers*, such that the following holds.
Each fiber $C$ has a neighborhood $U$ that is a union of fibers.
There is a homeomorphism from $U$ to some $T(a, b)$ that maps fibers to fibers and $C$ to the central circle.

## Remarks

Example: for a closed surface $S$, the product $S \times S^1$, decomposed into the circles $\set{s} \times S^1$, is a Seifert fiber space.
Each fiber has the neighborhood $B \times S^1$ with $B$ a small disk around $s$, which is $T(1, 0)$.

Non-example: on the $3$-torus $T^3 = \R^3 / \Z^3$, take the decomposition into images of lines parallel to $(1, \sqrt{2}, 0)$.
These images are not circles, because $\sqrt{2}$ is irrational, so the clause that the pieces are circles fails.

In $T(a, b)$ every fiber other than the central one closes up after $a$ trips around, so a compact Seifert fiber space has only finitely many exceptional fibers.
Variants of the definition allow boundary, and, for non-orientable manifolds, fibered solid Klein bottles as neighborhoods.
