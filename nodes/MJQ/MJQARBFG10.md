---
tag: MJQARBFG10
kind: concept
name: Fourier–Motzkin elimination
msc: [90C05, 15A39, 52B55]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Motzkin_elimination
same_as:
  wikidata: Q1440012
  wikipedia: Fourier–Motzkin elimination
---

## Summary

Fourier–Motzkin elimination removes one variable from a system of linear inequalities, as Gaussian elimination does for equations.
The new system has a solution exactly when the old one has, and its solutions are the projections of the old solutions.
Repeating it decides whether a system of linear inequalities is solvable.
It gives short proofs of [[Farkas' lemma|FYZC634H2D]] and of the fact that projections of polyhedra are polyhedra.
The number of inequalities can grow very fast, so it is mainly a theoretical tool.

## Explanations

### L1 human

To get rid of $y$, sort the inequalities into those that bound $y$ from above, those that bound it from below, and those without $y$.
A value of $y$ exists exactly when every lower bound is at most every upper bound.
So replace all inequalities with $y$ by the comparisons "lower bound $\le$ upper bound".
For $0 \le y \le 1 - x$ this gives $0 \le 1 - x$, that is $x \le 1$.
