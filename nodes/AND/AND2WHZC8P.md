---
tag: AND2WHZC8P
kind: concept
name: Presheaf
msc: [18F20, 18A25]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Presheaf_(category_theory)
same_as:
  wikidata: Q7241077
  wikipedia: Presheaf (category theory)
---

## Summary

A presheaf on a [[category|A2DE66937D]] $\mathcal{C}$ is a contravariant [[functor|28NQ0KRHD3]] from $\mathcal{C}$ to the category of sets.
Presheaves on $\mathcal{C}$ and the natural transformations between them form a category that contains $\mathcal{C}$ and has all limits and colimits.
The name comes from topology, where a presheaf on a space assigns data to open sets with restriction maps to smaller open sets.

## Explanations

### L1 human

A presheaf attaches a set to each object.
For each arrow $X \to Y$ it gives a way to pull elements back from the set at $Y$ to the set at $X$.
The model case is a [[topological space|0CQHFPGJ45]]: to each open set $U$ attach the set of continuous real functions on $U$.
If $V \subseteq U$, a function on $U$ restricts to a function on $V$, so the maps go from big sets to small sets, against the inclusion.
Restricting twice is the same as restricting once, which is the functor rule.
