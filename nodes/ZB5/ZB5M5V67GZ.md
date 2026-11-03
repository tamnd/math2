---
tag: ZB5M5V67GZ
kind: definition
name: Skin effect
msc: [78A25, 78A40]
defines: CH34Y1DWT4
uses: [9BWWD4QK8Y, 5MJQ5J5H8Z, F768YN0P2V]
sources:
  - url: https://en.wikipedia.org/wiki/Skin_effect
---

## Definition

Let a homogeneous conductor fill the half-space $z > 0$.
Let it have conductivity $\sigma > 0$, [[permeability|5MJQ5J5H8Z]] $\mu$ and [[permittivity|F768YN0P2V]] $\varepsilon$, and obey Ohm's law $\mathbf{J} = \sigma \mathbf{E}$.
Consider time-harmonic fields with angular frequency $\omega > 0$ and time factor $e^{-i\omega t}$, in the good-conductor regime $\sigma \gg \omega \varepsilon$.
The *skin depth* is
$$\delta = \sqrt{\frac{2}{\omega \mu \sigma}}.$$
In this regime [[Maxwell's equations|9BWWD4QK8Y]] reduce to $\nabla^2 \mathbf{E} = -i \omega \mu \sigma \mathbf{E}$.
The *skin effect* is the form of its bounded solutions that depend only on $z$:
$$\mathbf{E}(z) = \mathbf{E}_0 \, e^{i z/\delta} \, e^{-z/\delta}.$$
So the field and the current density $\mathbf{J} = \sigma \mathbf{E}$ fall by the factor $e$ over each skin depth into the conductor.

## Remarks

The decay rate comes from $k^2 = i \omega \mu \sigma$, whose root with positive imaginary part is $k = (1 + i)/\delta$.
Example: for copper, $\sigma \approx 5.96 \times 10^7$ S/m and $\mu \approx \mu_0 = 4\pi \times 10^{-7}$ H/m.
At $60$ Hz, $\omega \mu \sigma \approx 2.8 \times 10^4 \ \text{m}^{-2}$, so $\delta \approx 8.4$ mm.
Non-example: a lossless dielectric has $\sigma = 0$, so the good-conductor condition fails, and a plane wave enters it without decay.
The skin depth also gives the surface resistance $R_s = 1/(\sigma \delta)$ of the conductor.
