---
tag: S026HQSGY9
kind: concept
name: Zak transform
msc: [42A38, 42C15]
sources:
  - url: https://en.wikipedia.org/wiki/Zak_transform
same_as:
  wikidata: Q25303763
  wikipedia: Zak transform
---

## Summary

The Zak transform turns a function on $\R$ into a function of two variables by periodizing it with phase factors.
It is a unitary map from $L^2(\R)$ onto $L^2([0, 1)^2)$, and its values are quasi-periodic.
It diagonalizes Gabor systems at critical density, which makes it the main tool behind the [[Balian–Low theorem|XVVHKCYF2Z]].
It has been discovered several times; Joshua Zak introduced it in solid-state physics.

## Explanations

### L1 human

Take a function on the line and cut it into pieces of length $1$.
Stack the pieces on top of each other, and add them up with phase factors $e^{-2\pi i k \omega}$ that depend on a second variable $\omega$.
The result depends on a position $x$ within one piece and on $\omega$.
It is a Fourier series in the index $k$ of the pieces, for each fixed $x$.
For the box function $1_{[0, 1)}$ there is just one piece, and the Zak transform is constant $1$ on the unit square.
