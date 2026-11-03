---
tag: 5XTSCZCF7Z
kind: concept
name: Renormalization group
msc: [82B28, 81T17, 82B27]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
same_as:
  wikidata: Q1203669
  wikipedia: Renormalization group
---

## Summary

The renormalization group is a family of transformations that average out the short-distance details of a system and rescale lengths.
Each transformation maps a Hamiltonian to an effective one.
Repeating the transformation follows a flow in the space of couplings.
Critical points correspond to [[fixed points|H0B5TN4139]] of this flow, and the eigenvalues of the linearized flow there give the [[critical exponents|SQ41AZGZ2P]].
It explains scaling and [[universality|GWXP0KSW9Y]], and in quantum field theory it describes how couplings change with the energy scale.

## Explanations

### L1 human

Look at a photo of a magnet near its critical point, then blur it and shrink it.
Far from the critical point, the blurred picture looks more and more uniform, either all aligned or all random.
At the critical point, the blurred picture looks just like the original, because there are patches of every size.
The renormalization group turns this zooming out into a map on Hamiltonians, as in the [[block spin|H5PQFQS6CE]] construction.
For the Ising chain, summing over every second spin turns the coupling $K$ into a weaker coupling $K'$ with $\tanh K' = \tanh^2 K$.
So the chain is disordered at every positive temperature.
