---
tag: 4A82S5FVRT
kind: concept
name: Continuous dual space
msc: [46A20]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Continuous dual space
---

## Summary

The continuous dual space of a [[topological vector space|T32W553W95]] $E$ is the vector space $E'$ of all continuous [[linear forms|07YQ1C78G0]] on $E$.
It is a subspace of the algebraic [[dual space|07JBSZE0V4]], usually much smaller in infinite dimension.
For a normed space it is a Banach space with the dual norm.
Duality theory studies $E$ through $E'$ and the topologies on both, such as the [[weak topology|P6KHVSTPZV]] and the [[strong dual|RG52DZ1A8Y]] topology.

## Explanations

### L1 human

A linear form assigns a number to each vector, in a linear way.
In infinite dimension most linear forms are wild, so one keeps only the continuous ones.
Small changes of the vector should give small changes of the number.
For example, on continuous functions on $[0, 1]$, the map $f \mapsto \int_0^1 f$ and the map $f \mapsto f(1/2)$ are continuous linear forms for uniform convergence.
