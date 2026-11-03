---
tag: D6J73PTWPT
kind: definition
name: Hyperelastic material
msc: [74B20]
defines: ZHK2EVRD90
uses: [DV71K7X1JD, 3E9K1DRNYN, Q1MD7W6CT3]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperelastic_material
---

## Definition

A *hyperelastic material* is a [[Cauchy elastic material|DV71K7X1JD]] that has a [[strain energy density function|3E9K1DRNYN]] $W$.
That is, its first [[Piola–Kirchhoff stress|Q1MD7W6CT3]] is $P = \partial W / \partial F$, where $F$ is the deformation gradient and $W$ is a differentiable scalar function of $F$ with $\det F > 0$.

## Remarks

For a frame-indifferent material, $W(QF) = W(F)$ for all rotations $Q$.
If the material is also isotropic, $W$ is a function of the three principal invariants $I_1, I_2, I_3$ of the right Cauchy–Green tensor $C = F^T F$.
For an incompressible material the constraint $\det F = 1$ adds a pressure term: $P = \partial W / \partial F - p F^{-T}$, with $p$ a Lagrange multiplier.
Example: the incompressible neo-Hookean solid, with $W = \frac{\mu}{2}(I_1 - 3)$.
Non-example: take the response $P = \mu F + AF$ for a fixed nonzero antisymmetric matrix $A$.
Its stress depends only on $F$, but the derivative of $F \mapsto P$ is not symmetric.
So $P$ is not the derivative of any function $W$.
The total work of the stress around any closed path of deformations is zero for a hyperelastic material, and this property characterises hyperelasticity among Cauchy elastic materials.

## Explanations

### L1 human

The stress is the derivative of one stored energy function.
So the material gives back all the energy put into it, whatever the path of loading.
