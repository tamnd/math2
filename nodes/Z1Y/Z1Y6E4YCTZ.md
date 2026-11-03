---
tag: Z1Y6E4YCTZ
kind: statement
role: theorem
name: Hawking radiation
msc: ["83C47", "83C57", "81T20"]
uses: [46QNBD585F, D8NZ32Z3SQ, 5EHD2XBQDG]
about: [YHJ0PDNY8T]
sources:
  - url: https://en.wikipedia.org/wiki/Hawking_radiation
same_as:
  wikidata: Q497396
  wikipedia: Hawking radiation
---

## Statement

Consider a free quantum field on a spacetime, for example a massless scalar field obeying the [[wave equation|5EHD2XBQDG]] of the spacetime.
Assume that in this spacetime a [[black hole|YHJ0PDNY8T]] forms by gravitational collapse and settles down to a stationary black hole with surface gravity $\kappa$.
Assume the field is in its vacuum state in the far past, before the collapse.
Then at late times the state of the field near future null infinity is thermal.
The outgoing flux has the Hawking temperature
$$T_H = \frac{\hbar \kappa}{2\pi c\, k_B},$$
reduced in each mode by the probability that it passes the gravitational potential around the hole.

## Remarks

Hawking found the effect in 1974 by tracing late outgoing modes back in time.
They pass through the collapsing body just before the [[event horizon|D8NZ32Z3SQ]] forms and are blueshifted enormously.
Comparing them with the vacuum modes of the past gives Bogoliubov coefficients whose squared norms follow a Planck distribution at temperature $T_H$.
Rigorous versions of the result for linear fields have been proved in mathematical physics.

Example: for a Schwarzschild black hole of mass $M$, $\kappa = c^4/(4GM)$, so $T_H = \hbar c^3/(8\pi G M k_B)$.
For one solar mass this is about $6 \times 10^{-8}$ kelvin, far below the temperature of the cosmic microwave background.
A smaller black hole is hotter, so it radiates faster and evaporates.

## Explanations

### L1 human

Classically nothing comes out of a black hole.
Hawking showed that quantum effects near the horizon make a black hole glow faintly, like a hot body.
Its temperature is inversely proportional to its mass, so big black holes are extremely cold and tiny ones very hot.
By radiating, a black hole slowly loses mass and may in the end evaporate.

### L2 human

Hawking radiation turned the [[laws of black hole mechanics|46QNBD585F]] into real thermodynamics, fixing the [[Bekenstein–Hawking entropy|ANNJ7JR36T]] at a quarter of the area.
It is closely related to the Unruh effect, in which an accelerated observer in flat space sees the vacuum as a thermal bath.
Because the radiation is exactly thermal in Hawking's computation, it seems to carry no information about what fell in, which leads to the [[black hole information paradox|6ETFPK0E2G]].
