---
tag: 9VA6P5KQQT
kind: concept
name: Matrix difference equation
msc: [39A06]
specializes: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_difference_equation
same_as:
  wikidata: Q6787869
  wikipedia: Matrix difference equation
---

## Summary

A matrix difference equation describes how a vector of quantities changes in discrete time by multiplication by a matrix, possibly plus an input term.
It is the discrete analogue of a system of linear differential equations.
Every linear recurrence of higher order can be rewritten as a first-order matrix difference equation for a state vector.
With a constant matrix $A$, the homogeneous solutions are $x(n) = A^n x(0)$, so their behaviour is governed by the eigenvalues of $A$.

## Explanations

### L1 human

Think of a state, such as the numbers of young and old animals in a population, recorded once a year.
A matrix difference equation says that next year's state is a fixed matrix times this year's state.
For the Fibonacci numbers, the pair $(F_{n+1}, F_n)$ is obtained from $(F_n, F_{n-1})$ by the matrix with rows $(1, 1)$ and $(1, 0)$.
So repeated multiplication by one matrix generates the whole sequence.
