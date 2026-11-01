---
tag: GJHAF85F4S
kind: concept
name: Strict Henselization
msc: [13J15, 13B40]
specializes: [MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Summary

The strict Henselization of a [[local ring|MZ02BKPHJA]] $R$ is a [[Henselian local ring|RNXPV3KC5J]] over $R$.
Its residue field is a separable closure of the residue field of $R$.
It is universal among local maps from $R$ to strictly Henselian local rings, that is, Henselian local rings with a separably closed residue field.
It refines the [[Henselization|917PGHVZPM]], which keeps the residue field unchanged.
In algebraic geometry the strict Henselizations of the local rings of a scheme are the stalks of its structure sheaf for the étale topology.

## Explanations

### L1 human

The Henselization of a local ring lifts every simple root that exists modulo the maximal ideal.
The strict Henselization goes further: it first enlarges the residue field until every separable polynomial has a root there, and then lifts these roots.
For a field $k$, the strict Henselization is a separable closure of $k$.
For the $p$-adic integers, it is the ring of integers of the maximal unramified extension of the $p$-adic numbers.
It is the ring that sees a point of a space together with all its étale neighbourhoods.
