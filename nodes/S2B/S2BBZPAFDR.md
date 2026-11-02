---
tag: S2BBZPAFDR
kind: concept
name: Optimal control of partial differential equations
msc: [49J20, 49K20, 93C20]
specializes: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/PDE-constrained_optimization
same_as:
  wikidata: Q97358887
  wikipedia: PDE-constrained optimization
---

## Summary

Optimal control of partial differential equations studies how to choose a control, such as a heat source or a boundary temperature.
The aim is that the solution of a [[partial differential equation|GC5BDZ6QBC]] is as good as possible for a given cost.
The state lives in an infinite-dimensional function space, such as a [[Sobolev space|M4CEZ5K9HP]].
It is the infinite-dimensional branch of [[optimal control|T3V6ZNAMDN]] and is also called PDE-constrained optimization.
Its main tools are existence theory in function spaces, optimality systems with adjoint equations, and numerical methods such as the [[adjoint state method|YD8SA6WS01]].

## Explanations

### L1 human

Think of a metal plate heated by adjustable burners underneath.
You want the plate to reach a given temperature profile, while spending little energy on the burners.
The temperature obeys the heat equation, a partial differential equation, and the burner settings are the control.
Choosing the best burner settings is an optimal control problem for a partial differential equation.
