---
tag: 6TQSVJQDEH
kind: concept
name: Young measure
msc: [49J45, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/Young_measure
same_as:
  wikidata: Q8058552
  wikipedia: Young measure
---

## Summary

A Young measure on a set $\Omega \subseteq \R^n$ is a measurable family $(\nu_x)_{x \in \Omega}$ of [[probability measures|059TJN0NZ1]] on $\R^m$.
Young measures describe the limits of oscillating sequences of functions: $\nu_x$ is the distribution of the values that the functions take near $x$.
They let one pass to the limit in nonlinear expressions $\varphi(u_k)$ when $u_k$ converges only weakly.
They are a standard tool in the calculus of variations and in nonlinear partial differential equations.

## Explanations

### L1 human

Take the function on $(0,1)$ that jumps between $-1$ and $1$ on $k$ equal pieces, and let $k$ grow.
The functions oscillate faster and faster, and their weak limit is $0$.
But the square of each function is $1$, so the weak limit forgets something.
The Young measure keeps it: at every point it is the measure giving weight $1/2$ to $-1$ and $1/2$ to $1$.
It records which values occur and how often, not where they occur.
