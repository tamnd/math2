---
tag: V3MXN0MARH
kind: statement
role: proposition
name: Barometric formula
msc: [86A10]
uses: [F74BY6CT91, ZPXXA62VQB, 0J0FCWV32D, 0NT64JV96A]
about: [F74BY6CT91]
sources:
  - url: https://en.wikipedia.org/wiki/Barometric_formula
same_as:
  wikidata: Q808592
  wikipedia: Barometric formula
---

## Statement

Let a column of ideal gas of molar mass $M$ have pressure $p(z)$, density $\rho(z)$ and absolute temperature $T(z)$ at height $z$.
Assume hydrostatic balance $dp/dz = -\rho g$ with constant gravitational acceleration $g$.
Assume the ideal gas law $p = \rho R T/M$, where $R$ is the molar gas constant.
Let $p_0 = p(0)$.

1. If $T(z) = T_0$ is constant, then $p(z) = p_0 \exp(-z/H)$, where $H = R T_0/(M g)$ is the [[scale height|F74BY6CT91]].
2. If $T(z) = T_0 - L z$ with a constant [[lapse rate|ZPXXA62VQB]] $L > 0$, then for $0 \leq z < T_0/L$,
$$p(z) = p_0 \left( 1 - \frac{L z}{T_0} \right)^{g M/(R L)}.$$

## Remarks

Proof: the two laws give the [[ordinary differential equation|0NT64JV96A]] $dp/p = -\big( M g / (R T(z)) \big) \, dz$; integrate from $0$ to $z$.
For constant $T$ this gives an [[exponential|0J0FCWV32D]]; for $T = T_0 - Lz$ it gives $\ln(p/p_0) = (gM/(RL)) \ln(1 - Lz/T_0)$.
As $L \to 0$ the second formula tends to the first, since $(1 - Lz/T_0)^{gM/(RL)} \to e^{-gMz/(RT_0)}$.
Example: with $T_0 = 288$ K, $H \approx 8.4$ km, so in an isothermal model the pressure at $5.5$ km is about $p_0 e^{-0.65} \approx 0.52 \, p_0$, close to the observed half of sea-level pressure.
Without constant $g$ the formula fails at heights comparable with the planet's radius, where $g$ decreases.

## Explanations

### L1 human

Air pressure is the weight of the air above you.
Each step up removes a little air from above, and since the air is compressible, the amount removed is proportional to the pressure itself.
That is why pressure falls exponentially with height: halved every 5.5 km or so on Earth.
The formula is used to calibrate altimeters in aircraft.

### L2 human

The formula combines the two basic laws of a resting atmosphere: hydrostatic balance and the ideal gas law.
The standard atmosphere used in aviation is built from pieces of form 2, with different lapse rates in different layers.
The density obeys the same laws, with exponent $gM/(RL) - 1$ in case 2.
The hypsometric equation is the general form for any temperature profile.
