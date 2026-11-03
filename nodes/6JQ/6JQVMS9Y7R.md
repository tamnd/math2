---
tag: 6JQVMS9Y7R
kind: statement
role: theorem
name: Stefan–Boltzmann law
msc: [80A21, 78A40]
uses: [A2RMYX8A65, AJ8M9MGZGF, QKQ0V5S04R, XTXT8YSP5N, 1XWBY4N0VT, VETMCF1NQ5]
about: [A2RMYX8A65]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law
same_as:
  wikidata: Q704747
  wikipedia: Stefan–Boltzmann law
---

## Statement

Let a [[black body|A2RMYX8A65]] be in thermal equilibrium at absolute [[temperature|AJ8M9MGZGF]] $T$.
Let $M$ be the total power that it emits per unit area, over all wavelengths and into the whole hemisphere.
Then
$$M = \sigma T^4.$$
Here $\sigma = \dfrac{2 \pi^5 k_B^4}{15 c^2 h^3} \approx 5.670 \times 10^{-8} \ \mathrm{W\,m^{-2}\,K^{-4}}$ is the Stefan–Boltzmann constant, $k_B$ is the Boltzmann constant, $h$ the Planck constant and $c$ the speed of light.

## Remarks

Proof idea: by [[Lambert's cosine law|XTXT8YSP5N]], the exitance is $\pi$ times the radiance, so $M = \pi \int_0^\infty B_\nu \, d\nu$ with $B_\nu$ from [[Planck's law|QKQ0V5S04R]].
The substitution $x = h\nu / (k_B T)$ gives $M = \frac{2\pi k_B^4 T^4}{c^2 h^3} \int_0^\infty \frac{x^3}{e^x - 1} \, dx$.
The integral equals $\Gamma(4) \zeta(4) = 6 \cdot \pi^4/90 = \pi^4/15$, by the [[Riemann zeta function|1XWBY4N0VT]].
Josef Stefan inferred the $T^4$ law from measurements in 1879, and Ludwig Boltzmann derived it from thermodynamics in 1884.

Example: the surface of the Sun at about $5772$ K emits about $\sigma \cdot 5772^4 \approx 6.3 \times 10^7$ W per square metre.
For a real surface with [[emissivity|VETMCF1NQ5]] $\varepsilon$, the emitted power is $\varepsilon \sigma T^4$.
The law needs absolute temperature: in degrees Celsius the formula is wrong.

## Explanations

### L1 human

The hotter an object, the more heat it radiates, and the growth is very fast.
Doubling the absolute temperature multiplies the radiated power by sixteen.
This is why radiation is a minor effect for a warm cup of coffee but the main way a furnace or a star loses heat.

### L2 human

The net radiation between a small grey body at $T_1$ and large surroundings at $T_2$ is $\varepsilon \sigma A (T_1^4 - T_2^4)$, a basic formula of radiative heat transfer.
Linearising it gives a radiation heat transfer coefficient $4 \varepsilon \sigma T^3$ for small temperature differences.
The law is used to estimate the temperatures of stars and planets from their power output.
