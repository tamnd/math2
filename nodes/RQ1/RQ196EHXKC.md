---
tag: RQ196EHXKC
kind: concept
name: Kardar–Parisi–Zhang equation
msc: [60H15, 35R60, 35Q82]
sources:
  - url: https://en.wikipedia.org/wiki/Kardar%E2%80%93Parisi%E2%80%93Zhang_equation
same_as:
  wikidata: Q6369122
  wikipedia: Kardar–Parisi–Zhang equation
---

## Summary

The Kardar–Parisi–Zhang (KPZ) equation is the [[stochastic partial differential equation|PRCQG82QTK]] $h_t = \nu h_{xx} + \frac{\lambda}{2} (h_x)^2 + \xi$, where $\xi$ is space-time white noise.
It was proposed by Kardar, Parisi and Zhang in 1986 as a model for a randomly growing interface.
Its solutions are so rough that the square $(h_x)^2$ has no classical meaning, and giving the equation a meaning is a hard problem.
It is the centre of the KPZ universality class, which contains many growth and particle models.
The large-time fluctuations in this class are described by distributions from random matrix theory, such as the Tracy–Widom distribution.

## Explanations

### L1 human

Picture the edge of a burning sheet of paper or a growing bacterial colony.
The height $h$ of the edge grows faster where it is tilted, is smoothed by the second derivative, and is kicked by random noise.
The fluctuations of such an interface grow like $t^{1/3}$, not like $t^{1/4}$ as for the linear equation without the square term.
The [[Cole–Hopf transformation|VBMQ9SJ3DH]] $Z = e^{\lambda h/(2\nu)}$ turns the equation formally into a linear heat equation with random multiplicative noise.
