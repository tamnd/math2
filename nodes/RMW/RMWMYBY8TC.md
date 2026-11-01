---
tag: RMWMYBY8TC
kind: concept
name: Character of a representation
msc: [20C15]
sources:
  - url: https://en.wikipedia.org/wiki/Character_theory
---

## Summary

The character of a finite-dimensional [[group representation|WYGRXCG2RN]] $\rho$ is the function $g \mapsto \tr \rho(g)$ on the group.
It is constant on [[conjugacy classes|0DEBXAJ5SA]], because the trace does not change under conjugation.
For a finite group over the complex numbers, a representation is determined up to isomorphism by its character.
So characters turn the study of representations into the study of a finite list of numbers.

## Explanations

### L1 human

Replace each matrix of a representation by one number, its trace, the sum of its diagonal entries.
Surprisingly little is lost: for finite groups over $\C$ these numbers already tell which representation one has.
For example, let the symmetric group $S_3$ permute the coordinates of $\C^3$.
A permutation matrix has trace equal to the number of points it fixes.
So the character takes the value $3$ at the identity, $1$ at each transposition and $0$ at each $3$-cycle.
