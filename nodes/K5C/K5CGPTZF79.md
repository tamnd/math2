---
tag: K5CGPTZF79
kind: definition
name: Temperature
msc: [80A05, 80A10]
defines: KK46Q2YV1D
uses: [5EKTEE00FZ, TD4C13V3J6, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Temperature
---

## Definition

Let $\mathcal{S}$ be the set of equilibrium [[states|TD4C13V3J6]] of all thermodynamic systems.
Write $a \sim b$ when systems in states $a$ and $b$ are in thermal [[equilibrium|5EKTEE00FZ]] with each other.
By the zeroth law of thermodynamics, $\sim$ is an [[equivalence relation|0G8VEZ3WTK]] on $\mathcal{S}$.
An *empirical temperature* is a function $\theta \colon \mathcal{S} \to \R$ such that $\theta(a) = \theta(b)$ if and only if $a \sim b$.

## Remarks

The height of a column of mercury in a thermometer, put in thermal contact with a system, defines an empirical temperature over its working range.
A constant function on $\mathcal{S}$ is not an empirical temperature.
It fails the "only if" part, since it does not separate states that are not in thermal equilibrium.
The usual convention orders the values so that heat flows from higher to lower $\theta$.
Two empirical temperatures that both follow this convention are related by a strictly increasing map.
The thermodynamic temperature is the one fixed by the second law.
