---
tag: SCZ8PRVY00
kind: concept
name: Universal enveloping algebra
msc: [17B35, 16S30]
specializes: [3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_enveloping_algebra
same_as:
  wikidata: Q1673406
  wikipedia: Universal enveloping algebra
---

## Summary

The universal enveloping algebra $U(\mathfrak g)$ of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak g$ is the most general associative algebra containing $\mathfrak g$.
In it the Lie bracket becomes the commutator $xy - yx$.
Representations of $\mathfrak g$ are the same as modules over $U(\mathfrak g)$, so Lie theory can use the tools of ring theory.
By the [[Poincaré–Birkhoff–Witt theorem|HFEA4FKGW1]], $U(\mathfrak g)$ has a basis of ordered monomials in a basis of $\mathfrak g$.
It is also a [[Hopf algebra|7XFYP0N84H]], and its deformations give the quantum groups.

## Explanations

### L1 human

A Lie algebra has a bracket $[x, y]$ but no product $xy$.
The universal enveloping algebra adds a product, subject only to the rule $xy - yx = [x, y]$.
For an abelian Lie algebra, the rule says that the elements commute, and $U(\mathfrak g)$ is a polynomial ring.
For a Lie algebra with basis $x, y$ and $[x, y] = y$, it is the algebra of noncommutative polynomials in $x, y$ with $xy - yx = y$.
