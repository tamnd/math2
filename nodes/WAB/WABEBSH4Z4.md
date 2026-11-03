---
tag: WABEBSH4Z4
kind: example
name: Neo-Hookean solid
msc: [74B20]
instance_of: [ZHK2EVRD90]
uses: [3E9K1DRNYN, N5G8WNQFC3]
sources:
  - url: https://en.wikipedia.org/wiki/Neo-Hookean_solid
same_as:
  wikidata: Q6991734
  wikipedia: Neo-Hookean solid
---

## Example

The incompressible *neo-Hookean solid* is the [[hyperelastic material|ZHK2EVRD90]] with the [[strain energy density function|3E9K1DRNYN]] below.
$$W = \frac{\mu}{2}(I_1 - 3), \qquad I_1 = \tr(F^T F), \qquad \det F = 1.$$
Here $F$ is the deformation gradient, $I_1$ is the first invariant of the right [[Cauchy–Green tensor|N5G8WNQFC3]] and $\mu > 0$ is a constant.
Since $\partial I_1 / \partial F = 2F$, the first Piola–Kirchhoff stress is $P = \mu F - p F^{-T}$.
The Cauchy stress is $\sigma = \mu F F^T - p I$, with $p$ a pressure fixed by equilibrium and boundary conditions.
Check in simple tension with stretch $\lambda$: $F = \operatorname{diag}(\lambda, \lambda^{-1/2}, \lambda^{-1/2})$, and the lateral faces are free, so $\sigma_{22} = \mu \lambda^{-1} - p = 0$.
Then the axial stress is $\sigma_{11} = \mu(\lambda^2 - \lambda^{-1})$.
For $\lambda = 1 + \epsilon$ with small $\epsilon$, this is about $3\mu\epsilon$, which matches linear elasticity with shear modulus $\mu$ and Young's modulus $3\mu$ of an incompressible material.
Compressible versions add a term depending on $J = \det F$; several different forms are in use.

## Explanations

### L1 human

The neo-Hookean model is the simplest model of rubber at large stretches.
It has just one material constant, the shear modulus.
The energy grows with the sum of the squares of the principal stretches, the natural extension of Hooke's law to large deformations.
It describes rubber well up to moderate stretches, but underestimates the stiffening at very large ones.
