---
tag: G9S2QC8X3K
kind: definition
name: Flow plasticity theory
msc: [74C05, 74C15]
defines: A3V75E17RS
uses: [K8BBMTN0KV, CWWCEXZ8BH, XD47SRCJJF, SX32X1D537]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_plasticity_theory
---

## Definition

Work with small strains at a material point, with strain $\varepsilon$, stress $\sigma$ and a vector $q$ of internal (hardening) variables, all functions of time.
A rate-independent *flow plasticity model* consists of:

1. The additive split $\dot\varepsilon = \dot\varepsilon^e + \dot\varepsilon^p$ and the elastic law $\dot\sigma = C : \dot\varepsilon^e$, with $C$ an [[elasticity tensor|SX32X1D537]].
2. A yield function $f(\sigma, q)$, whose zero set in $\sigma$ is the current [[yield surface|CWWCEXZ8BH]], and the constraint $f(\sigma, q) \le 0$.
3. A flow rule $\dot\varepsilon^p = \dot\lambda \, \dfrac{\partial g}{\partial \sigma}(\sigma, q)$, where $g$ is a function called the plastic potential and $\dot\lambda$ is the plastic multiplier.
4. A [[hardening|XD47SRCJJF]] law $\dot q = \dot\lambda \, h(\sigma, q)$ for a given function $h$.
5. The loading and unloading conditions $\dot\lambda \ge 0$, $f(\sigma, q) \le 0$, $\dot\lambda \, f(\sigma, q) = 0$, and the consistency condition $\dot\lambda \, \dot f = 0$.

## Remarks

When $g = f$ the flow rule is the associated flow rule.
Example: one-dimensional linear isotropic hardening, with $C = E$, $q = \kappa$, $f(\sigma, \kappa) = \abs{\sigma} - (\sigma_y + H\kappa)$, $g = f$ and $\dot\kappa = \dot\lambda$.
During plastic loading, consistency gives $\dot\lambda = E\dot\varepsilon \sgn(\sigma)/(E + H)$, so $\dot\sigma = \frac{EH}{E + H}\dot\varepsilon$, the tangent modulus.
Non-example: a deformation theory such as Hencky's sets the total plastic strain as a function of the current stress.
It is not a flow model, since it has no rates and its response does not depend on the path.
The conditions in clause 5 say that plastic flow is possible only on the yield surface and that the stress stays on it while flow goes on.

## Explanations

### L1 human

The model gives the plastic strain rate in terms of the stress and the hardening state.
Plastic flow happens only when the stress sits on the yield surface and stays there.
