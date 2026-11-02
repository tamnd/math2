---
tag: 6EEAEDWXZ2
kind: concept
name: Discrete Poisson equation
msc: [39A14, 65N06, 35J05]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Poisson_equation
same_as:
  wikidata: Q5282040
  wikipedia: Discrete Poisson equation
---

## Summary

The discrete Poisson equation $\Delta u = f$ asks for a function on a grid or graph whose [[discrete Laplacian|ZN30Y1ZDB6]] is a given function $f$.
It is the finite difference version of Poisson's equation $\Delta u = f$, and with $f = 0$ it becomes the discrete form of [[Laplace's equation|S8RG6N1PRT]].
With boundary values prescribed, it becomes a large sparse linear system.
Solving this system fast is a central task of numerical analysis, done with iterative methods, multigrid or the fast Fourier transform.

## Explanations

### L1 human

Lay a square grid over a metal plate and keep the edges at fixed temperatures.
Inside, each grid value should equal the average of its four neighbours, corrected by a heat source term.
Writing this rule at every inner point gives one linear equation per point.
Solving all of them at once gives the temperature at every grid point.
