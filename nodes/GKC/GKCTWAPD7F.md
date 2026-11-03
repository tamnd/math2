---
tag: GKCTWAPD7F
kind: statement
role: proposition
name: Mayer's relation
msc: [80A10]
uses: [SYYGZ18FF5, N7R0H2VNDJ, 722RZK72P5, F6JVQ12X43]
about: [SYYGZ18FF5, N7R0H2VNDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mayer's_relation
same_as:
  wikidata: Q6104964
  wikipedia: Mayer's relation
---

## Statement

Let a fixed amount of $n$ moles of an [[ideal gas|N7R0H2VNDJ]] have [[heat capacities|SYYGZ18FF5]] $C_p$ at constant pressure and $C_V$ at constant volume.
Let $R$ be the molar gas constant.
Then
$$C_p - C_V = nR.$$

## Remarks

For an ideal gas the [[internal energy|F6JVQ12X43]] $U$ depends only on the temperature $T$, and $pV = nRT$.
So the [[enthalpy|722RZK72P5]] $H = U + pV = U(T) + nRT$ also depends only on $T$.
Differentiating gives $C_p = dH/dT = dU/dT + nR = C_V + nR$.
For a monatomic ideal gas, $C_V = \tfrac{3}{2} nR$ and $C_p = \tfrac{5}{2} nR$, and their difference is $nR$.
For an arbitrary simple system the general identity is $C_p - C_V = T V \alpha^2 / \kappa_T$.
Here $\alpha$ is the thermal expansion coefficient and $\kappa_T$ the isothermal compressibility.
For an ideal gas $\alpha = 1/T$ and $\kappa_T = 1/p$, which gives back $nR$.
The relation fails for real gases, where $U$ depends also on the volume.

## Explanations

### L1 human

Heating a gas at constant pressure takes more heat than heating it in a closed rigid box.
At constant pressure the gas expands and pushes on its surroundings, and this work also costs energy.
Mayer's relation says that for an ideal gas this extra cost is exactly $R$ per mole and per degree.

### L2 human

The relation is the first place where the two heat capacities are compared, and it uses both the equation of state and the fact that $U$ depends only on $T$.
Together with the heat capacity ratio $\gamma = C_p / C_V$ it gives $C_V = nR/(\gamma - 1)$ and $C_p = \gamma nR/(\gamma - 1)$.
Historically it allowed Mayer to estimate the mechanical equivalent of heat from gas data.
The general form $C_p - C_V = TV\alpha^2/\kappa_T$ is derived from the Maxwell relations and shows $C_p \ge C_V$ for every stable system.
