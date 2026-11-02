---
tag: 3BAJ8ZTVPX
kind: concept
name: von Neumann bounded set
msc: [46A17, 46A03]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_set_(topological_vector_space)
same_as:
  wikidata: Q17003677
  wikipedia: Bounded set (topological vector space)
---

## Summary

A subset of a topological vector space is von Neumann bounded if a large enough scaling shrinks it into any given neighbourhood of $0$.
It replaces the notion of a [[bounded set|09QSZVVM26]] of a metric space.
That notion does not suit topological vector spaces, since a metric may make the whole space bounded.
In a normed space the von Neumann bounded sets are the sets of finite norm diameter.
Bounded sets are used to define the [[strong dual space|RG52DZ1A8Y]], [[bornological spaces|4R6SQD60FN]] and [[Montel spaces|NWMYW2WK9S]].

## Explanations

### L1 human

Pick any small neighbourhood of the origin, however tiny.
A set is bounded if, after you divide it by a large enough number, it fits inside that neighbourhood.
In $\R^2$ this is the usual idea: a set is bounded if it fits inside some disc.
A straight line through the origin is not bounded, because no rescaling of it fits in a small disc.
In a space of functions with seminorms $p_n$, a set is bounded when each $p_n$ is bounded on it, possibly with a different bound for each $n$.
