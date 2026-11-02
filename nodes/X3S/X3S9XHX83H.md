---
tag: X3S9XHX83H
kind: concept
name: Lie symmetry method
msc: [34C14, 34A05]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_point_symmetry
same_as:
  wikidata: Q6543828
  wikipedia: Lie point symmetry
---

## Summary

The Lie symmetry method solves differential equations by using their continuous symmetries.
A Lie point symmetry is a one-parameter group of changes of variables that maps solutions to solutions.
In adapted coordinates, called canonical coordinates, the symmetry becomes a translation and the equation can be integrated by quadrature.
The method, due to Sophus Lie, explains most of the classical tricks for first-order equations, such as the substitution $y = x v$ for a [[homogeneous first-order equation|0RN88KZBJ3]].
See the [[definition|WZKRG7H3FX]].

## Explanations

### L1 human

Many solving tricks for differential equations look unrelated, but most of them use a hidden symmetry.
For example, the equation $y' = F(y/x)$ does not change if one scales $x$ and $y$ by the same factor.
So scaling a solution curve gives another solution curve.
In coordinates in which the scaling is a shift, such as $r = y/x$ and $s = \ln\abs{x}$, the equation no longer depends on $s$ and can be integrated directly.
