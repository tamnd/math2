---
tag: 5H8XESYCHQ
kind: concept
name: Wiener algebra
msc: [42A20, 46J10, 43A20]
specializes: [9KYWN94QDN]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_algebra
same_as:
  wikidata: Q7999136
  wikipedia: Wiener algebra
---

## Summary

The Wiener algebra $A(\mathbb{T})$ is the set of continuous periodic functions with an [[absolutely convergent Fourier series|HHBGB5R5S2]].
Its norm is the sum of the absolute values of the Fourier coefficients.
With pointwise multiplication it is a commutative [[Banach algebra|9KYWN94QDN]], isometrically isomorphic to the sequence algebra $\ell^1(\Z)$ with convolution.
It is the setting of [[Wiener's lemma|NC768TWZ3D]] and a basic example in the Gelfand theory of commutative Banach algebras.

## Explanations

### L1 human

Take all periodic functions whose Fourier coefficients have a finite sum of absolute values.
Adding or multiplying two such functions gives another one, so they form an algebra.
Measuring a function by the total size of its coefficients makes this algebra complete.
The functions $\cos x$ and $\sum_{n \in \Z} 2^{-\abs{n}} e^{inx}$ belong to it, while the square wave does not, because it is not even continuous.
