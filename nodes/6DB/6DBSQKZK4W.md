---
tag: 6DBSQKZK4W
kind: concept
name: Homoclinic orbit
msc: [34C37, 37C29]
sources:
  - url: https://en.wikipedia.org/wiki/Homoclinic_orbit
same_as:
  wikidata: Q690494
  wikipedia: Homoclinic orbit
---

## Summary

A homoclinic orbit is a [[trajectory|07TZ2Q4C1M]] that leaves an [[equilibrium point|0N8NGKDZDZ]] and returns to the same equilibrium.
It lies in both the stable and the unstable manifold of the equilibrium.
Homoclinic orbits separate regions of different behaviour in the phase plane, and they appear in global bifurcations.
In higher dimensions their transverse versions are a source of chaos.

## Explanations

### L1 human

Picture a loop in the phase plane that starts at a saddle point, swings around, and comes back to the same saddle.
A state on this loop takes infinitely long to leave the saddle and infinitely long to come back.
For the equation $x'' = x - x^2$, the solution $x(t) = \frac{3}{2} \operatorname{sech}^2(t/2)$ starts near $0$, rises to $\frac{3}{2}$ and falls back to $0$.
Its path in the $(x, x')$ plane is a homoclinic loop at the origin.
