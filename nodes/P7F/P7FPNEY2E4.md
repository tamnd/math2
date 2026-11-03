---
tag: P7FPNEY2E4
kind: statement
role: proposition
name: Rayleigh–Jeans law
msc: [80A21, 78A40]
uses: [A2RMYX8A65, AJ8M9MGZGF, QKQ0V5S04R]
about: [A2RMYX8A65]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Jeans_law
same_as:
  wikidata: Q849484
  wikipedia: Rayleigh–Jeans law
---

## Statement

Let a [[black body|A2RMYX8A65]] be in thermal equilibrium at absolute [[temperature|AJ8M9MGZGF]] $T > 0$, with spectral radiance per unit frequency $B_\nu(\nu, T)$.
Let $h$ be the Planck constant, $c$ the speed of light and $k_B$ the Boltzmann constant.
Then, in the limit of low frequency,
$$B_\nu(\nu, T) = \frac{2 \nu^2 k_B T}{c^2} \big(1 + O(h\nu / k_B T)\big) \quad \text{as } \frac{h\nu}{k_B T} \to 0.$$
So $B_\nu \approx 2 \nu^2 k_B T / c^2$ when $h\nu \ll k_B T$.

## Remarks

From [[Planck's law|QKQ0V5S04R]], with $x = h\nu/(k_B T)$, one has $B_\nu = \frac{2\nu^2 k_B T}{c^2} \cdot \frac{x}{e^x - 1}$, and $x/(e^x - 1) = 1 - x/2 + O(x^2)$ as $x \to 0$.
Classically, the law follows from equipartition: each of the $8\pi\nu^2/c^3$ cavity modes per unit volume and frequency gets the mean energy $k_B T$.

Without the low-frequency hypothesis the law fails badly.
It grows like $\nu^2$ without bound, so its integral over all frequencies diverges; this is the ultraviolet catastrophe, which showed that classical physics cannot describe black-body radiation.
The law is named after Lord Rayleigh and James Jeans.

## Explanations

### L1 human

Before quantum theory, physicists computed the radiation of a hot black object with classical physics and got this formula.
It matches experiments for long wavelengths, such as radio waves and far infrared.
For short wavelengths it predicts ever more radiation, and so infinite total energy, which is absurd.
Fixing this failure led to Planck's law.

### L2 human

In radio astronomy and microwave remote sensing, $h\nu \ll k_B T$ holds, and the law makes radiance proportional to temperature.
This is why radio brightness is often reported as a brightness temperature.
