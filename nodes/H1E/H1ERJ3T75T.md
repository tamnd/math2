---
tag: H1ERJ3T75T
kind: concept
name: Viscosity solution
msc: [35D40, 35F21]
sources:
  - url: https://en.wikipedia.org/wiki/Viscosity_solution
same_as:
  wikidata: Q7935676
  wikipedia: Viscosity solution
---

## Summary

A viscosity solution is a notion of weak solution for fully nonlinear first-order and second-order equations.
Such equations, for example Hamilton–Jacobi equations, need not have classical solutions.
It replaces derivatives of the solution, which may not exist, by derivatives of smooth test functions that touch the solution from above or from below.
The notion was introduced by Crandall and Lions, and for many equations it gives existence, uniqueness and stability under uniform limits.
Its name comes from the vanishing viscosity method.
In this method a small multiple of the Laplacian is added to the equation and then sent to zero.

## Explanations

### L1 human

Think of a function with a sharp corner, like a roof.
It has no derivative at the ridge, so it cannot satisfy a differential equation there in the usual sense.
The viscosity approach tests the function with smooth curves that touch it from above or from below at a point.
It asks the equation to hold as an inequality for the slopes of those curves.
For the equation $\abs{u'} = 1$ on $(-1, 1)$ with $u = 0$ at both ends, this singles out the roof $u(x) = 1 - \abs{x}$ and rejects the valley $\abs{x} - 1$.
