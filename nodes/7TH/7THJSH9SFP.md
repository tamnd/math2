---
tag: 7THJSH9SFP
kind: concept
name: LF-space
msc: [46A13]
specializes: [B6GY2KJMWW]
sources:
  - url: https://en.wikipedia.org/wiki/LF-space
same_as:
  wikidata: Q158565
  wikipedia: LF-space
---

## Summary

An LF-space is a [[locally convex space|B6GY2KJMWW]] obtained as the inductive limit of an increasing sequence of [[Fréchet spaces|3GAA614673]].
The letters stand for "limit of Fréchet spaces".
The main example is the space $C_c^\infty(\Omega)$ of test functions on an open set $\Omega \subseteq \R^d$.
It is the union, over compact sets $K \subseteq \Omega$, of the Fréchet spaces of smooth functions supported in $K$.
Its dual is the space of distributions.
LF-spaces are [[barrelled|ZE6DXEJB8H]] and [[bornological|4R6SQD60FN]], although they are usually not metrizable.

## Explanations

### L1 human

Some spaces are natural unions of a growing chain of nicer spaces.
Smooth functions with compact support are the union of the smooth functions supported in $[-1, 1]$, in $[-2, 2]$, in $[-3, 3]$, and so on.
Each piece is a Fréchet space with a good topology.
The LF topology glues these topologies together in the best convex way.
For test functions, a sequence converges when all its terms lie in one piece and it converges there.
In particular the supports must stay in a fixed compact set.
