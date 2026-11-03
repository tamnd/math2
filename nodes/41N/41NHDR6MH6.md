---
tag: 41NHDR6MH6
kind: statement
role: proposition
name: Fundamental thermodynamic relation
msc: [80A10, 80A05]
uses: [F6JVQ12X43, SPY89W0RJ7, AJ8M9MGZGF, F3DHZ45H6A, V14W2V4JSR, T11MGWEKJ3]
about: [F6JVQ12X43, SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_thermodynamic_relation
same_as:
  wikidata: Q1474109
  wikipedia: Fundamental thermodynamic relation
---

## Statement

Let a closed simple system, such as a fluid of fixed composition, pass between two neighbouring equilibrium states.
Let $U$ be its [[internal energy|F6JVQ12X43]], $S$ its [[entropy|SPY89W0RJ7]], $T$ its [[thermodynamic temperature|AJ8M9MGZGF]], $p$ its pressure and $V$ its volume.
Then
$$dU = T \, dS - p \, dV.$$
If the amounts $N_1, \dots, N_r$ of the substances may also change, then $dU = T \, dS - p \, dV + \sum_{i=1}^{r} \mu_i \, dN_i$, where $\mu_i$ is the chemical potential of substance $i$.

## Remarks

For a [[reversible|F3DHZ45H6A]] change, the [[second law|T11MGWEKJ3]] gives $\delta Q = T \, dS$ and the work done by the fluid is $\delta W = p \, dV$.
The [[first law|V14W2V4JSR]] $dU = \delta Q - \delta W$ then gives the relation.
Since every term involves only state functions, the relation holds for any change between the two equilibrium states, reversible or not.
For an irreversible change, though, $T \, dS$ is no longer the heat and $p \, dV$ is no longer the work.
Equivalently, $T = (\partial U / \partial S)_V$ and $p = -(\partial U / \partial V)_S$.
Example: for an ideal gas at constant temperature, $dU = 0$, so $dS = p \, dV / T = nR \, dV / V$ and $\Delta S = nR \ln(V_2 / V_1)$.

## Explanations

### L1 human

The relation says how the energy of a system changes when its entropy and volume change.
Adding entropy at temperature $T$ adds energy $T \, dS$, and letting the system expand against pressure $p$ removes energy $p \, dV$.

### L2 human

The fundamental relation is the master equation of equilibrium thermodynamics.
It shows that $U$ is a thermodynamic potential with natural variables $S$ and $V$.
Legendre transforms of $U$ give the enthalpy, the Helmholtz free energy and the Gibbs free energy, with analogous differentials.
The equality of mixed second derivatives of these potentials gives the Maxwell relations.
