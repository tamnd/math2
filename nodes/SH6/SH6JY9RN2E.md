---
tag: SH6JY9RN2E
kind: concept
name: Green's function
msc: [34B27, 35J08]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function
same_as:
  wikidata: Q378435
  wikipedia: Green's function
---

## Summary

A Green's function of a linear differential operator $L$ with boundary conditions is a kernel $G(x, s)$ that turns the source term into the solution.
The function $y(x) = \int G(x, s) f(s)\, ds$ solves $L y = f$.
Formally it is the response of the system to a unit point source at $s$, that is, $L G(\cdot, s) = \delta_s$ with the [[Dirac delta|0KPHENZ5S7]].
It turns a differential equation into an integral formula, and it is basic in boundary value problems, potential theory and physics.
The [[Green's function for the Laplacian|M36SD56MWQ]] is the main case for partial differential equations.
See the [[definition|ZH4V0WHSXT]] for ordinary differential equations.

## Explanations

### L1 human

Think of a taut string fixed at both ends.
Pushing it at one point $s$ with a unit force bends it into a shape $G(x, s)$.
A general load $f$ is a sum of many point pushes, so the string takes the shape $\int G(x, s) f(s)\, ds$.
For $y'' = f$ on $[0, 1]$ with $y(0) = y(1) = 0$, the Green's function is $G(x, s) = x (s - 1)$ for $x \le s$ and $G(x, s) = s (x - 1)$ for $x \ge s$.
