---
tag: ZYZM357DQV
kind: concept
name: hp-FEM
msc: [65N30, 65N50]
specializes: [98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Hp-FEM
same_as:
  wikidata: Q17027720
  wikipedia: Hp-FEM
---

## Summary

The hp-FEM is a version of the [[finite element method|98GZ9DVHTA]] that improves the approximation in two ways at once.
It refines the mesh, which makes the element size $h$ smaller, and it raises the polynomial degree $p$ on the elements.
Small elements are used near singularities of the solution, and high degrees where the solution is smooth.
Take an elliptic problem with piecewise analytic data on a polygon.
Babuška and Guo showed that a well chosen hp-sequence then converges exponentially in the number of unknowns.
See the [[definition|1F7NV6AT2X]].

## Explanations

### L1 human

A standard finite element method uses many small pieces, each with a simple polynomial such as a straight line.
The hp-FEM also lets each piece use a curved polynomial of high degree.
Where the solution is smooth, high degree pays off quickly; near a corner where the solution has a kink in its derivatives, small pieces work better.
Mixing the two well gives errors that drop much faster than with either one alone.
