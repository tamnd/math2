---
tag: 9G8XXBG9F3
kind: definition
name: Series-parallel partial order
msc: [06A07, 06A06]
defines: 2YC1Q1MDV8
uses: [0QV2JS9RJ3, 6AJ7QQCTQQ, TZWMEM7GKA]
sources:
  - url: https://en.wikipedia.org/wiki/Series-parallel_partial_order
---

## Definition

The class of *series-parallel partial orders* is the smallest class $\mathcal{S}$ of finite [[partially ordered sets|0QV2JS9RJ3]] such that:

1. every one-element poset is in $\mathcal{S}$;
2. if $P$ and $Q$ are in $\mathcal{S}$, then their [[ordinal sum|6AJ7QQCTQQ]] $P \oplus Q$ is in $\mathcal{S}$;
3. if $P$ and $Q$ are in $\mathcal{S}$, then their [[disjoint union|TZWMEM7GKA]] $P + Q$ is in $\mathcal{S}$;
4. every poset isomorphic to a member of $\mathcal{S}$ is in $\mathcal{S}$.

## Remarks

Example: the poset with $a < b < d$, $a < c < d$ and $b$, $c$ incomparable is $\set{a} \oplus (\set{b} + \set{c}) \oplus \set{d}$, so it is series-parallel.
Non-example: the poset $N$ on $\set{a, b, c, d}$ with $a < c$, $b < c$, $b < d$ as the only strict relations is not series-parallel.
It is connected, so it is not a disjoint union of two nonempty posets.
It is not an ordinal sum $A \oplus B$ of two nonempty posets either.
Nothing lies below $a$, so $a$ would be in $A$, and every element of $B$ would be above $a$.
The only element above $a$ is $c$, so $B = \set{c}$, but $d$ would then be below $c$, which fails.
A finite poset is series-parallel if and only if it has no subposet isomorphic to $N$.
Total orders and antichains are series-parallel.
