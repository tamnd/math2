---
tag: 380DYJJWT0
kind: statement
role: theorem
name: Hardy–Weinberg principle
msc: [92D10]
uses: [CCN582E2C4]
about: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle
same_as:
  wikidata: Q49974
  wikipedia: Hardy–Weinberg principle
---

## Statement

Consider a diploid population and one autosomal locus with two alleles $A$ and $a$.
Assume the following.

1. The population is infinite, and generations do not overlap.
2. Mating is random with respect to the genotype at the locus.
3. There is no selection, no mutation and no migration.
4. The allele frequencies are the same in both sexes.

Let $p$ be the frequency of $A$ and $q = 1 - p$ the frequency of $a$ in the parent generation.
Then in the offspring generation the genotypes $AA$, $Aa$ and $aa$ have frequencies $p^2$, $2pq$ and $q^2$.
The allele frequencies remain $p$ and $q$, and so these genotype frequencies remain the same in all later generations.

## Remarks

Proof idea: under the assumptions, each offspring receives two gene copies drawn independently from the gene pool.
Each copy is $A$ with probability $p$, so the offspring is $AA$ with probability $p^2$, $Aa$ with probability $2pq$, and $aa$ with probability $q^2$.
The frequency of $A$ among the offspring is $p^2 + \frac{1}{2} \cdot 2pq = p (p + q) = p$.

Example: if $p = 0.7$, the genotype frequencies are $0.49$, $0.42$ and $0.09$.
Conversely, if a recessive trait shows in $1\%$ of a population at equilibrium, then $q^2 = 0.01$, so $q = 0.1$ and about $18\%$ of the population are carriers.

If mating is not random, the conclusion fails.
For example, under complete self-fertilisation the frequency of heterozygotes halves in each generation, while the allele frequencies stay the same.
With $k$ alleles of frequencies $p_1, \dots, p_k$, the equilibrium frequencies are $p_i^2$ for $A_i A_i$ and $2 p_i p_j$ for $A_i A_j$ with $i < j$.

## Explanations

### L1 human

Without selection, mutation, migration and chance, gene variants do not drift toward or away from any value: their frequencies just stay put.
Moreover, after one round of random mating, the share of each genotype is fixed by the allele frequencies alone.
This is the baseline: when real data differ from $p^2$, $2pq$, $q^2$, some evolutionary force or non-random mating is at work.

### L2 human

The principle was found independently by G. H. Hardy and Wilhelm Weinberg in 1908.
It is the neutral reference point of [[population genetics|CCN582E2C4]], playing the role that uniform motion plays in mechanics.
Statistical tests of Hardy–Weinberg proportions, such as a chi-squared test, check data for genotyping errors, inbreeding or population structure.
With two loci, random mating does not reach equilibrium in one generation; the [[linkage disequilibrium|32QVKP24VJ]] only decays geometrically.
