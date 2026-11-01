---
tag: 7Z0QZP0FC0
kind: definition
name: Matroid minor
msc: [05B35]
defines: 4WCYBSH1P6
uses: [PX31ZNYS3Z, SYRCTH853H, 6QF83CFK2G]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid_minor
---

## Definition

Let $M = (E, \mathcal{I})$ be a [[matroid|PX31ZNYS3Z]] with [[rank function|SYRCTH853H]] $r$, and let $X \subseteq E$.

1. The *deletion* $M \setminus X$ is the matroid on $E \setminus X$ whose independent sets are the sets $I \in \mathcal{I}$ with $I \subseteq E \setminus X$.
2. The *contraction* $M / X$ is the matroid on $E \setminus X$ with rank function $r_{M/X}(A) = r(A \cup X) - r(X)$ for $A \subseteq E \setminus X$.
3. A matroid $N$ is a *minor* of $M$ if $N = (M \setminus X) / Y$ for some disjoint sets $X, Y \subseteq E$.

## Remarks

If $J$ is a maximal independent subset of $X$, then a set $I \subseteq E \setminus X$ is independent in $M / X$ if and only if $I \cup J \in \mathcal{I}$.
Deletion and contraction commute, and $M / X = (M^* \setminus X)^*$, where $M^*$ is the [[dual matroid|6QF83CFK2G]].
Many authors call $N$ a minor when it is isomorphic to a matroid of the form in clause 3.
For the graphic matroid of a graph, deleting or contracting an edge gives the graphic matroid of the graph with that edge deleted or contracted.

Example: let $M = U_{2,4}$, the matroid on $\set{1, 2, 3, 4}$ whose independent sets are the subsets with at most $2$ elements.
Then $M \setminus \set{4} = U_{2,3}$, and $M / \set{4} = U_{1,3}$, since $r(A \cup \set{4}) - 1 = \min(\abs{A} + 1, 2) - 1 = \min(\abs{A}, 1)$.

Non-example: $U_{2,4}$ is not a minor of $U_{1,5}$, because deletion and contraction never raise the rank, and $U_{2,4}$ has rank $2$ while $U_{1,5}$ has rank $1$.

A theorem of Tutte states that a matroid is representable over the field with two elements if and only if it has no minor isomorphic to $U_{2,4}$.
