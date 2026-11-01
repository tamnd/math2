---
tag: X9B1XETBPF
kind: concept
name: Permanent
msc: [15A15]
sources:
  - url: https://en.wikipedia.org/wiki/Permanent_(mathematics)
same_as:
  wikidata: Q1344007
  wikipedia: Permanent (mathematics)
---

## Summary

The permanent of a square matrix is the sum, over all permutations, of the products of one entry from each row and each column.
It is the [[determinant|00KDZRW4C0]] formula without the signs.
For the $0/1$ biadjacency matrix of a [[bipartite graph|0ZVQKTRKVQ]], it counts the [[perfect matchings|0NHK9MFFW9]].
Unlike the determinant, it is believed to be hard to compute: computing the permanent of a $0/1$ matrix is #P-complete.

## Explanations

### L1 human

Put $n$ rooks on an $n \times n$ board so that no two share a row or a column, and multiply the entries under the rooks.
The permanent is the sum of these products over all such placements.
The determinant uses the same products but adds some of them with a minus sign.
For $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ the permanent is $ad + bc$, while the determinant is $ad - bc$.
