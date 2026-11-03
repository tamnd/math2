---
tag: ZAR3CFP7K1
kind: definition
name: Diversity index
msc: [92D40]
defines: Q5EMPF44S1
uses: [0044CPHJBV]
sources:
  - url: https://en.wikipedia.org/wiki/Diversity_index
---

## Definition

Let a community contain $S \ge 1$ species, and let $p_1, \dots, p_S$ be their relative abundances, so that $p_i > 0$ for each $i$ and $p_1 + \cdots + p_S = 1$.
A *diversity index* is a function of the vector $(p_1, \dots, p_S)$ that measures the diversity of the community.
The standard diversity indices are these.

1. The *species richness* is $S$.
2. The *Shannon index* is $H = -\sum_{i=1}^{S} p_i \ln p_i$, where $\ln$ is the [[natural logarithm|0044CPHJBV]].
3. The *Simpson index* is $\lambda = \sum_{i=1}^{S} p_i^2$.
4. For a real number $q \ge 0$ with $q \ne 1$, the *Hill number of order $q$* is $^{q}D = \left( \sum_{i=1}^{S} p_i^q \right)^{1/(1-q)}$, and $^{1}D = e^{H}$.

## Remarks

The Hill numbers unify the other indices: $^{0}D = S$, $^{1}D = e^{H}$ is the limit of $^{q}D$ as $q \to 1$, and $^{2}D = 1/\lambda$.
The number $^{q}D$ is the number of equally abundant species that would give the same value of the index, so it is called an effective number of species.

Example: for $S = 2$ species with $p_1 = p_2 = 1/2$, one gets $H = \ln 2$ and $\lambda = 1/2$.
For $q \ne 1$, $^{q}D = (2 \cdot 2^{-q})^{1/(1-q)} = (2^{1-q})^{1/(1-q)} = 2$.
Indeed, for $S$ equally abundant species every Hill number equals $S$.

Non-example: the vector $(0.5, 0.6)$ is not a vector of relative abundances, because its entries sum to $1.1$ and not to $1$, so the indices above are not defined for it.

The Simpson index is the probability that two individuals drawn at random with replacement belong to the same species, so $1 - \lambda$ is often reported instead.
