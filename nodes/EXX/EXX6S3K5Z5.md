---
tag: EXX6S3K5Z5
kind: concept
name: Transfer matrix method
msc: [82B20, 82B23]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer-matrix_method_(statistical_mechanics)
same_as:
  wikidata: Q7833983
  wikipedia: Transfer-matrix method (statistical mechanics)
---

## Summary

The transfer matrix method applies to models built from layers.
It writes the partition function as the [[trace|0KZDNGA561]] of a power of one matrix, the transfer matrix.
The free energy per layer is then the logarithm of the largest [[eigenvalue|0BQAA2BK3Q]] of that matrix.
The correlation length comes from the ratio of the two largest eigenvalues.
It solves one-dimensional models with short-range interactions completely.
In two dimensions it turns the problem into the diagonalization of a large matrix.
This is the route of [[Onsager's solution|JJ4ZH5YD80]] and of many [[exactly solvable models|DVQ0PVHKY1]].

## Explanations

### L1 human

To sum over all configurations of a long chain, build the chain one site at a time.
A small table, the transfer matrix, records the Boltzmann weight of passing from one site state to the next.
Adding a site means multiplying by the table, so a ring of $N$ sites gives the trace of the $N$-th power of the table.
For the Ising chain the table is $2 \times 2$, and its larger eigenvalue $2 \cosh \beta J$ gives the free energy at once.
