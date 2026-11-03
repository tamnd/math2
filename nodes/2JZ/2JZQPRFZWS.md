---
tag: 2JZQPRFZWS
kind: statement
role: theorem
name: Saha ionization equation
msc: [85A15, 82D10]
uses: [3QSVWQJX11]
about: [3QSVWQJX11]
sources:
  - url: https://en.wikipedia.org/wiki/Saha_ionization_equation
same_as:
  wikidata: Q631222
  wikipedia: Saha ionization equation
---

## Statement

Consider a gas of atoms, ions and free electrons in thermal equilibrium at temperature $T$, treated as a mixture of ideal non-degenerate gases.
For $i \ge 0$, let $n_i$ be the number density of atoms that have lost $i$ electrons, and $g_i$ the statistical weight of their ground state.
Let $\chi_i$ be the energy needed to remove one more electron from such an atom.
Let $n_e$ be the number density of free electrons, $m_e$ the electron mass, $k_B$ the Boltzmann constant and $h$ the Planck constant, and set $\Lambda = h / \sqrt{2 \pi m_e k_B T}$.
If excited states are neglected, then
$$\frac{n_{i+1} \, n_e}{n_i} = \frac{2}{\Lambda^3} \, \frac{g_{i+1}}{g_i} \, \exp\left( -\frac{\chi_i}{k_B T} \right).$$

## Remarks

The proof applies the condition of chemical equilibrium $\mu_i = \mu_{i+1} + \mu_e$ for the reaction of ionization, with the chemical potential of each ideal gas from its [[Maxwell–Boltzmann distribution|3QSVWQJX11]].
The factor $2$ counts the two spin states of the electron, and $\Lambda$ is the thermal de Broglie wavelength of the electrons.
With excited states included, $g_i$ is replaced by the partition function of the ion.
Example: for pure hydrogen, with $\chi_0 = 13.6 \, \mathrm{eV}$, $g_0 = 2$ and $g_1 = 1$, writing $x$ for the fraction of ionized atoms and $n$ for the total density of hydrogen nuclei gives $x^2 / (1 - x) = \Lambda^{-3} n^{-1} e^{-\chi_0 / (k_B T)}$.
The equation needs non-degenerate electrons: at the densities of white dwarfs it fails, and pressure ionization takes over.

## Explanations

### L1 human

In a hot gas, collisions knock electrons off atoms, and electrons that meet ions recombine with them.
The Saha equation gives the balance between these two processes at a given temperature and density.
Heating ionizes the gas, and compressing it favours recombination.
Because the energy $\chi$ sits in an exponential, ionization switches on rather sharply in a narrow range of temperature.

### L2 human

The Saha equation explains the spectral sequence of stars.
The strength of the absorption lines of each element depends on how many of its atoms are in the right state of ionization, which is set by the surface temperature.
In stellar interiors it gives the ionization zones of hydrogen and helium, where the adiabatic gradient drops and convection is favoured.
In cosmology the same equation, for hydrogen, gives a first estimate of the time of recombination.
