---
tag: ATP1JK3V27
kind: concept
name: Alexandrov topology
msc: [54A05, 06A06]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Alexandrov_topology
same_as:
  wikidata: Q3532117
  wikipedia: Alexandrov topology
---

## Summary

An Alexandrov topology is a topology in which the intersection of any family of open sets, finite or infinite, is open.
Equivalently, every point has a smallest open neighbourhood.
Alexandrov topologies on a set correspond exactly to [[preorders|0VABYWJWH9]] on it: the open sets are the [[upper sets|ETCE287E2R]] of the preorder.
Every finite topological space is of this kind, so these spaces are the bridge between finite topology and order theory.

## Explanations

### L1 human

In most spaces, such as the real line, a point has smaller and smaller neighbourhoods with no smallest one.
In an Alexandrov space each point $x$ has a smallest open set around it, and this set says which points are "above" $x$.
So the whole topology is just a way of writing down an order.
For example, on $\set{1, 2, 3}$ ordered by $1 \le 2 \le 3$, the upper sets $\emptyset$, $\set{3}$, $\set{2, 3}$ and $\set{1, 2, 3}$ form an Alexandrov topology.
