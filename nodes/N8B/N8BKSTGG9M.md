---
tag: N8BKSTGG9M
kind: definition
name: Continuum damage mechanics
msc: [74R05, 74A45, 74R20]
defines: 1272BZTN53
uses: [Q4C55V47A8, SX32X1D537, 8QS6QMJF5Z, KG2XWEMJ30, MKXA9E1Z2T]
sources:
  - url: https://en.wikipedia.org/wiki/Damage_mechanics
---

## Definition

Let a body be made of a linear elastic material with [[elasticity tensor|SX32X1D537]] $C$ in its intact state.
An *isotropic continuum damage model* is a [[constitutive model|Q4C55V47A8]] with an internal variable $D(x, t) \in [0, 1]$, the *damage*, such that:

1. the [[stress|KG2XWEMJ30]] is $\sigma = (1 - D) \, C : \varepsilon$, where $\varepsilon$ is the [[strain|8QS6QMJF5Z]];
2. the damage does not decrease: $\dot D \ge 0$;
3. $\dot D$ is given by an evolution law in terms of the state variables, compatible with the [[Clausius–Duhem inequality|MKXA9E1Z2T]].

The *effective stress* is $\tilde\sigma = \sigma / (1 - D)$.
*Continuum damage mechanics* is the theory of such models and of their anisotropic generalizations, in which $D$ is a tensor.

## Remarks

Example: take the free energy $\psi = \frac{1}{2}(1 - D) \, \varepsilon : C : \varepsilon$.
The variable conjugate to $D$ is $Y = -\partial\psi/\partial D = \frac{1}{2} \varepsilon : C : \varepsilon \ge 0$.
The isothermal dissipation is $Y \dot D$, which is nonnegative whenever $\dot D \ge 0$, so clause 3 holds for any law with clause 2.
A typical law lets $D$ grow when $Y$ exceeds its largest past value and a threshold.
Non-example: a model in which $D$ can decrease on unloading violates clause 2; it would describe healing, which is excluded for cracks and voids.
The relation in clause 1 expresses the principle of strain equivalence: the damaged material under $\sigma$ deforms like the intact material under the effective stress.
In one dimension, measuring the reduced Young's modulus $\tilde E = (1 - D) E$ gives the damage as $D = 1 - \tilde E / E$.

## Explanations

### L1 human

Damage is a number between $0$ and $1$ at each point that says how much of the material is broken.
It scales down the stiffness, and it can only grow.
