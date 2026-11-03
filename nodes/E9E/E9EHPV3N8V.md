---
tag: E9EHPV3N8V
kind: definition
name: Equation of state
msc: [80A10, 76N15, 82D05]
defines: YPT3SJSS5T
uses: [GYNNJBMTCP, 5EKTEE00FZ, T8J5XRYBZZ, KK46Q2YV1D, 41NHDR6MH6]
sources:
  - url: https://en.wikipedia.org/wiki/Equation_of_state
---

## Definition

Let a [[thermodynamic system|GYNNJBMTCP]] consist of a fixed amount $n$ of a single substance.
Let its [[equilibrium states|5EKTEE00FZ]] be described by the [[state functions|T8J5XRYBZZ]] pressure $p$, volume $V$ and [[temperature|KK46Q2YV1D]] $T$.
An *equation of state* of the substance is a relation $F(p, V, T, n) = 0$ that holds in every equilibrium state.
Here $F$ is a function such that, at fixed $n$, any two of $p$, $V$, $T$ determine the third, at least locally.

## Remarks

Often the relation is solved for the pressure, $p = p(T, V, n)$, or written in molar form with $V_m = V/n$.
More generally, any relation between state variables of a system in equilibrium is called an equation of state.
For example, $U = U(T, V)$ is the caloric equation of state, and $p = p(T, V)$ the thermal one.
A thermal equation of state alone does not determine all thermodynamic properties; the [[fundamental thermodynamic relation|41NHDR6MH6]] of a substance does, and it implies all its equations of state.

Example: the ideal gas law $pV = nRT$, with the gas constant $R$, is the equation of state $F = pV - nRT = 0$.
Given $T$ and $V$, it gives $p = nRT/V$.

Non-example: the first law $dU = \delta Q - \delta W$ is not an equation of state.
It holds for every substance, it involves heat and work, which are not state functions, and it does not relate $p$, $V$, $T$ in equilibrium.
