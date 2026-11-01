---
tag: SQT6QCEXZ8
kind: concept
name: Hadamard product
msc: [15A99, 15B48]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
same_as:
  wikidata: Q3406746
  wikipedia: Hadamard product (matrices)
---

## Summary

The Hadamard product of two [[matrices|0VD9ZSWWJG]] of the same size is the matrix of the products of their corresponding entries.
It is also called the entrywise product or the Schur product.
Unlike ordinary [[matrix multiplication|032Q9FB8MT]], it is commutative.
The Schur product theorem says that it keeps positive semidefinite matrices positive semidefinite.

## Explanations

### L1 human

Lay two tables of numbers of the same shape on top of each other.
Multiply the two numbers in each cell, and write the result in that cell.
For example, the Hadamard product of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$ is $\begin{pmatrix} 5 & 12 \\ 21 & 32 \end{pmatrix}$.
This is different from the usual matrix product, which mixes rows with columns.
