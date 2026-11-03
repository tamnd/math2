---
tag: YC9TY98HJZ
kind: statement
role: proposition
name: Star–triangle relation
msc: [82B20, 82B23]
uses: [R0KGM32QN6]
about: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Yang%E2%80%93Baxter_equation
---

## Statement

Let $K_1, K_2, K_3$ be real numbers.
Set
$$c_0 = \cosh(K_1 + K_2 + K_3), \quad c_1 = \cosh(-K_1 + K_2 + K_3), \quad c_2 = \cosh(K_1 - K_2 + K_3), \quad c_3 = \cosh(K_1 + K_2 - K_3).$$
Define
$$L_1 = \tfrac{1}{4} \log \frac{c_0 c_1}{c_2 c_3}, \quad L_2 = \tfrac{1}{4} \log \frac{c_0 c_2}{c_1 c_3}, \quad L_3 = \tfrac{1}{4} \log \frac{c_0 c_3}{c_1 c_2}, \quad R = 2 (c_0 c_1 c_2 c_3)^{1/4}.$$
Then for all $\sigma_1, \sigma_2, \sigma_3 \in \set{-1, +1}$,
$$\sum_{\sigma_0 \in \set{-1, +1}} e^{\sigma_0 (K_1 \sigma_1 + K_2 \sigma_2 + K_3 \sigma_3)} = R \, e^{L_1 \sigma_2 \sigma_3 + L_2 \sigma_3 \sigma_1 + L_3 \sigma_1 \sigma_2}.$$

## Remarks

The left side equals $2 \cosh(K_1 \sigma_1 + K_2 \sigma_2 + K_3 \sigma_3)$, which is unchanged when all three spins flip.
So it takes only the four values $2c_0, 2c_1, 2c_2, 2c_3$, at $(\sigma_1, \sigma_2, \sigma_3) = (+,+,+), (-,+,+), (+,-,+), (+,+,-)$.
The right side has four free constants, and taking logarithms gives a linear system in $\log R, L_1, L_2, L_3$ whose solution is the formula above.
In an [[Ising model|R0KGM32QN6]], a star is a centre spin joined to three spins with couplings $K_i$.
Summing out the centre replaces the star by a triangle on the three outer spins with couplings $L_i$.
Combined with [[Kramers–Wannier duality|GBM9TF1V7K]], it relates the Ising models on the honeycomb and triangular lattices to each other and to the square lattice.
It is the simplest instance of the [[Yang–Baxter equation|663BP8ZHS5]] in the form used for spin models.

## Explanations

### L1 human

Take one spin joined to three neighbouring spins, like the hub of a three-spoked wheel.
Summing over the two values of the centre spin leaves an effect on the three neighbours alone.
The relation says that this effect is exactly that of a triangle of direct couplings between them, with explicit strengths.

### L2 human

The star–triangle transformation lets one move between lattices: decimating every other site of a honeycomb lattice gives a triangular lattice.
Baxter turned its generalization into the main engine of exactly solvable models.
When the weights depend on a spectral parameter, the star–triangle relation makes transfer matrices with different parameters commute.
