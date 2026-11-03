---
tag: XD14B1J3EQ
kind: concept
name: Watterson estimator
msc: [62P10, 92D10]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Watterson_estimator
same_as:
  wikidata: Q7974953
  wikipedia: Watterson estimator
---

## Summary

The Watterson estimator estimates the scaled mutation rate $\theta$ of a population from the number of segregating sites in a sample of DNA sequences.
It divides that number by the harmonic number $1 + 1/2 + \cdots + 1/(n-1)$, where $n$ is the sample size.
Under the neutral [[infinite sites model|13AS2R963M]] with [[Kingman's coalescent|P2H42E2V2N]] genealogy it is an unbiased [[estimator|0SSS6ERQ0S]].

## Explanations

### L1 human

The more mutations a population has, the more positions differ among sampled sequences.
But a larger sample also shows more differing positions, because its family tree has more branches.
The Watterson estimator corrects for this by dividing the count by a factor that grows slowly with the sample size.
For example, if $4$ sequences differ at $11$ positions, the factor is $1 + 1/2 + 1/3 = 11/6$ and the estimate is $6$.
