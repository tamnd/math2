---
tag: V265MVHF6M
kind: concept
name: Projection method
msc: [76M20, 76D05, 65M06]
specializes: [T4ZFKBZRYK]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_method_(fluid_dynamics)
same_as:
  wikidata: Q7249451
  wikipedia: Projection method (fluid dynamics)
---

## Summary

The projection method is a time-stepping scheme for the incompressible [[Navier–Stokes equations|18KXZHVF4M]].
Each step first advances the velocity without the pressure and then projects it onto divergence-free fields, which produces the pressure as a by-product.
The projection is the discrete form of the [[Helmholtz decomposition|C75W88ZVNY]] and costs one Poisson solve per step.
It was introduced by Alexandre Chorin, and independently by Roger Temam, and it is one of the standard methods of [[computational fluid dynamics|T4ZFKBZRYK]].
It is a different method from the [[projection method for integral equations|2AFNVJ54G7]].

## Explanations

### L1 human

In an incompressible fluid, velocity and pressure are tied together: the pressure is whatever it must be to keep the fluid from being squeezed.
Solving for both at once is expensive.
The projection method splits the job: first move the fluid as if there were no pressure, which squeezes it a little.
Then compute the pressure that undoes the squeezing and correct the velocity with it.
