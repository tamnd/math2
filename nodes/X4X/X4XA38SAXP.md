---
tag: X4XA38SAXP
kind: example
name: Kondo model
msc: [82D35, 82D40, 82B10]
uses: [FKZK5B1XED, S92G5M6X41, DVQ0PVHKY1]
illustrates: [DVQ0PVHKY1]
sources:
  - url: https://en.wikipedia.org/wiki/Kondo_model
same_as:
  wikidata: Q1781236
  wikipedia: Kondo model
---

## Example

Let $c_{k\sigma}$ be fermion operators for the conduction electrons of a metal, with energies $\varepsilon_k$.
Let $\psi_\sigma = N^{-1/2}\sum_k c_{k\sigma}$ annihilate an electron at the impurity site, where $N$ is the number of momenta.
Let $\mathbf{S}$ be the spin-$\tfrac12$ operator of a localized impurity.
Let $\mathbf{s} = \tfrac12 \sum_{\alpha, \beta} \psi_\alpha^\dagger \boldsymbol{\sigma}_{\alpha\beta} \psi_\beta$ be the conduction-electron spin at the impurity site, with $\boldsymbol{\sigma}$ the Pauli matrices.
For a coupling $J \in \R$, the *Kondo model* has Hamiltonian
$$H = \sum_{k, \sigma} \varepsilon_k c_{k\sigma}^\dagger c_{k\sigma} + J\, \mathbf{S} \cdot \mathbf{s}.$$
The coupling is antiferromagnetic for $J > 0$.
Check on the interaction alone, with a single conduction electron at the impurity site: $\mathbf{S} \cdot \mathbf{s} = \tfrac12\big((\mathbf{S} + \mathbf{s})^2 - \tfrac32\big)$.
So the singlet has energy $-\tfrac34 J$ and the triplet $\tfrac14 J$.
For $J > 0$ the conduction electron tends to screen the impurity spin.

## Remarks

The model arises from the [[Anderson impurity model|FKZK5B1XED]] in the local-moment regime by the Schrieffer–Wolff transformation.
Kondo (1964) showed that third-order perturbation theory in $J$ gives a contribution to the resistivity proportional to $\ln T$, which explains the resistance minimum of metals with magnetic impurities.
This logarithm signals that perturbation theory breaks down below the Kondo temperature $T_K$.
With $\rho$ the density of states at the Fermi level, $T_K$ scales as $\exp(-c/(\rho J))$, with a constant $c$ fixed by the normalization of $J$.
Wilson's numerical renormalization group (1975) showed that for $J > 0$ the impurity spin is screened at low temperature, forming a singlet with the conduction electrons.
The model is [[exactly solvable|DVQ0PVHKY1]]: Andrei and Wiegmann solved it by the [[Bethe ansatz|S92G5M6X41]] in 1980.

## Explanations

### L1 human

A magnetic atom placed in a metal has a spin that interacts with the spins of the surrounding mobile electrons.
At high temperature the atom behaves like a free little magnet.
As the temperature drops, the electrons gather around it and cancel its magnetism, forming a cloud with zero total spin.
This crossover, the Kondo effect, explains why the resistance of some metals rises again at very low temperature.
