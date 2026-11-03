---
tag: VH55PZZYKS
kind: problem
name: Ericksen's problem of universal deformations
msc: [74B20, 74G05]
uses: [ZHK2EVRD90, E51Y1CMF1Q]
about: [ZHK2EVRD90]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperelastic_material
history:
  posed_by: "Jerald Ericksen"
  first_stated: "1954"
---

## Problem

Fix a class of homogeneous isotropic [[hyperelastic materials|ZHK2EVRD90]].
A [[deformation|E51Y1CMF1Q]] of a body is *universal* for the class if every material in the class can be held in this deformation in equilibrium.
The equilibrium must hold without body forces, with surface tractions alone.
Find all universal deformations, separately for the class of compressible materials and for the class of incompressible materials, where only deformations with $\det F = 1$ are allowed.

## Remarks

Ericksen showed in 1955 that for compressible materials the universal deformations are exactly the homogeneous ones, those with constant deformation gradient.
For incompressible materials, the homogeneous isochoric deformations are universal.
Five families of inhomogeneous universal deformations are also known, including the bending of a block into a sector of a cylindrical tube and the inflation of spherical shells.
Whether this list is complete for incompressible materials is still open.
Universal deformations are important because they allow tests that work without knowing the strain energy function in advance, and they are the basis of the semi-inverse solutions of finite elasticity.

## Explanations

### L1 human

For most deformations of a rubber block, whether forces on the surface alone can hold them depends on the exact rubber.
Some deformations are special: they can be held by surface forces in every rubber-like material whatever its energy function.
Ericksen asked for the complete list of these special deformations.
For compressible materials the answer is simple, only uniform deformations; for incompressible ones the question is still not fully answered.
