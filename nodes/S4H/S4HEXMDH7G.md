---
tag: S4HEXMDH7G
kind: definition
name: Continuum mechanics
msc: [74A99, 76A02]
defines: X01DZTS224
uses: [0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Continuum_mechanics
---

## Definition

*Continuum mechanics* is the branch of mechanics that studies bodies modelled as continua.
A continuum body is given by the following data.

1. A *reference configuration*: a nonempty open set $B \subseteq \R^3$, whose points $X$ label the material points of the body.
2. A *motion*: a map $\chi \colon B \times I \to \R^3$, with $I$ a time interval, such that each $\chi(\cdot, t)$ is an orientation-preserving [[diffeomorphism|0KZZ70ZHXP]] of $B$ onto an open set $\Omega_t$.
3. A *mass density*: a positive function $\rho(x, t)$ on the current configuration $\Omega_t$, such that the mass of a part $P \subseteq B$ at time $t$ is $\int_{\chi(P, t)} \rho \, dx$.

The motion, the density and the forces are related by balance laws, valid for every body, and by constitutive equations, which describe a particular material.

## Remarks

A solid bar in $B = (0, L) \times (0, 1)^2$ stretched uniformly has the motion $\chi(X, t) = (\lambda(t) X_1, X_2, X_3)$ with $\lambda(t) > 0$.
It satisfies clause 2, since each $\chi(\cdot, t)$ is a diffeomorphism with Jacobian determinant $\lambda(t) > 0$.
Let $B$ contain points with $X_1$ of both signs.
Then $\chi(X, t) = (X_1^2, X_2, X_3)$ is not a motion, since it folds two material points onto one place and so is not injective.
The point of view is macroscopic: the fields are assumed smooth, and the atomic structure is ignored.

## Explanations

### L1 human

Continuum mechanics treats a body as a smooth blob of matter.
Each piece of the blob is followed in time by a map that sends its starting point to its current point.
Physics enters through balance of mass, momentum and energy, which hold for every material, and through constitutive equations, which say how a given material responds.
