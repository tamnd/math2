---
tag: YNB4ETM4FK
kind: definition
name: Log mean temperature difference
msc: [80A19, 80A20]
defines: 62ESNKESQV
uses: [97ASA870TV, KK46Q2YV1D, J821AD6YTE]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithmic_mean_temperature_difference
---

## Definition

Consider a [[heat exchanger|97ASA870TV]] with parallel flow or counterflow.
Let $\Delta T_1 > 0$ and $\Delta T_2 > 0$ be the [[temperature|KK46Q2YV1D]] differences between the hot and the cold stream at the two ends.
The *log mean temperature difference* is
$$\Delta T_{\mathrm{lm}} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)} \quad \text{if } \Delta T_1 \ne \Delta T_2,$$
and $\Delta T_{\mathrm{lm}} = \Delta T_1$ if $\Delta T_1 = \Delta T_2$.

## Remarks

The value at $\Delta T_1 = \Delta T_2$ is the limit of the formula, so $\Delta T_{\mathrm{lm}}$ is a continuous function of $(\Delta T_1, \Delta T_2)$.
It lies between the geometric and the arithmetic mean: $\sqrt{\Delta T_1 \Delta T_2} \le \Delta T_{\mathrm{lm}} \le (\Delta T_1 + \Delta T_2)/2$.

Example: $\Delta T_1 = 40$ K and $\Delta T_2 = 10$ K give $\Delta T_{\mathrm{lm}} = 30 / \ln 4 \approx 21.6$ K, which lies between $20$ K and $25$ K.

Non-example: suppose the cold stream leaves at the inlet temperature of the hot stream.
Then $\Delta T_2 = 0$ at that end, the positivity condition fails, and $\Delta T_{\mathrm{lm}}$ is not defined.
Such an exchanger would need infinite area.

For parallel flow or counterflow with constant [[overall heat transfer coefficient|J821AD6YTE]] $U$ and area $A$, the heat rate is $q = U A \, \Delta T_{\mathrm{lm}}$.
For crossflow and multipass exchangers one multiplies the counterflow value by a correction factor $F \le 1$.
