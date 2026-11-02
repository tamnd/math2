---
tag: SQ6APWZBTR
kind: concept
name: Topological group structure of a vector space
msc: [46A03, 22A05]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Summary

Every [[topological vector space|T32W553W95]] is, under addition, a commutative [[topological group|92700QAB5Y]].
This additive structure is the source of many basic facts about topological vector spaces.
Translations are homeomorphisms, so the whole topology is fixed by the neighbourhoods of $0$.
It also gives each topological vector space a canonical uniform structure, so Cauchy nets and completeness make sense without a metric.

## Explanations

### L1 human

In a topological vector space you may add vectors, and adding is a continuous operation.
So, if you forget scalar multiplication, what is left is a group with a topology that fits the group law.
Shifting the whole space by a fixed vector moves open sets to open sets.
Hence, to know what "near $x$" means, it is enough to know what "near $0$" means and then shift.
For example, in $\R^2$ the open discs around a point $x$ are exactly the open discs around $0$ moved by $x$.
