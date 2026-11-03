---
tag: T65EB2RBR8
kind: definition
name: Coefficient of performance
msc: [80A10, 80A05]
defines: W0Q5VTTFGX
uses: [AGRGCDWQF8, CY4GJQGF06, S8H21RWQ86, V14W2V4JSR, VECH3HZ04M]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_of_performance
---

## Definition

Consider a system that repeatedly performs a [[thermodynamic cycle|AGRGCDWQF8]].
In each cycle it absorbs [[heat|CY4GJQGF06]] $Q_C > 0$ from a cold reservoir and receives [[work|S8H21RWQ86]] $W > 0$ from its surroundings.
It gives heat $Q_H$ to a hot reservoir.
When the purpose is cooling, the system is a refrigerator and its *coefficient of performance* is
$$\mathrm{COP}_R = \frac{Q_C}{W}.$$
When the purpose is heating, the system is a heat pump and its coefficient of performance is
$$\mathrm{COP}_{HP} = \frac{Q_H}{W}.$$

## Remarks

By the [[first law of thermodynamics|V14W2V4JSR]], $Q_H = Q_C + W$, so $\mathrm{COP}_{HP} = \mathrm{COP}_R + 1$.
By the [[Clausius statement|VECH3HZ04M]] of the second law, heat cannot pass from cold to hot with no other effect, so the cycle needs work $W > 0$.
For a reversible cycle between thermodynamic temperatures $T_C < T_H$, the values are $T_C/(T_H - T_C)$ and $T_H/(T_H - T_C)$, and no cycle between these reservoirs does better.
Example: a reversible heat pump between $T_C = 270\,\mathrm{K}$ and $T_H = 300\,\mathrm{K}$ has $\mathrm{COP}_{HP} = 300/30 = 10$.
A non-example: an electric resistance heater turns work into heat but takes no heat from a cold reservoir, so the condition $Q_C > 0$ fails; its ratio $Q_H/W$ is only $1$.
