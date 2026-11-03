---
tag: 5G1DWA9DVY
kind: definition
name: Rheology
msc: [76A05, 76A10]
defines: EF27XBPW3N
uses: [P1KWMQG4NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Rheology
---

## Definition

Consider a continuous body whose internal forces are described by the Cauchy stress tensor $\sigma$ at each point and time.
A *constitutive equation* (or rheological equation of state) of a material is a relation of the following kind.
It determines $\sigma$ at a material point from the history of the deformation of the material up to the present time.
*Rheology* is the study of the deformation and flow of materials through their constitutive equations: their form, their measurement, and their consequences for flows.

## Remarks

Example: the Newtonian fluid law $\sigma = -p I + 2 \mu D$, where $D$ is the [[strain rate tensor|P1KWMQG4NZ]] and $\mu$ is a constant, is a constitutive equation.
It uses only the present value of the deformation rate.
The [[upper-convected Maxwell model|VN6MY7KWJ8]] is a constitutive equation in which the stress depends on the whole past of the deformation.

Non-example: the balance of momentum $\rho \, Du/Dt = \nabla \cdot \sigma + f$ is not a constitutive equation.
It holds for every continuous material and says nothing about how $\sigma$ depends on the deformation.

The word is mostly used for materials that are neither ideal elastic solids nor Newtonian fluids.
