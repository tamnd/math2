---
tag: YBG22HS28V
kind: definition
name: Order filter
msc: [06A06, 06B10]
defines: Z15FXM9WM1
uses: [0QV2JS9RJ3, ETCE287E2R, J2T75ATRV5]
sources:
  - url: https://en.wikipedia.org/wiki/Filter_(mathematics)
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
A *filter* of $P$ is a subset $F \subseteq P$ such that:

1. $F$ is nonempty;
2. if $x \in F$, $y \in P$ and $x \le y$, then $y \in F$;
3. if $x, y \in F$, then there is $z \in F$ with $z \le x$ and $z \le y$.

The filter $F$ is *proper* if $F \ne P$.

## Remarks

Clause 2 says that $F$ is an [[upper set|ETCE287E2R]].
If $P$ is a lattice, clause 3 can be replaced by: $x, y \in F$ implies $x \wedge y \in F$, using the [[meet|J2T75ATRV5]].
For $a \in P$, the set $\uparrow a = \set{x \in P : a \le x}$ is a filter, the *principal filter* of $a$.
Example: in the power set of $\N$, the cofinite sets $\set{A \subseteq \N : \N \setminus A \text{ is finite}}$ form a proper filter.
It contains $\N$, a superset of a cofinite set is cofinite, and $A \cap B$ is cofinite when $A$ and $B$ are, since $\N \setminus (A \cap B) = (\N \setminus A) \cup (\N \setminus B)$.
Non-example: in the power set of $\set{1, 2}$, the set $\set{\set{1}, \set{2}, \set{1, 2}}$ satisfies clauses 1 and 2 but not clause 3.
The only common lower bound of $\set{1}$ and $\set{2}$ is $\emptyset$, which is not in the set.
A filter on a set $X$ in the sense of [[set filters|15PF73BKY6]] is a proper filter of the power set of $X$.
