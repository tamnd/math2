---
tag: N8C4JXD90C
kind: example
name: Otto cycle
msc: [80A10, 80A05]
instance_of: [AGRGCDWQF8]
uses: [N7R0H2VNDJ, ECAXF3AWWX, YT8APTNYD5, NA1VVMJXVA, SYYGZ18FF5, Z686C32X8S, S7XFW04T3V]
sources:
  - url: https://en.wikipedia.org/wiki/Otto_cycle
same_as:
  wikidata: Q201762
  wikipedia: Otto cycle
---

## Example

Take $n$ moles of an [[ideal gas|N7R0H2VNDJ]] with constant molar [[heat capacity|SYYGZ18FF5]] $c_V$ at constant volume and constant [[heat capacity ratio|NA1VVMJXVA]] $\gamma > 1$.
Let $V_1 > V_2$ be two volumes, with compression ratio $r = V_1/V_2$.
The air-standard *Otto cycle* has four steps, with temperatures $T_1, T_2, T_3, T_4$ at their start points:

1. [[isentropic|ECAXF3AWWX]] compression from $V_1$ to $V_2$;
2. heat addition at constant volume $V_2$ ([[isochoric|YT8APTNYD5]]), absorbing $Q_H = n c_V (T_3 - T_2)$;
3. isentropic expansion from $V_2$ back to $V_1$;
4. heat rejection at constant volume $V_1$, rejecting $Q_C = n c_V (T_4 - T_1)$, back to the initial state.

The gas returns to its initial state, so this is a [[thermodynamic cycle|AGRGCDWQF8]].
On the isentropes $TV^{\gamma-1}$ is constant, so $T_2 = T_1 r^{\gamma-1}$ and $T_3 = T_4 r^{\gamma-1}$.
Hence $T_3 - T_2 = r^{\gamma-1}(T_4 - T_1)$ and the [[thermal efficiency|Z686C32X8S]] is
$$\eta = 1 - \frac{Q_C}{Q_H} = 1 - \frac{1}{r^{\gamma - 1}}.$$
For $r = 8$ and $\gamma = 1.4$, $\eta = 1 - 8^{-0.4} \approx 0.56$.
This is less than the Carnot value $1 - T_1/T_3$ for the extreme temperatures $T_1$ and $T_3$ of the cycle, since $T_1/T_3 < T_1/T_2 = r^{1-\gamma}$.

## Explanations

### L1 human

The Otto cycle is the idealised model of a petrol engine.
The piston squeezes the mixture of air and fuel, and a spark burns it so fast that the volume has no time to change.
Then the hot gas pushes the piston out, and the exhaust is let out.
The formula shows that the efficiency depends only on how much the air is squeezed: a higher compression ratio gives a more efficient [[heat engine|S7XFW04T3V]].
In real engines the ratio is limited because the fuel would ignite on its own, which is called knocking.
