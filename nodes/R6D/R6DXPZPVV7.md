---
tag: R6DXPZPVV7
kind: definition
name: n-skeleton
msc: [57Q05, 55U10]
defines: VBM8ZYTT2X
uses: [5W95QFHXPR, V8GZ0W1ZZ5, P976WYEFMB]
sources:
  - url: https://en.wikipedia.org/wiki/N-skeleton
---

## Definition

Let $n \ge 0$ be an integer.

1. Let $X$ be a [[CW complex|5W95QFHXPR]]. The *$n$-skeleton* $X^{(n)}$ of $X$ is the union of all closed cells of $X$ of dimension at most $n$.
2. Let $K$ be a [[simplicial complex|V8GZ0W1ZZ5]]. The *$n$-skeleton* $K^{(n)}$ of $K$ is the subcomplex of all simplices of $K$ of dimension at most $n$.

The notation $X^n$ is also common.

## Remarks

The torus $T^2$ has a CW structure with one $0$-cell, two $1$-cells $a$ and $b$, and one $2$-cell attached along $a b a^{-1} b^{-1}$.
Its $0$-skeleton is a point, its $1$-skeleton is a wedge of two circles, and its $2$-skeleton is $T^2$.

The skeleton depends on the cell structure and not only on the space.
The sphere $S^2$ with one $0$-cell and one $2$-cell has a point as $1$-skeleton.
The sphere $S^2$ as the boundary of a tetrahedron has as $1$-skeleton a graph with $4$ vertices and $6$ edges.
So "the $1$-skeleton of $S^2$" has no meaning before a cell structure is chosen.

For a CW complex, $X^{(n)}$ is obtained from $X^{(n-1)}$ by attaching $n$-cells along maps from their boundary spheres, and $X$ is the union of its skeleta with the weak topology.
The inclusion $X^{(n)} \to X$ induces an isomorphism on [[homotopy groups|P976WYEFMB]] $\pi_k$ for $k < n$ and a surjection for $k = n$.
