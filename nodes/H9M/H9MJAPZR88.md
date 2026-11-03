---
tag: H9MJAPZR88
kind: definition
name: Optical fiber modes
msc: [78A50, 78A40]
defines: QXJDCZGXGC
uses: [EWHJ19ND64, YFNRB1JNY3, 9VGK0SP6EQ, GS6CP71X4K, CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_fiber
---

## Definition

Let $r$ be the distance to the $z$-axis, and let $a > 0$ and $n_1 > n_2 > 0$.
A *step-index fiber* is a [[waveguide|EWHJ19ND64]] with [[refractive index|9VGK0SP6EQ]] $n(r) = n_1$ for $r < a$ (the core) and $n(r) = n_2$ for $r > a$ (the cladding).
Let $k_0 = \omega / c$ be the vacuum wavenumber of the light.
A *mode* of the fiber is a guided mode of this waveguide, that is, a field $(\mathbf{e}, \mathbf{h})(r, \varphi) \, e^{i(\beta z - \omega t)}$ solving the source-free Maxwell equations with square-integrable cross-section.
For a guided mode, $n_2 k_0 < \beta < n_1 k_0$.
The *normalized frequency* of the fiber is
$$V = k_0 a \sqrt{n_1^2 - n_2^2}.$$

## Remarks

Write $u = a\sqrt{n_1^2 k_0^2 - \beta^2}$ and $w = a\sqrt{\beta^2 - n_2^2 k_0^2}$, so that $u^2 + w^2 = V^2$.
The axial fields are proportional to $J_l(u r/a) e^{il\varphi}$ in the core and to $K_l(w r/a) e^{il\varphi}$ in the cladding.
Here $J_l$ is the [[Bessel function of the first kind|CZCMRDWDYW]] and $K_l$ the modified Bessel function of the second kind.
Matching the tangential fields at $r = a$ gives an equation for $\beta$.
Example: the fundamental $\mathrm{HE}_{11}$ mode exists for every $V > 0$, and it is the only guided mode when $V < 2.405$, the first zero of $J_0$.
A fiber with $a = 4\ \mu$m, $n_1 = 1.450$, $n_2 = 1.445$ at wavelength $1.55\ \mu$m has $V \approx 1.95$, so it is single-mode.
Non-example: a field with $\beta < n_2 k_0$ oscillates in the cladding instead of decaying, so it radiates away and is not a guided mode.
In the ray picture, guided modes correspond to rays that meet the core boundary beyond the critical angle of [[total internal reflection|GS6CP71X4K]].
