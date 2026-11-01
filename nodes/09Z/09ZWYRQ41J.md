---
tag: 09ZWYRQ41J
kind: concept
name: Linearisation at an equilibrium
aliases: [linearization]
msc: [34D20, 34C05]
uses: [0G4X36AE0X, 0VJF99CZ0Z, 0SKVEMXJWF]
sources:
  - url: https://en.wikipedia.org/wiki/Linearization
    locator: Stability analysis
  - url: https://en.wikipedia.org/wiki/Stability_theory
    locator: Non-linear autonomous systems
---

## Summary

Let $U \subseteq \mathbb{R}^n$ be open, let $f : U \to \mathbb{R}^n$ be continuously differentiable, and let $x^*$ be an [[equilibrium point|0G4X36AE0X]] of $x' = f(x)$.
Let $A = Df(x^*)$ be the Jacobian matrix of $f$ at $x^*$. The linearisation of the system at $x^*$ is the linear system $y' = A y$, where $y$ stands for $x - x^*$.
It comes from the first-order Taylor expansion $f(x) = A (x - x^*) + o(\|x - x^*\|)$.

## Remarks

If each eigenvalue of $A$ has negative real part, then $x^*$ is asymptotically stable for the nonlinear system. If one eigenvalue has positive real part, then $x^*$ is unstable.
If some eigenvalue has zero real part and none has positive real part, the linearisation does not decide stability. For $x' = -x^3$ and $x' = x^3$, the linearisation at $0$ is $y' = 0$ in both cases, but the first is stable and the second is not.
Near a hyperbolic equilibrium, the [[Hartman–Grobman theorem|0S8WX8A4V9]] says that the linearisation describes the phase portrait up to a homeomorphism.

## Explanations

### L1 human

Near an equilibrium, a smooth vector field looks like a linear one.
We replace the field by its best linear approximation and study the simpler linear system.
This works well unless the linear system is on the border between stable and unstable.
