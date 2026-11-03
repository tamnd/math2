---
tag: 1ZKSFVW128
kind: definition
name: Potential temperature
msc: [86A10, 80A10]
defines: SJTMRNXFZ3
uses: [XQ82TE42FH]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_temperature
---

## Definition

Consider dry air treated as an ideal gas with specific gas constant $R$ and specific heat at constant pressure $c_p$.
Fix a reference pressure $p_0 > 0$, by convention $p_0 = 1000$ hPa.
The *potential temperature* of air with absolute temperature $T$ and pressure $p > 0$ is
$$\theta = T \left( \frac{p_0}{p} \right)^{R / c_p}.$$

## Remarks

For dry air $R / c_p \approx 0.286$.
For a reversible adiabatic change of an ideal gas, the first law gives $c_p \, d \ln T - R \, d \ln p = 0$, that is $d \ln \theta = 0$.
So $\theta$ is conserved by a parcel that moves without heating, and $c_p \ln \theta$ equals the specific entropy up to a constant.

Example: at $p = 500$ hPa and $T = 253$ K, $\theta = 253 \cdot 2^{0.286} \approx 253 \cdot 1.219 \approx 308.5$ K.
At $p = p_0$ the potential temperature equals the temperature.

Non-example: moist air in which water vapour condenses receives latent heat, so its $\theta$ increases as it rises.
Then $\theta$ is not conserved, and the [[equivalent potential temperature|50GYDF3XWJ]] is used instead.

The vertical gradient of $\theta$ measures static stability: the squared [[Brunt–Väisälä frequency|XQ82TE42FH]] is $N^2 = (g / \theta) \, \partial \theta / \partial z$, with $g$ the gravitational acceleration.
The atmosphere is statically stable for dry displacements where $\partial \theta / \partial z > 0$.
