---
tag: 8G3X8MPG7E
kind: concept
name: Commuting matrices
msc: [15A27]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
same_as:
  wikidata: Q3360633
  wikipedia: Commuting matrices
---

## Summary

Two square matrices $A$ and $B$ commute when $AB = BA$.
[[Matrix multiplication|032Q9FB8MT]] is [[not commutative|0P506SPZP2]] in general, so commuting pairs are special.
Commuting matrices behave much like numbers: for example, $e^{A + B} = e^{A} e^{B}$ for [[commuting matrices|04BD23PSK5]].
Diagonalisable matrices can be diagonalised by one common basis exactly when they commute, by [[simultaneous diagonalisation|0FK17N4DKA]].

## Explanations

### L1 human

For numbers, the order of a product never matters, but for matrices it usually does.
Matrices that commute are the pairs for which the order does not matter.
As maps, applying $A$ then $B$ gives the same result as applying $B$ then $A$.
For example, every matrix commutes with itself, with its powers, and with every [[scalar matrix|067NKSBEWT]] $cI$.
The matrices $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ do not commute.
