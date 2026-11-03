---
tag: SDGE1W5JS4
kind: definition
name: Phase transition
msc: [82B26, 80A22, 80A10]
defines: 6WJ0NADBT4
uses: [5EKTEE00FZ, H9F9CNPBSN, RBG5ZBM35Y, WVH4PVW64P]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_transition
---

## Definition

Consider a substance in [[thermodynamic equilibrium|5EKTEE00FZ]], controlled by [[intensive variables|H9F9CNPBSN]] such as the temperature $T$ and the pressure $p$.
Let $g(T, p)$ be its equilibrium molar [[Gibbs free energy|RBG5ZBM35Y]], which for a pure substance is its [[chemical potential|WVH4PVW64P]].
A *phase* is a connected open region of the $(T, p)$ plane on which $g$ is real-analytic.
It must be maximal with this property.
A *phase transition* is the change from one phase to another as the control variables cross a point where $g$ is not analytic.

## Remarks

Water at the pressure $101.325\,\mathrm{kPa}$ boils at $T_b \approx 373.15\,\mathrm{K}$.
At $T_b$ the function $g$ is continuous, but its derivative $\partial g/\partial T = -s$, minus the molar entropy, jumps, so $g$ is not analytic there and boiling is a phase transition.
A non-example: one can go from liquid water to vapour along a path that passes above the critical point.
On that path $g$ stays analytic, so no phase transition takes place, although the start and the end look very different.
In statistical mechanics, sharp non-analytic points of the free energy occur only in the thermodynamic limit of infinitely many particles.
The same idea applies with other control variables, such as a magnetic field.
