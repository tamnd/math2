---
tag: SN45B41HSB
kind: definition
name: Optical soliton
msc: [78A60, 35C08, 35Q55]
defines: XQBA9P8QRE
uses: [BRJ36NF7KX, 63D4AXYCT4, A68PFZJ3ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Soliton_(optics)
---

## Definition

Let an optical field propagate along $z$ with complex envelope $A$, as in the [[nonlinear Schrödinger equation in optics|BRJ36NF7KX]] or a similar envelope equation.
Let $\xi$ be the time $T$ for a pulse, or the transverse position $(x, y)$ for a beam.
An *optical soliton* is a solution $A = U(\xi)\, e^{i \kappa z}$, with a real constant $\kappa$.
Here the profile $U$ is localized: it tends to $0$ at infinity.
So $\abs{A}$ does not depend on $z$.
A *temporal soliton* has $\xi = T$, and a *spatial soliton* has $\xi$ transverse.

## Remarks

The profile $U$ exists because the nonlinearity compensates dispersion or diffraction; it is a [[soliton|63D4AXYCT4]] in the broad sense of a localized wave of constant shape.

Example: in a fibre with $\beta_2 < 0$ and nonlinear coefficient $\gamma > 0$, take $U(T) = \sqrt{P_0}\, \mathrm{sech}(T / T_0)$ and $\kappa = \gamma P_0 / 2$ with $\gamma P_0 T_0^2 = \abs{\beta_2}$.
Since $\mathrm{sech}'' = \mathrm{sech} - 2\,\mathrm{sech}^3$, substitution in the pulse equation gives two conditions, one on the $\mathrm{sech}$ terms and one on the $\mathrm{sech}^3$ terms, and both hold.
This is the fundamental bright soliton.

Non-example: in a fibre with $\gamma = 0$, every localized pulse broadens under dispersion, so $\abs{A}$ changes with $z$ and no soliton exists.

In a medium with [[self-focusing|A68PFZJ3ZW]] in two transverse dimensions, spatial solitons exist but are unstable for the pure Kerr effect.
