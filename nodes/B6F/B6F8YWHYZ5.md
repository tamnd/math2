---
tag: B6F8YWHYZ5
kind: concept
name: QR algorithm
msc: [65F15, 15A18, 15A23]
sources:
  - url: https://en.wikipedia.org/wiki/QR_algorithm
same_as:
  wikidata: Q453132
  wikipedia: QR algorithm
---

## Summary

The QR algorithm computes all the [[eigenvalues|0BQAA2BK3Q]] of a square matrix.
It repeatedly factors the matrix as $QR$ by the [[QR decomposition|0ERWG4NXQ9]] and multiplies the factors in the reverse order, $RQ$.
Each step is a [[similarity|0E89HQATM8]] by an [[orthogonal matrix|0W02QESPJQ]], so the eigenvalues do not change.
The matrices tend to an [[upper triangular|0N4XY7Z3NN]] form with the eigenvalues on the diagonal.
With shifts and a preliminary reduction to [[Hessenberg form|YCEEWJTX56]], it is the standard method for dense eigenvalue problems.

## Explanations

### L1 human

The algorithm takes a matrix and splits it into an orthogonal part $Q$, which preserves lengths and angles, and a triangular part $R$.
Then it puts them back together the other way round.
The new matrix has the same eigenvalues as the old one.
Repeating this pushes the entries below the diagonal towards zero, so the eigenvalues appear on the diagonal.
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, one step gives $\begin{pmatrix} 2.8 & 0.6 \\ 0.6 & 1.2 \end{pmatrix}$, already closer to the eigenvalues $3$ and $1$ on the diagonal.
