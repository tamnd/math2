---
tag: 42WPJMQK0C
kind: example
name: Diesel cycle
msc: [80A10, 80A05]
instance_of: [AGRGCDWQF8]
uses: [N7R0H2VNDJ, ECAXF3AWWX, WYAY33ZVYQ, YT8APTNYD5, NA1VVMJXVA, SYYGZ18FF5, Z686C32X8S, S7XFW04T3V]
sources:
  - url: https://en.wikipedia.org/wiki/Diesel_cycle
same_as:
  wikidata: Q142663
  wikipedia: Diesel cycle
---

## Example

Take $n$ moles of an [[ideal gas|N7R0H2VNDJ]] with constant molar [[heat capacities|SYYGZ18FF5]] $c_V$ and $c_p = \gamma c_V$, where $\gamma > 1$ is the [[heat capacity ratio|NA1VVMJXVA]].
Let $V_2 < V_3 < V_1$ be volumes, with compression ratio $r = V_1/V_2$ and cut-off ratio $\rho = V_3/V_2 > 1$.
The air-standard *Diesel cycle* has four steps, with temperatures $T_1, T_2, T_3, T_4$ at their start points:

1. [[isentropic|ECAXF3AWWX]] compression from $V_1$ to $V_2$;
2. [[isobaric|WYAY33ZVYQ]] heat addition from $V_2$ to $V_3$, absorbing $Q_H = n c_p (T_3 - T_2)$;
3. isentropic expansion from $V_3$ to $V_1$;
4. [[isochoric|YT8APTNYD5]] heat rejection at $V_1$, rejecting $Q_C = n c_V (T_4 - T_1)$, back to the initial state.

The gas returns to its initial state, so this is a [[thermodynamic cycle|AGRGCDWQF8]].
From the isentropes and the ideal gas law: $T_2 = T_1 r^{\gamma-1}$, $T_3 = \rho T_2$, and $T_4 = T_3 (V_3/V_1)^{\gamma-1} = T_3 (\rho/r)^{\gamma-1} = T_1 \rho^{\gamma}$.
Hence the [[thermal efficiency|Z686C32X8S]] is
$$\eta = 1 - \frac{Q_C}{Q_H} = 1 - \frac{1}{r^{\gamma-1}} \cdot \frac{\rho^\gamma - 1}{\gamma(\rho - 1)}.$$
Since $\rho \mapsto \rho^\gamma$ is strictly convex, $\rho^\gamma - 1 > \gamma(\rho - 1)$ for $\rho > 1$, so for the same compression ratio the Diesel cycle is less efficient than the Otto cycle.
For $r = 18$, $\rho = 2$ and $\gamma = 1.4$, $\eta \approx 0.63$.

## Explanations

### L1 human

The Diesel cycle models a diesel engine.
The air alone is squeezed so hard that it becomes hot enough to ignite the fuel.
The fuel is sprayed in while the piston starts to move out, so the burning happens at roughly constant pressure.
Because no spark and no premixed fuel are involved, diesel engines can use much higher compression ratios than petrol engines.
That is why, as a [[heat engine|S7XFW04T3V]], a diesel engine is usually more efficient in practice even though the formula penalises the slow burning.
