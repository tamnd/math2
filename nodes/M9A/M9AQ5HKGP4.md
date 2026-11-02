---
tag: M9AQ5HKGP4
kind: concept
name: Analysis of variance
msc: [62J10]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_of_variance
same_as:
  wikidata: Q42297
  wikipedia: Analysis of variance
---

## Summary

Analysis of variance, or ANOVA, is a family of methods that split the total variation of a response into parts.
Each part is due to one source, such as treatment groups or random error.
Its best known use is to test whether several group means are equal.
The test compares the variation between groups with the variation within groups through an [[F-test|8MTVCMAATD]].
It was developed by Ronald Fisher for agricultural experiments and is a central tool of [[design of experiments|2TE42ZWJ3E]].
The fixed-effects models of ANOVA are special cases of the [[general linear model|A06SGFCSCE]].

## Explanations

### L1 human

Suppose three fertilisers are each tried on several plots and the yields vary.
Some of the variation is because the fertilisers differ, and some is just plot-to-plot noise.
ANOVA measures both: how far the group averages are from the overall average, and how far the plots are from their own group average.
If the first is large compared with the second, the fertilisers probably differ.
For the groups $\{1, 2, 3\}$ and $\{4, 5, 6\}$, the between-group sum of squares is $13.5$ and the within-group sum is $4$, which together make the total $17.5$.
