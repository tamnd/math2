---
tag: E8WYXVENC6
kind: object
name: Coxeter's integral octonions
msc: [17A75, 11H06, 17D05]
uses: [1HRMT3DSX2, KJ145M3CVT, E5DH1CSW1N, 2CXH65EKY7, H0TJPNCMXD, QHTAEPTKEB]
sources:
  - url: https://en.wikipedia.org/wiki/Octonion
    locator: Integral octonions
---

## Description

Let $\mathbb{O}$ be the [[octonions|1HRMT3DSX2]], with standard basis $1, e_1, \ldots, e_7$, conjugation $x \mapsto \bar{x}$ and norm $N(x) = x\bar{x}$.
The *Gravesian octonions* are the octonions whose eight coordinates are all integers.
They form a subring of $\mathbb{O}$ that is a lattice of rank $8$, on which $N$ and the trace $x + \bar{x}$ take integer values.
But it is not maximal among the subrings with these properties.
There are exactly seven maximal subrings of this kind that contain the Gravesian octonions.
*Coxeter's integral octonions* are any one of these seven rings.
The automorphisms of $\mathbb{O}$ permute the seven rings transitively, so the choice of one of them is harmless.
Coxeter studied them in his 1946 paper on integral Cayley numbers.

## Remarks

They are the octonion analogue of the [[Hurwitz quaternions|QHTAEPTKEB]], a [[maximal order|E5DH1CSW1N]] in the quaternions.
Besides the integer points they contain points with half-integer coordinates.
As a lattice in $\mathbb{O} \cong \R^8$ with the quadratic form $2N$, they form a copy of the [[E8 lattice|2CXH65EKY7]].
So the integral octonions of norm $1$ are $240$ elements, matching the $240$ roots of $E_8$.
These $240$ units are closed under multiplication and inverses and form a [[Moufang loop|H0TJPNCMXD]] that is not a group, because octonion multiplication is not associative.

## Explanations

### L1 human

The integers sit inside the real numbers as a discrete ring, and one can ask for the same kind of ring inside the octonions.
The obvious choice, octonions with integer coordinates, is too small: one can add certain points with half-integer coordinates and still have a ring with integer norms.
The largest such rings are Coxeter's integral octonions.
Their points form the $E_8$ lattice, which gives the densest packing of spheres in eight dimensions.
Their $240$ units are the centres of the $240$ spheres that touch the sphere centred at $0$.
