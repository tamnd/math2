---
tag: HQFRMB87MW
kind: statement
role: theorem
name: Lifshitz–Slyozov–Wagner theory of coarsening
msc: [82C24, 82C26, 82C70]
uses: [1DGJYHG10E]
about: [1DGJYHG10E]
sources:
  - url: https://en.wikipedia.org/wiki/Ostwald_ripening
---

## Statement

Consider the Lifshitz–Slyozov–Wagner (LSW) model of a dilute dispersion of spherical particles of a second phase, growing or shrinking by diffusion through the matrix.
Each particle has a radius $R > 0$, which evolves by
$$\frac{dR}{dt} = \frac{A}{R}\Big(\frac{1}{R_c(t)} - \frac{1}{R}\Big),$$
where $A > 0$ is a material constant.
The critical radius $R_c(t)$ is fixed at each time by requiring that the total volume of the particles is conserved.
Lifshitz, Slyozov and Wagner found a self-similar solution with the following properties.

1. The critical radius and the mean radius coincide and grow as $\langle R \rangle^3 = \tfrac{4}{9} A\, t$ up to an additive constant, that is, $\langle R \rangle \sim t^{1/3}$.
2. The number of particles per unit volume decays as $t^{-1}$.
3. The distribution of the scaled radius $R / \langle R \rangle$ is a fixed profile, independent of time, supported on $[0, \tfrac32]$.

For diffusion-limited growth, $A = 2\gamma c_\infty v_m^2 D / (R_g T)$.
Here $\gamma$ is the interfacial energy, $c_\infty$ the solubility at a flat interface, and $v_m$ the molar volume.
Also $D$ is the diffusion coefficient, $R_g$ the gas constant and $T$ the temperature.
So $\langle R \rangle^3 - \langle R \rangle_0^3 = \tfrac{8 \gamma c_\infty v_m^2 D}{9 R_g T}\, t$.

## Remarks

The growth law reflects the Gibbs–Thomson effect: small particles have higher solubility, so they dissolve and feed the larger ones.
In the equation, particles with $R < R_c$ shrink and particles with $R > R_c$ grow, and volume conservation forces $R_c$ to grow.
A scaling ansatz $R = R_c(t)\, u$ with $R_c^3 \propto t$ reduces the problem to an ordinary differential equation in $u$, whose admissible solution singles out the profile in item 3.
The model is mean-field: it neglects interactions between particles, so it describes the limit of vanishing volume fraction.
Mathematically, the LSW profile is only one of a family of self-similar solutions.
Niethammer and Pego showed that which one is reached depends on the tail of the initial size distribution.

## Explanations

### L1 human

In a mixture where small droplets or grains of one phase sit inside another, the small ones slowly disappear and the large ones grow.
This happens because atoms leave small, strongly curved particles more easily.
The theory predicts that the typical particle size grows like the cube root of time.
The same effect makes ice cream grainy over time and coarsens the microstructure of alloys.

### L2 human

Lifshitz and Slyozov (1961) and Wagner (1961) gave the first quantitative theory of this late stage of phase separation, called Ostwald ripening.
The $t^{1/3}$ law is the conserved-order-parameter analogue of the $t^{1/2}$ law for non-conserved coarsening, and it also appears in the Cahn–Hilliard equation.
The model is a nonlocal transport equation for the size distribution, and its long-time behaviour is a selection problem among self-similar solutions.
Experiments confirm the $t^{1/3}$ law well, while the measured size distributions are usually broader than the LSW profile at finite volume fraction.
