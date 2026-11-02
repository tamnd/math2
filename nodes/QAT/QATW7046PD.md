---
tag: QATW7046PD
kind: concept
name: Weierstrass zeta and sigma functions
msc: ["33E05", 30D30]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_sigma,_zeta,_and_eta_functions
---

## Summary

For a lattice $\Lambda$ in $\C$, the Weierstrass sigma function $\sigma$ is an [[entire function|0G4F0XB9X2]] with a simple zero at each lattice point.
The Weierstrass zeta function is its logarithmic derivative $\zeta = \sigma'/\sigma$.
They are companions of the [[Weierstrass elliptic function|361NAK68QK]] $\wp$, since $\zeta' = -\wp$.
Neither is elliptic: shifting by a period adds a constant to $\zeta$ and multiplies $\sigma$ by an exponential factor.
They are the building blocks for writing any elliptic function from its zeros and poles.

## Explanations

### L1 human

A polynomial can be written as a product over its roots.
The sigma function plays this role for the lattice: it is a product over all lattice points, with exponential correction factors so that the product converges.
Taking its logarithmic derivative gives the zeta function, a sum of simple poles, one at each lattice point.
Differentiating once more and changing sign gives $\wp$, which has double poles and is truly periodic.
So $\sigma$, $\zeta$, $\wp$ form a chain, and only the last one is elliptic.
