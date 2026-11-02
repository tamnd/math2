---
tag: AN0BYRKNRA
kind: concept
name: Dimension of an analytic set
msc: [32B10, 32C25]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Summary

The dimension of a [[complex analytic variety|GB7M582M5Y]] at a point measures how many complex parameters are needed to describe it near that point.
At a [[regular point|ZW5A88PCPK]] it is the dimension of the set as a complex manifold.
At a singular point it is the largest dimension of the manifold pieces nearby.
It agrees with the Krull dimension of the local ring of the set, and with the number $d$ of the local parametrization theorem.

## Explanations

### L1 human

A curve has dimension $1$ and a surface dimension $2$, counted in complex parameters.
An analytic set can mix pieces of different dimensions.
In $\C^3$, take the union of the plane $\set{z_3 = 0}$ and the line $\set{z_1 = z_2 = 0}$.
It has dimension $2$ at the origin, where the plane passes, and dimension $1$ at the points of the line away from the plane.
