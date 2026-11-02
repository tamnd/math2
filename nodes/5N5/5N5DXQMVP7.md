---
tag: 5N5DXQMVP7
kind: concept
name: Riesz potential operator
msc: [47G40, 31B15, 45P05]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_potential
same_as:
  wikidata: Q7333166
  wikipedia: Riesz potential
---

## Summary

The Riesz potential operator $I_\alpha$ of order $\alpha$, with $0 < \alpha < n$, is the integral operator on $\R^n$ with kernel a constant times $\abs{x - y}^{\alpha - n}$.
It is the inverse of the fractional power $(-\Delta)^{\alpha/2}$ of the [[Laplacian|0E0B6RA8K0]], so it acts as integration of order $\alpha$ in $n$ variables.
For $n = 3$ and $\alpha = 2$ it is the Newtonian potential of physics.
Its mapping properties between [[Lp spaces|SASP14MA1Z]], given by the [[Hardy–Littlewood–Sobolev inequality|HG65C9R1SP]], underlie the Sobolev embedding theorems.

## Explanations

### L1 human

The gravitational potential of a mass distribution in space is obtained by adding up contributions $1/\abs{x - y}$ from each piece of mass at $y$.
The Riesz potential replaces the power $1/\abs{x - y}$ by $\abs{x - y}^{\alpha - n}$ in $n$ dimensions.
Small $\alpha$ gives a sharply peaked kernel that smooths a function only a little, and larger $\alpha$ smooths more.
In one dimension with $0 < \alpha < 1$, it is a two-sided version of the [[Riemann–Liouville integral|JTKCZ44NN3]] of order $\alpha$.
