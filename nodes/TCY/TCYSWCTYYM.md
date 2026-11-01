---
tag: TCYSWCTYYM
kind: concept
name: Poisson kernel
msc: [31A10, 31A05]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_kernel
same_as:
  wikidata: Q2596534
  wikipedia: Poisson kernel
---

## Summary

The Poisson kernel is the integral kernel that produces a [[harmonic function|0DEB0JMN0W]] in a disc from its values on the boundary circle.
On the unit disc it is $P(z, \zeta) = (1 - \abs{z}^2)/\abs{\zeta - z}^2$ for $\abs{z} < 1$ and $\abs{\zeta} = 1$.
Integrating a continuous function on the circle against it solves the [[Dirichlet problem|8D56GQ4AG8]] for the disc.
Similar kernels exist for the upper half-plane and for balls in $\R^n$.
They are central in harmonic analysis and in the theory of [[Hardy spaces|PNNNFJVF6W]].

## Explanations

### L1 human

Suppose you know the temperature at every point of the rim of a round plate and the plate is in equilibrium.
The temperature at an interior point is a weighted average of the rim temperatures.
The Poisson kernel gives the weights: rim points close to the interior point count more.
At the centre all rim points count equally, so the centre temperature is the plain average of the rim.
