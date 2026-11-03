---
tag: BC5FTFKAXN
kind: definition
name: Transverse mode
msc: [78A50, 78A60]
defines: 1T9MVT21YB
uses: [EWHJ19ND64, YFNRB1JNY3]
sources:
  - url: https://en.wikipedia.org/wiki/Transverse_mode
---

## Definition

Let a [[waveguide|EWHJ19ND64]] be invariant along the $z$-axis, and let $(\mathbf{E}, \mathbf{H}) = (\mathbf{e}(x, y), \mathbf{h}(x, y)) \, e^{i(\beta z - \omega t)}$ be a guided mode of it.
The mode is classified by its axial components $E_z$ and $H_z$:

1. a *TEM mode* (transverse electromagnetic) has $E_z = 0$ and $H_z = 0$;
2. a *TE mode* (transverse electric) has $E_z = 0$ and $H_z \neq 0$;
3. a *TM mode* (transverse magnetic) has $H_z = 0$ and $E_z \neq 0$;
4. a *hybrid mode* has $E_z \neq 0$ and $H_z \neq 0$.

The *transverse mode pattern* is the profile $(\mathbf{e}, \mathbf{h})$ in the cross-section.

## Remarks

In a hollow metal guide with homogeneous filling, every guided mode is a sum of TE and TM modes.
They are labelled $\mathrm{TE}_{mn}$ and $\mathrm{TM}_{mn}$, where the integers count the half-period variations across the cross-section.
Example: in a coaxial cable, the field with $\mathbf{E}$ radial, $\mathbf{H}$ azimuthal and $\beta = \omega\sqrt{\mu\varepsilon}$ is a TEM mode; it has no axial components.
Non-example: a hollow metal guide whose cross-section is simply connected has no TEM mode, because a transverse electrostatic potential that is constant on the single wall must vanish.
The modes of an optical fiber are in general hybrid; in the weakly guiding approximation they are grouped into linearly polarized $\mathrm{LP}_{lm}$ modes.
For laser beams in free space, the same word refers to the paraxial beam profiles, written $\mathrm{TEM}_{mn}$ for the [[Hermite–Gaussian modes|9NKZHQSC8A]].
