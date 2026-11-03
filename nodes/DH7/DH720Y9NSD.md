---
tag: DH720Y9NSD
kind: concept
name: Kostant partition function
msc: [17B10, 17B22, "05E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Kostant_partition_function
same_as:
  wikidata: Q6433478
  wikipedia: Kostant partition function
---

## Summary

The Kostant partition function of a [[root system|AVVV93CASN]] counts the ways to write a vector as a sum of positive roots, with repetitions allowed.
It generalises the count of [[integer partitions|0JV30XN73Z]] into parts of given sizes.
It gives the weight multiplicities of [[Verma modules|809XR5G0DG]].
Through Kostant's multiplicity formula it also gives the weight multiplicities of finite-dimensional irreducible modules.

## Explanations

### L1 human

Think of the positive roots as coins of different kinds, where each coin is a vector rather than a number.
The partition function counts how many ways there are to pay a given vector with these coins.
For the root system $A_2$ the positive roots are $\alpha_1$, $\alpha_2$ and $\alpha_1 + \alpha_2$.
The vector $\alpha_1 + \alpha_2$ can be paid in two ways: with the single coin $\alpha_1 + \alpha_2$, or with one $\alpha_1$ and one $\alpha_2$.
