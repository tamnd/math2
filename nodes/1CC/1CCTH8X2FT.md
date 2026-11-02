---
tag: 1CCTH8X2FT
kind: concept
name: Parabolic partial differential equation
msc: [35K10, 35K25]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Parabolic_partial_differential_equation
same_as:
  wikidata: Q1575416
  wikipedia: Parabolic partial differential equation
---

## Summary

A parabolic partial differential equation is an evolution equation of the form $\partial_t u + L u = f$, where $L$ is an elliptic operator in the space variables.
The model case is the [[heat equation|VP2HN86VAG]].
Parabolic equations describe diffusion: they smooth out the initial data, propagate information at infinite speed, and are well posed forward in time but not backward.
See the [[definition|WJGY7XG3QR]].

## Explanations

### L1 human

Drop some ink in still water: it spreads out, its sharp edges blur, and after a while the colour is nearly uniform.
A parabolic equation describes such a process.
The [[heat equation|VP2HN86VAG]] $\partial_t u = \partial_x^2 u$ says that the temperature rises where the graph of $u$ curves upward, that is, where the point is colder than its neighbours.
So hot spots cool down and cold spots warm up.
Running the process backward in time, from a blurred state to a sharp one, is unstable.
