---
tag: XBNAJ1RRET
kind: concept
name: Euler–Poisson equation for higher derivatives
msc: [49K05, 34B15]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation
---

## Summary

The Euler–Poisson equation is the [[Euler–Lagrange equation|PS0VV149ET]] of an integral functional whose Lagrangian depends on derivatives of order higher than one.
If the Lagrangian involves derivatives up to order $k$, the equation is an ordinary differential equation of order at most $2k$.
The order is exactly $2k$ when the Lagrangian really depends on the $k$-th derivative.
It governs, for example, the bending of beams and the shape of cubic splines.

## Explanations

### L1 human

Some energies depend on how much a curve bends, not only on its slope.
Bending is measured by the second derivative, so the energy contains $y''$.
Asking that small changes of the curve do not lower the energy gives an equation of order four instead of two.
For the energy $\frac{1}{2} \int y''(x)^2 \, dx$ the equation is $y'''' = 0$, whose solutions are the cubic polynomials.
