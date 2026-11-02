---
tag: NEGHXN8RE1
kind: concept
name: Burgers' equation
msc: [35Q35, 35L65, 35L67]
specializes: [8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Burgers%27_equation
same_as:
  wikidata: Q1014918
  wikipedia: Burgers' equation
---

## Summary

Burgers' equation $u_t + u\, u_x = \nu\, u_{xx}$ is the simplest equation that combines nonlinear transport with diffusion.
For $\nu = 0$ it is the inviscid Burgers' equation, the model scalar [[conservation law|8RA7AMWSAF]], whose smooth solutions break down and form [[shock waves|JSDMGGTG7G]].
For $\nu > 0$ the [[Cole–Hopf transformation|VBMQ9SJ3DH]] turns it into the heat equation, so it can be solved exactly.
It is a standard test case for theory and for numerical methods in fluid dynamics.
See the [[definition|P4RF8A1562]].

## Explanations

### L1 human

In Burgers' equation each value of $u$ moves with speed equal to itself.
So high parts of a wave move faster than low parts, and the front of a wave gets steeper and steeper.
Without viscosity the profile eventually becomes vertical and a jump, a shock, appears.
For example, starting from $u(x, 0) = -x$, the solution is $u(x, t) = x/(t - 1)$, which becomes infinitely steep at time $t = 1$.
With a little viscosity the jump is smoothed out into a thin but steep layer.
