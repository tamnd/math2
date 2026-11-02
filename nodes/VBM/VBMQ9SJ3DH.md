---
tag: VBMQ9SJ3DH
kind: concept
name: Cole–Hopf transformation
msc: [35Q35, 35K05, 35A22]
sources:
  - url: https://en.wikipedia.org/wiki/Cole%E2%80%93Hopf_transformation
same_as:
  wikidata: Q116980355
  wikipedia: Cole–Hopf transformation
---

## Summary

The Cole–Hopf transformation turns the viscous [[Burgers' equation|NEGHXN8RE1]] into the linear [[heat equation|VP2HN86VAG]].
It sets $u = -2\nu\, \partial_x \log \varphi$, where $\varphi$ is a positive solution of the heat equation.
It gives an explicit formula for the solution of the initial value problem for Burgers' equation.
Letting the viscosity tend to zero in that formula recovers the entropy solution of the inviscid equation.
See the [[definition|PPM7V7WWHQ]].

## Explanations

### L1 human

Burgers' equation is nonlinear, so solutions cannot simply be added together.
The Cole–Hopf trick is a change of unknown that removes the nonlinearity.
After the change, the equation becomes the heat equation, which is solved by a known integral formula.
Changing back gives the solution of Burgers' equation with positive viscosity for given initial values.
For example, $\varphi(x, t) = x$ solves the heat equation, and it gives the solution $u = -2\nu / x$ of Burgers' equation for $x > 0$.
