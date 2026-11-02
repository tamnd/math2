---
tag: MG3X8Y1VT4
kind: concept
name: Space of bounded continuous functions
msc: ["46E15", 54C35, 46B25]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Space_of_continuous_functions_on_a_compact_space
---

## Summary

For a topological space $X$, the space $C_b(X)$ consists of the bounded continuous scalar functions on $X$, with the supremum norm.
It is a [[Banach space|06GZ956657]]: see [[completeness of the space of bounded continuous functions|09GRCZVR5E]] and the example of the [[sup norm|0PARCKE8WP]].
Convergence in this norm is uniform convergence on $X$.
When $X$ is compact, every continuous function is bounded and $C_b(X)$ is the classical space $C(X)$.

## Explanations

### L1 human

Think of all continuous functions on $X$ whose graphs stay inside some horizontal band.
The distance between two of them is the largest vertical gap between their graphs.
For $X = \R$, the functions $\sin$ and $\arctan$ belong to $C_b(\R)$, but $x \mapsto x$ does not.
A limit of such functions, uniform over all of $X$, is again bounded and continuous.
