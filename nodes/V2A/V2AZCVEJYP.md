---
tag: V2AZCVEJYP
kind: example
name: Debye model
msc: [82D20, 82D25, 82B10]
illustrates: [R5HWSRAK4H]
uses: [R5HWSRAK4H, G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Debye_model
same_as:
  wikidata: Q1151031
  wikipedia: Debye model
---

## Example

The *Debye model* treats the vibrations of a crystal of $N$ atoms as sound waves, or phonons.
Their dispersion is linear, $\omega = v_s \abs{k}$, where $v_s$ is a sound speed.
Counting plane-wave modes in a large box gives a number of modes proportional to $\omega^2 \, d\omega$.
The model cuts the frequencies off at the Debye frequency $\omega_D$, chosen so that the total number of modes is $3N$.
So the density of modes is
$$g(\omega) = \frac{9 N \omega^2}{\omega_D^3} \quad (0 \le \omega \le \omega_D), \qquad \text{check: } \int_0^{\omega_D} \frac{9 N \omega^2}{\omega_D^3} \, d\omega = 3N.$$
Phonons obey [[Bose–Einstein statistics|R5HWSRAK4H]] with chemical potential $0$, so a mode of frequency $\omega$ has mean energy $\hbar\omega / (e^{\hbar \omega / k_B T} - 1)$ above its zero-point energy.
With the Debye temperature $\Theta_D = \hbar \omega_D / k_B$, the heat capacity is
$$C_V = 9 N k_B \left( \frac{T}{\Theta_D} \right)^3 \int_0^{\Theta_D / T} \frac{x^4 e^x}{(e^x - 1)^2} \, dx.$$

## Remarks

At high temperature the integrand is about $x^2$, the integral is about $(\Theta_D/T)^3/3$, and $C_V \to 3 N k_B$, the Dulong–Petit value.
At low temperature the upper limit tends to infinity, and $\int_0^\infty \frac{x^4 e^x}{(e^x - 1)^2} dx = \frac{4\pi^4}{15}$, so
$$C_V \approx \frac{12 \pi^4}{5} N k_B \left( \frac{T}{\Theta_D} \right)^3.$$
This is the Debye $T^3$ law, which matches measurements on insulating crystals and corrects the exponential fall of the [[Einstein solid|NTR1NH6X6R]].
The same counting with photons in place of phonons, and no cut-off, gives the $T^4$ law of black-body radiation.

## Explanations

### L1 human

Instead of giving every atom the same vibration frequency, the Debye model lets the crystal carry sound waves of all wavelengths down to the spacing between atoms.
Long waves have low frequency, so even at very low temperature some of them can be excited.
There are few such long waves, and their number grows like $T^3$ as the temperature rises, which gives a heat capacity proportional to $T^3$.
At high temperature every mode is excited and the model agrees with the classical result $3 N k_B$.
