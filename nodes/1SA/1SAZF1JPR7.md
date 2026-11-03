---
tag: 1SAZF1JPR7
kind: definition
name: Parameterized post-Newtonian formalism
msc: ["83C25", "83B05", "83D05"]
defines: 2TAW8GAMM1
uses: [7HC8RM1EH9, 3MCZ97SW6V, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Parameterized_post-Newtonian_formalism
---

## Definition

Consider metric theories of gravity, in which matter couples only to a [[Lorentzian metric|BY4QYYS788]] $g$, applied to slowly moving, weakly gravitating systems of perfect-fluid matter.
The *parameterized post-Newtonian formalism* writes the [[first post-Newtonian|7HC8RM1EH9]] metric of every such theory in a standard gauge and coordinate frame.
In that form, the metric is one fixed linear combination of a fixed list of potentials built from the matter variables.
The coefficients of this combination are expressions in ten real constants, the PPN parameters
$$\gamma, \ \beta, \ \xi, \ \alpha_1, \ \alpha_2, \ \alpha_3, \ \zeta_1, \ \zeta_2, \ \zeta_3, \ \zeta_4,$$
whose values depend on the theory.
Take the special case of a static, spherically symmetric mass $M$ in isotropic coordinates.
Then the PPN metric reduces to
$$g_{00} = -1 + \frac{2U}{c^2} - 2\beta \frac{U^2}{c^4}, \qquad g_{0i} = 0, \qquad g_{ij} = \Big(1 + 2\gamma \frac{U}{c^2}\Big) \delta_{ij}.$$
Here $U = GM/r$, and higher-order terms are omitted.

## Remarks

The parameter $\gamma$ measures the space curvature produced by unit rest mass, and $\beta$ measures the nonlinearity in the superposition law for gravity.
The parameter $\xi$ measures preferred-location effects, the $\alpha_i$ measure preferred-frame effects, and the $\zeta_i$ together with $\alpha_3$ measure violations of conservation of total momentum.

Example: general relativity, through the [[Einstein field equations|3MCZ97SW6V]], gives $\gamma = \beta = 1$ and all other parameters $0$.
Indeed the Schwarzschild metric in isotropic coordinates has $g_{00} = -1 + 2U/c^2 - 2U^2/c^4 + \dots$ and $g_{ij} = (1 + 2U/c^2 + \dots)\delta_{ij}$.
Brans–Dicke theory with coupling constant $\omega$ gives $\gamma = (1 + \omega)/(2 + \omega)$ and $\beta = 1$.

Non-example: a theory in which matter couples directly to two different metrics, or to an extra field, is not a metric theory.
The formalism in this form does not cover it.

In terms of the parameters, the deflection of light by the Sun is $\frac{1 + \gamma}{2}$ times the general relativity value.
The perihelion advance of a planet is $\frac{2 + 2\gamma - \beta}{3}$ times the general relativity value, when preferred-frame effects and the solar quadrupole moment are neglected.
