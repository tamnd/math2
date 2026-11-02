---
tag: 5B6WEQX7XK
kind: concept
name: Microlocal analysis
msc: [35A27, 35S05, 58J40]
sources:
  - url: https://en.wikipedia.org/wiki/Microlocal_analysis
same_as:
  wikidata: Q430450
  wikipedia: Microlocal analysis
---

## Summary

Microlocal analysis studies functions, distributions and linear operators on $\R^n$ or on a manifold by localizing both in position $x$ and in frequency direction $\xi$.
Its natural home is phase space, the cotangent bundle, whose points are pairs $(x, \xi)$.
Its main tools are the [[wave front set|3T5Q9WVQX8]], [[pseudo-differential operators|FF27N0BWTP]] and [[Fourier integral operators|EVS4JPEE45]].
It explains where and in which directions solutions of linear [[partial differential equations|GC5BDZ6QBC]] are singular, and how these singularities move.

## Explanations

### L1 human

A function can be smooth in some places and rough in others.
Microlocal analysis also records the direction in which it is rough.
Picture a function on the plane that jumps across the line $x_1 = 0$: it is singular only on that line, and only in the directions $\pm(1, 0)$ normal to it.
The [[Fourier transform|DPVM34ADZV]] of the function, cut off near a point of the line, decays fast in every direction except those two.
This finer picture shows, for example, that singularities of waves travel along rays, as in [[propagation of singularities|P2QJ7NPW3Y]].
