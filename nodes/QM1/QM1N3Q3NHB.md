---
tag: QM1N3Q3NHB
kind: definition
name: Models of DNA evolution
msc: [92D15, 92D20, 60J27]
defines: 5G0AKZ8SXJ
uses: [8FQFR871KM, TWQFE0FZZS, 0KRH5157WP]
sources:
  - url: https://en.wikipedia.org/wiki/Models_of_DNA_evolution
---

## Definition

A *model of DNA evolution* is a [[substitution model|8FQFR871KM]] on the alphabet $\Sigma = \set{A, C, G, T}$.
So it is given by a rate matrix $Q = (q_{ij})$ indexed by the four nucleotides, with $q_{ij} \ge 0$ for $i \ne j$ and zero row sums.
The *general time-reversible model* (GTR) is the family of rate matrices of the form $q_{ij} = s_{ij} \pi_j$ for $i \ne j$.
Here $\pi = (\pi_A, \pi_C, \pi_G, \pi_T)$ is a probability vector with positive entries, and $s_{ij} = s_{ji} \ge 0$ are six exchange rates.

## Remarks

In GTR the vector $\pi$ is the [[stationary distribution|0KRH5157WP]], and $\pi_i q_{ij} = \pi_i \pi_j s_{ij} = \pi_j q_{ji}$, so the chain is time-reversible.
The standard named models are special cases of GTR.
The Jukes–Cantor model (JC69) has all $s_{ij}$ equal and all $\pi_j = 1/4$.
The Kimura two-parameter model (K80) has all $\pi_j = 1/4$ and two values of $s_{ij}$: one for transitions ($A \leftrightarrow G$, $C \leftrightarrow T$) and one for transversions.
The Felsenstein model (F81) has all $s_{ij}$ equal and arbitrary $\pi$.
The HKY85 model combines the two rates of K80 with the arbitrary $\pi$ of F81.
Non-example: take a nucleotide rate matrix with $q_{AC} = 1$ and $q_{CA} = 0$.
It cannot be written as $s_{ij} \pi_j$ with $s$ symmetric and $\pi$ positive, so it is a model of DNA evolution but not a GTR model.
