---
tag: WJWNYSQKK8
kind: concept
name: Matrix congruence
msc: [15A63, 15A21]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
same_as:
  wikidata: Q377286
  wikipedia: Matrix congruence
---

## Summary

Two square matrices $A$ and $B$ are congruent when $B = P^{T} A P$ for some invertible matrix $P$.
Congruent matrices are the matrices of one [[bilinear form|0SQZMXB6GP]] in two different bases.
Congruence is an equivalence relation, and its classification for real symmetric matrices is [[Sylvester's law of inertia|0WFED3K3DQ]].
It differs from [[similarity|0E89HQATM8]], which uses $P^{-1}$ in place of $P^{T}$.

## Explanations

### L1 human

A bilinear form, such as a dot product, gives a matrix once you choose a basis.
If you change the basis with a matrix $P$, the new matrix of the same form is $P^{T} A P$.
So congruent matrices describe the same form seen in two coordinate systems.
For example, $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix}$ are congruent, with $P = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$.
