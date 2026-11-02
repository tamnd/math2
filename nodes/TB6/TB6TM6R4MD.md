---
tag: TB6TM6R4MD
kind: concept
name: Sheaf
msc: [54B40, 18F20, 14F06]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_(mathematics)
same_as:
  wikidata: Q595298
  wikipedia: Sheaf (mathematics)
---

## Summary

A sheaf on a topological space assigns to each open set a set of data, such as functions, with restriction maps to smaller open sets.
The data must be determined by their local pieces, and compatible local pieces must glue together.
Sheaves organise local information on a space and measure how it fails to be global.
They are the language of modern algebraic geometry, where a scheme is a space with a sheaf of rings.
They are also the coefficients of sheaf cohomology in topology and complex analysis.

## Explanations

### L1 human

Think of the continuous functions on the open sets of a space.
A function on a big open set can be restricted to a smaller one.
Suppose you know a function on each set of an open cover, and the pieces agree on the overlaps.
Then there is exactly one function on the union that has these pieces.
A sheaf is any rule of this kind: data on open sets, restriction, and the two local conditions of uniqueness and gluing.
Bounded functions are not a sheaf on $\R$: the function $f(x) = x$ is bounded on each bounded interval, but these pieces glue to a function that is not bounded.
