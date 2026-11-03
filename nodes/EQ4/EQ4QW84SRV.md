---
tag: EQ4QW84SRV
kind: definition
name: Maxwell equal-area construction
msc: [80A10, 82B26]
defines: Q4BAT5RMWN
uses: [YPT3SJSS5T, X576BQTPQ5, WVH4PVW64P, JXKY6C8JTA, YYQRRFQAQP]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell_construction
---

## Definition

Fix a temperature $T$ and a fixed amount of a fluid with an [[equation of state|YPT3SJSS5T]].
Let $p(V)$ be the isotherm at $T$, and assume that $p$ is continuous and not monotone decreasing on an interval of volumes.
The *Maxwell equal-area construction* chooses a pressure $p^*$ and volumes $V_l < V_g$ with $p(V_l) = p(V_g) = p^*$ such that
$$\int_{V_l}^{V_g} p(V) \, dV = p^* (V_g - V_l).$$
The *corrected isotherm* equals $p^*$ on $[V_l, V_g]$ and equals $p(V)$ outside this interval.

## Remarks

The condition says that the region between the curve and the line $p = p^*$ has equal areas above and below the line.
It is equivalent to equality of the Gibbs free energies per mole, that is of the [[chemical potentials|WVH4PVW64P]], of the liquid at $V_l$ and the vapour at $V_g$.
Indeed, along an isotherm the [[Helmholtz free energy|JXKY6C8JTA]] satisfies $F(V_g) - F(V_l) = -\int_{V_l}^{V_g} p \, dV$, and $\mu = (F + pV)/n$; equal chemical potentials at equal pressure $p^*$ give the displayed equation.
On $[V_l, V_g]$ the fluid is a mixture of liquid and vapour, and the parts of the original isotherm with $\partial p / \partial V > 0$, which violate the [[stability conditions|YYQRRFQAQP]], are removed.

Example: for the [[van der Waals equation|X576BQTPQ5]] in reduced variables at $T_r = 0.9$, the construction gives a coexistence pressure $p_r^* \approx 0.65$.

Non-example: for $T \ge T_c$ every van der Waals isotherm is monotone decreasing.
There is no pair $V_l < V_g$ with equal pressure, and no construction is needed.
There is no liquid-vapour coexistence above the critical temperature.
