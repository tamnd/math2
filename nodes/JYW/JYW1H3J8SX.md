---
tag: JYW1H3J8SX
kind: concept
name: Siggers term
msc: [08B05, 08A70]
specializes: [QEAMRNRJJD]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Summary

A Siggers term is an idempotent term of arity $6$ that satisfies one fixed identity in three variables, $s(x, y, x, z, y, z) \approx s(y, x, z, x, z, y)$.
Every Siggers term is a [[Taylor term|QEAMRNRJJD]].
Conversely, a finite algebra that has a Taylor term also has a Siggers term, so one explicit identity replaces the whole family of Taylor conditions.
This makes the Siggers term a convenient test in the algebraic theory of constraint satisfaction problems.

## Explanations

### L1 human

Taylor terms come in many shapes and arities, which makes them hard to search for.
A Siggers term has one fixed shape: six inputs and one balanced equation in three letters.
For finite algebras, looking for this single shape is enough to decide whether some Taylor term exists.
For example, in a semilattice the term $x_1 \wedge x_2 \wedge \cdots \wedge x_6$ is a Siggers term, because both sides of the identity become $x \wedge y \wedge z$.
