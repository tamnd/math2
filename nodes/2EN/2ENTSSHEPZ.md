---
tag: 2ENTSSHEPZ
kind: definition
name: Inaccessible cardinal
msc: ["03E55"]
defines: NW4DREQ5DQ
uses: [0EBACQFAZW, 13ZV2F8JAR, 0W7FBYS1F1, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Inaccessible_cardinal
---

## Definition

Let $\kappa$ be a [[cardinal|0EBACQFAZW]].
The cardinal $\kappa$ is *(strongly) inaccessible* if:

1. $\kappa$ is [[uncountable|0W7FBYS1F1]].
2. $\kappa$ is [[regular|13ZV2F8JAR]]: $\kappa$ is not the union of fewer than $\kappa$ sets each of size less than $\kappa$.
3. $\kappa$ is a strong limit: $2^\lambda < \kappa$ for every cardinal $\lambda < \kappa$, where $2^\lambda$ is the cardinality of the [[power set|00E0YZCERH]] of a set of size $\lambda$.

The cardinal $\kappa$ is *weakly inaccessible* if it satisfies clauses 1 and 2 and is a limit cardinal: $\lambda^+ < \kappa$ for every cardinal $\lambda < \kappa$.

## Remarks

The cardinal $\aleph_0$ satisfies clauses 2 and 3, since a union of finitely many finite sets is finite and $2^n$ is finite; it fails only clause 1.
The cardinal $\aleph_1$ is regular but not inaccessible: it fails clause 3, since $2^{\aleph_0} \ge \aleph_1$.
Every inaccessible cardinal is weakly inaccessible, and under the generalized continuum hypothesis the two notions agree.
If $\kappa$ is inaccessible, then $V_\kappa$, the set of sets of rank less than $\kappa$, is a model of ZFC.
By Gödel's second incompleteness theorem, ZFC therefore cannot prove that an inaccessible cardinal exists, if ZFC is consistent.
In Mathlib the notion is `Cardinal.IsInaccessible`.
