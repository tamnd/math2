---
tag: FZ4BRYJ0YZ
kind: concept
name: Pseudospectral optimal control
msc: [49M37, 49M25, 65M70]
specializes: [T58W34D60G]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudospectral_optimal_control
same_as:
  wikidata: Q7255577
  wikipedia: Pseudospectral optimal control
---

## Summary

Pseudospectral optimal control is a form of [[direct collocation|T58W34D60G]] that uses a single global polynomial for the state on the whole time interval.
The nodes are the points of a Gaussian quadrature rule, such as the Legendre–Gauss–Lobatto points, and derivatives are taken with a differentiation matrix.
For smooth problems the error decreases faster than any power of the number of nodes, so few nodes give high accuracy.
The method is used in aerospace guidance, for example to plan spacecraft manoeuvres.

## Explanations

### L1 human

Low-order collocation draws a trajectory with many short pieces.
A pseudospectral method draws it with one high-degree polynomial through well-chosen points that cluster near the ends of the interval.
Clustering avoids the wild oscillations that equally spaced points would cause.
With three nodes $-1, 0, 1$, the method uses a parabola and integrates the cost with Simpson's rule.
For smooth problems, adding nodes improves the accuracy very quickly.
