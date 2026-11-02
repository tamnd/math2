---
tag: F20VTSH2FM
kind: concept
name: Pseudospectrum
msc: [65F15, 15A18, 47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudospectrum
same_as:
  wikidata: Q7255579
  wikipedia: Pseudospectrum
---

## Summary

The $\varepsilon$-pseudospectrum of a square matrix is a set of complex numbers.
It consists of the numbers that become [[eigenvalues|0BQAA2BK3Q]] after some perturbation of the matrix of norm less than $\varepsilon$.
Equivalently, it is the region where the norm of the [[resolvent|J5YNNKSB9P]] $(zI - A)^{-1}$ exceeds $1/\varepsilon$.
For non-normal matrices it can be much larger than the set of eigenvalues.
It then explains transient growth, slow convergence of iterative methods and sensitivity of computed eigenvalues, which the eigenvalues alone do not show.

## Explanations

### L1 human

Eigenvalues of some matrices are very fragile: a tiny change of the entries moves them far away.
The pseudospectrum draws, for a given tolerance $\varepsilon$, all the places the eigenvalues could move to under a change of size $\varepsilon$.
For a symmetric matrix this is just a disc of radius $\varepsilon$ around each eigenvalue.
For the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, whose only eigenvalue is $0$, it contains a disc of radius $\sqrt{\varepsilon}$, which is far larger than $\varepsilon$ when $\varepsilon$ is small.
