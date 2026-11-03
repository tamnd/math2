---
tag: KYCK3KFM4X
kind: concept
name: Computational phylogenetics
msc: [92B10, 92-08]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_phylogenetics
same_as:
  wikidata: Q3772859
  wikipedia: Computational phylogenetics
---

## Summary

Computational phylogenetics is the use of algorithms and statistics to infer [[phylogenetic trees|RK58WSHJSG]] from data such as DNA sequences.
Its main approaches are distance methods such as [[neighbor joining|M81NRAZVH0]], [[maximum parsimony|59450K6JK8]], maximum likelihood and Bayesian inference.
Because the number of trees grows faster than exponentially in the number of taxa, exact optimisation is hard and heuristic search is the rule.

## Explanations

### L1 human

We cannot watch evolution happen over millions of years, but we can compare the DNA of living species.
Species with similar DNA are probably closely related.
Computational phylogenetics turns this idea into precise methods that take many sequences and output a tree.
Each method scores possible trees, by how few mutations they need or by how probable they make the data, and searches for the best one.
