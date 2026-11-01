---
tag: 9V7YQA85PC
kind: concept
name: Spectral radius
msc: [15A18, 15A60]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_radius
same_as:
  wikidata: Q249748
  wikipedia: Spectral radius
---

## Summary

The spectral radius of a square complex matrix is the largest absolute value of its [[eigenvalues|0BQAA2BK3Q]].
It controls the long-run growth of the powers $A^k$: they tend to $0$ exactly when the spectral radius is less than $1$.
It is bounded by every operator norm, and [[Gelfand's formula|3KX0KQ7V05]] recovers it from the norms of the powers.

## Explanations

### L1 human

Draw the eigenvalues of a matrix in the complex plane.
The spectral radius is the radius of the smallest disc around $0$ that contains all of them.
For $\begin{pmatrix} 2 & 0 \\ 0 & -3 \end{pmatrix}$ the eigenvalues are $2$ and $-3$, so the spectral radius is $3$.
Applying the matrix many times makes vectors grow roughly like $3^k$.
