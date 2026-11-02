---
tag: P3VXR8FW17
kind: concept
name: Strict hyperbolicity
msc: [35L40, 35L45, 35L65]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_partial_differential_equation
---

## Summary

Strict hyperbolicity is a condition on a system of evolution equations that is stronger than [[hyperbolicity|92C3S03AQZ]].
For a first-order system $u_t + \sum_j A_j u_{x_j} = 0$ it asks that, in each direction, the matrix $\sum_j \xi_j A_j$ has real and distinct eigenvalues.
The eigenvalues are the speeds of the different waves, and distinct speeds keep the waves apart.
Strictly hyperbolic systems have a well-posed Cauchy problem, and they are the setting of the classical theory of [[hyperbolic conservation laws|XN081NCPF5]].

## Explanations

### L1 human

A hyperbolic system carries several kinds of waves, each with its own speed.
Strict hyperbolicity says that these speeds are real numbers and that no two of them are equal.
For example, the one-dimensional wave equation, written as a system, has the two speeds $c$ and $-c$, which are different, so it is strictly hyperbolic.
When two speeds coincide, waves can interact in delicate ways and some estimates break down.
