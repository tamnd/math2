---
tag: 8TD2KCVH5N
kind: concept
name: Birkhoff sum and average
msc: [37A30, 37A05]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodic_theory
---

## Summary

The Birkhoff sum of a function along an orbit adds up its values at the first $n$ points of the orbit.
The Birkhoff average divides this sum by $n$.
The average is the time average of an observable: the mean value seen by watching the system for $n$ steps.
The ergodic theorems of Birkhoff and von Neumann say when these averages converge and identify the limit.
For an [[ergodic transformation|AZRPHS478B]] and an integrable function, the limit is the space average of the function for almost every starting point.
Birkhoff sums also appear in the definitions of Lyapunov exponents, cocycles and the thermodynamic formalism.

## Explanations

### L1 human

Imagine a system moving step by step and a quantity, such as temperature, that one can read off at each state.
The Birkhoff sum adds up the readings over the first $n$ steps, and the Birkhoff average is their mean.
For example, let $f$ be $1$ on a region $A$ and $0$ elsewhere.
Then the Birkhoff sum counts how many of the first $n$ steps the orbit spends in $A$, and the average is the fraction of time spent in $A$.
