---
tag: AQ9VDJKJ3X
kind: definition
name: Infinite alleles model
msc: [92D10, 92D15]
defines: K7E0BWKBZK
uses: [SR4F169EKF, CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_alleles_model
---

## Definition

Let a population of genes evolve by a neutral reproduction model, such as the [[Wright–Fisher model|SR4F169EKF]].
In such a model each gene of the next generation copies the type of one parent gene.
Let $u \in (0, 1)$ be the mutation probability per gene per generation.
The *infinite alleles model* is the following rule for types:

1. Each offspring gene keeps the type of its parent with probability $1 - u$.
2. With probability $u$ it receives a new type, different from every type that is or ever was present in the population.

The data of the model is the partition of the genes into classes of equal type; the labels of the types carry no information.

## Remarks

Example: take the neutral Wright–Fisher model with $N$ diploid individuals.
Let $F$ be the probability that two genes drawn at random have the same type.
For large $N$ and small $u$, its equilibrium value is $F \approx 1/(1 + 4Nu)$.
This uses only clauses 1 and 2: two genes are of the same type exactly when no mutation occurs on either line back to their common ancestor.
Non-example: a model with two alleles $A$ and $a$ and mutation in both directions fails clause 2, since a mutation can recreate a type that is already present.
The quantity $\theta = 4Nu$ is the standard scaled mutation rate of the model.
