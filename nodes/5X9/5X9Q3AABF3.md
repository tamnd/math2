---
tag: 5X9Q3AABF3
kind: statement
role: fact
name: Dittus–Boelter equation
msc: [80A19, 76R05, 76F10]
uses: [THH3V9AHDN, JH9EJ0HA0R, C4KSBMR413, QFBG7W198Q, J821AD6YTE]
about: [QFBG7W198Q, THH3V9AHDN]
sources:
  - url: https://en.wikipedia.org/wiki/Nusselt_number
---

## Statement

Consider fully developed turbulent flow of a fluid in a smooth circular tube of inner diameter $D$.
Let $\mathrm{Nu}_D$ be the [[Nusselt number|THH3V9AHDN]] and $\mathrm{Re}_D$ the [[Reynolds number|JH9EJ0HA0R]], both based on $D$ and the mean velocity.
Let $\Pr$ be the [[Prandtl number|C4KSBMR413]], with the fluid properties taken at the bulk mean temperature.
Assume $\mathrm{Re}_D \ge 10^4$, $0.6 \le \Pr \le 160$, tube length at least $10D$, and a moderate difference between wall and fluid temperatures.
Then, approximately,
$$\mathrm{Nu}_D = 0.023 \, \mathrm{Re}_D^{4/5} \, \Pr^{n},$$
with $n = 0.4$ when the fluid is heated and $n = 0.3$ when it is cooled.

## Remarks

The equation is an empirical fit to measurements, not a consequence of a derivation.
The exponent $4/5$ agrees with the friction law for turbulent pipe flow through analogies between friction and heat transfer.
Example: water with $\Pr = 5$ heated in a tube at $\mathrm{Re}_D = 5 \times 10^4$ gives $\mathrm{Nu}_D \approx 0.023 \cdot 5743 \cdot 1.904 \approx 250$.
Outside the stated ranges, for example in laminar flow or with large property variations, the fit can be far off, and other correlations such as that of Gnielinski are used.

## Explanations

### L1 human

The equation gives a quick estimate of how well a turbulent flow in a pipe carries heat to or from the wall.
Faster flow and fluids that hold heat well give larger Nusselt numbers, and so more heat transfer.
It is one of the most used formulas in the design of heat exchangers.

### L2 human

From $\mathrm{Nu}_D$ one gets the [[heat transfer coefficient|J821AD6YTE]] $h = \mathrm{Nu}_D \, k / D$, where $k$ is the thermal conductivity.
This coefficient then enters an energy balance of the tube or of a heat exchanger.
The different exponents for heating and cooling account roughly for the change of viscosity with temperature near the wall.
