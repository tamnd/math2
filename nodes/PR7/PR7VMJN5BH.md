---
tag: PR7VMJN5BH
kind: concept
name: Cutting-plane method
msc: [90C10, 90C57]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
same_as:
  wikidata: Q1762039
  wikipedia: Cutting-plane method
---

## Summary

A cutting-plane method solves an [[integer program|9GX3WH5EQF]] by solving a sequence of [[linear programming relaxations|PYMHHM5Z6F]], each tighter than the last.
When the current relaxed optimum is not integral, one adds a linear inequality, called a cut.
Every integer feasible point satisfies the cut, but the relaxed optimum violates it.
The cuts carve the relaxation down towards the [[convex hull|0FQSDC2EQ2]] of the integer feasible points.
Ralph Gomory gave the first such method with finite convergence for pure integer programs, using [[Gomory's fractional cuts|AZJMC8A93H]].
The same idea for convex problems is treated in [[cutting-plane methods for convex optimization|MMC5V3VW89]].

## Explanations

### L1 human

Solving the problem without the whole-number rule gives a corner point that may be fractional.
A cutting plane is a straight wall that slices off that fractional corner while keeping every whole-number point on the allowed side.
After adding the wall, one solves again and gets a new corner.
Repeating this, the corners get closer to whole-number points, until the best corner is itself a whole-number point and the problem is solved.
