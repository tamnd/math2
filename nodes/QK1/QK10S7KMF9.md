---
tag: QK10S7KMF9
kind: statement
role: fact
name: Kramers' opacity law
msc: [85A25, 85A15]
uses: [4ZVBZ1SZF7, SBKFDNEMFF]
about: [4ZVBZ1SZF7]
sources:
  - url: https://en.wikipedia.org/wiki/Kramers%27_opacity_law
same_as:
  wikidata: Q17007596
  wikipedia: Kramers' opacity law
---

## Statement

Consider a stellar interior where the opacity is dominated by free–free and bound–free absorption.
Let $\rho$ be the density and $T$ the temperature.
Then the [[Rosseland mean opacity|4ZVBZ1SZF7]] is approximately $\kappa \approx \kappa_0 \, \rho \, T^{-7/2}$, with $\kappa_0$ a constant that depends on the chemical composition.

## Remarks

The law comes from H. A. Kramers' semiclassical formula for the absorption cross-section of an electron passing an ion.
This formula is averaged over a Maxwellian distribution of electrons and over frequencies with the Rosseland weight.
The factor $\rho$ appears because absorption needs an electron and an ion, so it grows like the square of the density, and the opacity is per unit mass.
Example: if the temperature doubles at fixed density, the opacity drops by the factor $2^{7/2} \approx 11$.
The law fails at low temperature, where absorption by negative hydrogen ions and by molecules dominates.
It also fails at high temperature, where electron scattering dominates and the opacity becomes nearly independent of $\rho$ and $T$.
In the equations of [[stellar structure|SBKFDNEMFF]] it gives, together with the ideal gas law, a mass–luminosity scaling close to $L \propto M^{5.5} R^{-0.5}$.

## Explanations

### L1 human

Opacity measures how hard it is for light to get through the gas in a star.
Kramers' law says that hot gas is much more transparent than cooler gas, and dense gas is more opaque than thin gas.
Doubling the temperature makes the gas about eleven times more transparent.
This simple rule is enough to explain many features of stars of about the mass of the Sun.

### L2 human

Opacity enters the radiative temperature gradient, so it decides how steep the temperature profile must be and where convection sets in.
Power laws of the form $\kappa \propto \rho^a T^{-b}$ allow homologous solutions of the stellar structure equations, so that scalings between mass, radius and luminosity can be derived without solving them.
Detailed models use tables of opacities instead, but Kramers' law remains the reference case.
