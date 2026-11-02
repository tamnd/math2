---
tag: RXBD58SGXZ
kind: concept
name: Continuous lattice
msc: [06B35, 06B23]
specializes: [D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_poset
---

## Summary

A continuous lattice is a complete lattice in which every element is the supremum of the elements [[way below|RDM7J5J9HQ]] it.
Continuous lattices were introduced by Dana Scott as models for the semantics of programming languages, and they connect order theory with topology.
Every [[algebraic lattice|3J0BTXSCVN]] is continuous, and so is the unit interval $[0, 1]$.

## Explanations

### L1 human

An element $x$ is way below $y$ when $x$ is reached by every increasing approach to $y$ before the approach is finished.
In $[0, 1]$, the number $x$ is way below $y$ when $x < y$, or $x = 0$.
A continuous lattice is one where every element can be approximated from below by elements way below it.
So $[0, 1]$ is continuous: each $y > 0$ is the supremum of the numbers $x < y$.
In an algebraic lattice the approximating elements can be taken compact, that is, "finite".
