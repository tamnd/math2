---
tag: 8HAEC947YG
kind: statement
role: theorem
name: Griffiths inequality
msc: [82B20, 60K35]
uses: [R0KGM32QN6]
about: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Griffiths_inequality
same_as:
  wikidata: Q5608940
  wikipedia: Griffiths inequality
---

## Statement

Let $\Lambda$ be a finite set, and for $A \subseteq \Lambda$ and $\sigma \in \set{-1, +1}^\Lambda$ write $\sigma_A = \prod_{i \in A} \sigma_i$.
Let $J_A \ge 0$ for every $A \subseteq \Lambda$ (a ferromagnetic interaction; the sets with one element give external fields).
Write $\langle F \rangle$ for the average of $F$ under the probability measure on $\set{-1, +1}^\Lambda$ proportional to $\exp\big(\sum_{A \subseteq \Lambda} J_A \sigma_A\big)$.
Then for all $A, B \subseteq \Lambda$:

1. (First Griffiths inequality) $\langle \sigma_A \rangle \ge 0$.
2. (Second Griffiths inequality) $\langle \sigma_A \sigma_B \rangle \ge \langle \sigma_A \rangle \langle \sigma_B \rangle$.

## Remarks

For the first inequality, expand $\exp(\sum_C J_C \sigma_C)$ as a power series in the $J_C$ with nonnegative coefficients.
Each term is a product of spins, and summing $\sigma_A$ times such a product over all $\sigma$ gives either $2^{\abs{\Lambda}}$ or $0$.
For the second, take two independent copies $\sigma, \sigma'$ and apply the same expansion in the variables $\sigma_i$ and $\sigma_i \sigma'_i$.
The second inequality says that $\partial \langle \sigma_A \rangle / \partial J_B = \langle \sigma_A \sigma_B \rangle - \langle \sigma_A \rangle \langle \sigma_B \rangle \ge 0$: correlations increase when any coupling increases.
The sign condition matters: with a single antiferromagnetic bond $J_{\set{1,2}} < 0$ on two sites, $\langle \sigma_1 \sigma_2 \rangle = \tanh J_{\set{1,2}} < 0$.

Example: for the [[Ising model|R0KGM32QN6]] with $J > 0$ and $h \ge 0$, the magnetization $\langle \sigma_0 \rangle$ is nonnegative and increases with $J$, with $h$, and, under free boundary condition, with the box.

## Explanations

### L1 human

In a ferromagnet, every interaction pushes spins to agree.
The first inequality says that spin products are on average nonnegative; the second says that strengthening any interaction makes every such correlation larger.
These facts sound obvious, but they need proof, and they hold exactly under the stated sign condition.

### L2 human

The inequalities were proved by Robert Griffiths in 1967 for pair interactions and extended by Kelly and Sherman; they are also called the GKS inequalities.
They imply that correlations of the [[Ising model|R0KGM32QN6]] increase with the volume under free boundary condition and decrease under plus boundary condition, so the infinite-volume limits exist.
They also give monotonicity of the critical temperature in the couplings and comparison between lattices of different dimension.
Related tools are the FKG inequality and the GHS inequality, which controls third-order correlations.
