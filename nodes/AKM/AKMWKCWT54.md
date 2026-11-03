---
tag: AKMWKCWT54
kind: definition
name: Self-focusing
msc: [78A60, 35Q55]
defines: A68PFZJ3ZW
uses: [Y7WQY4568B, 9VGK0SP6EQ, BRJ36NF7KX]
sources:
  - url: https://en.wikipedia.org/wiki/Self-focusing
---

## Definition

Let a beam of light of intensity profile $I(\mathbf{x})$ propagate in a medium with the optical [[Kerr effect|Y7WQY4568B]].
So the [[refractive index|9VGK0SP6EQ]] is $n = n_0 + n_2 I$, and assume $n_2 > 0$.
*Self-focusing* is the contraction of the beam caused by the larger index where the intensity is larger.
The *critical power* $P_{\mathrm{cr}}$ is the power at which this effect exactly balances diffraction.
It is proportional to $\lambda^2 / (n_0 n_2)$, where $\lambda$ is the vacuum wavelength, with a factor that depends on the beam profile.

## Remarks

In the paraxial model the beam envelope obeys the two-dimensional cubic focusing [[nonlinear Schrödinger equation in optics|BRJ36NF7KX]], and the beam power is its conserved $L^2$ norm.
For this equation, Weinstein proved that solutions whose $L^2$ norm is smaller than that of the ground state exist for all distances.
For larger norms, some solutions blow up at a finite distance.
In real media other effects, such as plasma formation or higher-order nonlinearity, stop the collapse.

Example: a Gaussian beam in a medium with $n_2 > 0$ and power well above $P_{\mathrm{cr}}$ narrows as it propagates.

Non-example: in a medium with $n_2 < 0$, the index is lower at the centre of the beam, and the beam spreads faster than by diffraction alone; this is self-defocusing.
