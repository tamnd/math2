---
tag: FFYQAVT7MB
kind: concept
name: Picard–Lefschetz theory
msc: [32S50, 14D05, 32S30]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lefschetz_theory
same_as:
  wikidata: Q7190517
  wikipedia: Picard–Lefschetz theory
---

## Summary

Picard–Lefschetz theory studies the topology of a complex manifold through a holomorphic function on it with nondegenerate critical points.
It looks at how the fibres change near the critical values.
Its central result, the Picard–Lefschetz formula, describes the [[monodromy|C8HD62AB6Q]] around a critical value in terms of the [[vanishing cycle|M5EK9AKXNR]] $\delta$ of the critical point.
Let $X_t$ be a smooth fibre of complex dimension $n$, near a critical value with a single nondegenerate critical point.
Let $T$ be the monodromy on $H_n(X_t; \Z)$ around this value.
Then $T(a) = a + \varepsilon_n \langle a, \delta \rangle \delta$, where $\langle \cdot, \cdot \rangle$ is the [[intersection form|WK8GKRKAVD]].
Here $\varepsilon_n = \pm 1$ is a sign that depends only on $n$ and on orientation conventions.
Émile Picard developed the case of surfaces and Solomon Lefschetz the general case.
Lefschetz used it to study the topology of algebraic varieties through Lefschetz pencils, together with the [[Lefschetz hyperplane theorem|EX6YSYN7B4]].
Its version in étale cohomology was a main tool in Deligne's proof of the Weil conjectures.

## Explanations

### L1 human

Cut a complex variety into a family of slices given by the level sets of a function.
Most slices look alike, but at finitely many values a slice gets a simple singular point, where a sphere in the slice has shrunk to a point.
Picard–Lefschetz theory tells what happens to the other cycles of a slice when one walks once around such a bad value.
A cycle comes back changed by a multiple of the shrinking sphere, and the multiple is the number of times the cycle crosses that sphere, counted with signs.
For curves, $n = 1$, the change is a [[Dehn twist|W890NRHGS4]] along the vanishing circle.
