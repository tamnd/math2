---
tag: HC0HPYQBD1
kind: concept
name: Total dual integrality
msc: [90C57, 90C10, 52B20]
sources:
  - url: https://en.wikipedia.org/wiki/Total_dual_integrality
same_as:
  wikidata: Q7828108
  wikipedia: Total dual integrality
---

## Summary

A system of linear inequalities $A x \le b$ is totally dual integral (TDI) when it passes the following test for every integer objective vector.
Whenever the [[dual linear program|14VMJNXMDC]] has an optimal solution, it has an integral one.
The notion was introduced by Jack Edmonds and Rick Giles.
Their theorem says that a TDI system with integral right-hand side defines a polyhedron whose minimal faces all contain integer points.
So the [[linear programming relaxation|PYMHHM5Z6F]] of the system is exact.
It is a property of the system, not of the polyhedron: the same polyhedron can have TDI and non-TDI descriptions.

## Explanations

### L1 human

Many min-max theorems in combinatorics have the same source.
An example is "the largest number of edge-disjoint paths equals the smallest number of edges whose removal cuts all paths".
Such a theorem holds because a linear program and its dual both have whole-number optimal solutions.
Total dual integrality is the property of the inequalities that makes the dual side whole-number.
A surprising theorem then gives the primal side for free when the right-hand sides are whole numbers.
