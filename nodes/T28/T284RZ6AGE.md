---
tag: T284RZ6AGE
kind: concept
name: Berkovich space
msc: [14G22, 32P05, 12J25]
sources:
  - url: https://en.wikipedia.org/wiki/Berkovich_space
same_as:
  wikidata: Q4892205
  wikipedia: Berkovich space
---

## Summary

A Berkovich space is an analytic space over a complete [[non-Archimedean|1H5F1BP6XS]] field whose points are multiplicative seminorms, see the [[definition|3JFF28P5NJ]].
Vladimir Berkovich introduced these spaces as a version of non-Archimedean analytic geometry with good topological properties.
Unlike the field itself, which is totally disconnected, Berkovich spaces are Hausdorff and locally path-connected, and the spectrum of a Banach algebra is compact.
They contain the points of a [[rigid analytic space|YAH6MZVG7K]] and add many new points.
This makes them a natural setting for [[non-Archimedean dynamics|6RM4RWWSSX]], potential theory and tropical geometry.

## Explanations

### L1 human

Over the $p$-adic numbers, two discs are either disjoint or one contains the other, and the space breaks into dust.
Berkovich's idea is to add a new point for every closed disc, together with some limit points.
A point is described by the way it measures the size of functions.
Over the field $\C_p$, the point of a disc measures a polynomial by its largest size on that disc.
For the closed unit disc, the new point for the whole disc measures $\sum a_n x^n$ by $\max_n \abs{a_n}$.
With these extra points the closed unit disc becomes a connected tree-like space, much closer to the picture of a complex disc.
