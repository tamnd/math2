---
tag: Z1MHMGFNFW
kind: concept
name: Subharmonic function
msc: [31A05, 31B05]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
same_as:
  wikidata: Q753658
  wikipedia: Subharmonic function
---

## Summary

A subharmonic function is an upper semicontinuous function whose value at each point is at most its average over small circles around that point.
Subharmonic functions play the role in two real dimensions that convex functions play in one.
For a holomorphic function $f$, the functions $\log\abs{f}$ and $\abs{f}^p$ with $p > 0$ are subharmonic, which links complex analysis with [[potential theory|9PM8Q2E30Q]].
They are the main tool in Perron's method for the [[Dirichlet problem|8D56GQ4AG8]] and in the study of growth of holomorphic functions.

## Explanations

### L1 human

A [[harmonic function|0DEB0JMN0W]] equals its average over every circle around a point.
A subharmonic function is at most that average, so it sags below its surroundings and cannot have a strict local maximum inside its domain.
A good picture is a rubber sheet pulled down at some points by weights hanging from it.
For example, $\abs{z}^2$ is subharmonic: its value $0$ at the origin is below its average $r^2$ over the circle of radius $r$.
