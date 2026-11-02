---
tag: JVDEWP6MWG
kind: definition
name: Hyperplane arrangement
msc: [52C35, 05B35, 32S22]
defines: N602W0WAVT
uses: [0PYW26VNT6, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Arrangement_of_hyperplanes
---

## Definition

Let $K$ be a field and $d \ge 1$.
An affine hyperplane in $K^d$ is a set $\set{x \in K^d : a_1 x_1 + \cdots + a_d x_d = b}$ with $(a_1, \dots, a_d) \ne 0$ and $b \in K$; it is an [[affine subspace|0PYW26VNT6]] of dimension $d - 1$.
A *hyperplane arrangement* in $K^d$ is a finite set $\mathcal{A}$ of affine hyperplanes in $K^d$.

## Remarks

The arrangement is *central* if all its hyperplanes have a common point.
Its *intersection poset* $L(\mathcal{A})$ is the set of all nonempty intersections of subsets of $\mathcal{A}$, including $K^d$ itself as the empty intersection, [[partially ordered|0QV2JS9RJ3]] by reverse inclusion.
For $K = \R$, the *regions* of $\mathcal{A}$ are the connected components of $\R^d \setminus \bigcup_{H \in \mathcal{A}} H$; each is an open convex set.

Example: in $\R^2$, the three lines $x = 0$, $y = 0$ and $x + y = 1$ form an arrangement.
It is not central, since the three lines have no common point.
They cut the plane into $7$ regions, one of them the bounded open triangle with vertices $(0,0)$, $(1,0)$ and $(0,1)$.

Non-example: the unit circle together with the line $y = 0$ is not a hyperplane arrangement, since the circle is not a hyperplane.
An infinite family such as the lines $x = k$, $k \in \Z$, is not one either, since an arrangement is finite.
