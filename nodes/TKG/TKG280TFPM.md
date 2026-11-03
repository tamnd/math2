---
tag: TKG280TFPM
kind: definition
name: Kerr effect
msc: [78A60, 78A10]
defines: Y7WQY4568B
uses: [7N71T3FKZ6, 9VGK0SP6EQ, 8CWCYQJ44T]
sources:
  - url: https://en.wikipedia.org/wiki/Kerr_effect
---

## Definition

Let a transparent medium be isotropic in the absence of fields, with [[refractive index|9VGK0SP6EQ]] $n_0$ at vacuum wavelength $\lambda$.
1. The *electro-optic Kerr effect* is the [[birefringence|8CWCYQJ44T]] induced by an applied static electric field of strength $E$.
Light polarized parallel and perpendicular to the field sees indices that differ by $\Delta n = \lambda K E^2$.
Here $K$ is the *Kerr constant* of the medium.
2. The *optical Kerr effect* is the dependence of the index on the intensity $I$ of the light itself, $n = n_0 + n_2 I$.
Here $n_2$ is the *nonlinear index* of the medium.

## Remarks

Both effects come from the third-order [[nonlinear susceptibility|7N71T3FKZ6]] $\chi^{(3)}$.
For a linearly polarized monochromatic wave in an isotropic medium, with $I = \tfrac12 n_0 \varepsilon_0 c \abs{E}^2$, SI units give $n_2 = 3\chi^{(3)} / (4 n_0^2 \varepsilon_0 c)$, where $\chi^{(3)}$ is the relevant component.

Example: in silica glass $n_2$ is positive and small, of order $10^{-20}\ \mathrm{m^2/W}$.
Over many kilometres of optical fibre, this small index change still gives a large phase shift.

Non-example: the Pockels effect is a change of index linear in the applied field.
It is not a Kerr effect, and it needs a medium without a centre of inversion.
