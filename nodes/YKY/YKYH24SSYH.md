---
tag: YKYH24SSYH
kind: definition
name: Effective temperature
msc: [85A25, 85A15, 80A21]
defines: WETKRE94E0
uses: [A2RMYX8A65]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_temperature
---

## Definition

Let a body emit radiation with total bolometric flux $F > 0$ per unit area of its surface.
This is the emitted power per unit area summed over all frequencies and directions.
Let $\sigma$ be the Stefan–Boltzmann constant.
The *effective temperature* of the body is the unique $T_{\text{eff}} > 0$ with
$$F = \sigma T_{\text{eff}}^4.$$
For a spherical star of radius $R$ and luminosity $L$, this means $L = 4\pi R^2 \sigma T_{\text{eff}}^4$.

## Remarks

Example: a [[black body|A2RMYX8A65]] at temperature $T$ emits $F = \sigma T^4$ by the [[Stefan–Boltzmann law|6JQVMS9Y7R]], so its effective temperature is $T$.
Non-example: the temperature at the centre of the Sun, about $1.5 \times 10^7$ K, is not its effective temperature.
The surface flux of the Sun corresponds to about $5772$ K.
In the Eddington grey atmosphere, $T^4(\tau) = \frac{3}{4} T_{\text{eff}}^4 (\tau + \frac{2}{3})$, so the local temperature equals $T_{\text{eff}}$ at [[optical depth|TWF69TQH3S]] $\tau = 2/3$.
