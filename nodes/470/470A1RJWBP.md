---
tag: 470A1RJWBP
kind: concept
name: Velocity potential
msc: [76B99, 76A02]
sources:
  - url: https://en.wikipedia.org/wiki/Velocity_potential
same_as:
  wikidata: Q1331126
  wikipedia: Velocity potential
---

## Summary

A velocity potential is a scalar function $\phi$ whose [[gradient|0ABK9V9Y64]] is the velocity of a flow, $\mathbf{u} = \nabla \phi$.
It exists for flows without [[vorticity|B3SXT9TWFA]] on simply connected regions.
For an incompressible flow the potential satisfies [[Laplace's equation|S8RG6N1PRT]], which makes potential flow one of the most tractable models in fluid mechanics.

## Explanations

### L1 human

Imagine a landscape whose height at each point is $\phi$.
The fluid moves straight uphill at each point, and faster where the slope is steeper.
Such a flow has no local spinning, because a gradient has no curl.
For example, $\phi = (x^2 - y^2)/2$ gives the velocity $(x, -y)$, the flow that comes in along the $y$-axis and leaves along the $x$-axis near a stagnation point.
