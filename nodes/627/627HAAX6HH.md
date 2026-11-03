---
tag: 627HAAX6HH
kind: definition
name: Gibbs free energy
msc: [80A10, 80A05]
defines: RBG5ZBM35Y
uses: [F6JVQ12X43, 722RZK72P5, SPY89W0RJ7, AJ8M9MGZGF, T8J5XRYBZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_free_energy
---

## Definition

Let a thermodynamic system in equilibrium have [[internal energy|F6JVQ12X43]] $U$, pressure $p$, volume $V$, [[thermodynamic temperature|AJ8M9MGZGF]] $T$ and [[entropy|SPY89W0RJ7]] $S$.
Its *Gibbs free energy* is the [[state function|T8J5XRYBZZ]]
$$G = U + pV - TS = H - TS,$$
where $H = U + pV$ is the [[enthalpy|722RZK72P5]].

## Remarks

From $dU = T \, dS - p \, dV$ one gets $dG = -S \, dT + V \, dp$.
So the natural variables of $G$ are $T$ and $p$, and $S = -(\partial G / \partial T)_p$, $V = (\partial G / \partial p)_T$.
When the amounts $N_i$ of substances may change, $dG = -S \, dT + V \, dp + \sum_i \mu_i \, dN_i$, where $\mu_i$ is the chemical potential of substance $i$.
Example: for a reaction at $T = 300$ K with $\Delta H = -10$ kJ and $\Delta S = -20$ J/K, one finds $\Delta G = -10\,000 + 300 \cdot 20 = -4\,000$ J, so the reaction can run by itself at fixed $T$ and $p$.
Non-example: $H - TV$ is not the Gibbs free energy, since $T$ must multiply its conjugate variable $S$.

## Explanations

### L1 human

The Gibbs free energy is enthalpy minus temperature times entropy.
It is the right potential when temperature and pressure are held fixed.
