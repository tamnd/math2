---
tag: RDM7J5J9HQ
kind: concept
name: Way-below relation
msc: [06B35, 06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Domain_theory
---

## Summary

The way-below relation $x \ll y$ on a partially ordered set says that $x$ is a necessary part of every directed approximation of $y$.
It refines the order $x \le y$ and formalizes the idea of "a finite piece of information about $y$".
It is used to define [[continuous lattices|RXBD58SGXZ]] and continuous domains, and an element is [[compact|9F7TYES4KE]] exactly when it is way below itself.

## Explanations

### L1 human

Suppose $y$ is approached by a directed family of elements, for instance an increasing sequence.
Then $x$ is way below $y$ if every such approach to $y$ passes above $x$ at some finite stage.
In the real interval $[0, 1]$, the number $0.4$ is way below $0.5$, because any increasing sequence with limit at least $0.5$ eventually exceeds $0.4$.
But $0.5$ is not way below itself, because the sequence $0.5 - 1/n$ approaches $0.5$ without reaching it.
