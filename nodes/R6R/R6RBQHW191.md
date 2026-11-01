---
tag: R6RBQHW191
kind: concept
name: Unimodular matrix
msc: [15B36, 11C20]
specializes: [0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Unimodular_matrix
same_as:
  wikidata: Q1367055
  wikipedia: Unimodular matrix
---

## Summary

A unimodular matrix is a square matrix with integer entries and [[determinant|00KDZRW4C0]] $+1$ or $-1$.
These are exactly the integer matrices whose inverse also has integer entries.
They form the group $\mathrm{GL}_n(\Z)$, the [[general linear group|0FCHE902D7]] over the integers.
Unimodular matrices describe the changes of basis of the lattice $\Z^n$, and they appear in the Smith and Hermite normal forms.

## Explanations

### L1 human

For real matrices, any nonzero determinant allows an inverse.
For integer matrices, an inverse with integer entries needs more: the determinant must be $1$ or $-1$.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has determinant $1$ and inverse $\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
Such a matrix maps the grid of integer points of the plane onto itself, one to one.
