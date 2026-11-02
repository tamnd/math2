---
tag: AC6WNX8F9Z
kind: concept
name: Yamabe flow
msc: ["53E20", "53C21"]
sources:
  - url: https://en.wikipedia.org/wiki/Yamabe_flow
same_as:
  wikidata: Q8047576
  wikipedia: Yamabe flow
---

## Summary

The Yamabe flow is an evolution equation for a [[Riemannian metric|Q61VFHCH2J]].
The metric changes in the direction of minus its [[scalar curvature|ZHX2VYQDZ3]] times itself.
Richard Hamilton introduced it as a tool for the Yamabe problem.
This problem asks for a metric of constant scalar curvature in a given conformal class.
The flow keeps the metric in its conformal class.
Its fixed points, after normalizing the volume, are the metrics of constant scalar curvature.

## Explanations

### L1 human

A metric tells how to measure lengths on a curved space.
The Yamabe flow rescales lengths at each point: it shrinks them where the scalar curvature is positive and stretches them where it is negative.
Angles never change, because the change at each point is a pure rescaling.
The hope is that the curvature evens out over time.
For example, the round sphere of dimension $n$ and radius $1$ shrinks: its metric at time $t$ is $1 - n(n-1)t$ times the original one, until it collapses at $t = 1/(n(n-1))$.
