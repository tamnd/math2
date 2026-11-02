---
tag: W8G3AZ0DNG
kind: concept
name: Nemytskii operator
msc: [47H30, 45G10]
sources:
  - url: https://en.wikipedia.org/wiki/Nemytskii_operator
same_as:
  wikidata: Q6991377
  wikipedia: Nemytskii operator
---

## Summary

A Nemytskii operator, also called a superposition operator, turns a function $g(x, u)$ of two variables into a map on functions.
It sends $u$ to the function $x \mapsto g(x, u(x))$.
It is the simplest kind of nonlinear operator on function spaces, since it acts point by point.
Nonlinear integral equations such as the Hammerstein equation are compositions of a linear integral operator with a Nemytskii operator.
Much of the theory is about when such an operator maps one [[$L^p$ space|SASP14MA1Z]] into another and is continuous.

## Explanations

### L1 human

Take a function $u$ and apply a fixed rule, such as squaring or taking the sine, to its value at every point.
The result is a new function, and the map from $u$ to this new function is a Nemytskii operator.
For example, with $g(x, u) = u^2$, the function $u(x) = x$ is sent to $x^2$.
The rule may also depend on the point, as in $g(x, u) = x \sin u$.
