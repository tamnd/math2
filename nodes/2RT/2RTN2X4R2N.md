---
tag: 2RTN2X4R2N
kind: concept
name: Semidefinite programming
msc: [90C22, 90C25]
specializes: [PAPN0JNEKN]
sources:
  - url: https://en.wikipedia.org/wiki/Semidefinite_programming
same_as:
  wikidata: Q2269096
  wikipedia: Semidefinite programming
---

## Summary

Semidefinite programming minimises a linear function of a symmetric matrix under linear equations.
It also requires the matrix to be [[positive semidefinite|01MMVW8CKC]].
It is the case of [[conic optimization|PAPN0JNEKN]] where the cone is the cone of positive semidefinite matrices.
It contains [[linear programming|VNMXB0J2KA]] and [[second-order cone programming|H80KQPNN9B]], and [[interior-point methods|M7HYT44ZJA]] solve it to any accuracy in polynomial time under mild conditions.
Semidefinite relaxations give strong bounds for hard problems, as in the [[Goemans–Williamson algorithm|ATERHVE8T7]] for [[maximum cut|T9B8T3FKRA]], and they underlie [[sum-of-squares optimization|AM0BYNK5YJ]].

## Explanations

### L1 human

In a linear program the unknowns are numbers that must be nonnegative.
In a semidefinite program the unknown is a symmetric matrix that must be "nonnegative" in the matrix sense: all its eigenvalues are at least $0$.
The objective and the other constraints are linear in the entries of the matrix.
For example, minimising $\tr(C X)$ over positive semidefinite $X$ with $\tr X = 1$ gives the smallest eigenvalue of the symmetric matrix $C$.
