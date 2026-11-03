---
tag: 1DXGQ8HGD2
kind: definition
name: Creep
msc: [74C10, 74D10]
defines: YFTQJ7VY31
uses: [HXGCGHS070, 8QS6QMJF5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Creep_(deformation)
---

## Definition

Consider a specimen loaded at time $t = 0$ by a [[stress|HXGCGHS070]] $\sigma_0$ that is then held constant, and let $\varepsilon(t)$ be its [[strain|8QS6QMJF5Z]] at time $t \ge 0$.
The material *creeps* if $\varepsilon(t)$ keeps increasing for $t > 0$.
The *creep strain* is $\varepsilon(t) - \varepsilon(0^+)$, the part of the strain that grows after the instantaneous response.
The curve $t \mapsto \varepsilon(t)$ is the *creep curve*, and for a linear material the ratio $J(t) = \varepsilon(t)/\sigma_0$ is the *creep compliance*.

## Remarks

Example: a spring of modulus $E$ in series with a dashpot of viscosity $\eta$ (the Maxwell material) has $\varepsilon(t) = \sigma_0/E + \sigma_0 t/\eta$, whose creep strain $\sigma_0 t / \eta$ grows linearly.
Non-example: a linear elastic solid has $\varepsilon(t) = \sigma_0/E$ for all $t > 0$, so its creep strain is zero.
Metals at high temperature typically show three stages.
They are primary creep with decreasing strain rate, secondary creep with a nearly constant rate, and tertiary creep with an increasing rate that ends in rupture.
The steady secondary rate is often fitted by Norton's power law $\dot\varepsilon = A \sigma_0^n$, with constants $A > 0$ and $n \ge 1$ that depend on the material and the temperature.
