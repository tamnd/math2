---
tag: 2WGB8R9SAD
kind: concept
name: Constraint qualifications
msc: [90C46, 90C30]
sources:
  - url: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
    locator: Regularity conditions (or constraint qualifications)
---

## Summary

A constraint qualification is a condition on the constraint functions of an optimization problem at a feasible point.
It guarantees that, at a local minimizer, Lagrange multipliers satisfying the Karush–Kuhn–Tucker conditions exist.
Common ones are the linear independence, Mangasarian–Fromovitz, linearity and Slater constraint qualifications.
Without such a condition, a minimizer may admit no multipliers.

## Explanations

### L1 human

Multipliers measure how much the active constraints push back against the objective.
This works only if the constraints describe the feasible set well near the point, without cusps or flat gradients.
A constraint qualification is a check that the description is good enough.
For example, the constraint $x^2 \le 0$ describes the point $0$ badly, because its gradient there is zero.
