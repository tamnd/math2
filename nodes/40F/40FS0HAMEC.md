---
tag: 40FS0HAMEC
kind: definition
name: Optical activity
msc: [78A10]
defines: 6037NA1P98
uses: [PJ8ZSJ0QDW, 9VGK0SP6EQ, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_rotation
---

## Definition

Let a linear transparent medium be given, and consider monochromatic [[plane waves|NM024G378A]] of vacuum wavelength $\lambda$ that travel in a fixed direction through it.
The medium is *optically active* in that direction when, without any external magnetic field, the two circular [[polarizations|PJ8ZSJ0QDW]] are modes.
These modes must have different [[refractive indices|9VGK0SP6EQ]] $n_L \ne n_R$.
The *optical rotation* over a path of length $d$ is the angle $\theta = \pi d (n_L - n_R) / \lambda$.
It is the angle by which the direction of a linear polarization turns, with a sign convention for the sense of rotation.

## Remarks

Write linear polarization as the sum of the two circular states with equal amplitudes.
After the path $d$ their phases differ by $2\pi d (n_L - n_R)/\lambda$, and the direction of the resulting linear polarization turns by half of this, which gives $\theta$.

Example: a solution of sucrose in water is optically active.
For solutions, the rotation is proportional to the path length and to the concentration, and the factor is the specific rotation of the substance.

Non-example: pure water is not optically active, since its molecules are not chiral and both circular states see the same index.

Optical activity is reciprocal: if light passes through the medium, is reflected and comes back, the two rotations cancel.
This distinguishes it from the Faraday effect, where the rotations add.
