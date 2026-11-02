---
tag: 5EHD2XBQDG
kind: concept
name: Wave equation
msc: [35L05, 35L15]
specializes: [92C3S03AQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_equation
same_as:
  wikidata: Q193846
  wikipedia: Wave equation
---

## Summary

The wave equation $u_{tt} = c^2 \Delta u$ is the basic [[hyperbolic partial differential equation|92C3S03AQZ]].
It describes vibrating strings and membranes, sound, and light in vacuum.
Its solutions travel at the finite speed $c$.
In one space dimension every solution is a sum of a wave moving left and a wave moving right.
It is the model for the theory of hyperbolic equations, just as the [[heat equation|VP2HN86VAG]] is for parabolic ones.

## Explanations

### L1 human

Pluck a guitar string: the displacement $u(x, t)$ of the string obeys the wave equation.
The acceleration $u_{tt}$ of a piece of string is proportional to its curvature $u_{xx}$, because tension pulls a bent piece back toward straight.
A bump on the string splits into two bumps that move apart at speed $c$ without changing shape.
For example, $u(x, t) = \sin(x - ct)$ is a wave that moves to the right at speed $c$.
