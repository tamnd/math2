---
tag: 4HHDPZ4BDY
kind: concept
name: Covering relation
msc: [06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_relation
same_as:
  wikidata: Q5179263
  wikipedia: Covering relation
---

## Summary

In a [[partially ordered set|011C29Q1S1]], an element $y$ covers an element $x$ when $x < y$ and nothing lies strictly between them.
The covering relation records the immediate steps of the order.
For a finite poset it determines the whole order, and it is exactly what a [[Hasse diagram|00EYM7MDKS]] draws.

## Explanations

### L1 human

The element $y$ covers $x$ when $y$ is the next step up from $x$, with no element in between.
In the integers, $n + 1$ covers $n$.
In the rational numbers nothing covers anything, because between two rationals there is always a third.
For the subsets of $\set{1, 2, 3}$ ordered by inclusion, $\set{1, 2}$ covers $\set{1}$, but $\set{1, 2, 3}$ does not cover $\set{1}$.
