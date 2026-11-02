---
tag: PFJP8T03C4
kind: concept
name: Caloric function
msc: ["35K05", "31C45"]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Summary

A caloric function is a solution of the [[heat equation|VP2HN86VAG]] $\partial_t u = \Delta u$ on an open set of space-time.
Caloric functions play for the heat equation the role that [[harmonic functions|0DEB0JMN0W]] play for the Laplace equation.
Much of classical potential theory, such as mean value formulas, maximum principles and the Perron method, has a parallel version for caloric functions.
This parallel theory is often called parabolic or caloric potential theory.

## Explanations

### L1 human

Think of $u(x, t)$ as the temperature at the place $x$ at the time $t$ in a body where heat simply spreads out.
A caloric function is any temperature profile that obeys the law of heat flow.
A harmonic function that does not depend on time is caloric, since it describes a steady temperature.
A simple example in one space variable is $u(x, t) = x^2 + 2t$: here $\partial_t u = 2$ and $\partial_x^2 u = 2$.
Another is $u(x, t) = e^{-t} \sin x$, a wave of heat that fades as time goes on.
