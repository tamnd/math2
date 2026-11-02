---
tag: PRCQG82QTK
kind: concept
name: Stochastic partial differential equation
msc: [60H15, 35R60, 60H17]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_partial_differential_equation
same_as:
  wikidata: Q16979017
  wikipedia: Stochastic partial differential equation
---

## Summary

A stochastic partial differential equation, or SPDE, is a [[partial differential equation|GC5BDZ6QBC]] driven by random noise.
Its unknown is a random field $u(t, x)$, and the noise is often space-time white noise, a random distribution that is very irregular.
SPDEs extend [[stochastic differential equations|B219G9SHJA]] from finitely many to infinitely many variables.
They model systems with random forcing in physics, biology and finance, such as growing interfaces described by the [[Kardar–Parisi–Zhang equation|RQ196EHXKC]].

## Explanations

### L1 human

Take the [[heat equation|VP2HN86VAG]], which describes how temperature spreads in a rod.
Now let the rod be heated by tiny random kicks, independent at every point and every instant.
The temperature then becomes a random function, and the equation that governs it is an SPDE.
Because the kicks are so rough, the solution is rough too, and even the meaning of the equation needs care.
In one space dimension the solution is still a continuous function, but in two or more dimensions it is only a distribution.
