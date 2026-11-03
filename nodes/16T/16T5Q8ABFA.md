---
tag: 16T5Q8ABFA
kind: definition
name: Fracture toughness
msc: [74R10, 74A45]
defines: BQ0AMNFJRA
uses: [8D619PN75J, H1J9Q4TVJ6, JQT1GBRYTY]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_toughness
---

## Definition

Let a material be tested with cracked specimens loaded in mode I of the [[modes of fracture|H1J9Q4TVJ6]].
Assume [[plane strain|JQT1GBRYTY]] conditions at the crack front.
Assume also that the plastic zone is small compared with the crack length and the specimen dimensions.
The *plane-strain fracture toughness* $K_{Ic}$ is the value of the [[stress intensity factor|8D619PN75J]] $K_I$ at which the crack starts to grow.
More generally, the *fracture toughness* is the critical value of a crack-tip parameter at the onset of crack growth.
Such parameters are $K$, the energy release rate $G$, the J-integral and the crack tip opening displacement.

## Remarks

Example: if a steel has $K_{Ic} = 50 \, \mathrm{MPa}\sqrt{\mathrm{m}}$, a through crack of length $2a = 2 \, \mathrm{cm}$ in a wide plate grows at the remote stress $\sigma = K_{Ic} / \sqrt{\pi a} = 50 / \sqrt{0.01 \pi} \approx 282 \, \mathrm{MPa}$.
Non-example: the tensile strength of a material is not a fracture toughness.
It is a critical stress measured on an uncracked specimen, and it does not involve a crack.
For a linear elastic isotropic material with Young's modulus $E$ and Poisson's ratio $\nu$, the critical energy release rate is $G_{Ic} = K_{Ic}^2 (1 - \nu^2) / E$.
Thin specimens, which are closer to plane stress, show a larger apparent toughness, which is why the plane-strain value is the reference.

## Explanations

### L1 human

Fracture toughness is the stress intensity at the crack tip that the material can just withstand before the crack grows.
