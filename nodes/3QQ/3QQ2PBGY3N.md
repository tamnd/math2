---
tag: 3QQ2PBGY3N
kind: concept
name: Sullivan minimal model
msc: [55P62]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_homotopy_theory
    locator: Sullivan algebras
---

## Summary

A Sullivan minimal model is a free graded-commutative differential graded algebra over $\Q$ with a decomposable differential.
It models the rational homotopy type of a space.
Every simply connected space of finite type has a minimal model, unique up to isomorphism.
Its generators in degree $n$ form the dual of the rational homotopy group $\pi_n(X) \otimes \Q$, and its cohomology is the rational cohomology of $X$.
So the minimal model is the main computational tool of [[rational homotopy theory|8G9QPMBT7R]].

## Explanations

### L1 human

The minimal model describes a space by a list of generators, one batch for each degree.
A rule $d$ says how each generator is "killed" by products of earlier ones.
The generators count the rational homotopy groups, and the rule records how they interact.
For the sphere $S^2$, one needs a generator $x$ in degree $2$ for the class of the sphere and a generator $y$ in degree $3$ with $dy = x^2$.
The second generator kills the square $x^2$, which must vanish in the cohomology of $S^2$, and it matches the rational homotopy group $\pi_3(S^2) \otimes \Q \cong \Q$ given by the Hopf map.
