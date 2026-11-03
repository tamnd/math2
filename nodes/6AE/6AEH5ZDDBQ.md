---
tag: 6AEH5ZDDBQ
kind: concept
name: Fitness landscape
msc: [92D15]
sources:
  - url: https://en.wikipedia.org/wiki/Fitness_landscape
same_as:
  wikidata: Q3307742
  wikipedia: Fitness landscape
---

## Summary

A fitness landscape assigns a fitness value to each genotype, where genotypes are arranged so that those differing by one mutation are neighbours.
Evolution under selection and mutation is then pictured as a walk uphill on this landscape.
The shape of the landscape, smooth or rugged, with one peak or many, decides whether adaptation can reach the best genotypes.

## Explanations

### L1 human

Picture all possible genotypes laid out on the ground, with neighbours one mutation apart, and the height at each point equal to its fitness.
A population climbs by taking small steps to fitter neighbours.
On a landscape with one hill it always reaches the top.
On a rugged landscape it can get stuck on a small hill, a local peak, far from the highest one.
For example, for genotypes of two genes with alleles $0$ and $1$, the four genotypes $00, 01, 10, 11$ form a square, and fitnesses $1, 0.8, 0.8, 1.2$ give two peaks, at $00$ and at $11$.
