---
tag: 6FPKEFX0X4
kind: concept
name: Orthomodular lattice
msc: [06C15, 81P10, 03G12]
specializes: [J7KN14DYV3]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_lattice
---

## Summary

An orthomodular lattice is an [[orthocomplemented lattice|J7KN14DYV3]] that satisfies the orthomodular law: if $a \le b$, then $b = a \vee (a^\perp \wedge b)$.
The lattice of closed subspaces of any [[Hilbert space|HM2HHE3J51]] is orthomodular, even when it is not [[modular|QX7WZ92QAK]].
Every [[Boolean algebra|0XADJKM699]] and every modular ortholattice is orthomodular.
Orthomodular lattices are the standard algebraic model of the propositions of [[quantum logic|2E9DMB7A6Q]].

## Explanations

### L1 human

If a subspace $A$ sits inside a closed subspace $B$ of a Hilbert space, then $B$ splits as $A$ plus the part of $B$ that is perpendicular to $A$.
The orthomodular law asks for this splitting in an abstract ortholattice.
It is weaker than distributivity and weaker than modularity, and it still holds for the closed subspaces of an infinite-dimensional Hilbert space.
For example, in $\R^3$, a plane $B$ containing a line $A$ is the join of $A$ with the line in $B$ perpendicular to $A$.
