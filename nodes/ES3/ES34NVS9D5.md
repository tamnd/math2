---
tag: ES34NVS9D5
kind: statement
role: theorem
name: Ewens's sampling formula
msc: [92D15, 92D10, 60C05]
uses: [K7E0BWKBZK, 0404R9P9J3]
about: [K7E0BWKBZK]
sources:
  - url: https://en.wikipedia.org/wiki/Ewens%27s_sampling_formula
same_as:
  wikidata: Q5419007
  wikipedia: Ewens's sampling formula
---

## Statement

Consider a selectively neutral population at stationarity under the [[infinite alleles model|K7E0BWKBZK]] with scaled mutation rate $\theta > 0$.
Take a random sample of $n \ge 1$ genes from the population.
For $j = 1, \dots, n$, let $A_j$ be the number of allelic types that occur exactly $j$ times in the sample.
Let $a_1, \dots, a_n$ be nonnegative integers with $\sum_{j=1}^{n} j a_j = n$.
Then
$$P(A_1 = a_1, \dots, A_n = a_n) = \frac{n!}{\theta (\theta + 1) \cdots (\theta + n - 1)} \prod_{j=1}^{n} \frac{\theta^{a_j}}{j^{a_j} \, a_j!}.$$

## Remarks

The vector $(a_1, \dots, a_n)$ encodes an [[integer partition|0404R9P9J3]] of $n$: it has $a_j$ parts equal to $j$.
So the formula is a probability distribution on the partitions of $n$, called the Ewens distribution.

Proof idea: trace the ancestry of the sample backwards in time.
Each lineage either merges with another lineage or is hit by a mutation, and a mutation ends the lineage as a new type.
With $k$ lineages, the next event is a mutation with probability $\theta / (\theta + k - 1)$.
Multiplying these probabilities and counting the labelled configurations gives the formula.

Example: for $\theta = 1$ the formula becomes $\prod_{j} 1/(j^{a_j} a_j!)$.
This is the probability that a uniform random permutation of $n$ elements has $a_j$ cycles of length $j$ for each $j$.
The same distribution arises from the [[Chinese restaurant process|2SEF8QTYQF]].

The number $K = A_1 + \cdots + A_n$ of distinct types in the sample has mean $\sum_{i=0}^{n-1} \theta / (\theta + i)$.
For a diploid population of effective size $N_e$ and mutation rate $\mu$ per gene per generation, one takes $\theta = 4 N_e \mu$.

## Explanations

### L1 human

Sample some genes from a population where every mutation creates a brand new variant and no variant is favoured.
Ewens's formula tells how likely each pattern of repeats is: how many variants appear once, how many twice, and so on.
The answer depends on a single number $\theta$, which measures how fast mutations arrive compared to how fast chance removes variants.

### L2 human

The formula is the basic tool for testing neutrality from genetic data.
The formula contains $\theta$ only through the factor $\theta^{K}$ and the normalising constant.
Hence, given the number $K$ of types, the sample pattern no longer depends on $\theta$.
So $K$ is a sufficient statistic for $\theta$, and the conditional distribution given $K$ is used to test the neutral hypothesis.
The formula also appears in the [[unified neutral theory of biodiversity|3KWX3V8MPZ]], where species play the role of alleles.
In combinatorics it is a one-parameter deformation of the cycle structure of random permutations.
