---
tag: W6DRHPVZE4
kind: statement
role: proposition
name: Hypsometric equation
msc: [86A10]
uses: [V3MXN0MARH, F74BY6CT91, 04DXAFN2ES]
about: [F74BY6CT91]
sources:
  - url: https://en.wikipedia.org/wiki/Hypsometric_equation
same_as:
  wikidata: Q1786344
  wikipedia: Hypsometric equation
---

## Statement

Let a column of ideal gas of molar mass $M$ be in hydrostatic balance $dp/dz = -\rho g$, with constant gravitational acceleration $g$.
Let $T(z)$ be the absolute temperature at height $z$, and let $p = \rho R T/M$, where $R$ is the molar gas constant.
Assume $p$ is strictly decreasing in $z$, and let $z_1 < z_2$ be the heights where the pressure equals $p_1 > p_2$.
Define the mean temperature of the layer by
$$\overline{T} = \frac{1}{\ln(p_1/p_2)} \int_{p_2}^{p_1} T \, \frac{dp}{p}.$$
Then the thickness of the layer is
$$z_2 - z_1 = \frac{R \, \overline{T}}{M g} \ln \frac{p_1}{p_2}.$$

## Remarks

Proof: the two laws give $dz = -\big( R T/(M g) \big) \, dp/p$; integrate from $p_1$ to $p_2$.
In meteorology the temperature $T$ is replaced by the virtual temperature, which accounts for water vapour, and $R/M$ by the gas constant of dry air.
Example: for the layer from $1000$ hPa to $500$ hPa with $\overline{T} = 255$ K, $R \overline{T}/(Mg) \approx 7.46$ km for dry air, so the thickness is $7.46 \ln 2 \approx 5.2$ km.
For constant $T$ it reduces to case 1 of the [[barometric formula|V3MXN0MARH]], with $R\overline{T}/(Mg)$ the [[scale height|F74BY6CT91]].

## Explanations

### L1 human

The distance between two pressure levels in the atmosphere depends only on how warm the air between them is.
Warm air is thin and takes up more room, so a warm layer is thicker.
Weather maps use this: the thickness between the 1000 hPa and 500 hPa levels shows where the air is warm and where it is cold.

### L2 human

The equation integrates hydrostatic balance in pressure coordinates, where the [[natural logarithm|04DXAFN2ES]] of pressure plays the role of height.
It is used to compute geopotential heights from radiosonde soundings and to reduce surface pressure to sea level.
Horizontal differences in thickness give the vertical shear of the geostrophic wind, the thermal wind.
