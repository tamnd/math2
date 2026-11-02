---
tag: Z4JZPEBM68
kind: definition
name: Condensed set
msc: [18F10, 18F20]
defines: 9NM376YWF2
uses: [ZV38HA5PAQ, AND2WHZC8P, RT8A8FJ566, S5744QZV4N, CTJ5AD8ST5]
sources:
  - url: https://en.wikipedia.org/wiki/Condensed_mathematics
---

## Definition

A *profinite set* is a [[Stone space|ZV38HA5PAQ]], that is, a compact Hausdorff totally disconnected space.
Fix an uncountable strong limit cardinal $\kappa$, and let $\mathbf{ProFin}_\kappa$ be the category of profinite sets of cardinality less than $\kappa$, with continuous maps.
A *$\kappa$-condensed set* is a [[presheaf|AND2WHZC8P]] $T \colon \mathbf{ProFin}_\kappa^{\mathrm{op}} \to \mathbf{Set}$ such that:

1. $T(\emptyset)$ is a one-point set.
2. For all $S_1, S_2$, the map $T(S_1 \sqcup S_2) \to T(S_1) \times T(S_2)$ is a bijection.
3. For each continuous surjection $p \colon S' \to S$, the map $T(p)$ is a bijection from $T(S)$ onto the [[equalizer|CTJ5AD8ST5]] of the two maps $T(S') \rightrightarrows T(S' \times_S S')$ induced by the projections.

A *condensed set* is a $\kappa$-condensed set for some such $\kappa$.
Formally, the category of condensed sets is the union (colimit) over $\kappa$ of the categories of $\kappa$-condensed sets.

## Remarks

The three conditions say exactly that $T$ is a [[sheaf|RT8A8FJ566]] for the Grothendieck topology whose covering families are the finite jointly surjective families.
The cardinal $\kappa$ only avoids set-theoretic size problems; other authors use sheaves on all compact Hausdorff spaces with a fixed universe.
Example: for a topological space $X$, the functor $\underline{X}(S) = C(S, X)$ of continuous maps is a condensed set.
A continuous map on $S_1 \sqcup S_2$ is a pair of continuous maps.
A continuous map on $S'$ that agrees on the two pullbacks descends to $S$, because a surjection of compact Hausdorff spaces is a quotient map.
Non-example: for a set $A$ with at least two points, the constant presheaf $T(S) = A$ fails clause 1, since $T(\emptyset) = A$.
The value $T(*)$ at a point is the underlying set of the condensed set.
