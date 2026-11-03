---
tag: 9GGRK9ESD6
kind: definition
name: Heritability
msc: [92D10, 62P10]
defines: 7DKAA05J6R
uses: [007QED3E0Y, 0DKRR22AEQ, PKFPHK189T]
sources:
  - url: https://en.wikipedia.org/wiki/Heritability
---

## Definition

Consider a quantitative trait in a population, and let $P$ be the phenotype of a random individual.
Write $P = G + E$, where $G$ is the genotypic value, the mean phenotype of individuals with that genotype.
Then $E = P - G$ is the environmental deviation; $P$, $G$ and $E$ are [[random variables|0DKRR22AEQ]].
Write $G = A + D + I$, with the dominance deviation $D$ and the epistatic deviation $I$.
Here the additive value $A$ is the best [[linear regression|PKFPHK189T]] of $G$ on the allele counts at the loci.
Assume $\operatorname{Cov}(G, E) = 0$, so that $V_P = V_G + V_E$, and that $V_P > 0$, where $V_X$ is the [[variance|007QED3E0Y]] of $X$.

1. The *broad-sense heritability* is $H^2 = V_G / V_P$.
2. The *narrow-sense heritability* is $h^2 = V_A / V_P$.

## Remarks

Under random mating and linkage equilibrium the parts $A$, $D$, $I$ are uncorrelated, so $V_G = V_A + V_D + V_I$, and $0 \le h^2 \le H^2 \le 1$.
Example: if $V_A = 20$, $V_D = 10$, $V_I = 0$ and $V_E = 70$, then $V_P = 100$, $H^2 = 0.3$ and $h^2 = 0.2$.
Non-example: in a population of genetically identical clones, $V_G = 0$, so $H^2 = 0$ even for a trait that genes fully control in other populations; heritability measures variation, not causation.
If the trait does not vary, $V_P = 0$ and heritability is not defined.
