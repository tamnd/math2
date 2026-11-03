---
tag: FKZK5B1XED
kind: example
name: Anderson impurity model
msc: [82D35, 82B10, 82D40]
uses: [3B76W03AN7, DVQ0PVHKY1]
illustrates: [DVQ0PVHKY1]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson_impurity_model
same_as:
  wikidata: Q4754237
  wikipedia: Anderson impurity model
---

## Example

Let $c_{k\sigma}$ be fermion operators for the conduction electrons of a metal, labelled by a momentum $k$ and a spin $\sigma \in \set{\uparrow, \downarrow}$, with energies $\varepsilon_k$.
Let $d_\sigma$ be fermion operators for one localized orbital of an impurity atom, with $n_{d\sigma} = d_\sigma^\dagger d_\sigma$.
For an orbital energy $\varepsilon_d \in \R$, an on-site repulsion $U \ge 0$ and hybridization amplitudes $V_k$, the *Anderson impurity model* (Anderson, 1961) has Hamiltonian
$$H = \sum_{k, \sigma} \varepsilon_k c_{k\sigma}^\dagger c_{k\sigma} + \sum_\sigma \varepsilon_d n_{d\sigma} + U n_{d\uparrow} n_{d\downarrow} + \sum_{k, \sigma}\big(V_k d_\sigma^\dagger c_{k\sigma} + \overline{V_k}\, c_{k\sigma}^\dagger d_\sigma\big).$$
Check without hybridization, $V_k = 0$: the impurity has the four states empty, $\uparrow$, $\downarrow$ and doubly occupied, with energies $0$, $\varepsilon_d$, $\varepsilon_d$ and $2\varepsilon_d + U$.
When $\varepsilon_d < 0 < \varepsilon_d + U$, the singly occupied states are lowest, so the impurity carries a local magnetic moment.

## Remarks

It is a one-site version of the [[Hubbard model|3B76W03AN7]] coupled to a band: the interaction acts only on the impurity orbital.
For $U = 0$ the Hamiltonian is quadratic and exactly solvable; the impurity level broadens into a resonance around $\varepsilon_d$ of half-width $\Gamma = \pi \sum_k \abs{V_k}^2 \delta(\varepsilon_d - \varepsilon_k)$, for a band that varies slowly near $\varepsilon_d$.
In the local-moment regime and for small hybridization, the Schrieffer–Wolff transformation (1966) maps the low-energy physics to the Kondo model.
The resulting coupling is antiferromagnetic and of order $\abs{V}^2 \big(\tfrac{1}{\varepsilon_d + U} - \tfrac{1}{\varepsilon_d}\big)$, with $V$ the hybridization at the Fermi level.
The model is [[exactly solvable|DVQ0PVHKY1]] by the Bethe ansatz for a linear dispersion with constant hybridization, and it is the impurity problem that dynamical mean-field theory solves self-consistently.

## Explanations

### L1 human

A metal contains a sea of mobile electrons, and an impurity atom inside it has one special orbital where electrons can sit.
Two electrons on that orbital repel each other strongly, so it often holds just one, which acts like a tiny magnet.
Electrons can also jump between the orbital and the sea.
The model asks how the sea and the tiny magnet affect each other, which explains, for example, why some metals with magnetic impurities show a resistance minimum at low temperature.
