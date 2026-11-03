---
tag: 9K50KFCY6S
kind: concept
name: Lattice-based cryptography
msc: [94A60, 11H06, 68P25]
specializes: [7YNRCX56CM]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice-based_cryptography
same_as:
  wikidata: Q6497083
  wikipedia: Lattice-based cryptography
---

## Summary

Lattice-based cryptography builds cryptographic schemes whose security rests on hard problems about [[lattices|WN9V7WSJKF]] in $\R^n$, such as finding a short nonzero lattice vector.
Many of its schemes come with proofs that breaking them on average is as hard as solving a lattice problem in the worst case.
No efficient quantum algorithm is known for these problems, so the schemes are candidates for post-quantum cryptography.
The [[learning with errors|TAKWH3D7R6]] problem is the main hardness assumption, and it also underlies most fully homomorphic encryption schemes in use.

## Explanations

### L1 human

A lattice is a regular grid of points, like the integer points of the plane, but possibly slanted and in hundreds of dimensions.
Given a basis of long, nearly parallel vectors, it is very hard to find the shortest nonzero point of the grid.
A user who knows a good basis of short vectors can solve problems that are hopeless with a bad basis.
This gap between good and bad bases is what lattice-based schemes exploit.
