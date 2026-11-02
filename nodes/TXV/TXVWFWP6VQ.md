---
tag: TXVWFWP6VQ
kind: concept
name: Representation of a quiver
msc: [16G20]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Summary

A representation of a [[quiver|RE9YFFS3TS]] over a field assigns a [[vector space|000AYPA9AJ]] to each vertex.
It also assigns to each arrow a [[linear map|0NRYHJPQG2]] from the space at its source to the space at its target.
Representations of a finite quiver are the same as modules over its [[path algebra|2PYANBGXFD]].
Classifying the [[indecomposable|E2P29GCD9T]] representations is a central problem; [[Gabriel's theorem|FC78F2E87E]] and [[Kac's theorem|59QJC3ZXA1]] describe their dimension vectors through root systems.
Many problems of linear algebra, such as the classification of pairs of matrices, are problems about quiver representations.

## Explanations

### L1 human

Take a quiver, a diagram of dots and arrows.
Put a vector space at each dot and a matrix along each arrow, going from the space at the start to the space at the end.
That is a representation.
For the quiver with one vertex and one loop, a representation is a single square matrix.
Over the complex numbers its classification up to change of basis is the Jordan normal form.
For one arrow $1 \to 2$, a representation is a linear map, determined up to isomorphism by the two dimensions and its rank.
