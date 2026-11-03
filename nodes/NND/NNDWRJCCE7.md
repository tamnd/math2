---
tag: NNDWRJCCE7
kind: definition
name: Linkage disequilibrium
msc: [92D10]
defines: 32QVKP24VJ
uses: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Linkage_disequilibrium
---

## Definition

Consider a population and two loci, the first with alleles $A$ and $a$ and the second with alleles $B$ and $b$.
Let $p_A$ and $p_B$ be the frequencies of $A$ and $B$, and let $p_{AB}$ be the frequency of chromosomes that carry both $A$ and $B$.
The *coefficient of linkage disequilibrium* is
$$D = p_{AB} - p_A \, p_B.$$
The two loci are in *linkage disequilibrium* if $D \ne 0$, and in linkage equilibrium if $D = 0$.

## Remarks

Example: let the chromosomes be $AB$ with frequency $1/2$ and $ab$ with frequency $1/2$.
Then $p_A = p_B = 1/2$ and $p_{AB} = 1/2$, so $D = 1/2 - 1/4 = 1/4 \ne 0$.

Non-example: let the four haplotypes $AB$, $Ab$, $aB$, $ab$ each have frequency $1/4$.
Then $p_{AB} = 1/4 = p_A \, p_B$, so $D = 0$ and the loci are in linkage equilibrium.

Normalised measures are common.
With $p_a = 1 - p_A$ and $p_b = 1 - p_B$, the squared correlation is $r^2 = D^2 / (p_A \, p_a \, p_B \, p_b)$, which lies in $[0, 1]$.
The measure $D'$ is $D$ divided by its largest possible absolute value given the allele frequencies.

Under random mating with recombination fraction $c$ between the loci, and with no other forces, $D_{t+1} = (1 - c) D_t$, so $D_t = (1 - c)^t D_0$.
