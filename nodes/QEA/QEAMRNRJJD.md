---
tag: QEAMRNRJJD
kind: concept
name: Taylor term
msc: [08B05, 08A70]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Summary

A Taylor term is an idempotent term with one identity in two variables $x, y$ for each argument place.
The identity for a place has $x$ in that place on one side and $y$ in that place on the other side.
Having a Taylor term is one of the weakest nontrivial [[Mal'cev conditions|6R0CA4JWWY]].
For an idempotent variety, having a Taylor term means that no nontrivial algebra in the variety has only projections as term operations.
It is central in the [[algebraic approach to constraint satisfaction|3EH4F5H7FT]].
There, a finite core structure has a polynomial-time problem when its idempotent polymorphisms include a Taylor operation.
Otherwise its problem is NP-complete.

## Explanations

### L1 human

A projection, such as $(x, y) \mapsto x$, simply copies one of its inputs and carries no real information.
A Taylor term is an operation that is provably not a projection: for every input place, some equation forces the output not to depend on that place alone.
For example, a binary operation $x \cdot y$ with $x \cdot x = x$ and $x \cdot y = y \cdot x$ is a Taylor term.
Commutativity rules out both projections, because $(x, y) \mapsto x$ is not commutative.
Algebras with such an operation have enough structure for strong algorithms and structure theorems.
