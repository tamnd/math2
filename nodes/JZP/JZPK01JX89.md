---
tag: JZPK01JX89
kind: definition
name: Windkessel model
msc: [92C35, 92C30, 34A30]
defines: 6PKF2XGEGQ
uses: [0NT64JV96A, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Windkessel_effect
---

## Definition

Let $Q(t) \ge 0$ be the volume flow of blood from the heart into the aorta at time $t$.
Let $P(t)$ be the arterial pressure, measured relative to venous pressure.
Let $C > 0$ be the arterial compliance and $R > 0$ the peripheral resistance.
The *two-element Windkessel model* is the [[ordinary differential equation|0NT64JV96A]]
$$C \frac{dP}{dt} + \frac{P}{R} = Q(t).$$
The *three-element Windkessel model* adds a characteristic impedance $Z > 0$ in series, so that the input pressure is $P_{\mathrm{in}} = P + Z Q$, where $P$ still solves the equation above.

## Remarks

The term $C\, dP/dt$ is the rate at which blood is stored in the elastic arteries, and $P/R$ is the outflow to the periphery.
Example: in diastole $Q = 0$, so $P(t) = P(t_0)\, e^{-(t - t_0)/(RC)}$, an [[exponential|0J0FCWV32D]] decay with time constant $RC$; one checks $C \cdot (-P/(RC)) + P/R = 0$.
Non-example: $P = R\, Q$ alone, with no compliance term, is a pure resistance model; it predicts that the pressure drops to zero as soon as the inflow stops.
The model is the equation of an electric circuit with a capacitor $C$ and a resistor $R$ in parallel, driven by the current $Q$.
