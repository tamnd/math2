---
tag: CPX8Q2GFGD
kind: concept
name: Sequential quadratic programming
msc: [90C55, 90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_quadratic_programming
same_as:
  wikidata: Q4373881
  wikipedia: Sequential quadratic programming
---

## Summary

Sequential quadratic programming (SQP) solves smooth constrained nonlinear problems by solving a sequence of quadratic programs.
Each quadratic program has a quadratic model of the Lagrangian as objective and the linearized constraints as constraints.
For equality constraints, an SQP step is a step of Newton's method applied to the first-order optimality conditions.
SQP methods are among the most effective methods for small and medium nonlinear programs.

## Explanations

### L1 human

Curved constraints and a curved objective are hard to handle all at once.
At the current guess, SQP replaces the constraints by their tangent planes and the objective by a bowl-shaped approximation.
That simpler problem, a quadratic program, can be solved exactly.
Its solution gives the next guess, and the process repeats.
