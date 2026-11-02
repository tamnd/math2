---
tag: 7XAPBCJK3B
kind: concept
name: Method of characteristics
msc: [35F20, 35A30, 35L02]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_characteristics
same_as:
  wikidata: Q1785085
  wikipedia: Method of characteristics
---

## Summary

The method of characteristics solves a first-order [[partial differential equation|GC5BDZ6QBC]] by reducing it to a system of [[ordinary differential equations|0NT64JV96A]].
Along special curves, the characteristics, the equation says how the unknown changes, so one integrates along these curves from the initial data.
It gives explicit solutions of transport, Hamilton–Jacobi and conservation law equations, and it explains why their solutions may break down in finite time.
See the [[definition|VDWKE1KK4H]].

## Explanations

### L1 human

A first-order equation such as $u_t + c\, u_x = 0$ says that $u$ does not change when one moves with speed $c$.
So one follows the lines $x = x_0 + ct$, and along each line $u$ keeps its initial value $u(x_0, 0)$.
This gives the solution $u(x, t) = u(x - ct, 0)$ at once.
In general the curves are not straight and $u$ may change along them, but one still only solves ordinary differential equations.
When two characteristic curves carrying different values cross, the solution cannot stay smooth, and a shock forms.
