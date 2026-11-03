---
tag: KZ8A16DTKX
kind: definition
name: Quantum Hall effect
msc: [81V70, 82D20]
defines: 11AZ4RGXVN
uses: [CX8GDHENTT]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Hall_effect
---

## Definition

Consider a two-dimensional system of electrons, of charge $-e$ and density $n$, in a perpendicular magnetic field of strength $B$, at low temperature.
A current $I$ flows along the $x$-direction; let $V_x$ be the voltage along the current and $V_H$ the voltage across it.
The longitudinal and Hall resistances are $R_{xx} = V_x / I$ and $R_{xy} = V_H / I$.
The system shows the *quantum Hall effect* if there are intervals of $B$ or of $n$, called plateaus, with the following property.
On each plateau there is a constant $\nu$ such that
$$R_{xy} = \frac{h}{\nu e^2} \quad \text{and} \quad R_{xx} = 0.$$
In the *integer* quantum Hall effect $\nu$ is a positive integer; in the *fractional* effect $\nu$ is a fraction such as $1/3$ or $2/5$.

## Remarks

The filling factor is $\nu_{\mathrm{f}} = nh/(eB)$, the number of filled Landau levels, the levels $E_j = \hbar\omega_c(j + \tfrac12)$, $\omega_c = eB/m$, of an electron in the field.
The plateaus with integer $\nu$ appear around integer filling factors.
On a plateau the Hall conductance is $\sigma_{xy} = \nu e^2/h$, and for the integer effect $\nu$ is a sum of Chern numbers of filled bands, the [[TKNN invariant|CX8GDHENTT]].

Example: on the plateau $\nu = 1$, $R_{xy} = h/e^2 \approx 25812.807\ \Omega$, the von Klitzing constant.

Non-example: in the classical (Drude) Hall effect, $R_{xy} = B/(ne)$ grows linearly with $B$ and has no plateaus, and $R_{xx}$ does not vanish.
