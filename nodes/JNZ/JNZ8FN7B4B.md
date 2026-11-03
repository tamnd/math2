---
tag: JNZ8FN7B4B
kind: definition
name: Universality class
msc: [82B27, 82B28]
defines: GWXP0KSW9Y
uses: [57789VKKAY, SQ41AZGZ2P]
sources:
  - url: https://en.wikipedia.org/wiki/Universality_class
---

## Definition

Consider the [[critical points|57789VKKAY]] of lattice models of statistical mechanics.
Call two critical points *equivalent* if:

1. their [[critical exponents|SQ41AZGZ2P]] $\alpha, \beta, \gamma, \delta, \nu, \eta$ are equal;
2. their scaling functions agree after a rescaling of the temperature, the field and the lengths by constant factors.

A *universality class* is an equivalence class of critical points for this relation.

## Remarks

Example: the nearest-neighbour Ising model on the square lattice and on the triangular lattice.
Both are exactly solved, and both have $\alpha = 0$, $\beta = 1/8$, $\gamma = 7/4$, $\delta = 15$, $\nu = 1$, $\eta = 1/4$; they lie in the two-dimensional Ising class.

Non-example: the three-state Potts model on the square lattice has $\beta = 1/9$ and $\nu = 5/6$.
So clause 1 fails, and it is not in the Ising class, although both models are two-dimensional with short-range interactions.
The difference comes from the symmetry group of the order parameter, $\Z/3$ or $S_3$ instead of $\Z/2$.

Many authors use clause 1 alone, since exponents are easier to compute or measure than scaling functions.
