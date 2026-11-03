---
tag: VF7JYBJ4G8
kind: definition
name: Enthalpy
msc: [80A10, 80A05]
defines: 722RZK72P5
uses: [F6JVQ12X43, T8J5XRYBZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Enthalpy
---

## Definition

Let a thermodynamic system in equilibrium have [[internal energy|F6JVQ12X43]] $U$, pressure $p$ and volume $V$.
Its *enthalpy* is the [[state function|T8J5XRYBZZ]]
$$H = U + pV.$$

## Remarks

From $dU = T \, dS - p \, dV$ one gets $dH = T \, dS + V \, dp$, where $T$ is the temperature and $S$ the entropy.
So the natural variables of $H$ are $S$ and $p$, and $T = (\partial H / \partial S)_p$, $V = (\partial H / \partial p)_S$.
In a process at constant pressure in which only expansion work is done, the heat taken in is $Q = \Delta H$.
Example: for $n$ moles of a monatomic ideal gas, $U = \frac{3}{2} nRT$ and $pV = nRT$, so $H = \frac{5}{2} nRT$, where $R$ is the gas constant.
Non-example: $U - pV$ is not the enthalpy; the sign of the term $pV$ matters, and $U - pV$ has differential $T \, dS - 2p \, dV - V \, dp$, with no simple meaning.

## Explanations

### L1 human

Enthalpy is energy plus pressure times volume.
It is the right energy to track when a process happens at constant pressure.
