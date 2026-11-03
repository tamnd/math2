---
tag: 7MR97B1NER
kind: statement
role: proposition
name: Raoult's law
msc: [80A50, 80A10]
uses: [WVH4PVW64P, N7R0H2VNDJ, 5EKTEE00FZ]
about: [WVH4PVW64P]
sources:
  - url: https://en.wikipedia.org/wiki/Raoult%27s_law
same_as:
  wikidata: Q241687
  wikipedia: Raoult's law
---

## Statement

Consider a liquid mixture of components $1, \dots, k$ in [[thermodynamic equilibrium|5EKTEE00FZ]] with its vapour at temperature $T$.
Let $x_i$ be the mole fraction of component $i$ in the liquid.
Assume that the liquid is an ideal solution: the [[chemical potential|WVH4PVW64P]] of each component is $\mu_i^{\text{liq}} = \mu_i^{*}(T) + RT \ln x_i$.
Here $\mu_i^{*}(T)$ is the chemical potential of the pure liquid $i$, and its dependence on pressure is neglected.
Assume also that the vapour is a mixture of [[ideal gases|N7R0H2VNDJ]].
Then the partial pressure of each component in the vapour is
$$p_i = x_i\, p_i^{*},$$
where $p_i^{*}$ is the vapour pressure of the pure component $i$ at $T$.
In particular the total vapour pressure is $p = \sum_i x_i p_i^{*}$.

## Remarks

For an ideal gas, $\mu_i^{\text{gas}} = \mu_i^{\circ}(T) + RT \ln(p_i/p^\circ)$ with a reference pressure $p^\circ$.
Equality of chemical potentials for the mixture, and again for the pure liquid with $x_i = 1$ and $p_i = p_i^*$, gives $RT\ln x_i = RT \ln(p_i/p_i^*)$, which is the law.
Mixtures of similar molecules, such as benzene and toluene, follow it closely.
Without the ideal solution hypothesis the law fails: ethanol and water deviate strongly from it and form an azeotrope.
For any real solution, the solvent still obeys the law in the limit of small solute fractions.

## Explanations

### L1 human

Raoult's law says that each liquid in a mixture evaporates in proportion to how much of it is there.
If a liquid makes up half of the mixture, its vapour pressure is half of what it would be on its own.
This is why dissolving a non-volatile substance such as salt in water lowers the vapour pressure of the water and raises its boiling point.

### L2 human

The law is the defining behaviour of an ideal solution, and real solutions are described by how far they deviate from it, through activity coefficients.
It is the basis of the simplest models of distillation: the vapour is richer in the more volatile component, so repeated evaporation separates the two.
For a dilute solute the companion law is [[Henry's law|A5VFJ0X9KH]], which has the same linear form but a different constant.
