---
tag: X1W3N6H6SV
kind: example
name: Stirling cycle
msc: [80A10]
instance_of: [AGRGCDWQF8]
uses: [N7R0H2VNDJ, C9MM7GFRWN, YT8APTNYD5, Z686C32X8S, 4Y41F2C3P9]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling_cycle
same_as:
  wikidata: Q910550
  wikipedia: Stirling cycle
---

## Example

The ideal *Stirling cycle* is a [[thermodynamic cycle|AGRGCDWQF8]] of $n$ moles of an [[ideal gas|N7R0H2VNDJ]].
It runs between a hot reservoir at temperature $T_h$ and a cold reservoir at temperature $T_c < T_h$.
Let $V_1 < V_2$ be two volumes and let $r = V_2 / V_1$.

1. [[Isothermal|C9MM7GFRWN]] compression at $T_c$ from $V_2$ to $V_1$.
2. [[Isochoric|YT8APTNYD5]] heating at $V_1$ from $T_c$ to $T_h$.
3. Isothermal expansion at $T_h$ from $V_1$ to $V_2$.
4. Isochoric cooling at $V_2$ from $T_h$ to $T_c$.

The gas returns to its initial state, so this is a cycle.
On the hot isotherm the gas takes in heat $Q_h = nRT_h \ln r$, and on the cold isotherm it gives off $Q_c = nRT_c \ln r$, where $R$ is the gas constant.
The two isochoric steps exchange the same heat $nC_V(T_h - T_c)$ in opposite directions, where $C_V$ is the molar heat capacity at constant volume.
An ideal regenerator stores the heat of step 4 and returns it in step 2.
Then the only heat from outside is $Q_h$, the net work is $Q_h - Q_c = nR(T_h - T_c)\ln r$, and the [[thermal efficiency|Z686C32X8S]] is
$$\eta = 1 - \frac{T_c}{T_h}.$$

## Remarks

With an ideal regenerator, the Stirling cycle reaches the Carnot efficiency, the upper bound of [[Carnot's theorem|4Y41F2C3P9]].
Without a regenerator, the heat of step 2 also comes from the hot reservoir, and the efficiency drops to
$$\eta = \frac{nR(T_h - T_c)\ln r}{nRT_h \ln r + nC_V(T_h - T_c)} < 1 - \frac{T_c}{T_h}.$$

## Explanations

### L1 human

The Stirling cycle shuttles a fixed amount of gas between a hot side and a cold side.
The gas expands while hot and is compressed while cold, so the expansion gives more work than the compression costs.
A regenerator, a heat sponge in the gas path, keeps the heat of the cooling step and gives it back in the heating step.
With a perfect regenerator the cycle is as efficient as a Carnot cycle between the same temperatures.
