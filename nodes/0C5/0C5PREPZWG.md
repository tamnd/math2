---
tag: 0C5PREPZWG
kind: definition
name: Hyperbolic equilibrium point
aliases: [hyperbolic-fixed-point]
msc: [34C05, 37C75]
defines: 01TPMXM6NM
uses: [0G4X36AE0X, 09ZWYRQ41J]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_equilibrium_point
    locator: Flows
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^n$, let $f : U \to \mathbb{R}^n$ be continuously differentiable, and let $x^* \in U$ be an [[equilibrium point|0G4X36AE0X]] of $x' = f(x)$.
The point $x^*$ is hyperbolic if no eigenvalue of the Jacobian matrix $Df(x^*)$ has real part $0$.

## Remarks

A saddle, a node and a spiral of a planar linear system are hyperbolic. A centre is not.
For the pendulum $x' = y$, $y' = -\sin x$, the equilibrium $(\pi, 0)$ is hyperbolic, with eigenvalues $\pm 1$. The equilibrium $(0, 0)$ is not, with eigenvalues $\pm i$.
Near a hyperbolic equilibrium, the [[linearisation|09ZWYRQ41J]] describes the system qualitatively, by the [[Hartman–Grobman theorem|0S8WX8A4V9]].
If all eigenvalues have negative real part, the point is a sink. If all have positive real part, it is a source. Otherwise it is a saddle.

## Explanations

### L1 human

At a hyperbolic equilibrium, each direction of the linearisation either contracts or expands.
No direction is neutral, so small changes of the field do not change the type of the equilibrium.
