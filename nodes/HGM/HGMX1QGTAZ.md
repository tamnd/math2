---
tag: HGMX1QGTAZ
kind: concept
name: Eikonal equation
msc: [35F21, 78A05, 35F30]
specializes: [5TRXQKP7DY]
sources:
  - url: https://en.wikipedia.org/wiki/Eikonal_equation
same_as:
  wikidata: Q1303846
  wikipedia: Eikonal equation
---

## Summary

The eikonal equation $\abs{\nabla u} = f$ says that the gradient of the unknown function has a prescribed length at each point.
It is a stationary [[Hamilton–Jacobi equation|5TRXQKP7DY]].
Its solutions measure travel times: with $f = 1$ and $u = 0$ on the boundary of a domain, the [[viscosity solution|H1ERJ3T75T]] is the distance to the boundary.
It is the basic equation of [[geometric optics|90F3NWRHVD]], where the level sets of $u$ are the wave fronts.
See the [[definition|X8CF1K8QB4]].

## Explanations

### L1 human

Light a fire along the edge of a field, and suppose that the fire spreads with speed $1/f(x)$ at the point $x$.
Let $u(x)$ be the time at which the fire reaches $x$.
Moving one step in the best direction raises the arrival time at rate $f(x)$, and this is what $\abs{\nabla u} = f$ says.
For a disc of radius $1$ with $f = 1$, the fire burns inward from the circle, and $u(x) = 1 - \abs{x}$.
At the centre the fronts from all sides meet, and $u$ has a corner there.
