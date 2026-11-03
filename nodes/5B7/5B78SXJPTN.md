---
tag: 5B78SXJPTN
kind: definition
name: Negative refraction
msc: [78A48, 78A10]
defines: 8EW2R66GXS
uses: [9VGK0SP6EQ, F768YN0P2V, 5MJQ5J5H8Z, QDV9SBK6W0, P3PK0Q02CZ, CQ9A45JF68]
sources:
  - url: https://en.wikipedia.org/wiki/Negative_refraction
---

## Definition

Let a plane wave pass through a flat interface from a medium of [[refractive index|9VGK0SP6EQ]] $n_1 > 0$ into a second medium.
Let the second medium have relative [[permittivity|F768YN0P2V]] $\varepsilon_2$ and relative [[permeability|5MJQ5J5H8Z]] $\mu_2$.
If $\varepsilon_2 < 0$ and $\mu_2 < 0$, the refractive index of the second medium is $n_2 = -\sqrt{\varepsilon_2 \mu_2} < 0$.
The angles of incidence $\theta_1$ and of refraction $\theta_2$, measured from the normal and signed by the side, obey [[Snell's law|QDV9SBK6W0]] $n_1 \sin\theta_1 = n_2 \sin\theta_2$.
*Negative refraction* is the case $\theta_2 < 0$ for $\theta_1 > 0$.
Then the refracted ray, the direction of the [[Poynting vector|P3PK0Q02CZ]], lies on the same side of the normal as the incident ray.

## Remarks

In a medium with $\varepsilon < 0$ and $\mu < 0$, the vectors $\mathbf{E}$, $\mathbf{H}$, $\mathbf{k}$ form a left-handed triple, so the wave vector points against the Poynting vector.
The choice of the negative square root for $n_2$ follows from this and from causality.

Example: with $n_1 = 1$, $\varepsilon_2 = \mu_2 = -1$ and $\theta_1 = 30^\circ$, one gets $n_2 = -1$ and $\sin\theta_2 = -1/2$, so $\theta_2 = -30^\circ$.
The refracted ray is the mirror image of the continued incident ray in the normal.

Non-example: a medium with $\varepsilon_2 < 0$ and $\mu_2 > 0$, such as a metal below its plasma frequency, has imaginary index and supports no propagating wave.
It fails the condition that both parameters are negative.

Such media are made as [[metamaterials|CQ9A45JF68]].
