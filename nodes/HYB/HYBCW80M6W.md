---
tag: HYBCW80M6W
kind: definition
name: Heat capacity ratio
msc: [80A10, 76N15]
defines: NA1VVMJXVA
uses: [SYYGZ18FF5, N7R0H2VNDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_capacity_ratio
---

## Definition

Let a system have [[heat capacity|SYYGZ18FF5]] $C_p$ at constant pressure and $C_V$ at constant volume, with $C_V > 0$.
The *heat capacity ratio*, or *adiabatic index*, of the system is
$$\gamma = \frac{C_p}{C_V}.$$

## Remarks

Since both heat capacities are extensive, $\gamma$ is intensive, and it equals the ratio of the molar or of the specific heat capacities.

Example: for a monatomic [[ideal gas|N7R0H2VNDJ]], $C_V = \tfrac{3}{2} nR$ and $C_p = \tfrac{5}{2} nR$, so $\gamma = 5/3$.
For a diatomic ideal gas near room temperature, $C_V = \tfrac{5}{2} nR$ and $C_p = \tfrac{7}{2} nR$, so $\gamma = 7/5$.

Non-example: a pure substance at a first-order phase transition, such as water boiling at fixed pressure, absorbs heat without a change of temperature.
There $C_p$ is not a finite number, so $\gamma$ is not defined.

For an ideal gas with constant $\gamma$, a reversible adiabatic process satisfies $pV^\gamma = \text{const}$ and $TV^{\gamma - 1} = \text{const}$.
For every stable system $C_p \ge C_V$, so $\gamma \ge 1$.
