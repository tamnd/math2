---
tag: VXVGVDSJ0W
kind: statement
role: fact
name: Ideal gas law
msc: [80A10, 82D05]
uses: [N7R0H2VNDJ, YPT3SJSS5T, AJ8M9MGZGF, QMJ04KSQ59, X576BQTPQ5]
about: [N7R0H2VNDJ, YPT3SJSS5T]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_gas_law
same_as:
  wikidata: Q191785
  wikipedia: Ideal gas law
---

## Statement

Let $n$ moles of a gas be in equilibrium at pressure $p$, volume $V$ and [[thermodynamic temperature|AJ8M9MGZGF]] $T$.
Then, in the limit of low density $n/V \to 0$ at fixed $T$,
$$\frac{pV}{nRT} \to 1,$$
where $R \approx 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$ is the molar gas constant, the same for all gases.
So a dilute gas obeys approximately the [[equation of state|YPT3SJSS5T]] $pV = nRT$, and an [[ideal gas|N7R0H2VNDJ]] obeys it exactly.

## Remarks

The law combines three older laws.
Boyle's law says that $pV$ is constant at fixed $T$ and $n$.
Charles's law says that $V$ is proportional to $T$ at fixed $p$ and $n$, and Avogadro's law that $V$ is proportional to $n$ at fixed $p$ and $T$.
In kinetic theory it is derived for non-interacting point particles.
The pressure is the momentum given to the walls per unit area and time, which gives $pV = \tfrac{2}{3} N \langle E_{\mathrm{kin}} \rangle$.
The average kinetic energy is $\tfrac{3}{2} kT$, so $pV = NkT$ with $R = N_A k$.
Example: one mole at $T = 273.15\,\mathrm{K}$ and $p = 101\,325\,\mathrm{Pa}$ has $V = RT/p \approx 0.0224\,\mathrm{m^3}$.
The low-density hypothesis is needed: at high pressure, or near condensation, the attraction and the size of molecules give large deviations, measured by the compressibility factor $Z = pV/(nRT) \ne 1$.

## Explanations

### L1 human

For a gas that is not too dense, pressure times volume is proportional to the amount of gas times the temperature.
The constant of proportionality is the same for every gas.
So doubling the temperature at fixed volume doubles the pressure, and doubling the amount of gas at fixed pressure doubles the volume.

### L2 human

The ideal gas law is the simplest equation of state.
Most of the elementary thermodynamics of gases, such as work in isothermal processes and Mayer's relation, is computed with it.
The fact that $pV/n$ tends to a common limit for all gases is also the basis of the gas thermometer, which realises the thermodynamic temperature scale.
Corrections for real gases come from the [[virial expansion|QMJ04KSQ59]] $pV_m/(RT) = 1 + B(T)/V_m + \cdots$ or from model equations such as the [[van der Waals equation|X576BQTPQ5]].
