---
tag: AS4WVMYEDZ
kind: concept
name: Boolean matrix
msc: [15B34, 05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_matrix
same_as:
  wikidata: Q1994977
  wikipedia: Logical matrix
---

## Summary

A Boolean matrix, also called a logical matrix or a $(0,1)$-matrix, is a [[matrix|0VD9ZSWWJG]] whose entries are $0$ and $1$, read as false and true.
It records a [[binary relation|05AVARPXA2]] between two finite sets.
With Boolean arithmetic, the product of two such matrices records the [[composition of the relations|0PYSR20HGF]].
The [[adjacency matrix|08B9CX109G]] of a [[directed graph|0KFYGSHHF5]] is the main example.

## Explanations

### L1 human

Write the elements of one set along the rows and the elements of another set along the columns.
Put a $1$ in a cell when the row element is related to the column element, and a $0$ otherwise.
For the relation "divides" on $\set{1, 2, 3}$, the first row is $1, 1, 1$, because $1$ divides every number.
The second row is $0, 1, 0$ and the third row is $0, 0, 1$.
