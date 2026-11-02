---
tag: MTCRZC5QKT
kind: concept
name: Upwind scheme
msc: [65M06, 65M08]
specializes: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Upwind_scheme
same_as:
  wikidata: Q7899499
  wikipedia: Upwind scheme
---

## Summary

An upwind scheme is a [[finite difference|X7HYEBA5SA]] or finite volume scheme for advection problems.
Its spatial differences are taken on the side from which the information comes.
For the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$ with $a > 0$, waves move to the right.
So the scheme uses the values at the point and at its left neighbour.
Following the direction of propagation gives stable schemes under the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]], while the centred or the opposite choice leads to instability.
The first-order upwind scheme is the basic building block of Godunov-type methods for conservation laws.

## Explanations

### L1 human

Think of smoke carried by the wind: what happens here next depends on what is upwind now, not downwind.
An upwind scheme updates each grid value using its neighbour on the upwind side.
For $u_t + u_x = 0$ with time step equal to half the grid spacing, the new value is the average of the old value and its left neighbour.
This makes the scheme stable and free of wiggles, though it smears sharp fronts a little.
