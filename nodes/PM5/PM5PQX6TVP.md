---
tag: PM5PQX6TVP
kind: concept
name: Optimal experimental design
msc: [62K05]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_experimental_design
same_as:
  wikidata: Q7098942
  wikipedia: Optimal experimental design
---

## Summary

Optimal experimental design chooses the conditions of an experiment so that the parameters of a given model are estimated as precisely as possible.
Precision is measured by the information matrix of the design, and an optimality criterion turns that matrix into a number.
D-optimality maximises its determinant, A-optimality minimises the trace of its inverse, and E-optimality maximises its smallest eigenvalue.
The approximate theory, where a design is a probability measure on the design region, makes these problems convex.
The [[Kiefer–Wolfowitz equivalence theorem|71XBFB49HE]] shows that D-optimal and G-optimal designs coincide in that theory.

## Explanations

### L1 human

To estimate the slope of a straight line over an interval, where should one measure?
Spreading the points evenly feels natural, but putting half of them at each end gives a more precise slope.
Optimal design makes such choices systematic: it picks the measuring points that make the estimates as sharp as possible.
Different goals, such as precise coefficients or precise predictions, lead to different criteria and sometimes to different designs.
