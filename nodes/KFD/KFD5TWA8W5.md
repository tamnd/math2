---
tag: KFD5TWA8W5
kind: concept
name: Pre-Lie algebra
msc: [17D25, 17A30]
specializes: [6Z35W744KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Pre-Lie_algebra
same_as:
  wikidata: Q7239170
  wikipedia: Pre-Lie algebra
---

## Summary

A pre-Lie algebra, also called a left-symmetric algebra, is a [[nonassociative algebra|60W3THKGA7]] whose [[associator|RT4YV20367]] is symmetric in two of its three arguments.
Its commutator $xy - yx$ is always a Lie bracket, so every pre-Lie algebra gives a [[Lie algebra|5JJYBJ6A8K]].
Pre-Lie algebras arise from flat torsion-free connections and from the composition of vector fields on affine space.
They also arise from rooted trees in the study of numerical integrators, and in deformation theory.

## Explanations

### L1 human

Associative algebras have associator zero, so their commutator is a Lie bracket.
A pre-Lie algebra relaxes associativity just enough to keep this property: the associator need not vanish, but it must be symmetric in the first two variables.
The basic example is the product of vector fields on $\R^n$ given by differentiating the second field along the first.
On polynomials in one variable it reads $a \cdot b = a b'$, and its commutator $a b' - b a'$ is the bracket of the vector fields $a \frac{d}{dx}$ and $b \frac{d}{dx}$.
