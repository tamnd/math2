---
tag: E4VEYCFB25
kind: definition
name: Fermi surface
msc: [82D35, 82D20]
defines: GK3SVTXXKX
uses: [QP0TK2M29V, EKTERAYFJ2, FM6XWC4BST]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi_surface
---

## Definition

Consider non-interacting electrons in a crystal with [[band functions|QP0TK2M29V]] $E_m \colon B \to \R$, $m \ge 1$, on the [[Brillouin zone|EKTERAYFJ2]] $B$.
Let $E_F$ be the Fermi energy, the chemical potential at zero temperature fixed by the electron density.
The *Fermi surface* is the set
$$S_F = \set{k \in B : E_m(k) = E_F \text{ for some } m \ge 1}.$$
At zero temperature, by [[Fermi–Dirac statistics|FM6XWC4BST]], the states with $E_m(k) < E_F$ are occupied and those with $E_m(k) > E_F$ are empty.
So $S_F$ is the boundary of the occupied region in each band.

## Remarks

Example: free electrons in $\R^3$ with $E(k) = \hbar^2 \abs{k}^2 / 2m$.
The Fermi surface is the sphere $\abs{k} = k_F$ with $E_F = \hbar^2 k_F^2 / 2m$.
Counting two spin states per wave vector, the density is $n = 2 \cdot \tfrac{4}{3}\pi k_F^3 / (2\pi)^3 = k_F^3 / 3\pi^2$, so $k_F = (3\pi^2 n)^{1/3}$.

Example: for the one-dimensional tight-binding band $E(k) = -2t\cos k$ at half filling, $E_F = 0$ and the Fermi surface is the pair of points $k = \pm\pi/2$.

Non-example: in a band insulator $E_F$ lies in a spectral gap, so no $E_m$ takes the value $E_F$ and the Fermi surface is empty.
