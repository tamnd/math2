---
tag: CNZV00JQRC
kind: concept
name: Transfer operator
msc: [37C30, 37A30, 37D20]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer_operator
same_as:
  wikidata: Q3354606
  wikipedia: Transfer operator
---

## Summary

The transfer operator of a map $f$ with weight $g$ acts on functions $\varphi$.
The value of the new function at $x$ is the sum of $g \varphi$ over the preimages of $x$.
It moves densities forward under the map, while the [[Koopman operator|37TRG5DBQC]] moves observables, and the two are dual to each other.
Invariant densities are fixed points of the transfer operator, and its spectrum controls the speed of mixing and decay of correlations.
It is also called the Ruelle operator or, for the weight given by the Jacobian, the Perron–Frobenius operator.

## Explanations

### L1 human

Spread some dust on an interval with a density $\varphi$, then move every grain by the map $f$.
The new density at a point $x$ collects the dust from all points that land on $x$, weighted by how much the map stretches near them.
This rule is linear in $\varphi$, and the transfer operator is that linear rule.
For the doubling map $x \mapsto 2x \bmod 1$, each $x$ has the two preimages $x/2$ and $(x+1)/2$, and the map stretches by $2$.
So the new density is the average of $\varphi$ at these two points.
The constant density is unchanged, which says that the doubling map preserves length.
