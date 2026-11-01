---
tag: RGCZ2P9QRM
kind: statement
role: theorem
name: Bing metrization theorem
msc: ["54E35"]
uses: [0CQHFPGJ45, 03HMJASQBQ, 0S1FJ8VEX9, 091GJ3FYD7]
about: [091GJ3FYD7]
sources:
  - url: https://en.wikipedia.org/wiki/Bing_metrization_theorem
same_as:
  wikidata: Q17081508
  wikipedia: Bing metrization theorem
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]].
A family $\mathcal{F}$ of subsets of $X$ is *discrete* if each point of $X$ has a neighbourhood that meets at most one member of $\mathcal{F}$.
A family is *$\sigma$-discrete* if it is a union of countably many discrete families.
Then $X$ is [[metrizable|091GJ3FYD7]] if and only if $X$ is [[regular|03HMJASQBQ]], [[Hausdorff|0S1FJ8VEX9]] and has a $\sigma$-discrete base.

## Remarks

A discrete family is locally finite, so one direction follows from the [[Nagata–Smirnov metrization theorem|KB11T6389G]].
For the other direction, take a metric space.
The cover by balls of radius $1/n$ has a $\sigma$-discrete open refinement, built with a well-order of the balls.
The union over $n$ of these refinements is a $\sigma$-discrete base.
In the real line, the open intervals with rational endpoints form a countable base, and a countable base is $\sigma$-discrete.

## Explanations

### L1 human

The theorem is another exact test for when a topology comes from a distance.
It asks for basic open sets in countably many layers, where in each layer the sets are spread apart.
Near each point at most one set of the layer is present.

### L2 human

The theorems of Bing and of Nagata–Smirnov were found independently and give the same class of spaces.
Bing's form is often handy in proofs, because a discrete family behaves like a disjoint family of sets that are also kept apart from each other.
In the same work Bing proved that a collectionwise normal [[Moore space|68MA0RM5P6]] is metrizable.
