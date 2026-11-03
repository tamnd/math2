---
tag: DDK9QN9KX5
kind: definition
name: Cosmological redshift
msc: ["83F05"]
defines: 8K69WPX4GS
uses: [ECJMS4VDTF, J70F32P86W]
sources:
  - url: https://en.wikipedia.org/wiki/Redshift
    locator: Expansion of space
---

## Definition

Let $g = -dt^2 + a(t)^2 \gamma_k$ be a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] with [[scale factor|J70F32P86W]] $a$, and use units with $c = 1$.
Let light be emitted by a comoving source at time $t_e$ and received by a comoving observer at time $t_o > t_e$.
The *cosmological redshift* of the source is the number $z$ defined by
$$1 + z = \frac{a(t_o)}{a(t_e)}.$$

## Remarks

The definition agrees with the spectroscopic redshift $z = (\lambda_o - \lambda_e)/\lambda_e$, where $\lambda_e$ and $\lambda_o$ are the emitted and observed wavelengths.
Indeed, a radial light ray satisfies $d\chi/dt = 1/a(t)$, so two crests that leave the source $\delta t_e$ apart arrive $\delta t_o$ apart with $\delta t_e / a(t_e) = \delta t_o / a(t_o)$.
Example: if $a(t_o) = 3\, a(t_e)$, then $z = 2$ and every wavelength has tripled.
Non-example: a source moving with respect to the comoving frame has an extra Doppler shift, so its measured redshift is not given by the formula alone.
In an expanding model $z > 0$; for nearby sources $z \approx H(t_o)\, D$ to first order, where $D$ is the proper distance and $H = \dot a / a$.
