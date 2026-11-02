---
tag: VY3J2NKGKW
kind: concept
name: Lax–Friedrichs method
msc: [65M06, 65M08, 35L65]
specializes: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Lax%E2%80%93Friedrichs_method
same_as:
  wikidata: Q6505312
  wikipedia: Lax–Friedrichs method
---

## Summary

The Lax–Friedrichs method is an explicit [[finite difference method|X7HYEBA5SA]] for hyperbolic equations such as [[conservation laws|8RA7AMWSAF]].
It replaces the value at the current point by the average of its two neighbours and then applies a centred difference of the flux.
The averaging adds numerical viscosity, which makes the scheme stable under the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]].
It is first-order accurate and smears shocks, but it is simple and robust.
See the [[definition|53H8EVRC1J]].

## Explanations

### L1 human

To update a value on a grid, a naive scheme uses the old value plus a centred estimate of the change, and this blows up.
The Lax–Friedrichs method uses the average of the two neighbouring old values instead of the old value itself.
This small change acts like a little diffusion, and it damps the growing oscillations.
For the equation $u_t + a u_x = 0$, the new value is a weighted average of the two neighbours when $\abs{a} \Delta t \le \Delta x$.
