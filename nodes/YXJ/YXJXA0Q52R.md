---
tag: YXJXA0Q52R
kind: concept
name: Group cohomology
msc: [20J06, 18G15]
sources:
  - url: https://en.wikipedia.org/wiki/Group_cohomology
same_as:
  wikidata: Q1408937
  wikipedia: Group cohomology
---

## Summary

Group cohomology attaches to a [[group|G5S1M9]] $G$ and a $G$-module $M$ a sequence of abelian groups $H^n(G, M)$, for $n \ge 0$.
They are the right [[derived functors|NPMC3K6J2F]] of the functor of invariants $M \mapsto M^G$, or equivalently the groups $\operatorname{Ext}^n_{\Z[G]}(\Z, M)$.
In low degrees they have classical meanings.
$H^0$ is the invariants, $H^1$ classifies crossed homomorphisms up to principal ones, and $H^2$ classifies extensions of $G$ by $M$.
It is dual to [[group homology|CFAG3VRXEA]], and [[Galois cohomology|9MPCZ3EAJM]] is the case of Galois groups.

## Explanations

### L1 human

A group acting on an abelian group $M$ leaves some elements fixed; these form $H^0(G, M)$.
Taking fixed points does not respect quotients well, and the higher cohomology groups record this failure.
They can be computed with cochains, which are functions of several group elements with values in $M$.
When every element of $G$ acts on $M$ as the identity, $H^1(G, M)$ is just the group of homomorphisms from $G$ to $M$.
For a cyclic group of order $m$ acting on $\Z$ as the identity, the cohomology is $\Z/m\Z$ in every positive even degree and $0$ in every odd degree.
