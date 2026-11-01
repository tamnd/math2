---
tag: DP3KSCRKFP
kind: concept
name: Embedding dimension
msc: [13H05, 13H99]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_local_ring
---

## Summary

The embedding dimension of a Noetherian [[local ring|MZ02BKPHJA]] $(R, \mathfrak m, k)$ is the dimension of its [[cotangent space|Z1CGB483J6]] $\mathfrak m / \mathfrak m^2$ over $k$.
By [[Nakayama's lemma|15JHBYR6KH]] it equals the minimal number of generators of $\mathfrak m$.
It is always at least the [[Krull dimension|MVGBS3J1P7]] of $R$, and equality defines a [[regular local ring|63XXTF6B5M]].

## Explanations

### L1 human

The embedding dimension counts how many coordinates you need to describe a space near a point.
A smooth curve needs one coordinate, but the cusp $y^2 = x^3$ at the origin needs two, even though it is still a curve.
The difference between the embedding dimension and the actual dimension measures how singular the point is.
The [[definition|BRXX5Y929C]] states it.
