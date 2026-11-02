---
tag: EY362KR0KB
kind: concept
name: Differential-algebraic system of equations
msc: [34A09, 65L80]
specializes: [08WWTN738R]
sources:
  - url: https://en.wikipedia.org/wiki/Differential-algebraic_system_of_equations
same_as:
  wikidata: Q955889
  wikipedia: Differential-algebraic system of equations
---

## Summary

A differential-algebraic system of equations, or DAE, is a system $F(t, x, x') = 0$ that cannot be solved for the derivative $x'$.
Typically some equations contain derivatives and others are pure constraints between the unknowns.
Such systems arise in electrical circuits, in constrained mechanics and in chemical engineering.
See the [[definition|FD7H5AM1R7]].

## Explanations

### L1 human

An ordinary differential equation tells how every unknown changes in time.
In a DAE some unknowns have no equation for their rate of change; they are tied to the others by algebraic rules instead.
A pendulum written in Cartesian coordinates is an example: the position moves by Newton's law, but it must also stay at a fixed distance from the pivot.
Because of the constraints, the starting values cannot be chosen freely.
