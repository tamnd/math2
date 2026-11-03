---
tag: 1EEFBQJJ7K
kind: definition
name: Population genetics
msc: [92D10, 92D15]
defines: CCN582E2C4
uses: [0QB913WM5E, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Population_genetics
---

## Definition

Consider a population of organisms and a genetic locus with a finite set of alleles $\set{A_1, \dots, A_k}$.
The *allele frequency* $p_i(t)$ is the fraction of gene copies at the locus that are $A_i$ at time $t$.
So $p_i(t) \ge 0$ and $p_1(t) + \cdots + p_k(t) = 1$.
*Population genetics* is the study of the change of allele frequencies and of genotype frequencies in populations.
Its models give the frequencies at time $t + 1$ from those at time $t$, either deterministically or as a [[stochastic process|0QH5ENKZM1]].
They describe the effects of the following forces.

1. Mutation, which changes one allele into another.
2. Selection, which gives different reproductive success to different genotypes.
3. Genetic drift, which is the random change of frequencies in a finite population.
4. Migration between populations, and recombination between loci.

## Remarks

Example: in a diploid population with alleles $A$ and $a$, the allele frequency $p$ of $A$ is $(2 n_{AA} + n_{Aa}) / (2 n)$.
Here $n_{AA}$ and $n_{Aa}$ are the numbers of individuals of genotypes $AA$ and $Aa$, and $n$ is the population size.
For $n = 100$, $n_{AA} = 30$ and $n_{Aa} = 40$, one gets $p = 100/200 = 0.5$.

Non-example: the vector $(0.6, 0.6)$ is not a vector of allele frequencies, since its entries do not sum to $1$.

The vector of allele frequencies is a [[probability distribution|0QB913WM5E]] on the set of alleles, that is, a point of a simplex.
