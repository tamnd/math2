---
tag: CG6EER6X4S
kind: statement
role: proposition
name: Kelvin's estimate of the age of the Earth
msc: [86A04, 35K05, 80A19]
uses: [18RT45BK1K, VP2HN86VAG, N9RFPKXE2Z]
about: [N9RFPKXE2Z]
sources:
  - url: https://en.wikipedia.org/wiki/Age_of_Earth
---

## Statement

Model the Earth near its surface as a half-space of constant thermal diffusivity $\kappa$, with no internal heat sources.
Assume heat is carried only by conduction.
Assume that at time $0$ it had the uniform temperature $T_m$ and that since then its surface has been held at the temperature $T_0 < T_m$.
Let $G > 0$ be the [[geothermal gradient|N9RFPKXE2Z]] measured at the surface at the present time $t$.
Then
$$t = \frac{(T_m - T_0)^2}{\pi \kappa G^2}.$$

## Remarks

Proof: by the [[half-space cooling model|18RT45BK1K]], the temperature is $T_0 + (T_m - T_0)\operatorname{erf}(z/(2\sqrt{\kappa t}))$, so the surface gradient is $G = (T_m - T_0)/\sqrt{\pi \kappa t}$; solve for $t$.
Example: $T_m - T_0 = 2000$ K, $\kappa = 10^{-6}$ m²/s and $G = 25$ K/km give $t \approx 2 \times 10^{15}$ s, about $65$ million years.
William Thomson, later Lord Kelvin, made this argument in 1862 and concluded that the Earth is between 20 and 400 million years old.
The modern age, from radiometric dating, is about $4.5$ billion years.
The hypotheses fail in two ways.
Radioactive decay in the rock supplies heat.
The mantle carries heat by convection, which keeps the interior hot and the near-surface gradient steep much longer than pure conduction would.

## Explanations

### L1 human

A hot cannonball left to cool gets a steeper temperature gradient near its surface when it is young and a gentler one when it is old.
Kelvin used the measured warming of rock with depth to read off how long the Earth had been cooling.
He found tens of millions of years, far too short for geologists and for Darwin's theory of evolution.
The calculation was right, but the model was wrong: the Earth has inner heat sources and a flowing mantle.

### L2 human

This is the classical application of the solution of the [[heat equation|VP2HN86VAG]] in a half-space with a sudden change of surface temperature.
The age scales as the square of the temperature contrast and as the inverse square of the gradient.
So modest errors in the data change the answer a lot, but not by the factor of about 70 needed.
The same mathematics gives the half-space cooling model of the ocean floor, with the time since the rock left a ridge in place of the age of the Earth.
There the hypotheses hold well.
