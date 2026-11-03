---
tag: 94PEKQHHHT
kind: concept
name: Jordan–Wigner transformation
msc: [82B20, 81V74, 81S05]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Wigner_transformation
same_as:
  wikidata: Q898893
  wikipedia: Jordan–Wigner transformation
---

## Summary

The Jordan–Wigner transformation turns spin-$1/2$ operators on a chain of sites into fermion creation and annihilation operators.
It attaches to the spin-lowering operator at site $j$ a string of sign operators on all the sites to the left of $j$.
The string turns the commutation of operators on different sites into the anticommutation that fermions need.
It maps some spin chains, such as the transverse-field Ising chain and the XY chain, to free fermions, which can then be solved exactly.

## Explanations

### L1 human

A spin-$1/2$ at a site is either up or down, and a fermion orbital is either empty or full, so one site looks like one orbital.
The difference is in the sign rules: spins on different sites commute, while fermions on different orbitals anticommute.
The transformation fixes this by counting the occupied sites to the left and multiplying by $-1$ for each of them.
For example, a nearest-neighbour exchange term $\sigma^x_j \sigma^x_{j+1} + \sigma^y_j \sigma^y_{j+1}$ becomes a fermion hopping term $2(c_j^\dagger c_{j+1} + c_{j+1}^\dagger c_j)$.
This only works so simply in one dimension, where "to the left" has a clear meaning.
