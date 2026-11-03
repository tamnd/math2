---
tag: 663MJA8NAC
kind: example
name: Fermi gas
msc: [82D05, 82B10, 81V74]
illustrates: [FM6XWC4BST]
uses: [FM6XWC4BST, FPYQWE8X12]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi_gas
same_as:
  wikidata: Q1072904
  wikipedia: Fermi gas
---

## Example

An ideal *Fermi gas* is a system of $N$ non-interacting identical fermions obeying [[Fermi–Dirac statistics|FM6XWC4BST]].
Take spin-$1/2$ fermions of mass $m$ in a cubic box of volume $V$ in three dimensions, with periodic boundary conditions.
The single-particle states are plane waves with wave vector $k \in (2\pi / V^{1/3}) \Z^3$ and energy $\varepsilon = \hbar^2 \abs{k}^2 / (2m)$, each with two spin states; here $\hbar$ is the reduced Planck constant.

At temperature $T = 0$ the fermions fill the lowest states, one per state, up to a Fermi wave number $k_F$.
In the [[thermodynamic limit|FPYQWE8X12]] with density $n = N/V$ fixed, a ball of radius $k_F$ holds about $V k_F^3 / (6\pi^2)$ wave vectors, so
$$N = 2 \cdot \frac{V k_F^3}{6 \pi^2}, \qquad k_F = (3 \pi^2 n)^{1/3}, \qquad E_F = \frac{\hbar^2}{2m} (3 \pi^2 n)^{2/3}.$$
Check of the energy: the number of states with energy below $\varepsilon$ grows like $\varepsilon^{3/2}$, so the density of states is proportional to $\varepsilon^{1/2}$.
The mean energy per particle is then
$$\frac{\int_0^{E_F} \varepsilon \cdot \varepsilon^{1/2} \, d\varepsilon}{\int_0^{E_F} \varepsilon^{1/2} \, d\varepsilon} = \frac{2/5}{2/3} E_F = \frac{3}{5} E_F.$$

## Remarks

The total energy at $T = 0$ is $\frac35 N E_F > 0$, and the pressure is $P = \frac{2}{3} E / V = \frac{2}{5} n E_F > 0$.
This degeneracy pressure exists even at zero temperature; it holds up white dwarf stars against gravity.
At small positive temperature, the Sommerfeld expansion gives corrections in powers of $(k_B T / E_F)^2$.

## Explanations

### L1 human

Pour electrons into a box one at a time, and each must take an empty state, since two cannot share one.
The last ones in must sit at high energy, the Fermi energy, even though the box is cold.
So a cold Fermi gas still has a large kinetic energy and pushes outward on its walls.
Conduction electrons in a metal behave roughly like this, with a Fermi energy of a few electronvolts.
