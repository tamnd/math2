---
tag: QKJ743GE3J
kind: definition
name: Cardinal function
msc: [54A25]
defines: XVNJPJ53W8
uses: [0CQHFPGJ45, 0EBACQFAZW, 0QT00PB5G2, 0NA0732YAG, 0BSJSX7ME2, 0G0ASKNA6Z, 07SG12TQH3]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinal_function
---

## Definition

A *cardinal function* is a rule $\varphi$ that assigns to each [[topological space|0CQHFPGJ45]] $X$ a [[cardinal number|0EBACQFAZW]] $\varphi(X)$.
It is required that $\varphi(X) = \varphi(Y)$ whenever $X$ and $Y$ are [[homeomorphic|0QT00PB5G2]].

## Remarks

Common examples, for a space $X$:

1. the weight $w(X)$, the least [[cardinality|0G0ASKNA6Z]] of a [[base|0NA0732YAG]] of the topology;
2. the density $d(X)$, the least cardinality of a [[dense|0BSJSX7ME2]] subset;
3. the character $\chi(X)$, the least cardinal $\kappa$ such that every point has a neighbourhood base of cardinality at most $\kappa$;
4. the cellularity $c(X)$, the supremum of the cardinalities of families of pairwise disjoint nonempty open sets.

Many authors add $\aleph_0$ to each value, so that these functions are infinite.
Two basic inequalities follow.
First, $d(X) \le w(X)$: choose one point in each nonempty member of a base.
Second, $\abs{X} \le 2^{w(X)}$ for a [[T0 space|07SG12TQH3]] $X$, since a point is determined by the base members that contain it.

Example: for $X = \R$, one has $w(X) = d(X) = \aleph_0$, by the base of intervals with rational endpoints and the dense set $\Q$.

Non-example: the rule $X \mapsto$ the number of points of $X$ that lie in $[0, 1]$, defined only for subspaces of $\R$, is not a cardinal function.
It is not invariant under homeomorphism: $[0, 1]$ and $[2, 3]$ are homeomorphic but give $\mathfrak c$ and $0$.
