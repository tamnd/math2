---
tag: 9YJ1T3TW4S
kind: definition
name: Effective medium approximations
msc: [74Q15, "74E30", 78A48]
defines: VSBFY8EN2H
uses: [5RSREPYN0F]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_medium_approximations
---

## Definition

Let a composite in $\R^d$ consist of $n$ phases with conductivities $\sigma_1, \dots, \sigma_n > 0$ and volume fractions $f_1, \dots, f_n \ge 0$, with $f_1 + \cdots + f_n = 1$.
Its *effective conductivity* $\sigma^*$ is the matrix given by [[homogenization|5RSREPYN0F]].
It relates the averages of the current $J$ and of the electric field $E$ by $\langle J \rangle = \sigma^* \langle E \rangle$.
An *effective medium approximation* is an explicit formula $\sigma^* \approx \Phi(\sigma_1, \dots, \sigma_n; f_1, \dots, f_n)$ derived from a simplified model of the microstructure.
The same name is used for the analogous formulas for the dielectric constant, the elastic moduli and other linear properties.

## Remarks

The *Bruggeman approximation* for an isotropic mixture of spherical grains in $\R^d$ defines $\sigma^* > 0$ as the solution of
$$\sum_{i=1}^n f_i \, \frac{\sigma_i - \sigma^*}{\sigma_i + (d-1)\sigma^*} = 0.$$
Check for one phase ($n = 1$, $f_1 = 1$): the equation forces $\sigma^* = \sigma_1$, as it must.
For two phases in $\R^2$ with $f_1 = f_2 = 1/2$, the equation gives $\sigma^* = \sqrt{\sigma_1 \sigma_2}$, which is the exact value for the two-dimensional checkerboard, by Keller's interchange theorem.
Non-example: the exact effective conductivity of a laminate measured across the layers is the harmonic mean $(\sum_i f_i / \sigma_i)^{-1}$; it is computed exactly from the geometry and is not an approximation.
Every reasonable approximation should lie between the harmonic and arithmetic means of the $\sigma_i$, the conductivity analogue of the [[Voigt and Reuss bounds|Y7WKXDD9SJ]].
For isotropic mixtures it should also lie between the sharper [[Hashin–Shtrikman bounds|FZGYFV69HK]].

## Explanations

### L1 human

The exact effective property of a mixture depends on every detail of how the phases are arranged.
An effective medium approximation forgets most of these details and keeps only the volume fractions and a picture of a typical grain.
It then gives a formula that is easy to evaluate.
