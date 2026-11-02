---
tag: GTBXZXK146
kind: concept
name: Friedrichs extension
msc: [47B25, 47A20, 47A07]
sources:
  - url: https://en.wikipedia.org/wiki/Friedrichs_extension
same_as:
  wikidata: Q1464339
  wikipedia: Friedrichs extension
---

## Summary

The Friedrichs extension is a canonical [[self-adjoint|0NEGN5CRSC]] extension of a densely defined [[symmetric operator|H971WGMV6C]] that is bounded below.
It is built from the quadratic form of the operator, by completing the domain in the form norm.
It has the same lower bound as the original operator.
It is the standard way to turn a formal differential operator such as $-\Delta + V$ with $V \ge 0$ into a self-adjoint operator.

## Explanations

### L1 human

A symmetric operator is often given only on nice functions, and this domain is too small for the operator to be self-adjoint.
There can be many ways to enlarge the domain, and they give different operators.
When the operator is bounded below, the Friedrichs construction picks one of them in a natural way.
The idea is to use the energy $\ip{Tx}{x}$ to measure functions, and to keep exactly the functions of finite energy.
For $-d^2/dx^2$ on smooth functions with compact support in $(0, 1)$, the Friedrichs extension is the second derivative with the Dirichlet conditions $f(0) = f(1) = 0$.
