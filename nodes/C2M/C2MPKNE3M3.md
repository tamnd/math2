---
tag: C2MPKNE3M3
kind: definition
name: Computational phylogenetics
msc: [92B10, 92-08]
defines: KYCK3KFM4X
uses: [5624H8KWKK, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_phylogenetics
---

## Definition

Let $X$ be a finite set of taxa.
The data is either a distance matrix on $X$ or a character matrix.
A character matrix assigns to each taxon a state for each of $m$ characters, such as the sites of aligned DNA sequences.
A *tree inference problem* asks for a [[phylogenetic tree|5624H8KWKK]] on $X$ that optimises a criterion of fit to the data.
The tree may carry edge lengths, and the usual criteria are:

1. the number of character changes the tree requires (maximum parsimony);
2. the probability of the data under a stochastic model of evolution along the tree (maximum likelihood);
3. the agreement between the tree distances and the given distances (distance methods);
4. the posterior probability of the tree under a prior (Bayesian inference).

*Computational phylogenetics* is the study of [[algorithms|9DMSG5HAQX]] that solve or approximate tree inference problems, and of their statistical properties.

## Remarks

Example: for three taxa $a, b, c$ and one binary character with states $0, 0, 1$, all three rooted binary trees need exactly one change, so maximum parsimony cannot choose between them.
Non-example: drawing a tree by hand from expert opinion about shared features, with no stated criterion, is not a tree inference problem in this sense.
Key properties studied are consistency (recovering the true tree as the data grow) and complexity (for example, maximum parsimony is NP-hard).
