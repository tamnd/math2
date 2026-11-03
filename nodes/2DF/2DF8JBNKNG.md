---
tag: 2DF8JBNKNG
kind: example
name: Carnot cycle
msc: [80A10, 80A05]
instance_of: [AGRGCDWQF8]
uses: [N7R0H2VNDJ, C9MM7GFRWN, ECAXF3AWWX, F3DHZ45H6A, NA1VVMJXVA, Z686C32X8S, S7XFW04T3V, 4Y41F2C3P9]
sources:
  - url: https://en.wikipedia.org/wiki/Carnot_cycle
same_as:
  wikidata: Q188910
  wikipedia: Carnot cycle
---

## Example

Take $n$ moles of an [[ideal gas|N7R0H2VNDJ]] with constant [[heat capacity ratio|NA1VVMJXVA]] $\gamma > 1$, and two reservoirs at temperatures $T_H > T_C$.
The *Carnot cycle* consists of four [[reversible|F3DHZ45H6A]] steps, through volumes $V_1 < V_2 < V_3$ and $V_1 < V_4 < V_3$:

1. [[isothermal|C9MM7GFRWN]] expansion at $T_H$ from $V_1$ to $V_2$, absorbing heat $Q_H = nRT_H \ln(V_2/V_1)$;
2. [[isentropic|ECAXF3AWWX]] expansion from $V_2$ to $V_3$, during which the gas cools from $T_H$ to $T_C$;
3. isothermal compression at $T_C$ from $V_3$ to $V_4$, rejecting heat $Q_C = nRT_C \ln(V_3/V_4)$;
4. isentropic compression from $V_4$ back to $V_1$, during which the gas warms from $T_C$ to $T_H$.

Check that it is a [[thermodynamic cycle|AGRGCDWQF8]] and compute its efficiency.
The gas ends at volume $V_1$ and temperature $T_H$, its initial state.
On an isentrope of an ideal gas, $TV^{\gamma - 1}$ is constant, so $T_H V_2^{\gamma-1} = T_C V_3^{\gamma-1}$ and $T_H V_1^{\gamma-1} = T_C V_4^{\gamma-1}$.
Dividing gives $V_2/V_1 = V_3/V_4$.
The two isentropic steps exchange no heat.
On an isotherm of an ideal gas the internal energy is constant, so the heat equals the work $nRT\ln(V_{\text{end}}/V_{\text{start}})$; this gives $Q_H$ and $Q_C$.
Hence the [[thermal efficiency|Z686C32X8S]] is
$$\eta = 1 - \frac{Q_C}{Q_H} = 1 - \frac{T_C}{T_H},$$
the largest value allowed by [[Carnot's theorem|4Y41F2C3P9]].
For $T_H = 500\,\mathrm{K}$ and $T_C = 300\,\mathrm{K}$, $\eta = 0.4$.

## Explanations

### L1 human

The Carnot cycle is the ideal [[heat engine|S7XFW04T3V]]: it takes in heat only at the hot temperature and gives heat out only at the cold temperature.
In between, the gas expands or is compressed without any heat exchange, so its temperature moves from one level to the other.
Every step is done infinitely slowly, so nothing is wasted.
No real engine runs like this, since it would be far too slow, but it shows the best that any engine could ever do between two temperatures.
