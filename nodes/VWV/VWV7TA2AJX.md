---
tag: VWV7TA2AJX
kind: concept
name: Tensor decomposition
msc: [15A69, 15A23, 65F55]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_decomposition
same_as:
  wikidata: Q30103009
  wikipedia: Tensor decomposition
---

## Summary

A tensor decomposition writes a multi-way array as a combination of simpler pieces.
It plays the role that a matrix factorization plays for matrices.
The canonical polyadic (CP) decomposition writes the tensor as a sum of simple tensors.
The Tucker decomposition combines a small core tensor with one factor matrix per mode.
The shortest CP decomposition has length equal to the [[tensor rank|W84NTF77M0]].
Tensor decompositions are used to compress data and to find hidden structure in signal processing, statistics and chemistry.

## Explanations

### L1 human

Think of a cube of numbers, such as ratings indexed by user, product and month.
A CP decomposition writes the cube as a sum of a few "outer products" of three vectors, one for each direction.
Each term is a simple pattern: a group of users who like a group of products during certain months.
For example, the cube with entries $a_{ijk} = x_i y_j z_k$ is a single term, so it has a decomposition with one piece.
This extends the idea of the [[singular value decomposition|000NPTMX6J]] from tables to cubes.
