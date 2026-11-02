---
tag: DBD64TH52D
kind: concept
name: Least fixed point
msc: [06A06, 47H10]
sources:
  - url: https://en.wikipedia.org/wiki/Least_fixed_point
same_as:
  wikidata: Q6134913
  wikipedia: Least fixed point
---

## Summary

The least fixed point of a map $f$ from a [[partially ordered set|0QV2JS9RJ3]] to itself is a point $x$ with $f(x) = x$.
It must lie below every other point with this property.
When it exists it is unique.
Least fixed points give meaning to recursive and inductive definitions: the set defined inductively by some rules is the least set closed under the rules.
The [[Knaster–Tarski theorem|RHXP3HA64M]] and the [[Kleene fixed-point theorem|DDAHG7QRY8]] guarantee least fixed points of monotone maps under completeness hypotheses.

## Explanations

### L1 human

A fixed point of a map is a point that the map leaves where it is.
Among all fixed points, the least one is the one that lies below all the others.
For the map $x \mapsto x^2$ on the real numbers, the fixed points are $0$ and $1$, and the least fixed point is $0$.
The set of even natural numbers is the least set that contains $0$ and contains $n + 2$ whenever it contains $n$.
It is the least fixed point of the map $S \mapsto \set{0} \cup \set{n + 2 : n \in S}$ on subsets of $\N$.
