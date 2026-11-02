---
tag: 84BR7X6HET
kind: concept
name: Sparse grid
msc: [65D32, 41A63, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_grid
same_as:
  wikidata: Q7573793
  wikipedia: Sparse grid
---

## Summary

A sparse grid is a set of points in a cube in $\R^d$ built by Smolyak's construction from one-dimensional rules.
It keeps only those products of one-dimensional levels whose total level is small, instead of the full tensor grid.
For functions with bounded mixed derivatives, sparse grids give nearly the accuracy of full grids with far fewer points.
They are used for integration and interpolation in moderately high dimensions, where full grids suffer from the [[curse of dimensionality|YS424FTY4E]].

## Explanations

### L1 human

A full grid with $m$ points in each of $d$ directions has $m^d$ points, which is far too many when $d$ is large.
A sparse grid allows fine resolution in one direction only when the other directions are coarse.
The picture in two dimensions looks like a cross or a star: dense along the axes and thin near the corners.
For example, from the levels $\set{0}$ and $\set{-1, 0, 1}$ in each direction, the sparse grid of the next level in $d$ dimensions has $2d + 1$ points, while the full grid has $3^d$.
