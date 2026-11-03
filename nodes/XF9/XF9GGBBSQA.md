---
tag: XF9GGBBSQA
kind: definition
name: Elastic metamaterial
msc: [74Q10, 74J05, "74E30"]
defines: QAQM7B6DAY
uses: [VSBFY8EN2H, T1PYEBKBAJ, 4F812GHFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Acoustic_metamaterial
---

## Definition

An *elastic metamaterial* is a solid composite with a periodic or regular microstructure of cell size $\ell$ such that:

1. For waves of wavelength much larger than $\ell$, the material behaves like a homogeneous medium.
   Its effective mass density $\rho_{\mathrm{eff}}(\omega)$ and moduli $C_{\mathrm{eff}}(\omega)$ depend on the frequency $\omega$.
2. In some frequency band these effective quantities take values that no constituent has, typically $\rho_{\mathrm{eff}}(\omega) < 0$ or an effective modulus below $0$.

## Remarks

Example: the mass-in-mass cell has an outer mass $m_1$ and an inner mass $m_2$ attached to it by a spring of stiffness $k_2$.
Let $\omega_0 = \sqrt{k_2/m_2}$.
If the outer mass moves as $x_1 e^{i\omega t}$, the inner mass moves as $x_2 e^{i\omega t}$ with $x_2 = k_2 x_1 / (k_2 - m_2 \omega^2)$.
The total force on the cell is $-\omega^2 (m_1 x_1 + m_2 x_2) = -\omega^2 m_{\mathrm{eff}} x_1$ with
$$m_{\mathrm{eff}}(\omega) = m_1 + \frac{m_2 \omega_0^2}{\omega_0^2 - \omega^2}.$$
This is negative exactly for $\omega_0 < \omega < \omega_0 \sqrt{1 + m_2/m_1}$, and a chain of such cells has a band gap there.

Non-example: in the long-wavelength limit, a laminate of two ordinary elastic layers has positive effective density and moduli.
They are averages of the positive constants of the layers, so clause 2 fails.

The effective constants of clause 1 come from [[effective medium approximations|VSBFY8EN2H]] or from dynamic homogenization.
The negative band is caused by the [[resonance|4F812GHFZK]] of the inner mass.
