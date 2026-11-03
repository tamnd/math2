---
tag: CBWW23FDJH
kind: definition
name: Helmholtz free energy
msc: [80A10, 80A05]
defines: JXKY6C8JTA
uses: [F6JVQ12X43, SPY89W0RJ7, AJ8M9MGZGF, T8J5XRYBZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_free_energy
---

## Definition

Let a thermodynamic system in equilibrium have [[internal energy|F6JVQ12X43]] $U$, [[thermodynamic temperature|AJ8M9MGZGF]] $T$ and [[entropy|SPY89W0RJ7]] $S$.
Its *Helmholtz free energy* is the [[state function|T8J5XRYBZZ]]
$$F = U - TS.$$

## Remarks

The notation $A$ is also common.
From $dU = T \, dS - p \, dV$ one gets $dF = -S \, dT - p \, dV$, where $p$ is the pressure and $V$ the volume.
So the natural variables of $F$ are $T$ and $V$, and $S = -(\partial F / \partial T)_V$, $p = -(\partial F / \partial V)_T$.
Example: for an ideal gas of $n$ moles, $F(T, V) = f(T) - nRT \ln V$ for some function $f$, and indeed $-(\partial F / \partial V)_T = nRT / V = p$.
Non-example: $U - TV$ is not the Helmholtz free energy; the product must be of the conjugate pair $T$ and $S$, and $U - TV$ has no thermodynamic meaning.

## Explanations

### L1 human

The Helmholtz free energy is energy minus temperature times entropy.
It is the right potential when temperature and volume are held fixed.
