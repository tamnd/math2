---
tag: PQ6Q143ARJ
kind: concept
name: Sheaf cohomology
msc: [14F06, 55N30, 18G10]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_cohomology
same_as:
  wikidata: Q1493952
  wikipedia: Sheaf cohomology
---

## Summary

Sheaf cohomology assigns to a sheaf $\mathcal{F}$ on a space $X$ a sequence of groups $H^i(X, \mathcal{F})$, the right derived functors of the global sections functor.
In algebraic geometry it is applied to sheaves of modules on schemes, above all to [[quasi-coherent|KPKND0K7W6]] and [[coherent sheaves|56RXEJ8Z6S]].
For these the groups are modules, and in good cases finite-dimensional vector spaces.
It measures the failure of local sections to glue and of surjections of sheaves to be surjective on global sections.
The topological side of the theory, with constant and locally constant coefficients, is described in [[sheaf cohomology in topology|KB76923A1M]].

## Explanations

### L1 human

Global sections of a sheaf are the objects you can define on the whole space at once, such as functions or sections of a bundle.
When a short exact sequence of sheaves is given, the global sections need not form an exact sequence: something can exist locally but not globally.
Sheaf cohomology measures exactly this defect, in degree $1$, $2$, and so on.
For example, on the projective line over a field, $H^0$ of the structure sheaf is the field itself, the constant functions.
The bundle $\mathcal{O}(-2)$ has no sections, but its first cohomology group is one-dimensional.
