---
tag: 1J2YM04YYY
kind: concept
name: Hubbard–Stratonovich transformation
msc: [82B05, 81S40]
sources:
  - url: https://en.wikipedia.org/wiki/Hubbard%E2%80%93Stratonovich_transformation
same_as:
  wikidata: Q17027759
  wikipedia: Hubbard–Stratonovich transformation
---

## Summary

The Hubbard–Stratonovich transformation writes the exponential of a quadratic expression as a [[Gaussian integral|0DFT1GP1JP]] over an auxiliary variable.
The integrand is an exponential that is linear in the original variables.
In a partition function this replaces an interaction between particles or spins by the coupling of each of them to a fluctuating auxiliary field.
The particles then become independent for each fixed value of the field.
The remaining integral over the field can be treated by saddle-point methods or numerically.
It is the standard route from interacting models to field theories and to [[mean-field theory|1DGJYHG10E]].

## Explanations

### L1 human

The trick rests on one formula: the exponential of $x^2$ is an average, over a Gaussian variable $y$, of the exponential of $x y$.
A square couples a quantity with itself, but $x y$ is linear in $x$.
In a magnet the square is the total magnetization squared, which couples every spin to every other spin.
After the trick each spin only feels the auxiliary variable $y$, which acts like a magnetic field.
So the hard problem of many coupled spins becomes an easy problem of independent spins, followed by one integral over $y$.
