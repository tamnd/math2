---
tag: CXQXNR0PNV
kind: definition
name: Metabolic control analysis
msc: [92C42, 92C45]
defines: Z5J0Z6MD6G
uses: [0NT64JV96A, 0N8NGKDZDZ, 09EGC6F8PT, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Metabolic_control_analysis
---

## Definition

Consider a reaction network with metabolite concentrations $s \in \R^m$ and stoichiometric matrix $N \in \R^{m \times r}$.
Let $v_k(s, e_k)$ be the rate of reaction $k = 1, \dots, r$, where $e_k > 0$ is the activity of its enzyme and $v_k$ is proportional to $e_k$.
Assume that the [[ordinary differential equation|0NT64JV96A]] $ds/dt = N v(s, e)$ has an asymptotically stable [[equilibrium|0N8NGKDZDZ]] $s^*(e)$.
Assume that $s^*(e)$ depends differentiably on $e$, and let $J_j(e) = v_j(s^*(e), e) \ne 0$ be the steady-state fluxes.

1. The *flux control coefficient* of enzyme $k$ on flux $J_j$ is $C^{J_j}_{k} = \dfrac{e_k}{J_j} \dfrac{\partial J_j}{\partial e_k} = \dfrac{\partial \ln J_j}{\partial \ln e_k}$.
2. The *concentration control coefficient* of enzyme $k$ on metabolite $i$ is $C^{s_i}_{k} = \dfrac{\partial \ln s^*_i}{\partial \ln e_k}$, when $s^*_i > 0$.
3. The *elasticity* of reaction $k$ with respect to metabolite $i$ is $\varepsilon^{v_k}_{s_i} = \dfrac{s_i}{v_k} \dfrac{\partial v_k}{\partial s_i}$, a [[partial derivative|09EGC6F8PT]] taken with the other concentrations fixed.

## Remarks

Control coefficients are properties of the whole system at steady state, while elasticities are local properties of one rate law.
Example: for a single reaction with no intermediates, $J = v = k e$, so $C^J_1 = (e / J)\, k = 1$; all control lies in the one enzyme.
Non-example: the quantity $\partial J / \partial e_k$ alone is not a control coefficient, because it is not scaled; it changes with the units of $e_k$ and $J$.
For an unbranched pathway, the *summation theorem* states $\sum_k C^J_k = 1$, and the *connectivity theorem* states $\sum_k C^J_k\, \varepsilon^{v_k}_{s_i} = 0$ for each internal metabolite $s_i$.
