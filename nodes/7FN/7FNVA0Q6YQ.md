---
tag: 7FNVA0Q6YQ
kind: concept
name: Point spectrum
msc: [47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
---

## Summary

The point spectrum of an operator is its set of eigenvalues.
It is the part of the [[spectrum|BMKATJ802A]] where $T - \lambda I$ fails to be injective.
For matrices the point spectrum is the whole spectrum, but in infinite dimensions it can be a small part of it, or empty.

## Explanations

### L1 human

An eigenvalue $\lambda$ is a number for which some nonzero vector is just multiplied by $\lambda$.
The point spectrum collects these numbers.
For the left shift $(x_1, x_2, \ldots) \mapsto (x_2, x_3, \ldots)$ on square-summable sequences, the sequence $(1, \lambda, \lambda^2, \ldots)$ is an eigenvector for every $\abs{\lambda} < 1$.
For the right shift, which only moves entries further out, there are no eigenvalues at all.
