---
tag: VE54BEPVKT
kind: concept
name: Dantzig–Wolfe decomposition
msc: [90C05, 90C06]
sources:
  - url: https://en.wikipedia.org/wiki/Dantzig–Wolfe_decomposition
same_as:
  wikidata: Q4388617
  wikipedia: Dantzig–Wolfe decomposition
---

## Summary

Dantzig–Wolfe decomposition is a method for large [[linear programs|VNMXB0J2KA]] with a special structure.
Their constraints split into a few linking constraints and an easy remainder, often with a block structure.
It writes each point of the easy part as a convex combination of its [[extreme points|3MSGFJM2NX]].
The program in the weights of these combinations is the master problem.
The master problem has a huge number of columns, so it is solved by column generation.
A subproblem over the easy part produces a new column whenever one can improve the objective.
George Dantzig and Philip Wolfe introduced it in 1960.

## Explanations

### L1 human

Think of a company with several factories that share a few common resources.
Each factory can plan its own production easily; the hard part is only the sharing.
The method lets a central planner set prices for the shared resources, asks each factory for its best plan at those prices, and mixes the plans it has received.
It repeats this until no factory can offer a plan that would improve the mix.
