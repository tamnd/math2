---
tag: WZYEADV8E1
kind: concept
name: Condorcet method
msc: [91B12, 91B14]
sources:
  - url: https://en.wikipedia.org/wiki/Condorcet_method
same_as:
  wikidata: Q868720
  wikipedia: Condorcet method
---

## Summary

A Condorcet method is a voting rule that elects the Condorcet winner whenever there is one.
A Condorcet winner is a candidate who beats every other candidate in a head-to-head majority vote.
Since a Condorcet winner need not exist, the different Condorcet methods differ in what they do when pairwise majorities form a cycle.
Copeland's method, the Schulze method, ranked pairs and the Kemeny–Young method are Condorcet methods.

## Explanations

### L1 human

Voters rank the candidates, and one imagines a separate two-way race between every pair of candidates.
If some candidate wins all of her two-way races, a Condorcet method must declare her the winner.
For example, if the voters' rankings make $a$ beat $b$ by $3$ to $2$ and also beat $c$ by $3$ to $2$, then $a$ wins.
Ordinary plurality voting is not a Condorcet method: a candidate liked by most voters as a second choice can lose.
