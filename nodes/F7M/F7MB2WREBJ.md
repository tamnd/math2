---
tag: F7MB2WREBJ
kind: concept
name: State on a C*-algebra
msc: [46L30, 46L05]
sources:
  - url: https://en.wikipedia.org/wiki/State_(functional_analysis)
same_as:
  wikidata: Q2917249
  wikipedia: State (functional analysis)
---

## Summary

A state on a C*-algebra is a positive linear functional of norm $1$.
On a unital C\*-algebra this means a linear functional that takes nonnegative values on [[positive elements|NA8DF5X3M4]] and the value $1$ at the unit.
States play the role of probability measures.
For a compact Hausdorff space $X$, the states on $C(X)$ are the integrals against regular Borel probability measures on $X$.
In quantum mechanics, the states of a system with observable algebra $A$ are the states on $A$.

## Explanations

### L1 human

A state assigns to each observable an expected value.
For a quantum system described by a unit vector $\xi$, the state assigns to an operator $T$ the number $\ip{T \xi}{\xi}$.
For a classical system on a space $X$, a state assigns to a function its average with respect to a probability distribution on $X$.
The states that cannot be written as mixtures of two other states are called pure states.
