---
tag: DG4ZP6XWDB
kind: definition
name: Thermodynamic temperature
msc: [80A05, 80A10]
defines: AJ8M9MGZGF
uses: [KK46Q2YV1D, CY4GJQGF06, F3DHZ45H6A, AGRGCDWQF8]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_temperature
---

## Definition

Let $\theta$ be an empirical [[temperature|KK46Q2YV1D]].
Let two heat reservoirs have empirical temperatures $\theta_1 > \theta_2$.
Consider a [[reversible|F3DHZ45H6A]] [[cycle|AGRGCDWQF8]] that exchanges heat only with these two reservoirs.
Let it absorb [[heat|CY4GJQGF06]] $Q_1 > 0$ from the first reservoir and give heat $Q_2 > 0$ to the second.
By the second law, $Q_1 / Q_2 = \varphi(\theta_1) / \varphi(\theta_2)$ for a positive function $\varphi$ that does not depend on the cycle.
The *thermodynamic temperature* is $T = c \, \varphi(\theta)$, where the constant $c > 0$ fixes the unit.

## Remarks

So $T$ is defined by the rule $T_1 / T_2 = Q_1 / Q_2$ for reversible cycles between two reservoirs.
The unit is the kelvin; since 2019 the kelvin is fixed by setting the Boltzmann constant to $1.380649 \times 10^{-23}$ joule per kelvin.
For an ideal gas, $T$ agrees with the ideal-gas temperature $pV/(nR)$.
The Celsius scale is not a thermodynamic temperature in this sense: $t_1 / t_2$ is not the heat ratio, and $t$ can be negative.
For a system with internal energy $U$ and entropy $S$, one has $T = (\partial U / \partial S)_{V, N}$.
