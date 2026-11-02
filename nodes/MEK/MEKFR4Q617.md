---
tag: MEKFR4Q617
kind: object
name: Suslin line
msc: ["03E50", 06A05, "03E35"]
instance_of: [0FRXBVVR03]
uses: [0316AYH1SC, JB9HJ9CPEN, 0GKJ78948V, D1T39KHPDN]
sources:
  - url: https://en.wikipedia.org/wiki/Suslin%27s_problem
---

## Description

A *Suslin line* is a nonempty [[totally ordered set|0316AYH1SC]] $(L, <)$ with these properties.

1. $L$ has no least element and no greatest element.
2. The order is [[dense|JB9HJ9CPEN]].
3. The order is complete: each nonempty subset of $L$ that is bounded above has a least upper bound.
4. Each family of pairwise disjoint nonempty open intervals of $L$ is countable.
5. $L$ is not [[separable|0GKJ78948V]]: no countable subset of $L$ meets every nonempty open interval.

## Remarks

The real line satisfies clauses 1 to 4 but not clause 5, so $\R$ is not a Suslin line.
In fact, a total order with clauses 1 to 3 and separability is order isomorphic to $\R$.
So a Suslin line is exactly a counterexample to [[Suslin's problem|D1T39KHPDN]].
The existence of a Suslin line is independent of ZFC, if ZFC is consistent.
The [[diamond principle|HFQSSB1Z23]] implies that a Suslin line exists.
[[Martin's axiom|Z8XMCCZFA4]] together with the failure of the continuum hypothesis implies that no Suslin line exists.
A Suslin line exists if and only if a Suslin tree exists.

## Explanations

### L1 human

A Suslin line would be a line that looks almost exactly like the real line, but is not the real line.
It has no ends and no gaps, and one can only fit countably many disjoint intervals into it.
Yet it has no countable set of points that is spread through all of it, as the rationals are spread through the reals.
Whether such a line exists cannot be decided from the usual axioms of set theory.
