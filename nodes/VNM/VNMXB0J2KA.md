---
tag: VNMXB0J2KA
kind: concept
name: Linear programming
msc: [90C05, 52B55]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming
same_as:
  wikidata: Q202843
  wikipedia: Linear programming
---

## Summary

Linear programming is the optimization of a linear function over the set of solutions of finitely many linear inequalities.
The feasible set is a convex polyhedron.
When an optimum exists, it is attained on a face, and at a vertex when the polyhedron has vertices.
Each linear program has a dual program.
If one of the two has an optimal solution, so does the other, with the same optimal value; this is tied to [[Farkas' lemma|FYZC634H2D]].
Linear programs are solved in practice by the [[simplex algorithm|MH272QHWPM]] and by interior point methods.
The ellipsoid method and interior point methods solve them in polynomial time.

## Explanations

### L1 human

A factory makes two products, each using some amounts of limited resources, and earns some profit on each.
How much of each should it make to earn the most?
The limits are straight-line conditions, so the allowed plans form a polygon, and the best plan is found at one of its corners.
Linear programming is the study of such problems, with any number of variables and conditions.
