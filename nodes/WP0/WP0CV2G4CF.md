---
tag: WP0CV2G4CF
kind: definition
name: Chemical potential
msc: [80A10, 80A50]
defines: WVH4PVW64P
uses: [F6JVQ12X43, SPY89W0RJ7, RBG5ZBM35Y, 05AXG3QRKR]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_potential
---

## Definition

Let a system in thermodynamic equilibrium contain $r$ chemical species with amounts $N_1, \dots, N_r$.
Let its [[internal energy|F6JVQ12X43]] be a differentiable function $U(S, V, N_1, \dots, N_r)$ of the [[entropy|SPY89W0RJ7]] $S$, the volume $V$ and the amounts.
The *chemical potential* of species $i$ is the [[partial derivative|05AXG3QRKR]]
$$\mu_i = \left( \frac{\partial U}{\partial N_i} \right)_{S, V, N_{j \ne i}}.$$

## Remarks

Equivalently, with the [[Gibbs free energy|RBG5ZBM35Y]] $G(T, p, N_1, \dots, N_r)$, one has $\mu_i = (\partial G / \partial N_i)_{T, p, N_{j \ne i}}$.
The fundamental relation then reads $dU = T\,dS - p\,dV + \sum_i \mu_i\,dN_i$.
For one species, $G = \mu N$, so $\mu$ is the Gibbs free energy per particle or per mole.

Example: for $n$ moles of an ideal gas at temperature $T$ and pressure $p$, $G = n\big(\mu^\circ(T) + RT \ln(p/p^\circ)\big)$, where $p^\circ$ is a reference pressure and $R$ the gas constant.
Differentiating in $n$ at fixed $T$ and $p$ gives $\mu = \mu^\circ(T) + RT \ln(p/p^\circ)$.

Non-example: the derivative $(\partial U / \partial N_i)_{T, V}$ at fixed temperature instead of fixed entropy is in general not $\mu_i$.
For a monatomic ideal gas, $U = \tfrac{3}{2} N k T$, so this derivative is $\tfrac{3}{2} kT$, which does not depend on the pressure, while $\mu$ does.

The chemical potential is intensive, and its unit is energy per particle or energy per mole.
