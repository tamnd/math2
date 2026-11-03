---
tag: GC0Z0R2ECJ
kind: example
name: Ericsson cycle
msc: [80A10]
instance_of: [AGRGCDWQF8]
uses: [N7R0H2VNDJ, C9MM7GFRWN, WYAY33ZVYQ, Z686C32X8S, X1W3N6H6SV]
sources:
  - url: https://en.wikipedia.org/wiki/Ericsson_cycle
same_as:
  wikidata: Q384539
  wikipedia: Ericsson cycle
---

## Example

The ideal *Ericsson cycle* is a [[thermodynamic cycle|AGRGCDWQF8]] of $n$ moles of an [[ideal gas|N7R0H2VNDJ]].
It runs between a hot reservoir at temperature $T_h$ and a cold reservoir at temperature $T_c < T_h$.
Let $p_L < p_H$ be two pressures.

1. [[Isothermal|C9MM7GFRWN]] compression at $T_c$ from $p_L$ to $p_H$.
2. [[Isobaric|WYAY33ZVYQ]] heating at $p_H$ from $T_c$ to $T_h$.
3. Isothermal expansion at $T_h$ from $p_H$ to $p_L$.
4. Isobaric cooling at $p_L$ from $T_h$ to $T_c$.

The gas returns to its initial state, so this is a cycle.
For an ideal gas the internal energy depends only on temperature, so on each isotherm the heat equals the work.
The gas takes in $Q_h = nRT_h \ln(p_H/p_L)$ on the hot isotherm and gives off $Q_c = nRT_c \ln(p_H/p_L)$ on the cold isotherm.
The two isobaric steps exchange the same heat $nC_p(T_h - T_c)$ in opposite directions, where $C_p$ is the molar heat capacity at constant pressure.
With an ideal regenerator this heat stays inside the engine, and the [[thermal efficiency|Z686C32X8S]] is
$$\eta = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{T_c}{T_h}.$$

## Remarks

The Ericsson cycle is the constant-pressure analogue of the [[Stirling cycle|X1W3N6H6SV]], which uses isochoric steps instead of isobaric ones.
Both reach the Carnot efficiency only because of the ideal regenerator.

## Explanations

### L1 human

The Ericsson cycle compresses gas while it is cold and lets it expand while it is hot, keeping the temperature fixed in both steps.
Between these steps the gas is heated or cooled at constant pressure.
A regenerator recycles the heat of the cooling step into the heating step.
Then all outside heat enters at the top temperature and leaves at the bottom one, just as in a Carnot cycle.
