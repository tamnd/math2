---
tag: 0N7ATVF2X8
kind: concept
name: Classification of equilibria of planar linear systems
msc: [34C05, 34D20]
uses: [0VJF99CZ0Z, 05VDGH129F, 0SKVEMXJWF]
sources:
  - url: https://en.wikipedia.org/wiki/Stability_theory
    locator: Stability of fixed points in 2D
  - url: https://en.wikipedia.org/wiki/Stability_theory
    locator: Classification of stability types
---

## Summary

Let $A$ be a real $2 \times 2$ matrix with $\det A \neq 0$, let $\tau = \operatorname{tr} A$ and $\Delta = \det A$, and consider $x' = A x$ in the [[phase plane|05VDGH129F]].
The origin is a saddle if $\Delta < 0$. It is a node if $\Delta > 0$ and $\tau^2 - 4 \Delta \ge 0$, and a spiral, or focus, if $\tau \neq 0$ and $\tau^2 - 4 \Delta < 0$. It is a centre if $\tau = 0$ and $\Delta > 0$.
A node or a spiral is stable for $\tau < 0$ and unstable for $\tau > 0$.

## Remarks

The eigenvalues are the roots of $\lambda^2 - \tau \lambda + \Delta = 0$. A saddle has real eigenvalues of opposite signs. A node has real eigenvalues of the same sign. A spiral or a centre has complex conjugate eigenvalues.
The case $\tau^2 = 4 \Delta$ gives a repeated eigenvalue. The origin is then a star node or a degenerate node.
The trace and the determinant do not change under a change of basis $A \mapsto C^{-1} A C$. So the classification depends only on the system, not on the coordinates.
The [[damped harmonic oscillator|0RNXVVTJTJ]] gives a stable spiral when it is underdamped and a stable node when it is overdamped.

## Explanations

### L1 human

For a linear system in the plane, two numbers, the trace and the determinant, tell the shape of the phase portrait near the origin.
For a node, trajectories run into or out of the origin along straight directions. They turn around it for a spiral, and they go around it in closed loops for a centre.
