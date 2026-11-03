---
tag: RCS2X0F9SS
kind: definition
name: Solid mechanics
msc: [74A99]
defines: JRD6BDKT1X
uses: [X01DZTS224, Q4C55V47A8, HTYRR2WDQ6]
sources:
  - url: https://en.wikipedia.org/wiki/Solid_mechanics
---

## Definition

*Solid mechanics* is the part of [[continuum mechanics|X01DZTS224]] that studies bodies made of solid materials.
A material is treated as a *solid* when its [[constitutive equation|Q4C55V47A8]] refers to a reference configuration.
This means that the stress at a material point depends on the [[deformation gradient|HTYRR2WDQ6]] relative to a fixed natural shape.
It does not depend only on the rate of deformation.

## Remarks

An elastic material, whose Cauchy stress is a function $\hat\sigma(F)$ of the deformation gradient $F$, is a solid in this sense.
Its stress records how far the body is from its reference shape.
An ideal fluid, whose stress $-p I$ depends only on the density, is not a solid: it has no preferred shape, and any volume-preserving rearrangement leaves its stress unchanged.
The line between solids and fluids is blurred for viscoelastic materials, which show both behaviours on different time scales.

## Explanations

### L1 human

Solid mechanics studies things that keep a shape: beams, shells, bones, rocks.
The key feature is that the internal forces in a solid depend on how much it has been deformed from its natural state.
