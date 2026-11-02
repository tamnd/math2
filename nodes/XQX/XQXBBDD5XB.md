---
tag: XQXBBDD5XB
kind: definition
name: Ideal completion
msc: [06B23, 06B35]
defines: A5HTJ565DN
uses: [0QV2JS9RJ3, D9RY4667K6, 7TSXP95QN6, 9F7TYES4KE, 5GW2T2AM1A]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(order_theory)
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
An *order ideal* of $P$ is a subset $I \subseteq P$ such that:

1. $I$ is nonempty;
2. $I$ is a down-set: if $x \in I$ and $y \le x$, then $y \in I$;
3. $I$ is [[directed|D9RY4667K6]]: for all $x, y \in I$ there is $z \in I$ with $x \le z$ and $y \le z$.

The *ideal completion* of $P$ is the set $\operatorname{Idl}(P)$ of all order ideals of $P$, ordered by inclusion.
It comes with the map $x \mapsto {\downarrow} x = \set{y \in P : y \le x}$ from $P$ to $\operatorname{Idl}(P)$.

## Remarks

$\operatorname{Idl}(P)$ is a [[directed-complete partial order|7TSXP95QN6]]: the supremum of a directed family of ideals is its union.
The map $x \mapsto {\downarrow} x$ is an order embedding, and the principal ideals ${\downarrow} x$ are exactly the [[compact elements|9F7TYES4KE]] of $\operatorname{Idl}(P)$, so $\operatorname{Idl}(P)$ is an algebraic dcpo.
When $P$ is a lattice, the order ideals are its [[lattice ideals|5GW2T2AM1A]] and $\operatorname{Idl}(P)$ is an algebraic lattice if $P$ has a least element.
Example: for $P = \N$, the ideals are the sets $\set{0, \ldots, n}$ and $\N$ itself, so $\operatorname{Idl}(\N) \cong \N \cup \set{\infty}$.
Non-example: in $\N$, the set $\set{0, 2}$ is not an ideal, because $1 \le 2$ but $1 \notin \set{0, 2}$.
