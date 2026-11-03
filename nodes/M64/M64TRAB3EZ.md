---
tag: M64TRAB3EZ
kind: statement
role: theorem
name: Wien's displacement law
msc: [80A21, 78A40]
uses: [A2RMYX8A65, AJ8M9MGZGF, QKQ0V5S04R]
about: [A2RMYX8A65]
sources:
  - url: https://en.wikipedia.org/wiki/Wien%27s_displacement_law
same_as:
  wikidata: Q214336
  wikipedia: Wien's displacement law
---

## Statement

Let a [[black body|A2RMYX8A65]] be in thermal equilibrium at absolute [[temperature|AJ8M9MGZGF]] $T > 0$.
Let $\lambda_{\max}$ be the wavelength at which its spectral radiance per unit wavelength $B_\lambda(\lambda, T)$ is largest.
Then
$$\lambda_{\max} \, T = b,$$
where $b = hc / (x_0 k_B) \approx 2.898 \times 10^{-3}$ m K, and $x_0 \approx 4.965$ is the positive solution of $x = 5(1 - e^{-x})$.
Here $h$ is the Planck constant, $c$ the speed of light and $k_B$ the Boltzmann constant.

## Remarks

Proof idea: by [[Planck's law|QKQ0V5S04R]], $B_\lambda$ is a constant times $T^5 f(x)$ with $x = hc/(\lambda k_B T)$ and $f(x) = x^5 / (e^x - 1)$.
Setting $f'(x) = 0$ gives $5(e^x - 1) = x e^x$, that is $x = 5(1 - e^{-x})$, which has one positive root $x_0$.
So the maximum sits at a fixed value of $\lambda T$.

Example: the Sun at about $5772$ K has $\lambda_{\max} \approx 502$ nm, in the visible; a human body at $310$ K has $\lambda_{\max} \approx 9.3$ micrometres, in the infrared.
The peak of the spectrum per unit frequency is not at $c/\lambda_{\max}$: it is at $\nu_{\max} = x_1 k_B T / h$ with $x_1 \approx 2.821$ the root of $x = 3(1 - e^{-x})$.
Wilhelm Wien derived the law in 1893, before Planck's law was known.

## Explanations

### L1 human

The hotter an object, the shorter the wavelength at which it glows most brightly.
That is why a heated iron bar glows first red, then orange, then yellow-white.
The peak wavelength times the temperature is always the same number.

### L2 human

The law lets one read off a temperature from the colour of a thermal source, which is how the surface temperatures of stars are estimated.
In engineering it tells which spectral range matters.
For furnace and room-temperature surfaces most energy lies in the infrared.
