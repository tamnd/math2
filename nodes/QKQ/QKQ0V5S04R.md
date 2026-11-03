---
tag: QKQ0V5S04R
kind: statement
role: theorem
name: Planck's law
msc: [80A21, 78A40, 82B30]
uses: [A2RMYX8A65, S6XR2K4N8G, AJ8M9MGZGF, VETMCF1NQ5]
about: [A2RMYX8A65]
sources:
  - url: https://en.wikipedia.org/wiki/Planck%27s_law
same_as:
  wikidata: Q212986
  wikipedia: Planck's law
---

## Statement

Let a [[black body|A2RMYX8A65]] be in thermal equilibrium at absolute [[temperature|AJ8M9MGZGF]] $T > 0$.
Let $h$ be the Planck constant, $c$ the speed of light in vacuum and $k_B$ the Boltzmann constant.
Then, in every direction, its spectral radiance per unit frequency at frequency $\nu > 0$ is
$$B_\nu(\nu, T) = \frac{2 h \nu^3}{c^2} \, \frac{1}{e^{h\nu / (k_B T)} - 1}.$$
Here spectral radiance is the emitted power per unit area normal to the direction, per unit solid angle and per unit frequency.
Equivalently, the spectral radiance per unit wavelength at wavelength $\lambda > 0$ is
$$B_\lambda(\lambda, T) = \frac{2 h c^2}{\lambda^5} \, \frac{1}{e^{hc / (\lambda k_B T)} - 1}.$$

## Remarks

Proof idea: in a cavity, the number of electromagnetic modes per unit volume and unit frequency is $8\pi \nu^2 / c^3$.
If each mode of frequency $\nu$ can hold only energies $n h \nu$ with $n = 0, 1, 2, \dots$, the Boltzmann distribution gives the mean energy $h\nu / (e^{h\nu/(k_B T)} - 1)$ per mode.
Multiplying gives the energy density $u_\nu$, and the radiance is $B_\nu = c \, u_\nu / (4\pi)$.
The second form follows from $B_\lambda \, |d\lambda| = B_\nu \, |d\nu|$ with $\nu = c/\lambda$.

For $h\nu \ll k_B T$ the law reduces to the Rayleigh–Jeans law $B_\nu \approx 2 \nu^2 k_B T / c^2$, and for $h\nu \gg k_B T$ to Wien's approximation $B_\nu \approx (2h\nu^3/c^2) e^{-h\nu/(k_B T)}$.
Integrating over frequency gives the Stefan–Boltzmann law, and locating the maximum gives Wien's displacement law.
Max Planck found the law in 1900.

## Explanations

### L1 human

Planck's law tells exactly how much light of each colour a perfectly black object emits at a given temperature.
The curve is small at long wavelengths, rises to a peak, and falls off steeply at short wavelengths.
Hotter objects give a higher curve with the peak shifted toward blue.
Explaining this curve required the idea that light energy comes in packets, which started quantum theory.

### L2 human

The law is the reference spectrum of radiative heat transfer: real surfaces are described by their [[emissivity|VETMCF1NQ5]] relative to it.
The two classical limits show where classical physics works: at low frequency equipartition is correct, and at high frequency the quantisation of energy suppresses emission.
The same formula describes the cosmic microwave background, which fits a black-body spectrum at about $2.7$ K.
