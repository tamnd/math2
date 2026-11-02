---
tag: 2T8MYCZ7N4
kind: concept
name: Finite element exterior calculus
msc: [65N30, 65N12, 58A12]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_exterior_calculus
same_as:
  wikidata: Q19597249
  wikipedia: Finite element exterior calculus
---

## Summary

Finite element exterior calculus is a framework for designing and analysing finite element methods with the tools of [[differential forms|0E3G0GRPZ6]] and [[de Rham cohomology|GX74C07T0G]].
It was developed by Douglas Arnold, Richard Falk and Ragnar Winther.
Its central idea is that finite element spaces should form a subcomplex of the de Rham complex, with projections that commute with the [[exterior derivative|0ZHSTAG8ZY]].
Such spaces give stable [[mixed finite element methods|87VMQ892VW]] for the Hodge Laplacian and explain many earlier elements in one theory.
See the [[definition|GRBZT7SWK0]].

## Explanations

### L1 human

In three dimensions, the gradient, the curl and the divergence form a chain: the curl of a gradient is zero, and so is the divergence of a curl.
Good numerical methods for electromagnetism or fluid flow must respect this chain.
Finite element exterior calculus builds matching chains of finite element spaces, one space for each link.
For example, continuous piecewise linear functions, Nédélec edge elements, Raviart–Thomas face elements and piecewise constants form such a chain.
