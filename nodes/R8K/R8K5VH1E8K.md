---
tag: R8K5VH1E8K
kind: concept
name: Fourier–Stieltjes algebra
msc: [43A30, 43A35, 22D25]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_algebra
---

## Summary

The Fourier–Stieltjes algebra $B(G)$ of a [[locally compact group|AHV05ZBCYW]] $G$ is the algebra of coefficient functions $x \mapsto \ip{\pi(x)\xi}{\eta}$ of all continuous [[unitary representations|74BPYJNZTM]] $\pi$ of $G$.
It is the linear span of the continuous [[positive-definite functions|3PRZ02APFA]] on $G$.
It is a commutative unital Banach algebra under pointwise operations, the dual of the group C\*-algebra.
For abelian $G$ it is the image of the measure algebra of the dual group under the Fourier–Stieltjes transform, which explains the name.

## Explanations

### L1 human

A unitary representation lets the group act on a Hilbert space by rotations.
Choosing two vectors and recording how one of them, moved by each group element, lines up with the other gives a function on the group.
The Fourier–Stieltjes algebra consists of all functions obtained in this way.
For the integers, these are the sequences of Fourier coefficients of finite measures on the circle.
The constant function $1$ is always one of them, coming from the trivial representation.
