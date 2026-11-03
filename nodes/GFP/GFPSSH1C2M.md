---
tag: GFPSSH1C2M
kind: concept
name: Lemke's algorithm
msc: [90C33, 90C49]
sources:
  - url: https://en.wikipedia.org/wiki/Lemke%27s_algorithm
same_as:
  wikidata: Q6521168
  wikipedia: Lemke's algorithm
---

## Summary

Lemke's algorithm is a pivoting method for the [[linear complementarity problem|8G30AFBZNQ]].
It adds one artificial variable and then performs complementary pivots.
In such a pivot, the variable entering the basis is the partner of the one that just left.
It stops either at a solution or on an unbounded ray, and for important classes of matrices a ray proves that there is no solution.
It is named after Carlton E. Lemke, and a related method of Lemke and Howson finds equilibria of bimatrix games.

## Explanations

### L1 human

The algorithm starts with an easy point that would solve the problem if one extra helper variable were allowed.
It then changes one variable at a time, like the simplex method, while keeping the rule "in each pair, at least one is zero" for all pairs but one.
Each step is forced by the previous one, so the path never branches.
When the helper variable drops to zero, the current point solves the original problem.
