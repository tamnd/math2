---
tag: SCMS389SBG
kind: concept
name: Positive-definite kernel
msc: ["46E22", 43A35]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_kernel
same_as:
  wikidata: Q7233207
  wikipedia: Positive-definite kernel
---

## Summary

A positive-definite kernel on a set $X$ is a function $K \colon X \times X \to \C$ with the following property.
Every matrix $\big(K(x_i, x_j)\big)_{i,j}$ built from finitely many points of $X$ is [[positive semidefinite|01MMVW8CKC]].
It generalises positive semidefinite matrices from finite index sets to arbitrary sets.
Each positive-definite kernel is the reproducing kernel of a unique [[reproducing kernel Hilbert space|4CK2GSRAGD]], and conversely.
On a group, the kernels $K(g, h) = \varphi(g^{-1}h)$ that are positive-definite are those given by [[positive-definite functions|3PRZ02APFA]] $\varphi$.

## Explanations

### L1 human

A positive-definite kernel measures similarity between points in a way that behaves like an inner product.
The basic example is $K(x, y) = \ip{x}{y}$ on a space of vectors.
Another one is the Gaussian kernel $K(x, y) = e^{-\norm{x - y}^2}$ on $\R^n$, which is $1$ for equal points and decays as they move apart.
The theory says that every such kernel really is an inner product, after the points are mapped into a suitable, possibly infinite-dimensional, Hilbert space.
This is the basis of kernel methods in statistics and machine learning.
