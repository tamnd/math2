---
tag: 6HWFBXYPZP
kind: concept
name: Schur complement
msc: [15A09, 15A15]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
same_as:
  wikidata: Q1778169
  wikipedia: Schur complement
---

## Summary

The Schur complement of an invertible block $A$ in a [[block matrix|0ASDFEQS6P]] $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is the matrix $D - C A^{-1} B$.
It is what remains of the block $D$ after block Gaussian elimination removes the block $C$.
It gives the [[determinant via the Schur complement|0KA7A4ENVJ]], formulas for the inverse of a block matrix, and tests for positive definiteness.

## Explanations

### L1 human

Think of a system of two vector equations in two unknown vectors $x$ and $y$.
If you solve the first equation for $x$ and put the result into the second, the matrix in front of $y$ is the Schur complement.
For numbers, take $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a \ne 0$.
The Schur complement of $a$ is the number $d - cb/a$.
Then the determinant $ad - bc$ equals $a \cdot (d - cb/a)$.
