---
tag: PYAEW7M109
kind: definition
name: Second-harmonic generation
msc: [78A60]
defines: 4C67FMA3M7
uses: [7N71T3FKZ6, ASQAH710WN]
sources:
  - url: https://en.wikipedia.org/wiki/Second-harmonic_generation
---

## Definition

Let a medium have second-order [[nonlinear susceptibility|7N71T3FKZ6]] $\chi^{(2)}$, and let a monochromatic field $E(t) = \mathcal{E} e^{-i\omega t} + \overline{\mathcal{E}} e^{i\omega t}$ act on it, written for one component.
The second-order part of the [[polarization density|ASQAH710WN]] is
$$\varepsilon_0 \chi^{(2)} E(t)^2 = 2\varepsilon_0 \chi^{(2)} \abs{\mathcal{E}}^2 + \varepsilon_0 \chi^{(2)} \left( \mathcal{E}^2 e^{-2i\omega t} + \overline{\mathcal{E}}^2 e^{2i\omega t} \right).$$
*Second-harmonic generation* is the radiation of light at frequency $2\omega$ by the term that oscillates at $2\omega$.

## Remarks

The constant term $2\varepsilon_0 \chi^{(2)} \abs{\mathcal{E}}^2$ is a static polarization, called optical rectification.
The generated power grows like the square of the input intensity, as long as the input is not depleted.
Efficient conversion needs phase matching, so that the waves radiated at different points of the crystal add in phase.

Example: the crystal potassium titanyl phosphate lacks a centre of inversion, so it has $\chi^{(2)} \ne 0$ and doubles $1064$ nm light to $532$ nm.

Non-example: a glass plate has a centre of inversion in its bulk, so $\chi^{(2)} = 0$ there and it produces essentially no second harmonic.
