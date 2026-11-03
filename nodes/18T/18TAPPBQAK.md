---
tag: 18TAPPBQAK
kind: definition
name: Thermoelasticity
msc: [74F05, 74B05]
defines: 58ZRHE8MQK
uses: [6W00ZECYT0, V56XAESDNE, 8QS6QMJF5Z, KG2XWEMJ30, 80737NDZ4V, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_stress
---

## Definition

Consider a body of homogeneous isotropic material with mass density $\rho$ and [[Lamé parameters|80737NDZ4V]] $\lambda, \mu$.
Let $\alpha$ be its coefficient of linear thermal expansion, $c$ its specific heat at constant strain, and $k$ its thermal conductivity.
Let $u$ be the displacement, $\varepsilon = \tfrac12 (\nabla u + \nabla u^T)$ the [[infinitesimal strain|8QS6QMJF5Z]], $\sigma$ the [[stress|KG2XWEMJ30]], $T_0$ a reference temperature, and $\theta = T - T_0$ a small temperature change.
*Linear thermoelasticity* is the system of the following three equations, where $f$ is the body force and $r$ the heat supply per unit volume.

1. Constitutive law: $\sigma = \lambda (\tr \varepsilon) I + 2\mu \varepsilon - (3\lambda + 2\mu) \alpha \theta I$.
2. Balance of momentum: $\nabla \cdot \sigma + f = \rho \ddot u$.
3. Energy balance: $\rho c \dot\theta + (3\lambda + 2\mu) \alpha T_0 \tr \dot\varepsilon = k \Delta \theta + r$.

## Remarks

Example: the uniform state $\theta = \theta_0$, $\varepsilon = \alpha \theta_0 I$, $\sigma = 0$, $u(x) = \alpha \theta_0 x$ solves all three equations with $f = 0$ and $r = 0$: the stress vanishes by (1) since $\tr \varepsilon = 3\alpha\theta_0$, and both sides of (3) vanish.
Non-example: if the term $-(3\lambda + 2\mu)\alpha\theta I$ is dropped from (1), the law is plain [[Hooke's law|V56XAESDNE]] and temperature has no mechanical effect, which is isothermal [[linear elasticity|6W00ZECYT0]].
Dropping the coupling term $(3\lambda + 2\mu)\alpha T_0 \tr \dot\varepsilon$ from (3) gives *uncoupled* thermoelasticity, where $\theta$ solves the [[heat equation|VP2HN86VAG]] first and then acts as a load; this is accurate for most slow processes.
