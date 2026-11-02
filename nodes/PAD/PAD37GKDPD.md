---
tag: PAD37GKDPD
kind: concept
name: Chern class
msc: [14C17, 57R20, 55R40]
specializes: [7HACJC0JE2]
sources:
  - url: https://en.wikipedia.org/wiki/Chern_class
same_as:
  wikidata: Q1069818
  wikipedia: Chern class
---

## Summary

Chern classes are [[characteristic classes|7HACJC0JE2]] of complex vector bundles, with values in cohomology.
In algebraic geometry they are defined for algebraic vector bundles, with values in the [[Chow ring|4HV4WTAX9P]].
A vector bundle $E$ of rank $r$ has classes $c_0(E) = 1, c_1(E), \ldots, c_r(E)$, with $c_i$ in degree $i$.
They measure how far $E$ is from being trivial, and they enter the Riemann–Roch theorems through the [[Todd class|2YDB5089FR]].
For a line bundle, $c_1$ is the class of the corresponding divisor.

## Explanations

### L1 human

A vector bundle attaches a vector space to each point of a space, and it may twist as one moves around.
Chern classes are invariants that record this twisting in a way that can be computed and added.
For the line bundle $\mathcal{O}(d)$ on the projective line, the first Chern class is $d$ times the class of a point: its sections vanish at $d$ points.
For the tangent bundle of a compact complex curve of genus $g$, the first Chern class has degree $2 - 2g$, the Euler characteristic.
