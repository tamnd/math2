---
tag: G7968MRFNH
kind: concept
name: Fourier transform on finite groups
msc: [43A30, 20C15, 43A25]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform_on_finite_groups
same_as:
  wikidata: Q5475803
  wikipedia: Fourier transform on finite groups
---

## Summary

The Fourier transform on a finite group $G$ sends $f \colon G \to \C$ to the matrices $\widehat{f}(\rho) = \sum_{a \in G} f(a)\rho(a)$.
There is one matrix for each [[irreducible representation|FX3NEFYFFN]] $\rho$ of $G$.
For an abelian group the irreducible representations are the [[characters|H1WNVN5V7F]], and the transform is a function on the [[character group|FPRA2KEHFF]].
For $\Z/n\Z$ it is the [[discrete Fourier transform|TST0GH66A5]].
It turns convolution into products of matrices, and it can be inverted.
It is used in combinatorics, probability on groups, coding theory and fast algorithms.

## Explanations

### L1 human

A function on a finite group can be split into pieces that transform in the simplest possible ways under the group.
For the cyclic group $\Z/n\Z$ the pieces are the waves $a \mapsto e^{2\pi i k a / n}$, and the transform lists how much of each wave the function contains.
For a nonabelian group some pieces are small matrices instead of numbers, because the group has irreducible representations of dimension greater than $1$.
For example, the transform of the indicator function of the identity element is the identity matrix at every irreducible representation.
