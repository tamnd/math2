---
tag: 46NHWJHW44
kind: concept
name: Logarithmic potential
msc: [31A15]
specializes: [JHKSF3XFY2]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Summary

The logarithmic potential of a finite measure $\mu$ with compact support in the plane is $p_\mu(z) = \int \log(1/\abs{z - w}) \, d\mu(w)$.
It is the [[potential of the measure|JHKSF3XFY2]] $\mu$ with respect to the [[logarithmic kernel|VDZ5FKYC2T]].
It is harmonic off the support of $\mu$ and superharmonic on the whole plane.
Logarithmic potentials connect potential theory with complex analysis.
For a polynomial $p$ with zeros $z_1, \dots, z_d$, $\log(1/\abs{p})$ is, up to a constant, the logarithmic potential of the point masses at the zeros.

## Explanations

### L1 human

In the plane a point charge creates a potential that changes like the logarithm of the distance.
Spread charge along a curve or over a region, and add up the logarithmic contributions: this is the logarithmic potential.
For one unit charge at the origin it is $\log(1/\abs{z})$.
For a monic polynomial $p(z) = (z - z_1)\cdots(z - z_d)$, the potential of unit charges at the roots is $-\log\abs{p(z)}$.
