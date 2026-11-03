---
tag: 1WTNGZ5T5A
kind: concept
name: Rank of a projective module
msc: [13C10, 19A49]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Summary

The rank of a [[finitely generated projective module|HQA9YHDSH5]] $P$ over a commutative ring $R$ is a function on prime ideals.
It assigns to $\mathfrak{p}$ the rank of the free module $P_\mathfrak{p}$ over the [[local ring|MZ02BKPHJA]] $R_\mathfrak{p}$.
It is a locally constant function on the [[spectrum|FB45BHHA2J]] of $R$, so it is constant when the spectrum is connected.
It extends the dimension of a vector space and gives a homomorphism from [[$K_0(R)$|Q14JS2MA1C]] to the group of locally constant integer-valued functions on $\mathrm{Spec}\, R$.

## Explanations

### L1 human

A projective module looks free near each point of the spectrum, so near each point it has a number of coordinates.
That number is the rank at the point.
On a connected spectrum the rank cannot jump, so it is a single number, like the dimension of a vector space or the rank of a vector bundle.
Over $\Z/6\Z$, whose spectrum has two points, the module $\Z/2\Z$ has rank $1$ at one point and rank $0$ at the other.
