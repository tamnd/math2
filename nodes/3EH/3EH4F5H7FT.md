---
tag: 3EH4F5H7FT
kind: concept
name: Algebraic approach to constraint satisfaction
msc: [08A70, 68Q25]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Summary

The algebraic approach studies the constraint satisfaction problem of a fixed finite structure through the [[polymorphisms|A0K9EZRM7E]] of that structure.
Its basic fact is that the complexity of the problem depends only on the clone of polymorphisms.
Polymorphisms satisfying good identities, such as [[Taylor|QEAMRNRJJD]], [[Siggers|JYW1H3J8SX]] or cyclic identities, give efficient algorithms.
The approach led to the proof of the [[CSP dichotomy theorem|ZA4YXJ9T1P]]: every such problem is either in polynomial time or NP-complete.

## Explanations

### L1 human

Many puzzles ask for values of variables that satisfy given constraints, for example colouring a map so that neighbours get different colours.
If the allowed constraints are fixed, one can ask how hard the puzzle is.
The algebraic approach looks for operations that combine several solutions into a new solution.
For example, for $2$-colouring a graph, the majority of three valid colourings is again a valid colouring, and $2$-colouring is easy.
For $3$-colouring no such good operation exists, and the problem is NP-complete.
