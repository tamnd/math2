---
tag: EW5PMAGN8F
kind: concept
name: Gamma filtration
msc: ["19E08", "19L20", "14C35"]
specializes: [HNK1Y62G7V]
sources:
  - url: https://en.wikipedia.org/wiki/Λ-ring
---

## Summary

The gamma filtration is a decreasing [[filtration|HNK1Y62G7V]] of an augmented [[lambda-ring|E2KA3XP47F]], built from the gamma operations $\gamma^n$.
On the K-group $K_0(X)$ of a smooth variety it is an algebraic substitute for the filtration by codimension of support.
Grothendieck showed that, after tensoring with $\Q$, its graded pieces match the [[Chow groups|EBEF6PEK4N]] of $X$.

## Explanations

### L1 human

In $K_0(X)$ every element has a rank, and the elements of rank $0$ form the first step of the filtration.
Products of rank-zero elements are "smaller", and the gamma operations give further small elements.
The $n$-th step collects everything that is at least $n$ steps small in this sense.
For the projective line, $x = 1 - [\mathcal{O}(-1)]$ has rank $0$, and $x^2 = 0$, so the filtration stops after two steps.
This matches the geometry: the only kinds of cycles on the projective line are points and the whole line.
