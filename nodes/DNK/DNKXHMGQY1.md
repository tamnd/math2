---
tag: DNKXHMGQY1
kind: concept
name: M-matrix
msc: [15B48, 15A18]
specializes: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/M-matrix
same_as:
  wikidata: Q3064355
  wikipedia: M-matrix
---

## Summary

An M-matrix is a real square matrix of the form $sI - B$, where $B$ is a [[nonnegative matrix|JPQCCFCY8X]].
The number $s$ must be at least the [[spectral radius|9V7YQA85PC]] of $B$.
Since $B$ has no negative entry, the entries of an M-matrix off the diagonal are nonpositive.
Such matrices appear when a linear system is discretised, in economic input-output models and in Markov chains.
A nonsingular M-matrix has an inverse with all entries nonnegative, so it turns nonnegative data into nonnegative solutions.

## Explanations

### L1 human

Think of a matrix with positive numbers on the diagonal and negative or zero numbers elsewhere.
It is an M-matrix when the diagonal is strong enough to dominate the rest in a precise sense.
The matrix $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, which comes from the second difference of a function, is an example.
Its inverse $\frac{1}{3}\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has only nonnegative entries.
