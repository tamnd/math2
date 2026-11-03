---
tag: PJZ35X5QHM
kind: example
name: Transverse-field Ising model
msc: [82B20, 82B10, 82B26]
instance_of: [PAEME5EQRM]
uses: [PAEME5EQRM, R0KGM32QN6, EY0X2NKA3S, N8HS434PPV, 94PEKQHHHT]
sources:
  - url: https://en.wikipedia.org/wiki/Transverse-field_Ising_model
same_as:
  wikidata: Q85810512
  wikipedia: Transverse-field Ising model
---

## Example

Let $L \ge 2$ and let $\mathcal{H} = (\C^2)^{\otimes L}$ be the [[tensor product|EY0X2NKA3S]] space of $L$ spins $\tfrac12$.
Let $\sigma^x_j, \sigma^z_j$ be the Pauli matrices acting on site $j$, with $\sigma^z_{L+1} = \sigma^z_1$.
For $J > 0$ and $h \ge 0$, the *transverse-field Ising chain* is the [[lattice model|PAEME5EQRM]] with Hamiltonian
$$H = -J \sum_{j=1}^{L} \sigma^z_j \sigma^z_{j+1} - h \sum_{j=1}^{L} \sigma^x_j.$$
The first term is the [[Ising model|R0KGM32QN6]] coupling and the second is a magnetic field perpendicular to the Ising axis.
Check at the two ends.
For $h = 0$ the ground states are the two aligned states $\lvert\uparrow\cdots\uparrow\rangle$ and $\lvert\downarrow\cdots\downarrow\rangle$, with energy $-JL$.
For $J = 0$ the unique ground state has every spin in the $+1$ eigenstate of $\sigma^x$, with energy $-hL$.

## Remarks

The two terms do not commute, so the model is genuinely quantum even though it is built from Ising variables.
The [[Jordan–Wigner transformation|94PEKQHHHT]] maps it to free fermions, which was done by Pfeuty (1970); the single-particle energies are $\varepsilon_k = 2\sqrt{J^2 + h^2 - 2Jh\cos k}$.
The gap $\min_k \varepsilon_k = 2\abs{J - h}$ closes at $h = J$, which is a [[quantum phase transition|N8HS434PPV]] between a ferromagnetically ordered phase for $h < J$ and a paramagnetic phase for $h > J$.
The chain is dual to itself under the Kramers–Wannier map, which exchanges $J$ and $h$ and so explains why the transition sits at $h = J$.
The $d$-dimensional quantum model is related to the classical Ising model in $d + 1$ dimensions through the transfer matrix.

## Explanations

### L1 human

Start with a row of magnets that want to line up with their neighbours, either all up or all down.
Now add a sideways magnetic field, which pushes each magnet to point sideways instead.
When the sideways field is weak the magnets still mostly agree on up or down; when it is strong they all point sideways and lose the up-down order.
The switch between these two behaviours happens at zero temperature, driven only by quantum effects, at the point where the field equals the coupling.
