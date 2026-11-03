---
tag: 474JPPF2XS
kind: definition
name: Gamow factor
msc: [85A15, 81V35]
defines: 49W4RZYEA3
uses: [3QSVWQJX11]
sources:
  - url: https://en.wikipedia.org/wiki/Gamow_factor
---

## Definition

Consider two nuclei with charge numbers $Z_a, Z_b \ge 1$ and reduced mass $m_r$, colliding with energy $E > 0$ in their centre-of-mass frame.
Let $\alpha$ be the fine-structure constant and $c$ the speed of light.
The *Gamow energy* of the pair is
$$E_G = 2 m_r c^2 \left( \pi \alpha Z_a Z_b \right)^2,$$
and the *Gamow factor* at energy $E$ is
$$P_G(E) = \exp\left( -\sqrt{\frac{E_G}{E}} \right).$$

## Remarks

The Gamow factor approximates the probability of tunnelling through the Coulomb barrier when $E$ is much smaller than the height of the barrier.
With the relative speed $v$ and $E = m_r v^2 / 2$, it equals $e^{-2 \pi \eta}$, where $\eta = Z_a Z_b \alpha c / v$ is the Sommerfeld parameter; indeed $(2 \pi \eta)^2 = 2 m_r c^2 (\pi \alpha Z_a Z_b)^2 / E$.
Example: for two protons, $m_r$ is half the proton mass, so $m_r c^2 \approx 469 \, \mathrm{MeV}$ and $E_G \approx 2 \cdot 469 \cdot (\pi / 137)^2 \, \mathrm{MeV} \approx 0.49 \, \mathrm{MeV}$; at $E = 1.3 \, \mathrm{keV}$, typical in the core of the Sun, $P_G \approx e^{-19.5}$, about $3.5 \times 10^{-9}$.
Non-example: a neutron and a nucleus have $Z_a Z_b = 0$, which the definition excludes; there is no Coulomb barrier, and no Gamow factor applies.
Multiplied by the Maxwell–Boltzmann weight $e^{-E / (k_B T)}$, the Gamow factor gives the Gamow peak, whose maximum lies at $E_0 = (E_G (k_B T)^2 / 4)^{1/3}$.
