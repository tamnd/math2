---
tag: 8RA7AMWSAF
kind: concept
name: Conservation law
msc: [35L65, 35F20]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Conservation_law
---

## Summary

A conservation law is a [[partial differential equation|GC5BDZ6QBC]] of the form $u_t + \nabla \cdot F(u) = 0$.
It says that the amount of $u$ in a region changes only by the flux $F(u)$ through its boundary.
Mass, momentum and energy in continuum mechanics obey such laws.
Nonlinear conservation laws develop discontinuities in finite time, so their theory is built on weak solutions, [[shock waves|JSDMGGTG7G]] and entropy conditions.
See the [[definition|XYWMB0G011]].

## Explanations

### L1 human

Think of cars on a long road, with $u(x, t)$ the number of cars per kilometre.
Cars are neither created nor destroyed, so the number of cars between two points changes only because cars drive in at one end and out at the other.
The rate at which cars pass a point is the flux $F(u)$, which depends on how dense the traffic is.
Writing this bookkeeping for very short stretches of road gives the equation $u_t + F(u)_x = 0$.
