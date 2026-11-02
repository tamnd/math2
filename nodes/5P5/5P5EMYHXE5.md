---
tag: 5P5EMYHXE5
kind: concept
name: Hierarchical matrix
msc: [65F55, 65F05, 65N38]
sources:
  - url: https://en.wikipedia.org/wiki/Hierarchical_matrix
same_as:
  wikidata: Q17029389
  wikipedia: Hierarchical matrix
---

## Summary

A hierarchical matrix, or $\mathcal{H}$-matrix, is a matrix split into a hierarchy of blocks.
Each block that couples well-separated groups of indices has low [[rank|0ZC9YTXZRY]].
Such matrices are stored and multiplied with a vector in about $n \log n$ operations instead of $n^2$.
Approximate inverses and factorizations can be kept in the same format.
This gives fast solvers for the dense matrices of integral equations and for finite element matrices.

## Explanations

### L1 human

Think of $n$ points in space and a matrix whose entry $(i, j)$ measures the interaction of point $i$ with point $j$, such as $1 / \abs{x_i - x_j}$.
Two clusters of points that are far apart interact smoothly, so the block of the matrix linking them is close to a matrix of small rank.
Such a block can be stored with a few vectors instead of all its entries.
Only the blocks of nearby points are stored in full, and these are small.
A hierarchical matrix applies this idea at all scales at once.
