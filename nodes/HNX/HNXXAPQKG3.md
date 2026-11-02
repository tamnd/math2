---
tag: HNXXAPQKG3
kind: concept
name: Topological conjugacy
msc: [37C15, 37B02]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_conjugacy
same_as:
  wikidata: Q2443460
  wikipedia: Topological conjugacy
---

## Summary

Two maps are topologically conjugate when a [[homeomorphism|0QT00PB5G2]] between their spaces turns one map into the other.
Conjugate systems have the same dynamics up to a continuous change of coordinates: fixed points, periodic orbits, dense orbits and attractors correspond.
Topological conjugacy is the basic notion of "same system" in topological dynamics, and many classification results, such as structural stability, are stated with it.
If the homeomorphism is only required to be a continuous surjection, one gets the weaker notion of a [[semiconjugacy|AEXJNRBASV]].

## Explanations

### L1 human

Imagine two maps that do the same thing, but one is drawn on a rubber sheet that has been stretched.
A conjugacy is the stretching that matches them up, step by step.
For example, $f(x) = x/2$ and $g(x) = x/8$ on the real line are conjugate through $h(x) = x^3$.
Indeed, $h(f(x)) = x^3/8 = g(h(x))$, so moving by $f$ and then changing coordinates is the same as changing coordinates and then moving by $g$.
