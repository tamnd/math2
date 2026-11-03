---
tag: NTR1NH6X6R
kind: example
name: Einstein solid
msc: [82D20, 82B10]
illustrates: [G1P1A0N7NZ]
uses: [G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_solid
same_as:
  wikidata: Q1190709
  wikipedia: Einstein solid
---

## Example

The *Einstein solid* models a crystal of $N$ atoms as $3N$ independent quantum harmonic oscillators, all with the same angular frequency $\omega > 0$.
An oscillator has energy levels $\hbar \omega (n + \frac12)$ for $n = 0, 1, 2, \ldots$, where $\hbar$ is the reduced Planck constant.
In the [[canonical ensemble|G1P1A0N7NZ]] at temperature $T$, with $\beta = 1/(k_B T)$, one oscillator has partition function
$$Z_1 = \sum_{n \ge 0} e^{-\beta \hbar \omega (n + 1/2)} = \frac{e^{-\beta \hbar \omega / 2}}{1 - e^{-\beta \hbar \omega}}.$$
The mean energy of the solid is $U = -3N \, \partial_\beta \ln Z_1 = 3N \hbar \omega \left( \frac12 + \frac{1}{e^{\beta \hbar \omega} - 1} \right)$.
With the Einstein temperature $\Theta_E = \hbar \omega / k_B$ and $x = \Theta_E / T$, the heat capacity is
$$C_V = \frac{dU}{dT} = 3 N k_B \, \frac{x^2 e^x}{(e^x - 1)^2}.$$

## Remarks

At high temperature, $x \to 0$ and $x^2 e^x / (e^x - 1)^2 \to 1$, so $C_V \to 3 N k_B$: this is the Dulong–Petit law, as in the classical equipartition theorem.
At low temperature, $C_V \approx 3 N k_B \, x^2 e^{-x}$, which tends to $0$, as the third law of thermodynamics requires.
This explained why heat capacities of solids fall at low temperature, a puzzle for classical physics.
Measured heat capacities of insulating crystals fall like $T^3$, not exponentially; the [[Debye model|V2AZCVEJYP]] fixes this by allowing a spread of frequencies.

## Explanations

### L1 human

Picture each atom of a crystal tied to its place by springs, and treat each direction of wobble as a separate quantum spring.
A quantum spring can only take energy in packets of size $\hbar \omega$.
When the temperature is so low that $k_B T$ is much smaller than one packet, the springs can hardly absorb heat, and the heat capacity collapses.
When the temperature is high, the packets look small and each spring takes its classical share $k_B T$ of energy.
