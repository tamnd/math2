---
tag: ANNJ7JR36T
kind: statement
role: proposition
name: Bekenstein–Hawking entropy
msc: ["83C57", "83C47", "80A10"]
uses: [46QNBD585F, Z1Y6E4YCTZ]
about: [YHJ0PDNY8T]
sources:
  - url: https://en.wikipedia.org/wiki/Black_hole_thermodynamics
---

## Statement

Let a stationary black hole have horizon area $A$ and surface gravity $\kappa$.
Let $G$ be the gravitational constant, $c$ the speed of light, $\hbar$ the reduced Planck constant and $k_B$ the Boltzmann constant.
Define the Hawking temperature and the Bekenstein–Hawking entropy by
$$T_H = \frac{\hbar \kappa}{2\pi c\, k_B}, \qquad S_{BH} = \frac{k_B c^3 A}{4 G \hbar}.$$
Then the first of the [[laws of black hole mechanics|46QNBD585F]] takes the thermodynamic form
$$\delta(M c^2) = T_H\, \delta S_{BH} + \Omega_H\, \delta J + \Phi_H\, \delta Q.$$

## Remarks

The identity is a direct substitution: $T_H\, \delta S_{BH} = \frac{\hbar\kappa}{2\pi c k_B} \cdot \frac{k_B c^3}{4 G \hbar}\, \delta A = \frac{\kappa c^2}{8\pi G}\, \delta A$, which is the area term of the first law in SI units.
The physical content is that $T_H$ is the temperature of the [[Hawking radiation|Z1Y6E4YCTZ]], so that $S_{BH}$ is the entropy that thermodynamics then assigns to the black hole.
Bekenstein proposed in 1972 that a black hole has an entropy proportional to its area, and Hawking's computation of $T_H$ fixed the factor $1/4$.
In Planck units the formula reads $S_{BH} = A/4$, one quarter of the area measured in Planck areas.

Example: for a Schwarzschild black hole of mass $M$, $A = 16\pi G^2 M^2/c^4$, so $S_{BH} = 4\pi k_B G M^2/(\hbar c)$.
For one solar mass this is of order $10^{77} k_B$, far more than the entropy of the star that collapsed.

## Explanations

### L1 human

A black hole hides everything that falls in, but the second law of thermodynamics says that entropy cannot just vanish.
Bekenstein and Hawking showed that a black hole itself carries entropy, equal to a quarter of its horizon area in Planck units.
This makes black holes the objects with the most entropy for their size.

### L2 human

The Bekenstein–Hawking entropy is the bridge between gravity and quantum theory.
It suggests that the number of quantum states of a black hole is about $e^{S_{BH}/k_B}$, a number that grows with the area and not with the volume.
Explaining this count from a microscopic theory is a test for any quantum theory of gravity; string theory reproduced it for certain extremal black holes.
It also leads to the generalised second law, that the sum of $S_{BH}$ and the ordinary entropy outside never decreases, and to the [[Bekenstein bound|7C2CSSHPKA]].
