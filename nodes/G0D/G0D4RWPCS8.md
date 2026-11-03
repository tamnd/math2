---
tag: G0D4RWPCS8
kind: definition
name: Representative elementary volume
msc: [74Q05, 74A60, "74E30"]
defines: ZMZY201H89
uses: [5RSREPYN0F]
sources:
  - url: https://en.wikipedia.org/wiki/Representative_elementary_volume
---

## Definition

Let a heterogeneous material have a microstructure with characteristic length $\ell$, such as the size of its grains.
Let $L$ be the length on which the body or the applied loads vary.
For a region $V$ of the material and a field $g$, write $\langle g \rangle_V = \frac{1}{\abs{V}} \int_V g \, dx$.
A region $V$ of diameter $D$ is a *representative elementary volume* (RVE) for a property $P$ when:

1. $\ell \ll D \ll L$;
2. the apparent value of $P$ computed on $V$ changes by less than a prescribed tolerance when $V$ is moved or enlarged;
3. this apparent value changes by less than the same tolerance when the affine, uniform-traction or periodic boundary conditions on $V$ are exchanged.

## Remarks

Example: for a periodic composite, a single period cell with periodic boundary conditions gives the exact homogenized tensor of [[homogenization|5RSREPYN0F]], so it is an RVE for every linear property.
Non-example: for a polycrystal, a cube containing three grains violates clause 2, since its apparent stiffness depends strongly on the orientations of those three grains.
For a random material the definition depends on the property and on the tolerance; a larger volume is usually needed for nonlinear properties than for the elastic moduli.
For an elastic modulus, the apparent value is computed from the averages $\langle \sigma \rangle_V$ and $\langle \varepsilon \rangle_V$.
The [[Hill–Mandel condition|AS9YN2169W]] links the averages of stress and strain on an RVE to the macroscopic energy.

## Explanations

### L1 human

An RVE is a piece of material big enough to contain a fair sample of its microstructure.
Testing it gives the same answer wherever it is cut and however it is held.
