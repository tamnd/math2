---
tag: X7HYEBA5SA
kind: concept
name: Finite difference method
msc: [65M06, 65N06]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference_method
same_as:
  wikidata: Q1147751
  wikipedia: Finite difference method
---

## Summary

The finite difference method solves differential equations approximately on a grid of points.
It replaces each derivative by a difference quotient of the values at nearby grid points, which turns the equation into a system of algebraic equations.
It is the oldest and simplest numerical method for [[partial differential equations|GC5BDZ6QBC]].
Its convergence rests on consistency and stability, as in the [[Lax equivalence theorem|D5M7TRD3MY]].
For time-dependent problems, stability often requires a step restriction such as the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]].

## Explanations

### L1 human

A derivative is a limit of slopes $(u(x + h) - u(x))/h$ as $h \to 0$.
The finite difference method simply stops before the limit and uses a small fixed $h$.
Put points $0, h, 2h, \ldots$ on the line and keep track only of the values of the unknown function there.
For example, $u''(x)$ is replaced by $(u(x + h) - 2u(x) + u(x - h))/h^2$, which is exact for quadratic polynomials.
The equation then becomes one linear equation per grid point, which a computer can solve.
