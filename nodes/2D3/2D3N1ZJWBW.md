---
tag: 2D3N1ZJWBW
kind: concept
name: Fully nonlinear PDE
msc: [35A99, 35J60]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_partial_differential_equation
---

## Summary

A fully nonlinear PDE is a [[partial differential equation|GC5BDZ6QBC]] that depends nonlinearly on the highest-order derivatives of the unknown.
Examples are the [[Monge–Ampère equation|14AKAC0S0T]], the [[eikonal equation|HGMX1QGTAZ]] and the [[Hamilton–Jacobi equation|5TRXQKP7DY]].
Such equations often lack classical solutions, and notions such as [[viscosity solutions|H1ERJ3T75T]] were developed for them.
See the [[definition|MTQ3SGX56W]].

## Explanations

### L1 human

In a fully nonlinear equation the highest derivatives are squared, multiplied together or put inside other nonlinear functions.
For instance, $\abs{\nabla u} = 1$ asks for a function whose gradient always has length $1$.
The distance to a closed set has this property wherever it is differentiable away from the set, but it can have corners.
For example, the distance to the two points $\pm 1$ on the real line has a corner at $0$.
So even simple fully nonlinear equations force one to accept nonsmooth solutions.
